import numpy as np # linear algebra
import pandas as pd # data processing, CSV file I/O (e.g. pd.read_csv)
import os
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False


url=r'D:\BC53\我的文档\XTC\PYTHON\titanic'
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
for i in train_data.columns:
   sns.countplot(x=i,data=train_data)
   plt.show()

# 数值列
num_cols = train_data.select_dtypes(
  include=['int64','float64']
).columns
for col in num_cols:
  print("="*30)
  print(col)
  # 基础统计
  # print(train_data[col].describe())
  # 偏度，≈0——接近正泰，>0——右偏（长尾在右），>1——明显偏态，>2——严重偏态
  skew = train_data[col].skew()
  print("偏度:", round(skew,2))
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
  plt.hist(
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

corr_matrix = train_data[num_cols].corr()
# Fare与Pclass强负相关
# 热力图
# filtered = corr_matrix.copy() # 只保留强相关
# filtered[abs(filtered) < 0.5] = np.nan
sns.heatmap(
    # filtered,
    corr_matrix,
    annot=True,        # 显示数值
    cmap='coolwarm',   # 配色
    center=0,          # 0为中心
    linewidths=0.5
)
plt.title("Correlation Heatmap")
plt.show()


plt.scatter(train_data['Age'],train_data['Fare'],marker='.',
           cmap = 'Reds',
           alpha = 0.8,)


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

from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import KFold
from sklearn.preprocessing import StandardScaler, PowerTransformer
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import Pipeline

y = train_data["Survived"]
features = ["Pclass", "Sex", "SibSp", "Parch"]
X = pd.get_dummies(train_data[features])
X_test = pd.get_dummies(test_data[features])
model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
y_predict = model.predict(X)
predictions = model.predict(X_test)

pipe_clf = Pipeline([
        ('sc',StandardScaler()),
        ('power_trans',PowerTransformer()),
        ('polynom_trans',PolynomialFeatures(degree=3)),
        # ('logistic_clf', LogisticRegression(penalty='l1', fit_intercept=True, 
        #                                     solver='liblinear'))
        ('rf',RandomForestClassifier(n_estimators=100, max_depth=5, 
                                     random_state=1))
        ])
# 查看模型表现
import warnings
from sklearn.metrics import accuracy_score, precision_score, recall_score, roc_auc_score
warnings.filterwarnings('ignore')
pipe_clf.fit(X,y)
y_predict = pipe_clf.predict(X)
print(f'accuracy score is: {accuracy_score(y,y_predict)}')
print(f'precision score is: {precision_score(y,y_predict)}')
print(f'recall score is: {recall_score(y,y_predict)}')
print(f'auc: {roc_auc_score(y,y_predict)}')

output = pd.DataFrame({'PassengerId': test_data.PassengerId, 'Survived': predictions})
output.to_csv(r'D:\BC53\我的文档\XTC\tmp\my_submission.csv', index=False)
print("Your submission was successfully saved!")

