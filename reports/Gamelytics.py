import numpy as np
import pandas as pd
import os

os.chdir(r'C:\tmp\Gamelytics')

# Unix 时间戳转换，unit——单位是秒，.dt.date——只取日期部分
# registration timestamps，uid不重复
df_reg=pd.read_csv('reg_data.csv',delimiter=';')
df_reg['reg_ts'] = pd.to_datetime(df_reg['reg_ts'],unit='s').dt.date
# login timestamps
df_auth=pd.read_csv('auth_data.csv',delimiter=';')
df_auth['auth_ts'] = pd.to_datetime(df_auth['auth_ts'],unit='s').dt.date
df_auth.drop_duplicates(['auth_ts','uid'],inplace=True) # 无重复
# 每日新增用户
df_reg_num=pd.pivot_table(df_reg,values='uid',index='reg_ts',aggfunc='count')
# df_reg.groupby("reg_ts")["uid"].nunique() # 返回该序列中唯一值的数量
# DAU（日活）
df_auth_num=pd.pivot_table(df_auth,values='uid',index='auth_ts',aggfunc='count')
# 次日留存：d1注册，d2还登录
# 7日留存：第7日当天登录，留存 ≠ 回访
# cohort analysis（次日留存，3日留存，7日留存百分比）