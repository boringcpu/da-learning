import numpy as np
import pandas as pd

type(x3)

#List——有序对象

# 多变量赋值
a = b = c = 1
d , e , f = 1 , 2 , 'hello'

# 序列链接与重复
lst1 = [1,2,3]
lst2 = ['a','b','c']
print(lst1+lst2)  # "+"：序列的链接
print(lst1*3,lst2*2)  # "*"：序列重复

lst = [1,1,2,3,3,4,4,4,4,5,6]
print(lst.index(3))  # .index(obj)方法：从列表中找出某个值第一个匹配项的索引位置
print(lst.count(4))  # .count(obj)方法：计算值的出现次数

lst.insert(3,'a')# x.insert(i,m)方法：在索引i处插入m，这里索引3代表第四个值
# str.replace(old,new,count)：修改字符串，count：更换几个；string不能直接赋值

print(st.upper())  # 全部大写
print(st.lower())  # 全部小写，不影响原来的变量

first_name = "ada"
last_name = "lovelace"
full_name = f"{first_name} {last_name}"
message = f"Hello, {full_name.title()}!" #所有单词的首字母都转化为大写

# 字典
dic = dict(m = 10 ,n = 'aa', h = [1,2,3])

# 可变参数，默认会把可变参数传入一个元组；且要放最后
def f(*x):
    print(x)

f = lambda a,b,c:a+b+c
print(f(2,3,4))

import random
random.random()# 随机生成一个[0:1)的随机数
random.randint(1,10)# 随机生成一个[1:10]的整数
random.shuffle(lst)# 将一个列表内的元素打乱，inplace=True
samples = np.random.normal(size=(4,4)) # # 生成一个标准正太分布的4*4样本值
samples1 = np.random.rand(1000)#均匀分布
samples2 = np.random.randn(1000)#正态分布

import time
print(time.strftime('%Y-%m-%d %H:%M:%S',time.localtime()))

f = open(path2, 'r')
print(f.read())
f.close()

print(f.read(2))# f.read(n):n代表读取多少个字符
print(f.readline())# 读取行到字符串，一次性读取一行
print(f.readline(4))# f.readline(n)：读取该行的前n个字符

data = [['name',name],['lng',lng],['lat',lat],['address',ad]]  # 做成嵌套列表
m.append(dict(data))  # 生成字典，并追加如列表m

f = open(path, 'w', encoding = 'utf8') # 只能写文本格式
# 'a'附加在原内容末尾
f.write('hello world!')
f.writelines(lst)
f.close()

pic = open( 'C:\\Users\\Hjx\\Desktop\\data.pkl', 'wb')
# 以二进制来存储：rb, wb, wrb, ab
pickle.dump(data,pic)
pic.close()

# 读取：pickle.load(file)
f = open( 'C:\\Users\\Hjx\\Desktop\\data.pkl', 'rb')
st = pickle.load(f)

ar1 = np.linspace(2.0, 3.0, num=5)

# 存储数组数据 .npy文件
np.save('arraydata.npy', ar)
# 读取数组数据 .npy文件
ar_load =np.load('arraydata.npy')

ar1 = np.linspace(2.0, 3.0, num=5)
ar2 = np.linspace(2.0, 3.0, num=5, endpoint=False)
ar3 = np.linspace(2.0, 3.0, num=5, retstep=True)
# retstep：如果为真，返回（样本，步长）

# 数组堆叠
a = np.arange(5)    # a为一维数组，5个元素
b = np.arange(5,10) # b为一维数组,4个元素
ar1 = np.hstack((a,b))  # 注意:((a,b))，这里形状可以不一样
ar2 = np.vstack((a,b))
ar1 = np.stack((a,b))
ar2 = np.stack((a,b),axis = 1) # {0 or ‘index’, 1 or ‘columns’}, default 0

bs2 = s.isnull()
bs3 = s.notnull()
s1 = s.reindex(['c','b','a','d'], fill_value = 0) # 可以创建不存在的index

data4 = df.loc[['one','two']]# 按照index选择行
# 选择一行时返回series，选择>1行时返回dataframe

