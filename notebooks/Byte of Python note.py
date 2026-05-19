help('len') #显示出有关len函数的帮助


age = 20
name = 'Swaroop'
print('{0} was {1} years old when he wrote this book'.format(name, age))
print('Why is {0} playing with that python?'.format(name))
#不用name + 'is' +str(age) + 'years old'是因为实现丑陋，且也容易出错【没觉得】
#也可不加{}中的数字
age = 20
name = 'Swaroop'
print('{} was {} years old when he wrote this book'.format(name, age))
print('Why is {} playing with that python?'.format(name))
#更详细的格式
print('{0:.3f}'.format(1.0/3))
#使用下划线填充文本，保持文字处于中间位置，字符串长度为 11
print('{0:_^11}'.format('hello'))
# 基于关键词输出 'Swaroop wrote A Byte of Python'
print('{name} wrote {book}'.format(name='Swaroop', book='A Byte of Python'))


#需转译字符：'\
'What\'s your name?'
#放置在末尾的反斜杠表示字符串将在下一行继续，但不会添加新的一行
"This is the first sentence. \
This is the second sentence."


#if
number = 23
guess = int(input('Enter an integer : '))
if guess == number:
    print('Congratulations, you guessed it.')
    print('(but you do not win any prizes!)')
elif guess < number:
    print('No, it is a little higher than that')
else:
    print('No, it is a little lower than that')
print('Done')


#while
number = 23
running = True
while running:
    guess = int(input('Enter an integer : '))
    if guess == number:
        print('Congratulations, you guessed it.')
        running = False
    elif guess < number:
        print('No, it is a little higher than that.')
    else:
        print('No, it is a little lower than that.')
else:
    print('The while loop is over.')
print('Done')


#for
for i in range(1, 5):
    print(i)
else:
    print('The for loop is over')


#默认参数值应该是常数，拥有默认参数值的参数不能位于没有默认参数值的参数之前
def say(message, times=1):
    print(message * times)
say('Hello')
say('World', 5)

#可变参数，*param——Tuple，**param——字典
def total(a=5, *numbers, **phonebook):
    print('a', a)
    for single_item in numbers:
        print('single_item', single_item)
    for first_part, second_part in phonebook.items():
        print(first_part,second_part)
print(total(10,1,2,3,Jack=1123,John=2231,Inge=1560))

def build_profile(first, last, **user_info):
    """Build a dictionary containing everything we know about a user."""
    user_info['first_name'] = first
    user_info['last_name'] = last
    return user_info

user_profile = build_profile('albert', 'einstein',
                             location='princeton',
                             field='physics')
print(user_profile)


def some_function():
    pass
some_function()

def print_max(x, y):
    #文档字符串（DocString）
    '''Prints the maximum of two numbers.打印两个数值中的最大数。
    
    The two values must be integers.这两个数都应该是整数'''
    # 如果可能，将其转换至整数类型
    x = int(x)
    y = int(y)
    if x > y:
        print(x, 'is maximum')
    else:
        print(y, 'is maximum')
print_max(3, 5)
print(print_max.__doc__)


import sys
print('The command line arguments are:')
#运行的脚本名称对应 sys.argv[0]，之后为传递给程序的参数
for i in sys.argv:
    print(i)
print('\n\nThe PYTHONPATH is', sys.path, '\n')

#查看你的程序目前所处在的目录
import os
print(os.getcwd())

from math import sqrt
print("Square root of 16 is", sqrt(16))

import mymodule
mymodule.say_hi()
print('Version', mymodule.__version__)

# 给出 sys 模块中的属性名称
import sys
dir(sys)
# 给出当前模块的属性名称
dir()
a = 5
dir()
del a
dir()
dir(str)


#list
shoplist = ['apple', 'mango', 'carrot', 'banana']
print('I have', len(shoplist), 'items to purchase.')
print('These items are:', end=' ') #指定以空白结尾，否则以回车结尾
for item in shoplist:
    print(item, end=' ')
print('\nI also have to buy rice.')
shoplist.append('rice')
print('My shopping list is now', shoplist)
print('I will sort my list now')
shoplist.sort()#影响到的是列表本身
cars.sort(reverse=True)
sorted(cars) #保留列元素原来的顺序，也有参数reverse=True
cars.reverse() #反转列表元素的排列顺序，inplace=True
print('Sorted shopping list is', shoplist)
print('The first item I will buy is', shoplist[0])
olditem = shoplist[0]
del shoplist[0]
print('I bought the', olditem)
print('My shopping list is now', shoplist)


#tuple
zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))
#元组中所包含的元组不会失去其所拥有的身份
new_zoo = 'monkey', 'camel', zoo
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is',
      len(new_zoo)-1+len(new_zoo[2]))
#如果你想指定一个包含项目 2 的元组，必须指定 singleton = (2, ) 


