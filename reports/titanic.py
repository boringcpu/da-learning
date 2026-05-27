import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import StratifiedKFold
# 混淆矩阵，准确率，精准率，召回率，roc，auc
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score
from sklearn.metrics import roc_curve, auc, confusion_matrix
from lightgbm import LGBMClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import BaggingClassifier
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler, PowerTransformer
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline
import shap
import os

plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

RANDOM_STATE=42 


# url=r'D:\BC53\我的文档\XTC\PYTHON\titanic'
url=r'C:\tmp\Titanic'
for dirname, _, filenames in os.walk(url):
    for filename in filenames:
        print(os.path.join(dirname, filename))
        
train_data = pd.read_csv(url+r'\train.csv')
test_data = pd.read_csv(url+r'\test.csv')

# 基础信息
train_data.shape
train_data.info()
train_data.describe()
train_data.isnull().sum()
# age有约20%空值，Cabin字段缺失严重
# 不使用Cabin变量，age以中位数填充

# 目标变量分布
cat_cols = train_data.select_dtypes(
    include=['object']
).columns.tolist()
cat_cols += ['Pclass','Survived']
for i in cat_cols:
   sns.countplot(x=i,hue='Survived',data=train_data) # 分类
   plt.show()
# 男性死亡率高，女性存活率高
# 头等舱存活率高，三等舱死亡率高

# 数值列
num_cols = train_data.select_dtypes(
  include=['int64','float64']
).columns
remove_cols = ['PassengerId','Survived']
num_cols = [
    col for col in num_cols
    if col not in remove_cols
]
for col in num_cols:
    print("="*30)
    print(col)
    # 基础统计
    # print(train_data[col].describe())
    # 偏度是在看一个变量自身分布是不是对称，
    # ≈0——接近正态，>0——右偏（长尾在右），>1——明显偏态，>2——严重偏态
    skew = train_data[col].skew()
    print("偏度:", round(skew,2))
    # Fare，SibSp，Parch严重右偏
    # 大部分人都没有亲属，票价较低，少数人有亲属&高票价
    # IQR异常值
    Q1 = train_data[col].quantile(0.25)
    Q3 = train_data[col].quantile(0.75)
    IQR = Q3 - Q1
    lower = Q1 - 1.5*IQR
    upper = Q3 + 1.5*IQR
    outlier_num = (
        (train_data[col]<lower)|(train_data[col]>upper)
    ).sum()
    print("异常值数量:", outlier_num)
    
    # 分布图
    plt.figure(figsize=(8,4))
    plt.hist( # 连续
        train_data[col].dropna(),
        bins=30
    )
    plt.title(
        f'{col}\nSkew={skew:.2f}'
    )
    plt.show()
    # 箱线图
    plt.figure(figsize=(8,2))
    plt.boxplot(
        train_data[col].dropna(),
        vert=False # 是否垂直
    )
    plt.title(col)
    plt.show()
# 类别相对平衡

# Pearson 相关系数默认假设连续变量、线性关系
corr_matrix = train_data[num_cols].corr()
mask=np.triu(
    np.ones_like(corr_matrix,dtype=bool)
) # mask 中非零值对应的单元格会被隐藏
# Fare与Pclass强负相关，高等级舱位票价更高
# 热力图
# filtered = corr_matrix.copy() # 只保留强相关
# filtered[abs(filtered) < 0.5] = np.nan
sns.heatmap(
    # filtered,
    corr_matrix,
    mask=mask,
    annot=True,        # 显示数值
    cmap='coolwarm',   # 配色
    center=0,          # 0为中心
    linewidths=0.5
)
plt.title("Correlation Heatmap")
plt.show()

plt.figure(figsize=(8,5))
plt.scatter(train_data['Age'],train_data['Fare'],marker='.',
            c=train_data['Survived'],
            cmap = 'Reds',
            alpha = 0.8,) # 颜色表示是否生存
plt.xlabel("Age")
plt.ylabel("Fare")
plt.title(
    "Age vs Fare by Survival"
)
plt.colorbar(
    label='Survived'
)
plt.show()

plt.figure(figsize=(8,5))
sns.boxplot(
    x='Survived',
    y='Age',
    data=train_data
)
plt.title(
    "Age vs Survival"
)
plt.show()