# 先选择列再选择行 —— 相当于对于一个数据，先筛选字段，再选择数据量

df1.sort_values(['a'], ascending = False)
df2.sort_values(['a','c'])
df1.sort_index()# 默认 ascending=True, inplace=False

import datetime
today = datetime.date.today()#当前日期
t = datetime.date(2016,6,1)
str(today) # 转换为字符串格式

# %y 两位数的年份表示（00-99）
# %Y 四位数的年份表示（000-9999）
# %m 月份（01-12）
# %d 月内中的一天（0-31）
# %H 24小时制小时数（0-23）
# %I 12小时制小时数（01-12）
# %M 分钟数（00=59）
# %S 秒（00-59）
# %a 本地简化星期名称
# %A 本地完整星期名称
# %b 本地简化的月份名称
# %B 本地完整的月份名称
# %c 本地相应的日期表示和时间表示
# %j 年内的一天（001-366）
# %p 本地A.M.或P.M.的等价符
# %U 一年中的星期数（00-53）星期天为星期的开始
# %w 星期（0-6），星期天为星期的开始
# %W 一年中的星期数（00-53）星期一为星期的开始
# %x 本地相应的日期表示
# %X 本地相应的时间表示
# %Z 当前时区的名称
# %% %号本身
now = datetime.datetime.now()#当前时间
t1 = datetime.datetime(2016,6,1)
t2 = datetime.datetime(2014,1,1,12,44,33)
t2-t1# 相减得到时间差 —— timedelta
t1_hour = t1.replace(minute=0, second=0)

# datetime.timedelta：时间差
today = datetime.datetime.today()  #=now
yestoday = today - datetime.timedelta(1)  

# parser.parse：日期字符串转换
from dateutil.parser import parse
date = '12-21-2017'
t = parse(date)
# 直接将str转化成datetime.datetime
print(parse('2000-1-1'),'\n',
     parse('5/1/2014'),'\n', # 默认月在日前
     parse('5/1/2014', dayfirst = True),'\n',  # 国际通用格式中，日在月之前，可以通过dayfirst来设置
     parse('Jan 31, 1997 10:45 PM'))
# 各种格式可以解析，但无法支持中文

date1 = datetime.datetime(2016,12,1,12,45,30)  # 创建一个datetime.datetime
date2 = '2017-12-21'  # 创建一个字符串
t1 = pd.Timestamp(date1)
t2 = pd.Timestamp(date2)
t1 = pd.to_datetime(date1)
t2 = pd.to_datetime(date2)
lst_date = [ '2017-12-21', '2017-12-22', '2017-12-23']
t3 = pd.to_datetime(lst_date, errors = 'ignore')
df_data['日期']=pd.to_datetime(df_data['日期'],unit='d',origin='1899-12-30')
# errors = 'ignore':不可解析时返回原始输入
# errors = 'coerce':不可扩展，缺失值返回NaT

rng = pd.DatetimeIndex(['12/1/2017','12/2/2017','12/3/2017','12/4/2017','12/5/2017'])
# pd.date_range()-日期范围：生成日期范围
rng1 = pd.date_range('1/1/2017','1/10/2017', normalize=True)
# normalize：时间参数值正则化到午夜时间戳
rng2 = pd.date_range(start = '1/1/2017', periods = 10)
rng3 = pd.date_range(end = '1/30/2017 15:00:00', periods = 10)
# 默认freq = 'D'：每日历日；B：每工作日；H：每小时；T/MIN：每分；S：每秒
print(pd.date_range('2017/1/1','2017/2/1', freq = 'W-MON'))  
# W-MON：从指定星期几开始算起，每周
# 星期几缩写：MON/TUE/WED/THU/FRI/SAT/SUN
print(pd.date_range('2017/1/1','2017/5/1', freq = 'WOM-2MON'))  
# WOM-2MON：每月的第几个星期几开始算，这里是每月第二个星期一
# M：每月最后一个日历日
# Q-月：指定月为季度末，每个季度末最后一月的最后一个日历日
# A-月：每年指定月份的最后一个日历日
# 月缩写：JAN/FEB/MAR/APR/MAY/JUN/JUL/AUG/SEP/OCT/NOV/DEC
# 所以Q-月只有三种情况：1-4-7-10,2-5-8-11,3-6-9-12
# BM：每月最后一个工作日
# BQ-月：指定月为季度末，每个季度末最后一月的最后一个工作日
# BA-月：每年指定月份的最后一个工作日
# BMS：每月第一个工作日
# BQS-月：指定月为季度末，每个季度末最后一月的第一个工作日
# BAS-月：每年指定月份的第一个工作日
#7D：7天；2h30min：2小时30分钟；2M：2月，每月最后一个日历日
ts.asfreq('4H',method = 'ffill')# 改变频率

