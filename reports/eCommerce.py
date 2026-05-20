"""
漏斗分析项目

1. 各步骤人数
2. 各步骤转化率
3. 最大流失环节
4. 新老用户漏斗对比
5. 工作日/周末漏斗对比
6. 商品类别漏斗对比
7. 输出业务建议

v1.1：映射字典
"""


import pandas as pd
import numpy as np

np.random.seed(42)

# 数据集生成
n_users = 500

uid = np.arange(1, n_users+1)
events = ['register', 'login', 'browse', 'click', 'purchase']

records = []

for u in uid:
    timestamp = pd.Timestamp('2026-05-01') + pd.to_timedelta(np.random.randint(0, 10), unit='D')
    # 注册
    records.append([u, 'register', timestamp])
    if np.random.rand() < 0.8:
        records.append([u, 'login', timestamp + pd.Timedelta(days=1)])
    if np.random.rand() < 0.6:
        records.append([u, 'browse', timestamp + pd.Timedelta(days=2)])
    if np.random.rand() < 0.4:
        records.append([u, 'click', timestamp + pd.Timedelta(days=3)])
    if np.random.rand() < 0.2:
        records.append([u, 'purchase', timestamp + pd.Timedelta(days=4)])

df = pd.DataFrame(records, columns=['uid','event','timestamp'])

print(df.head())


# 漏斗分析
event_map = {
    'register':'0_register',
    'login':'1_login',
    'browse':'2_browse',
    'click':'3_click',
    'purchase':'4_purchase'
}
df['event'] = df['event'].map(event_map)
# 每一步人数
df_step_num=df.groupby('event')['uid'].nunique()
# 计算转化率
funnel=df_step_num/df_step_num.shift(1)

funnel=funnel.to_frame()
funnel.fillna(1,inplace=True)
funnel.reset_index(inplace=True)
funnel.rename(columns={'uid':'conversion'},inplace=True)
funnel['drop_rate']=1-funnel['conversion']
print(funnel.loc[funnel['drop_rate']==max(funnel['drop_rate']),'event'])