#字典
ab = {
    'Swaroop': 'swaroop@swaroopch.com',
    'Larry': 'larry@wall.org',
    'Matsumoto': 'matz@ruby-lang.org',
    'Spammer': 'spammer@hotmail.com',
}
print("Swaroop's address is", ab['Swaroop'])
del ab['Spammer']
print('\nThere are {} contacts in the address-book\n'.format(len(ab)))
for name, address in ab.items():#字典的 item 方法，返回一份包含元组的列表
    print('Contact {} at {}'.format(name, address))
for name in favorite_languages.keys():
    print(name.title())
for language in favorite_languages.values():
    print(language.title())
ab['Guido'] = 'guido@python.org'
if 'Guido' in ab:
    print("\nGuido's address is", ab['Guido'])

shoplist = ['apple', 'mango', 'carrot', 'banana']
name = 'swaroop'
print('Item 1 to -1 is', shoplist[1:-1])

shoplist = ['apple', 'mango', 'carrot', 'banana']
shoplist[::2]


#集合
bri = set(['brazil', 'russia', 'india']) # 可直接剔除重复项
languages = {'python', 'ruby', 'python', 'c'}
'india' in bri
'usa' in bri
bric = bri.copy()
bric.add('china')
bric.issuperset(bri)
bri.remove('russia') #只删除第一个指定的值
bri & bric # OR bri.intersection(bric)

name = 'Swaroop'
if name.startswith('Swa'):
    print('Yes, the string starts with "Swa"')
if 'a' in name:
    print('Yes, it contains the string "a"')
if name.find('war') != -1:#如果找不到相应的子字符串， find会返回 -1
    print('Yes, it contains the string "war"')
delimiter = '_*_'
mylist = ['Brazil', 'Russia', 'India', 'China']
print(delimiter.join(mylist))


import os
import time
source = ['/Users/swa/notes']
target_dir = '/Users/swa/backup'
#os.sep——根据操作系统给出相应的分隔符
#%Y——年，%m——01 至 12 的十进制数所表示的月份
target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'
if not os.path.exists(target_dir):# 如果目标目录还不存在，则进行创建
    os.mkdir(target_dir) # 创建目录
#' '.join(source)——将列表 source 转换成字符串
zip_command = 'zip -r {0} {1}'.format(target,' '.join(source))
print('Zip command is:')
print(zip_command)
print('Running:')
if os.system(zip_command) == 0:#运行成功返回 0 
    print('Successful backup to', target)
else:
    print('Backup FAILED')


#类
class Person:
    pass # 一个空的代码块
p = Person()
print(p)

class Person:
    def say_hi(self):
        print('Hello, how are you?')
p = Person()
p.say_hi()

class Person:
    def __init__(self, name):
        self.name = name #self.name是某个叫做"self"的对象的一部分
    def say_hi(self):
        print('Hello, my name is', self.name)
p = Person('Swaroop')
p.say_hi()
# 前面两行同时也能写作
# Person('Swaroop').say_hi()

class Robot:
    population = 0 # 一个类变量，用来计数机器人的数量，可以被属于该类的所有实例访问
    #当任何一个对象对类变量作出改变时，发生的变动将在其它所有实例中都会得到体现
    def __init__(self, name):
        self.name = name
        print("(Initializing {})".format(self.name))
        Robot.population += 1 # 当有人被创建时，机器人将会增加人口数量
    def die(self):
        print("{} is being destroyed!".format(self.name))
        Robot.population -= 1
        if Robot.population == 0:
            print("{} was the last one.".format(self.name))
        else:
            print("There are still {:d} robots working.".format(
                    Robot.population))
    def say_hi(self):
        print("Greetings, my masters call me {}.".format(self.name))
        
    @classmethod #装饰器（Decorator）——等价于调用how_many = classmethod(how_many)
    def how_many(cls): #属于类的方法
        print("We have {:d} robots.".format(cls.population))

droid1 = Robot("R2-D2")
droid1.say_hi()
Robot.how_many()  #除了 Robot.popluation ，还可以使用 self.__class__.population
#因为每个对象都通过self.__class__ 属性来引用它的类。
droid2 = Robot("C-3PO")
droid2.say_hi()
Robot.how_many()
droid1.die()
droid2.die()
Robot.how_many()
#访问类的文档字符串：Robot.__doc__
#访问方法的文档字符串：Robot.say_hi.__doc__

class SchoolMember:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('(Initialized SchoolMember: {})'.format(self.name))
    def tell(self):
        print('Name:"{}" Age:"{}"'.format(self.name, self.age), end=" ")

class Teacher(SchoolMember): #子类：定义类时需要在类后面跟一个包含基类名称的元组
    def __init__(self, name, age, salary):
        #因为在子类中定义了__init__方法，Python不会自动调用基类SchoolMember
        #的构造函数，必须显式调用它
        SchoolMember.__init__(self, name, age)
        #super().__init__(name, age)
        self.salary = salary
        print('(Initialized Teacher: {})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Salary: "{:d}"'.format(self.salary))

class Student(SchoolMember):
    def __init__(self, name, age, marks):
        SchoolMember.__init__(self, name, age)
        self.marks = marks
        print('(Initialized Student: {})'.format(self.name))
    def tell(self):
        SchoolMember.tell(self)
        print('Marks: "{:d}"'.format(self.marks))

