import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import matplotlib.pyplot as plt
import seaborn as sns

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
data = pd.concat([train_data, test_data], sort=False)
data["Name_len"] = data["Name"].apply(lambda x: len(x.split()))
data["Has_Mr"] = data["Name"].str.contains("Mr").astype(int)
data["Has_Miss"] = data["Name"].str.contains("Miss").astype(int)
data["Has_Mrs"] = data["Name"].str.contains("Mrs").astype(int)
# 缺失处理
data["Age"] = data["Age"].fillna(data["Age"].median())
data["Fare"] = data["Fare"].fillna(data["Fare"].median())
data["Embarked"].fillna(data["Embarked"].mode()[0],inplace=True) # 用众数填充
# 类别编码
data = pd.get_dummies(data, columns=["Sex", "Embarked"], drop_first=True)

train = data[data["Survived"].notna()]
test = data[data["Survived"].isna()]

X = train.drop(["Survived", "Name", "Ticket", "Cabin", "PassengerId"], axis=1)
y = train["Survived"]

X_test = test.drop(["Survived", "Name", "Ticket", "Cabin", "PassengerId"], 
                   axis=1)


from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler, PowerTransformer
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline


# 随机森林
model = RandomForestClassifier(n_estimators=100, max_depth=5, 
                               random_state=RANDOM_STATE)
model.fit(X, y)
y_predict = model.predict(X)
predictions = model.predict(X_test)

# 逻辑回归_l1
pipe_clf = Pipeline([
      ('sc',StandardScaler()),
      ('power_trans',PowerTransformer()),
      ('polynom_trans',PolynomialFeatures(degree=3)),
      ('logistic_clf', LogisticRegression(penalty='l1', fit_intercept=True,
                                           solver='liblinear'))
      # ('rf',RandomForestClassifier(n_estimators=100, max_depth=5,
      #                              random_state=1))
      ])
pipe_clf.fit(X,y)
predictions = pipe_clf.predict(X_test)

# GBDT
from lightgbm import LGBMClassifier
from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import BaggingClassifier


pipe_clf = Pipeline([
      ('sc',StandardScaler()),
      ('power_trans',PowerTransformer()),
      ('polynom_trans',PolynomialFeatures(degree=3)),
      ('LGBM_clf', LGBMClassifier(
          n_estimators=500, #3、500~2000
          learning_rate=0.05, #1
          max_depth=-1, #2
          random_state=RANDOM_STATE))
      # ('rf',RandomForestClassifier(n_estimators=100, max_depth=5,
      #                              random_state=1))
      ])
pipe_clf.fit(X,y)
predictions = pipe_clf.predict(X_test)



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

# 混淆矩阵，准确率，精准率，召回率，roc，auc
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score
from sklearn.metrics import roc_curve, auc, confusion_matrix
import matplotlib.pyplot as plt


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

# submit
output = pd.DataFrame({'PassengerId': test["PassengerId"], 
                       'Survived': predictions.astype(int)})
output.to_csv(r'C:\tmp\Titanic\my_submission.csv', index=False)
print(output.head())
print("Your submission was successfully saved!")
print(output.shape)
print(output.columns)
print(output["Survived"].value_counts())