# pd.date_range()-日期范围：超前/滞后数据

ts = pd.Series(np.random.rand(4),
              index = pd.date_range('20170101','20170104'))
ts.shift(2)# 正数：数值后移（滞后）ts.shift(2)['col']
ts.shift(2, freq = 'D')
# 加上freq参数：对时间戳进行位移，而不是对数值进行位移

p = pd.Period('2017', freq = 'M')
print(p + 1)
print(pd.Period('2012', freq = 'A-DEC') - 1)
prng = pd.period_range('1/1/2011', '1/1/2012', freq='M')

rng = pd.date_range('2017/1/1', periods = 10, freq = 'M')
prng = pd.period_range('2017','2018', freq = 'M')
ts1 = pd.Series(np.random.rand(len(rng)), index = rng)
ts1.to_period()
# 每月最后一日，转化为每月
ts2 = pd.Series(np.random.rand(len(prng)), index = prng)
ts2.to_timestamp()
# 每月，转化为每月第一天

# 时间序列标签索引，支持各种时间字符串

#重采样构建器，频率改为5天
ts_re2 = ts.resample('5D').sum()

sc = s.value_counts(sort = False)

df.columns = df.columns.str.upper()
s.str.len()
df.columns.str.replace(' ','-',n=1)


s = pd.Series(['a,b,c','1,2,3',['a,,,c'],np.nan])
s.str.split(',')[0]
print(s.str.split(',', expand=True))
print(s.str.split(',', expand=True, n = 1))

s = pd.Series(list('ascaazsd'))
print(s.replace({'a':'hello world!','s':123}))
s.replace([1,2,3],np.nan,inplace = True)# 多值用np.nan代替

sre = pd.concat([s5,s6], axis=1, keys = ['one','two'])#keys为列名
print(df.groupby('a')['b'].agg({'result1':np.mean,
                               'result2':np.sum}))#keys为列名

#透视表
date = ['2017-5-1','2017-5-2','2017-5-3']*3
rng = pd.to_datetime(date)
df = pd.DataFrame({'date':rng,
                   'key':list('abcdabcda'),
                  'values':np.random.rand(9)*10})
# .values数据类型为ndarray
print(pd.pivot_table(df, values = 'values', index = 'date'
                     , columns = 'key', aggfunc=np.sum))  # 也可以写 aggfunc='sum'
print(pd.pivot_table(df, values = 'values', index = ['date','key'], aggfunc=len))

#交叉表：crosstab
df = pd.DataFrame({'A': [1, 2, 2, 2, 2],
                   'B': [3, 3, 4, 4, 4],
                   'C': [1, 1, np.nan, 1, 1]})
df_tmp=pd.crosstab(df['A'],df['B'],values=df['C'],aggfunc=np.sum, margins=True)

data1 = pd.read_table('data1.txt', delimiter=',',header = 0, index_col=1)
# delimiter：用于拆分的字符，也可以用sep：sep = ','
# header：用做列名的序号，默认为0（第一行）
# index_col：指定某列为行索引，否则自动索引0, 1, .....
# read_table主要用于读取简单的数据，txt/csv
data2 = pd.read_csv('data2.csv',engine = 'python')

print(1, 2, 3, sep=' < ') # 输出结果：1 < 2 < 3
max(100, 51, 14, key=mod_5) # key为函数

df = df.cumsum()

data['value'].mode().tolist() #众数；可能不止一个
data['value'].median() #中位数