t = Teacher('Mrs. Shrividya', 40, 30000)
s = Student('Swaroop', 25, 75)
print()
members = [t, s]
for member in members:
    member.tell()

something = input("Enter text: ")


#文件的读取与写入
poem = '''\
Programming is fun
When the work is done
if you wanna make your work also fun:
use Python!
'''
f = open('poem.txt', 'w')
f.write(poem)
f.close()
f = open('poem.txt')
while True:
    line = f.readline()
    if len(line) == 0:
        break
    print(line, end='')
f.close()

# 以二进制来存储：rb, wb, wrb, ab
import pickle
shoplistfile = 'shoplist.data'
shoplist = ['apple', 'mango', 'carrot']
f = open(shoplistfile, 'wb')
pickle.dump(shoplist, f)
f.close()
del shoplist
f = open(shoplistfile, 'rb')
# 读取：pickle.load(file)
storedlist = pickle.load(f)
print(storedlist)

# encoding=utf-8
import io
f = io.open("abc.txt", "wt", encoding="utf-8")
f.write(u"Imagine non-English language here")
f.close()
text = io.open("abc.txt", encoding="utf-8").read()
print(text)


try:
    text = input('Enter something --> ')
except EOFError:
    print('Why did you do an EOF on me?')
except KeyboardInterrupt:
    print('You cancelled the operation.')
else:# try代码成功执行后
    print('You entered {}'.format(text))

class ShortInputException(Exception):
    def __init__(self, length, atleast):
        Exception.__init__(self)
        self.length = length
        self.atleast = atleast
try:
    text = input('Enter something --> ')
    if len(text) < 3:
        raise ShortInputException(len(text), 3)
except EOFError:
    print('Why did you do an EOF on me?')
except ShortInputException as ex:
    print(('ShortInputException: The input was ' +
           '{0} long, expected at least {1}')
                .format(ex.length, ex.atleast))
else:
    print('No exception was raised.')

import sys
import time
f = None
try:
    f = open("poem.txt")
    while True:
        line = f.readline()
        if len(line) == 0:
            break
        print(line, end='')
        sys.stdout.flush() #以便它能被立即打印到屏幕上【没太大感觉】
        print("Press ctrl+c now")
        time.sleep(2)
except IOError:
    print("Could not find file poem.txt")
except KeyboardInterrupt:
    print("!! You cancelled the reading from the file.")
finally: #无论是否出错都会执行
    if f:
        f.close()
    print("(Cleaning up: Closed the file)")
    
with open("poem.txt") as f: #将关闭文件的操作交由with open来自动完成，默认只读模式，
# 写入时会直接删除原内容
    for line in f: # 按行读入为list
        print(line, end='')
        
with open('pi_digits.txt') as file_object:
    contents = file_object.read()
    print(contents)

sys.version_info #正在使用的 Python 软件的版本

import os
import platform
import logging
if platform.platform().startswith('Windows'):
    #合并位置路径以符合当前操作系统
    logging_file = os.path.join(os.getenv('HOMEDRIVE'),
                                os.getenv('HOMEPATH'),
                                'test.log')
else:
     logging_file = os.path.join(os.getenv('HOME'),
                                 'test.log')
print("Logging to", logging_file)
logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s : %(levelname)s : %(message)s',
        filename=logging_file,
        filemode='w',
)
logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")   

def get_error_details():
    return (2, 'details')
errnum, errstr = get_error_details()#将表达式的结果解释为具有两个值的一个元组
print(errnum)


#交换两个变量
a = 5; b = 8
print(a,b)
a, b = b, a
print(a,b)

points = [{'x': 2, 'y': 3},{'x': 4, 'y': 1}]
points.sort(key=lambda i: i['y'])
print(points)

listone = [2, 3, 4]
listtwo = [2*i for i in listone if i > 2]
print(listtwo)

mylist = ['item']
assert len(mylist) >= 1
mylist.pop() #pop出的元素原列表中删除
assert len(mylist) >= 1


from time import sleep
from functools import wraps
import logging
logging.basicConfig()
log = logging.getLogger("retry")
def retry(f):
    @wraps(f)
    def wrapped_f(*args, **kwargs):
        MAX_ATTEMPTS = 5
        for attempt in range(1, MAX_ATTEMPTS + 1):
            try:
                return f(*args, **kwargs)
            except:
                log.exception("Attempt %s/%s failed : %s",
                              attempt,
                              MAX_ATTEMPTS,
                              (args, kwargs))
                sleep(10 * attempt)
        log.critical("All %s attempts failed : %s",
                     MAX_ATTEMPTS,
                     (args, kwargs))
    return wrapped_f
counter = 0

@retry
def save_to_database(arg):
    print("Write to a database or make a network call or etc.")
    print("This will be automatically retried if exception is thrown.")
    global counter
    counter += 1
    if counter < 2:
        raise ValueError(arg)

if __name__ == '__main__':
    save_to_database("Some bad value")
···

