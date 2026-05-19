import numpy as np
import pandas as pd
import os

os.chdir(r'D:\BC250\我的文档\tmp\Gamelytics')

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
# 次日留存：d0注册，d1还登录
df_reg['D1']=df_reg['reg_ts']+pd.Timedelta(days=1)
df_reg['D3']=df_reg['reg_ts']+pd.Timedelta(days=3)
df_reg['D7']=df_reg['reg_ts']+pd.Timedelta(days=7)
df=df_reg.copy()
for i in ('1','3','7'):
   df=pd.merge(df,df_auth,how='left',left_on=['D'+i,'uid'],
               right_on=['auth_ts','uid'])
   df.rename(columns={'auth_ts':'auth_D'+i}, inplace=True)
for i in ('1','3','7'):
   df.loc[~df['auth_D'+i].isna(),'auth_D'+i]=1
   df.loc[df['auth_D'+i].isna(),'auth_D'+i]=0
# 7日留存：第7日当天登录，留存 ≠ 回访
# cohort analysis（每天的次日留存，3日留存，7日留存百分比）
df_coh=pd.DataFrame([])
for i in ('1','3','7'):
   df_D1_num=pd.pivot_table(df,values='auth_D'+i,index='reg_ts',aggfunc='sum')
   df_res=df_D1_num['auth_D'+i]/df_reg_num['uid']
   df_coh=pd.concat([df_coh,df_res],axis=1)
   df_coh.rename(columns={0:'auth_D'+i}, inplace=True)
# ARPU 平均每用户收入（Average Revenue Per User）= ARPPU × 付费率
# = 特定时期内的总收入 / 同一时期的用户（或活跃用户）总数
# 社交媒体平台可能使用“日活跃用户（DAU）”或“月活跃用户（MAU）”
# ARPPU（每付费用户平均收入） = 总收入 / 付费用户总数