df_s = pd.DataFrame({'血糖浓度':s.index,'次数':s.values})

ages=[20,22,25,27,21,23,37,31,61,45,41,32]
bins = [18,25,35,60,100]
group_names=['Youth','YoungAdult','MiddleAged','Senior']
cats = pd.cut(ages,bins,labels=group_names)
print(cats.codes, type(cats.codes))  # 0-3对应分组后的四个区间，用代号来注释数据对应区间，结果为ndarray

bins = pd.cut(df_filtered["PTS"], 6)
bin_centers = [(b.left + b.right) / 2 for b in bins]

data = np.random.randn(1000)
s = pd.Series(data)
cats = pd.qcut(s,4)  # 按四分位数进行切割，可以试试 pd.qcut(data,10)
cats = pd.qcut(data,[0,0.1,0.5,0.9,1])

x[:,np.newaxis] #将数组变成(n,1)形状；增加维度，写一个表示增加一维
np.dot(d,e) #点击

x = np.random.uniform(x_min, x_max, n) # 均匀分布
res = sum(np.where(d < r, 1, 0))

#求解矩阵方程
Phi = np.array([[0,0,0,1], [1,1,1,1], [2,4,8,1], [3,9,27,1]])
Y_hat = np.array([0,3,2,1])
theta = np.linalg.solve(Phi, Y_hat)

#↑即求逆后相乘，但↑计算更效率
Phi_inverse = np.linalg.inv(Phi)
theta = Phi_inverse @ Y_hat

#从一个df中选取样本
six_vehicles = vehicle_data.sample(6)

diamond_training_data, diamond_validation_data, diamond_test_data = np.split(diamond_data, [1500,1800])

#[(0, 'a'),(1, 'b'),...]
list(enumerate('abcdefghijklmnopqrstuvwxyz'))

# combine both array into one big array
both_books_train = np.concatenate([mobydick_train, ge_train])

# 将x中的元素从小到大排列，提取其对应的index
np.argsort(abs(lm.coef_))[0][-5:]

# key -- 字典中要查找的键；value -- 可选，如果指定键的值不存在时，返回该默认值
dict.get(key[, value]) # 没指定value则返回None

import copy # 复制像class一样的复合对象
centers = copy.deepcopy(centers)# deepcopy用的是.copy()

smallest_distance = float("inf")

from scipy.spatial import distance
# Compute distance between each pair of the two collections of inputs
distance.cdist(cluster1[["petal_length", "petal_width"]], cluster2[["petal_length", "petal_width"]]).min()

X.query("petal_length < 3.2 and petal_length > 2")

df_1972_to_2016 = ( 
                    df.iloc[:, -14:]    
                        .drop(['Unnamed: 60'], axis = 1) 
                        .rename(columns = {"2000 ‡": "2000", "2016 ‡": "2016", "State.1": "State"}) 
                        .drop([25, 52]) 
                        .set_index("State")
                    ) # columns=['Unnamed: 60']

even_numbers = list(range(2, 11, 2))

my_t = (3,)

requested_toppings = []
if requested_toppings: #列表为空时返回False
    for requested_topping in requested_toppings:
        print(f"Adding {requested_topping}.")
        print( " \nFinished making your pizza! ")
else:
    print ( "Are you sure you want a plain pizza?")

#切片[:]创建副本，传给函数时传原列表更节约时间

class Car:
    """A simple attempt to represent a car."""

    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0
        
    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")
        
    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")
    
    def increment_odometer(self, miles):
        self.odometer_reading += miles

class Battery:
    """A simple attempt to model a battery for an electric car."""
    
    def __init__(self, battery_size=75):
        """Initialize the battery's attributes."""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            range = 260
        elif self.battery_size == 100:
            range = 315
            
        print(f"This car can go about {range} miles on a full charge.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""
    
    def __init__(self, make, model, year):
        """
        Initialize attributes of the parent class.
        Then initialize attributes specific to an electric car.
        """
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"This car has a {self.battery_size}-kWh battery.")

my_tesla = ElectricCar('tesla', 'model s', 2019)
print(my_tesla.get_descriptive_name())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