# Sex×Pclass
pd.crosstab(
    train["Sex"],
    train["Pclass"],
    values=train["Survived"],
    aggfunc="mean"
)

# 数值特征分布分析主要关注偏态、异常值和长尾现象。
# 通常通过统计偏度、箱线图和直方图进行分析。
# 如果存在严重长尾分布，可以考虑对数变换；
# 对于异常值，需要结合业务判断是否处理。

women = train_data.loc[train_data.Sex == 'female']["Survived"]
rate_women = sum(women)/len(women)
print("% of women who survived:", rate_women)
men = train_data.loc[train_data.Sex == 'male']["Survived"]
rate_men = sum(men)/len(men)
print("% of men who survived:", rate_men)


# def preprocess(df):
#     df = df.copy()    
#     df["Name"] = (
#         df["Name"]
#         .str.replace(r'[,\(\)\[\].\"\']','',regex=True) # 正则
#         )
#     df["Ticket_number"] = (
#         df["Ticket"]
#         .str.split(" ")
#         .str[-1]
#         )
#     df["Ticket_item"] = (
#         df["Ticket"].str.split(" ")
#         .str[:-1]
#         .str.join('_')
#         .replace('','None') # 整列判断不用str
#         )
#     return df

# preprocessed_train_df = preprocess(train_data)
# preprocessed_serving_df = preprocess(test_data)
# preprocessed_train_df.head(5)


# 训练集 + 测试集合并做特征工程
# sort根据版本不同，默认值不同
data = pd.concat([train_data, test_data], sort=False) 
# 特征工程
data["FamilySize"] = data["SibSp"] + data["Parch"] + 1
data["IsAlone"] = (data["FamilySize"] == 1).astype(int)
data["Name_len"] = data["Name"].apply(lambda x: len(x.split()))
# 性别的作用依赖于舱位，即男性在一等舱影响小在三等舱影响巨大
# data["Sex_Pclass"] = data["Sex_male"] * data["Pclass"]
# 从每个字符串中提取匹配第一个捕获组的内容
# expand=False返回的是一个 Series（而不是单列的 DataFrame）
# ，避免出现不必要的嵌套列
data["Title"] = data["Name"].str.extract(" ([A-Za-z]+)\.", expand=False)
data["Title"] = data["Title"].replace(
    ["Mlle","Ms"], "Miss"
).replace(
    ["Mme"], "Mrs"
)
data["Title"] = data["Title"].replace(
    ["Lady","Countess","Capt","Col","Don","Dr","Major","Rev","Sir","Jonkheer","Dona"],
    "Rare"
)
data["HasCabin"] = data["Cabin"].notnull().astype(int)
data["Fare_log"] = np.log1p(data["Fare"])
# 缺失处理
data["Age"] = data["Age"].fillna(data["Age"].median())
data["Fare"] = data["Fare"].fillna(data["Fare"].median())
data["Embarked"].fillna(data["Embarked"].mode()[0],inplace=True) # 用众数填充
# 类别编码
data = pd.get_dummies(
    data,
    columns=["Sex","Embarked","Title"],
    drop_first=True # 删除通过编码生成的第一个类别，避免虚拟变量陷阱
)

train = data[data["Survived"].notna()]
test = data[data["Survived"].isna()]

X = train.drop(["Survived", "Name", "Ticket", "Cabin", "PassengerId", 'Fare'],
               axis=1)
y = train["Survived"]

X_test = test.drop(["Survived", "Name", "Ticket", "Cabin", "PassengerId", 'Fare'], 
                   axis=1)




# “特征决定上限，模型逼近上限”
# 树能学到 “Sex × Pclass” 这种组合规则
# 缺点：不做 boosting → 提升有限
model = RandomForestClassifier(n_estimators=100, max_depth=5, 
                               random_state=RANDOM_STATE)
model.fit(X, y)
y_predict = model.predict(X)
predictions = model.predict(X_test)

