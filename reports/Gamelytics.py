import numpy as np
import pandas as pd
import os

os.chdir(r'D:\BC250\我的文档\tmp\Gamelytics')

# Unix 时间戳转换，unit——单位是秒，.dt.date——只取日期部分
# registration timestamps，uid不重复
df_reg=pd.read_csv('reg_data.csv',delimiter=';')
# 保留datetime，时间归0
df_reg['reg_ts'] = pd.to_datetime(df_reg['reg_ts'],unit='s').dt.normalize()
# login timestamps
df_auth=pd.read_csv('auth_data.csv',delimiter=';')
df_auth['auth_ts'] = pd.to_datetime(df_auth['auth_ts'],unit='s').dt.normalize()
df_auth.drop_duplicates(['auth_ts','uid'],inplace=True) # 无重复
# 每日新增用户
# 按某列分组，再对另一列做聚合
reg_num = df_reg.groupby('reg_ts')['uid'].nunique() # 返回该列中不同值的个数
# DAU（日活）
df_auth_num = df_auth.groupby('auth_ts')['uid'].nunique()
# 次日留存：d0注册，d1还登录
# 构建长表
# map 对于大数据集（如百万级以上）速度较快
df_reg_map = (
  df_reg
  .set_index('uid')['reg_ts']
) # 索引是 uid，值是 reg_ts

df_auth['reg_ts'] = (
  df_auth['uid']
  .map(df_reg_map)
) # 对于 df_auth 中每一行的 uid，去 df_reg_map 中查找对应的 reg_ts 值
df_auth['diff_day']=(df_auth['auth_ts']-df_auth['reg_ts']).dt.days
df_auth=df_auth[df_auth['diff_day'].between(1,7)]
# 7日留存：第7日当天登录，留存 ≠ 回访
# cohort analysis（每天的次日留存，3日留存，7日留存百分比）
retention=(df_auth
          .groupby(['reg_ts','diff_day'])['uid']
          .nunique()
          .unstack(fill_value=0))
cohort=retention.div(reg_num,axis=0)
# ARPU 平均每用户收入（Average Revenue Per User）= ARPPU × 付费率
# = 特定时期内的总收入 / 同一时期的用户（或活跃用户）总数
# 社交媒体平台可能使用“日活跃用户（DAU）”或“月活跃用户（MAU）”
# ARPPU（每付费用户平均收入） = 总收入 / 付费用户总数