from random import choice
first_up = choice(players) # 随机返回列表or元组中的某个元素

print(line.rstrip()) # 删除末尾空格和换行符
print(line.strip()) # 删除空格和换行符

try:
    with open(filename, encoding='utf-8') as f:
        contents = f.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} does not exist.")
else:
    # Count the approximate number of words in the file.
    words = contents.split() # 默认空格为分隔符
    num_words = len(words)
    print(f"The file {filename} has about {num_words} words.")
    
import json
numbers = [2, 3, 5, 7, 11, 13]
filename = 'numbers.json'
with open(filename, 'w') as f:
    json.dump(numbers, f)

with open(filename) as f:
    numbers = json.load(f)
print(numbers)


import unittest

from name_function import get_formatted_name

class NamesTestCase(unittest.TestCase):
    """Tests for 'name_function.py'."""
    
    def test_first_last_name(self): # 方法名必须以test_打头才会自动运行
        """Do names like 'Janis Joplin' work?"""
        formatted_name = get_formatted_name('janis', 'joplin') # 输入
        self.assertEqual(formatted_name, 'Janis Joplin') # 是否等于输出

    def test_first_last_middle_name(self):
        """Do names like 'Wolfgang Amadeus Mozart' work?"""
        formatted_name = get_formatted_name(
            'wolfgang', 'mozart', 'amadeus')
        self.assertEqual(formatted_name, 'Wolfgang Amadeus Mozart')

if __name__ == '__main__':
    unittest.main()

# assertNotEqual(a, b)
# assertTrue(x)
# assertFalse(x)
# assertIn(item , list )
# assertNotIn(item , list )

import unittest
from survey import AnonymousSurvey
# 句点表示通过，E表示未通过，F表示断言失败
class TestAnonymousSurvey(unittest.TestCase):
    """Tests for the class AnonymousSurvey"""
    
    def setUp(self):
        """
        Create a survey and a set of responses for use in all test methods.
        """
        question = "What language did you first learn to speak?"
        self.my_survey = AnonymousSurvey(question)
        self.responses = ['English', 'Spanish', 'Mandarin']

    def test_store_single_response(self):
        """Test that a single response is stored properly."""
        self.my_survey.store_response(self.responses[0])
        self.assertIn(self.responses[0], self.my_survey.responses)

    def test_store_three_responses(self):
        """Test that three individual responses are stored properly."""
        for response in self.responses:
            self.my_survey.store_response(response)
        for response in self.responses:
            self.assertIn(response, self.my_survey.responses)

if __name__ == '__main__':
    unittest.main()

# 变量/方法?——描述变量or方法

empty_dict = {}
d1 = {"a": "some value", "b": [1, 2, 3, 4]}
d1["dummy"] = "another value"
ret = d1.pop("dummy") # ret='another value', pop出的元素原字典中删除

# 哈希性——是否可以作为key值（唯一性）

seq1 = ["foo", "bar", "baz"]
seq2 = ["one", "two", "three"]
zipped = zip(seq1, seq2)
list(zipped)
# [('foo', 'one'), ('bar', 'two'), ('baz', 'three')]

# map——对可迭代对象中的元素进行批量操作
set(map(len, strings)) # 即{len(x) for x in strings}
value = re.sub("[!#?]", "", value) # 移除!#?三种符号

strings = ["foo", "card", "bar", "aaaa", "abab"]
strings.sort(key=lambda x: len(set(x))) # set("foo")={'f', 'o'}
dic.update(dic2) # 更新/合并一个字典

ar.shape    # 数组的维度，对于n行m列的数组，shape为（n，m）
# eg. [1 2 3 4 5 6 7]--(7,)

os.listdir() # 返回指定目录下的所有文件和目录名
# 函数返回一个路径的目录名和文件名
os.path.split('C:\\Users\\Hjx\\Desktop\\text.txt')  

arr.swapaxes(0, 1) #.T
values = np.array([6, 0, 0, 3, 2, 5, 6])
np.in1d(values, [2, 3, 6]) # 检查一个数组是否在另一个数组中
(np.abs(walk) >= 10).argmax() # 最大值的位置