# 逻辑回归_l1，能吃到“性别 + Pclass”主信号，但抓不到复杂交互
# 有多重共线性风险
# 多项式特征：
# 特征少、样本量大、真实边界非线性明显——应该添加，特征多、样本量一般——谨慎添加，配合 L1/L2 正则化
# 实用建议：
# 先用无交互项的线性模型做 baseline
# 再通过交叉验证尝试添加少量有业务意义的交互项
# 如果性能提升明显且验证集稳定，则保留；否则移除
pipe_clf = Pipeline([
      ('sc',StandardScaler()),
      ('power_trans',PowerTransformer()),
      ('polynom_trans',PolynomialFeatures(degree=3)), # Titanic通常手动构造更合理
      ('logistic_clf', LogisticRegression(penalty='l1', fit_intercept=True,
                                           solver='liblinear'))
      # ('rf',RandomForestClassifier(n_estimators=100, max_depth=5,
      #                              random_state=1))
      ])
pipe_clf.fit(X,y)
predictions = pipe_clf.predict(X_test)

# GBDT，树模型不依赖矩阵求逆，共线性问题没那么大
# 原则：小步走 + 多棵树
# learning_rate	n_estimators
# 0.1	         100~300
# 0.05	         300~800
# 0.03	         800~1500
# 0.01	         2000+
skf = StratifiedKFold(n_splits=5, shuffle=True, random_state=42)

oof_scores = []
test_preds = np.zeros(len(X_test))

for fold, (train_idx, val_idx) in enumerate(skf.split(X, y)):

    X_train, X_val = X.iloc[train_idx], X.iloc[val_idx]
    y_train, y_val = y.iloc[train_idx], y.iloc[val_idx]

    model = LGBMClassifier(
        n_estimators=1000,
        learning_rate=0.03,
        num_leaves=31, # 31/63/127
        subsample=0.8, # 随机抽80%样本减少过拟合
        colsample_bytree=0.8, # 随机抽80%特征增加多样性
        random_state=42
    )

    model.fit(X_train, y_train)

    val_pred = model.predict(X_val)
    acc = accuracy_score(y_val, val_pred)
    oof_scores.append(acc)

    test_preds += model.predict(X_test) / 5

print("CV Accuracy:", np.mean(oof_scores))

# 实验记录
results = []
results.append({
    "model": "LGBM_v1",
    "features": "basic + name_features",
    "imputation": "median + mode",
    "score": 0.82
})
pd.DataFrame(results).sort_values("score", ascending=False)

# 如何“公平比较模型”
# ① 数据划分一致
# ② 特征一致
# ③ 预处理一致
# 变动模型、特征、预处理其中一个，看其提升程度
print(f'confusion_matrix：{confusion_matrix(y,y_predict)}')
print(f'accuracy score is: {accuracy_score(y,y_predict)}')
print(f'precision score is: {precision_score(y,y_predict)}')
print(f'recall score is: {recall_score(y,y_predict)}')
print(f'auc: {roc_auc_score(y,y_predict)}')

# logistic_clf = pipe_clf.named_steps['logistic_clf']
# ROC
y_hat = pipe_clf.predict_proba(X)[:, 1] #各类别的概率
fpr, tpr, thresholds = roc_curve(y,y_hat)
roc_auc = auc(fpr, tpr)
plt.figure(figsize=(6,5))
plt.plot(fpr, tpr, color='darkorange', lw=2,
        label=f'ROC curve (AUC = {roc_auc:.2f})')
plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('False Positive Rate')
plt.ylabel('True Positive Rate')
plt.title('Receiver Operating Characteristic (ROC)')
plt.legend(loc="lower right")
plt.grid(alpha=0.3)

# 转 DataFrame
feat_imp = pd.DataFrame({
    "feature": pipe_clf[:-1].get_feature_names_out(),
    "importance": importance
})

# 排序
feat_imp = feat_imp.sort_values(
    by="importance",
    ascending=False
)

# 画图
plt.barh(
    feat_imp["feature"],
    feat_imp["importance"]
)

plt.show()

# SHAP解释
explainer = shap.TreeExplainer(model)
shap_values = explainer.shap_values(X)

shap.summary_plot(shap_values, X)

# submit
output = pd.DataFrame({'PassengerId': test["PassengerId"], 
                       'Survived': (test_preds >= 0.5).astype(int)})
output.to_csv(r'C:\tmp\Titanic\my_submission.csv', index=False)
print(output.head())
print("Your submission was successfully saved!")
print(output.shape)
print(output.columns)
print(output["Survived"].value_counts())