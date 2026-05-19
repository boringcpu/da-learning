import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

plt.rcParams['font.sans-serif'] = [u'SimHei']
plt.rcParams['axes.unicode_minus'] = False

ax = plt.subplot(111) #注意:一般都在ax中设置,不在plot中设置
#折线图
plt.plot(np.random.rand(10),linestyle = '-.',marker = '.')
# '-'       solid line style
# '--'      dashed line style
# '-.'      dash-dot line style
# ':'       dotted line style
# secondary_y=True → y副坐标轴
s = pd.Series(np.random.randn(100))
s.plot(style = 'k--o',figsize=(10,5))

# marker参数

s = pd.Series(np.random.randn(100).cumsum())
s.plot(linestyle = '--',
      marker = '.')
# '.'       point marker
# ','       pixel marker
# 'o'       circle marker
# 'v'       triangle_down marker
# '^'       triangle_up marker
# '<'       triangle_left marker
# '>'       triangle_right marker
# '1'       tri_down marker
# '2'       tri_up marker
# '3'       tri_left marker
# '4'       tri_right marker
# 's'       square marker
# 'p'       pentagon marker
# '*'       star marker
# 'h'       hexagon1 marker
# 'H'       hexagon2 marker
# '+'       plus marker
# 'x'       x marker
# 'D'       diamond marker
# 'd'       thin_diamond marker
# '|'       vline marker
# '_'       hline marker

fig,axes = plt.subplots(4,1,figsize = (10,10))
ts = pd.Series(np.random.randn(1000), index=pd.date_range('1/1/2000', 
                                                          periods=1000))
ts = ts.cumsum()

# 整体风格样式

import matplotlib.style as psl
print(plt.style.available)
# 查看样式列表
psl.use('ggplot')#bmh
ts = pd.Series(np.random.randn(1000).cumsum(), index=pd.date_range('1/1/2000', 
                                                                   periods=1000))
ts.plot(style = '--g.',grid = True,figsize=(10,6))
# 一旦选用样式后，所有图表都会有样式，重启后才能关掉

ts.plot(kind='line',#line,bar,barh
       label = 'hehe',
       style = '--g.',
       #color = 'red',
       alpha = 0.4,
       use_index = True,#是否以index作为横坐标
       rot = 45,
       grid = True,
       ylim = [-50,50],
       yticks = list(range(-50,50,10)),
       figsize = (8,4),
       title = 'test',
       #subplots = False,
       #colormap = 'Greens',
       #ax = axes[0],
       #stacked=True
       legend = True)
# Series.plot()：series的index为横坐标，value为纵坐标
# kind → line,bar,barh...（折线图，柱状图，柱状图-横...）
# label → 图例标签，Dataframe格式以列名为label
# style → 风格字符串，这里包括了linestyle（-），marker（.），color（g）
# color → 颜色，有color指定时候，以color颜色为准
# alpha → 透明度，0-1
# use_index → 将索引用为刻度标签，默认为True
# rot → 旋转刻度标签，0-360
# grid → 显示网格，一般直接用plt.grid
# xlim,ylim → x,y轴界限
# xticks,yticks → x,y轴刻度值
# figsize → 图像大小
# title → 图名
# legend → 是否显示图例，一般直接用plt.legend()
# 也可以 → plt.plot()
plt.show()

# 柱状图 plt.bar()
plt.figure(figsize=(10,4))
x = np.arange(10)
y1 = np.random.rand(10)
y2 = -np.random.rand(10)
plt.bar(x,y1,width = 1,facecolor = 'yellowgreen',edgecolor = 'white',
        yerr = y1*0.1)
plt.bar(x,y2,width = 1,facecolor = 'lightskyblue',edgecolor = 'white',
        yerr = y2*0.1)
# x,y参数：x，y值
# width：宽度比例
# facecolor柱状图里填充的颜色、edgecolor是边框的颜色
# left-每个柱x轴左边界,bottom-每个柱y轴下边界 → bottom扩展即可化为甘特图 Gantt Chart
# align：决定整个bar图分布，默认left表示默认从左边界开始绘制,center会将图绘制在中间位置
# xerr/yerr ：x/y方向error bar
for i,j in zip(x,y1):
    plt.text(i+0.3,j-0.15,'%.2f' % j, color = 'white')
for i,j in zip(x,y2):
    plt.text(i+0.3,j+0.05,'%.2f' % -j, color = 'white')
# 给图添加text
# zip() 函数用于将可迭代的对象作为参数，将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表。

#各变量直方图
df = pd.DataFrame(np.random.rand(50,2),columns=['A','B'])
df.hist(figsize=(12,5),color='g',alpha=0.8)

# 图名，图例，轴标签，轴边界，轴刻度，轴刻度标签等
df = pd.DataFrame(np.random.rand(10,2),columns=['A','B'])
fig = df.plot(figsize=(6,4),colormap = 'GnBu')
# colormap：颜色板，包括：
# Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r,
# Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, 
# PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples, Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, 
# RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, 
# YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, 
# cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r,
# gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, 
# gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, hsv_r, inferno, inferno_r, jet, jet_r, magma, magma_r, nipy_spectral, 
# nipy_spectral_r, ocean, ocean_r, pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, seismic, seismic_r, spectral, 
# spectral_r ,spring, spring_r, summer, summer_r, terrain, terrain_r, viridis, viridis_r, winter, winter_r

plt.text(5,0.5,'hahaha',fontsize=10)# 注解 → 横坐标，纵坐标，注解字符串
plt.title('Interesting Graph - Check it out')  # 图名
plt.xlabel('Plot Number')  # x轴标签
plt.ylabel('Important var') # y轴标签
plt.legend(loc = 'upper right')  
# 显示图例，loc表示位置
# 'best'         : 0, (only implemented for axes legends)(自适应方式)
# 'upper right'  : 1,
# 'upper left'   : 2,
# 'lower left'   : 3,
# 'lower right'  : 4,
# 'right'        : 5,
# 'center left'  : 6,
# 'center right' : 7,
# 'lower center' : 8,
# 'upper center' : 9,
# 'center'       : 10,
plt.xlim([0,12])  # x轴边界
plt.ylim([0,1.5])  # y轴边界
plt.xticks(range(10))  # 设置x刻度
plt.yticks([0,0.2,0.4,0.6,0.8,1.0,1.2])  # 设置y刻度
fig.set_xticklabels("%.1f" %i for i in range(10))  # x轴刻度标签
fig.set_yticklabels("%.2f" %i for i in [0,0.2,0.4,0.6,0.8,1.0,1.2])  # y轴刻度标签
# 范围只限定图表的长度，刻度则是决定显示的标尺 → 这里x轴范围是0-12，但刻度只是0-9，刻度标签使得其显示1位小数
# 轴标签则是显示刻度的标签
plt.grid(True, linestyle = "--",color = "gray", linewidth = "0.5",axis = 'x')  
# axis：x，y，both，显示x/y/两者的格网
plt.tick_params(bottom='on',top='off',left='on',right='off') 
    
import matplotlib
matplotlib.rcParams['xtick.direction'] = 'out' 
matplotlib.rcParams['ytick.direction'] = 'inout' 
# 设置刻度的方向，in,out,inout

frame = plt.gca()
#plt.axis('off')
# 关闭坐标轴
#frame.axes.get_xaxis().set_visible(False)
#frame.axes.get_yaxis().set_visible(False)
# x/y 轴不可见

plt.close()    # 关闭窗口
plt.gcf().clear()  # 每次清空图表内内容

# 刻度

from matplotlib.ticker import MultipleLocator, FormatStrFormatter

t = np.arange(0.0, 100.0, 1)
s = np.sin(0.1*np.pi*t)*np.exp(-t*0.01)
ax = plt.subplot(111) #注意:一般都在ax中设置,不再plot中设置
plt.plot(t,s,'--*')
plt.grid(True, linestyle = "--",color = "gray", linewidth = "0.5",axis = 'both')  
# 网格
#plt.legend()  # 图例

xmajorLocator = MultipleLocator(10) # 将x主刻度标签设置为10的倍数
xmajorFormatter = FormatStrFormatter('%.0f') # 设置x轴标签文本的格式
xminorLocator   = MultipleLocator(5) # 将x轴次刻度标签设置为5的倍数  
ymajorLocator = MultipleLocator(0.5) # 将y轴主刻度标签设置为0.5的倍数
ymajorFormatter = FormatStrFormatter('%.1f') # 设置y轴标签文本的格式
yminorLocator   = MultipleLocator(0.1) # 将此y轴次刻度标签设置为0.1的倍数  

ax.xaxis.set_major_locator(xmajorLocator)  # 设置x轴主刻度
ax.xaxis.set_major_formatter(xmajorFormatter)  # 设置x轴标签文本格式
ax.xaxis.set_minor_locator(xminorLocator)  # 设置x轴次刻度

ax.yaxis.set_major_locator(ymajorLocator)  # 设置y轴主刻度
ax.yaxis.set_major_formatter(ymajorFormatter)  # 设置y轴标签文本格式
ax.yaxis.set_minor_locator(yminorLocator)  # 设置y轴次刻度

ax.xaxis.grid(True, which='both') #x坐标轴的网格使用主刻度
ax.yaxis.grid(True, which='minor') #y坐标轴的网格使用次刻度
# which：格网显示

#删除坐标轴的刻度显示
#ax.yaxis.set_major_locator(plt.NullLocator()) 
#ax.xaxis.set_major_formatter(plt.NullFormatter()) 

plt.savefig('C:/Users/Hjx/Desktop/pic.png',
            dpi=400,
            bbox_inches = 'tight',
            facecolor = 'g',
            edgecolor = 'b')
# 可支持png，pdf，svg，ps，eps…等，以后缀名来指定
# dpi是分辨率
# bbox_inches：图表需要保存的部分。如果设置为‘tight’，则尝试剪除图表周围的空白部分。
# facecolor，edgecolor： 图像的背景色，默认为‘w’（白色）

fig1 = plt.figure(num=1,figsize=(4,2))
plt.plot(np.random.rand(50).cumsum(),'k--')
fig2 = plt.figure(num=2,figsize=(4,2))
plt.plot(50-np.random.rand(50).cumsum(),'k--')

# 子图创建1 - 先建立子图然后填充图表
fig = plt.figure(figsize=(10,6),facecolor = 'gray')
ax1 = fig.add_subplot(2,2,1)  # 第一行的左图
plt.plot(np.random.rand(50).cumsum(),'k--')
plt.plot(np.random.randn(50).cumsum(),'b--')
# 先创建图表figure，然后生成子图，(2,2,1)代表创建2*2的矩阵表格，然后选择第一个，
# 顺序是从左到右从上到下
ax2 = fig.add_subplot(2,2,2)  # 第一行的右图
ax2.hist(np.random.rand(50),alpha=0.5)
ax4 = fig.add_subplot(2,2,4)  # 第二行的右图
df2 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
ax4.plot(df2,alpha=0.5,linestyle='--',marker='.')

# 子图创建2 - 创建一个新的figure，并返回一个subplot对象的numpy数组 → plt.subplot
fig,axes = plt.subplots(2,3,figsize=(10,4))
ts = pd.Series(np.random.randn(1000).cumsum())
print(axes, axes.shape, type(axes))
ax1 = axes[0,1]
ax1.plot(ts)

# plt.subplots,参数调整
fig,axes = plt.subplots(2,2,sharex=True,sharey=True)
# sharex,sharey：是否共享x，y刻度
for i in range(2):
    for j in range(2):
        axes[i,j].hist(np.random.randn(500),color='k',alpha=0.5)
plt.subplots_adjust(wspace=0,hspace=0)
# wspace,hspace：用于控制宽度和高度的百分比，比如subplot之间的间距

# 子图创建3 - 多系列图，分别绘制
df = pd.DataFrame(np.random.randn(1000, 4), index=ts.index, columns=list('ABCD'))
df = df.cumsum()
df.plot(style = '--.',alpha = 0.4,grid = True,figsize = (8,8),
       subplots = True,
       layout = (2,3),#2行3列
       sharex = False)
plt.subplots_adjust(wspace=0,hspace=0.2)
# plt.plot()基本图表绘制函数 → subplots，是否分别绘制系列（子图）
# layout：绘制子图矩阵，按顺序填充

# 外嵌图表plt.table()
# table(cellText=None, cellColours=None,cellLoc='right', colWidths=None,
# rowLabels=None, rowColours=None, rowLoc='left',
# colLabels=None, colColours=None, colLoc='center',loc='bottom', bbox=None)
data = [[ 66386, 174296,  75131, 577908,  32015],
        [ 58230, 381139,  78045,  99308, 160454],
        [ 89135,  80552, 152558, 497981, 603535],
        [ 78415,  81858, 150656, 193263,  69638],
        [139361, 331509, 343164, 781380,  52269]]
columns = ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail')
rows = ['%d year' % x for x in (100, 50, 20, 10, 5)]
df = pd.DataFrame(data,columns = ('Freeze', 'Wind', 'Flood', 'Quake', 'Hail'),
                 index = ['%d year' % x for x in (100, 50, 20, 10, 5)])
df.plot(kind='bar',grid = True,colormap='Blues_r',stacked=True,figsize=(8,3))
# 创建堆叠图
plt.table(cellText = data,
          cellLoc='center',
          cellColours = None,
          rowLabels = rows,
          rowColours = plt.cm.BuPu(np.linspace(0, 0.5,5))[::-1],  # BuPu可替换成其他colormap
          colLabels = columns,
          colColours = plt.cm.Reds(np.linspace(0, 0.5,5))[::-1], 
          rowLoc='right',
          loc='bottom')
# cellText：表格文本
# cellLoc：cell内文本对齐位置
# rowLabels：行标签
# colLabels：列标签
# rowLoc：行标签对齐位置
# loc：表格位置 → left，right，top，bottom
plt.xticks([])
# 不显示x轴标注

# 面积图
fig,axes = plt.subplots(2,1,figsize = (8,6))
df1 = pd.DataFrame(np.random.rand(10, 4), columns=['a', 'b', 'c', 'd'])
df2 = pd.DataFrame(np.random.randn(10, 4), columns=['a', 'b', 'c', 'd'])
df1.plot.area(colormap = 'Greens_r',alpha = 0.5,ax = axes[0])
df2.plot.area(stacked=False,colormap = 'Set2',alpha = 0.5,ax = axes[1])
# 使用Series.plot.area()和DataFrame.plot.area()创建面积图
# stacked：是否堆叠，默认情况下，区域图被堆叠
# 为了产生堆积面积图，每列必须是正值或全部负值！
# 当数据有NaN时候，自动填充0，所以图标签需要清洗掉缺失值

# 填图
fig,axes = plt.subplots(2,1,figsize = (8,6))
x = np.linspace(0, 1, 500)
y1 = np.sin(4 * np.pi * x) * np.exp(-5 * x)
y2 = -np.sin(4 * np.pi * x) * np.exp(-5 * x)
axes[0].fill(x, y1, 'r',alpha=0.5,label='y1')
axes[1].fill(x, y2, 'g',alpha=0.5,label='y2')
# 对函数与坐标轴之间的区域进行填充，使用fill函数
# 也可写成：plt.fill(x, y1, 'r',x, y2, 'g',alpha=0.5)
x = np.linspace(0, 5 * np.pi, 1000) 
y1 = np.sin(x)  
y2 = np.sin(2 * x)  
axes[1].fill_between(x, y1, y2, color ='b',alpha=0.5,label='area')  
# 填充两个函数之间的区域，使用fill_between函数
for i in range(2):
    axes[i].legend()
    axes[i].grid()
# 添加图例、格网

# 饼图 plt.pie()
s = pd.Series(3 * np.random.rand(4), index=['a', 'b', 'c', 'd'], name='series')
plt.axis('equal')  # 保证长宽相等
plt.pie(s,
       explode = [0.1,0,0,0],
       labels = s.index,
       #colors=['r', 'g', 'b', 'c'],
       colors=plt.cm.BuPu(np.linspace(0,0.5,5))[::-1],
       autopct='%.2f%%',
       pctdistance=0.6,
       labeldistance = 1.2,
       shadow = True,
       startangle=0,
       radius=1.5,
       frame=False)
# 第一个参数：数据
# explode：指定每部分的偏移量
# labels：标签
# colors：颜色
# autopct：饼图上的数据标签显示方式
# pctdistance：每个饼切片的中心和通过autopct生成的文本开始之间的比例
# labeldistance：被画饼标记的直径,默认值：1.1
# shadow：阴影
# startangle：开始角度
# radius：半径
# frame：图框
# counterclock：指定指针方向，顺时针或者逆时针

# 直方图+密度图
s = pd.Series(np.random.randn(1000))
s.hist(bins = 20,
       histtype = 'bar',
       align = 'mid',
       orientation = 'vertical',
       alpha=0.5
       ,density =True
       )
# bin：箱子的宽度
# histtype 风格，bar，barstacked，step，stepfilled
# orientation 水平还是垂直{‘horizontal’, ‘vertical’}
# align : {‘left’, ‘mid’, ‘right’}, optional(对齐方式)
s.plot(kind='kde',style='k--')
# 密度图

# 堆叠直方图
plt.figure(num=1)
df = pd.DataFrame({'a': np.random.randn(1000) + 1, 'b': np.random.randn(1000),
                    'c': np.random.randn(1000) - 1, 'd': np.random.randn(1000)-2},
                   columns=['a', 'b', 'c','d'])
df.plot.hist(stacked=True,
             bins=20,
             colormap='Greens_r',
             alpha=0.5,
             grid=True)
# 使用DataFrame.plot.hist()和Series.plot.hist()方法绘制
# stacked：是否堆叠
df.hist(bins=50)
# 生成多个直方图

# plt.scatter()散点图
# plt.scatter(x, y, s=20, c=None, marker='o', cmap=None, norm=None, vmin=None, vmax=None, 
# alpha=None, linewidths=None, verts=None, edgecolors=None, hold=None, data=None, **kwargs)
plt.figure(figsize=(8,6))
x = np.random.randn(1000)
y = np.random.randn(1000)
plt.scatter(x,y,marker='.',
           s = np.random.randn(1000)*100,# 显示大小
           cmap = 'Reds',
           c = y,# 显示颜色
           alpha = 0.8,)
plt.grid()
# vmin,vmax：亮度设置，标量
# cmap：colormap

# pd.scatter_matrix()散点矩阵
# pd.scatter_matrix(frame, alpha=0.5, figsize=None, ax=None, 
# grid=False, diagonal='hist', marker='.', density_kwds=None, hist_kwds=None, range_padding=0.05, **kwds)
df = pd.DataFrame(np.random.randn(100,4),columns = ['a','b','c','d'])
pd.plotting.scatter_matrix(df,figsize=(10,6),
                 marker = 'o',
                 diagonal='kde',
                 alpha = 0.5,
                 range_padding=0.1)
# diagonal：({‘hist’, ‘kde’})，必须且只能在{‘hist’, ‘kde’}中选择1个 → 每个指标的频率图
# range_padding：(float, 可选)，图像在x轴、y轴原点附近的留白(padding)，该值越大，留白距离越大，图像远离坐标原点

# 创建极坐标轴
s = pd.Series(np.arange(20))
theta=np.arange(0,2*np.pi,0.02)

fig = plt.figure(figsize=(8,4))
ax1 = plt.subplot(121, projection = 'polar')
ax2 = plt.subplot(122)
# 创建极坐标子图
# 还可以写：ax = fig.add_subplot(111,polar=True)
ax1.plot(theta,theta*3,linestyle = '--',lw=1)  
ax1.plot(s, linestyle = '--', marker = '.',lw=2)
ax2.plot(theta,theta*3,linestyle = '--',lw=1)
ax2.plot(s)
plt.grid()
# 创建极坐标图，参数1为角度（弧度制），参数2为value
# lw → 线宽
# 极坐标参数设置
theta=np.arange(0,2*np.pi,0.02)
plt.figure(figsize=(8,4))
ax1= plt.subplot(121, projection='polar')
ax2= plt.subplot(122, projection='polar')
ax1.plot(theta,theta/6,'--',lw=2)
ax2.plot(theta,theta/6,'--',lw=2)
# 创建极坐标子图ax
ax2.set_theta_direction(-1)
# set_theta_direction()：坐标轴正方向，默认逆时针
ax2.set_thetagrids(np.arange(0.0, 360.0, 90),['a','b','c','d'])
ax2.set_rgrids(np.arange(0.2,2,0.4))
# set_thetagrids()：设置极坐标角度网格线显示及标签 → 网格和标签数量一致
# set_rgrids()：设置极径网格线显示，其中参数必须是正数
ax2.set_theta_offset(np.pi/2)
# set_theta_offset()：设置角度偏移，逆时针，弧度制
ax2.set_rlim(0.2,1.2)
ax2.set_rmax(2)
ax2.set_rticks(np.arange(0.1, 1.5, 0.2))
# set_rlim()：设置显示的极径范围
# set_rmax()：设置显示的极径最大值
# set_rticks()：设置极径网格线的显示范围
# 三者会相互影响

# 雷达图1 - 极坐标的折线图/填图 - plt.plot()
plt.figure(figsize=(8,4))
ax1= plt.subplot(111, projection='polar')
ax1.set_title('radar map\n')  # 创建标题
ax1.set_rlim(0,12)
data1 = np.random.randint(1,10,10)
data2 = np.random.randint(1,10,10)
data3 = np.random.randint(1,10,10)
theta=np.arange(0,2*np.pi,2*np.pi/10)
# 创建数据
ax1.plot(theta,data1,'.--',label='data1')
ax1.fill(theta,data1,alpha=0.2)
ax1.plot(theta,data2,'.--',label='data2')
ax1.fill(theta,data2,alpha=0.2)
ax1.plot(theta,data3,'.--',label='data3')
ax1.fill(theta,data3,alpha=0.2)
# 绘制雷达线

# 雷达图2 - 极坐标的折线图/填图 - plt.polar()
# 首尾闭合
labels = np.array(['a','b','c','d','e','f']) # 标签
dataLenth = 6 # 数据长度
data1 = np.random.randint(0,10,6) 
data2 = np.random.randint(0,10,6) # 数据

angles = np.linspace(0, 2*np.pi, dataLenth, endpoint=False) # 分割圆周长
data1 = np.concatenate((data1, [data1[0]])) # 闭合
data2 = np.concatenate((data2, [data2[0]])) # 闭合
angles = np.concatenate((angles, [angles[0]])) # 闭合

plt.polar(angles, data1, 'o-', linewidth=1) #做极坐标系
plt.fill(angles, data1, alpha=0.25)# 填充
plt.polar(angles, data2, 'o-', linewidth=1) #做极坐标系
plt.fill(angles, data2, alpha=0.25)# 填充

plt.thetagrids(angles * 180/np.pi, labels) # 设置网格、标签
plt.ylim(0,10)  # polar的极值设置为ylim

# 极轴图 - 极坐标的柱状图
plt.figure(figsize=(8,4))
ax1= plt.subplot(111, projection='polar')
ax1.set_title('radar map\n')  # 创建标题
ax1.set_rlim(0,12)
data = np.random.randint(1,10,10)
theta=np.arange(0,2*np.pi,2*np.pi/10)
# 创建数据
bar = ax1.bar(theta,data,alpha=0.5)
for r,bar in zip(data, bar):
    bar.set_facecolor(plt.cm.jet(r/10.))  # 设置颜色
plt.thetagrids(np.arange(0.0, 360.0, 90), []) # 设置网格、标签（这里是空标签，则不显示内容）

# 箱型图
'''
【课程3.12】  箱型图

箱型图：又称为盒须图、盒式图、盒状图或箱线图，是一种用作显示一组数据分散情况资料的统计图
包含一组数据的：最大值、最小值、中位数、上四分位数（Q1）、下四分位数（Q3）、异常值
① 中位数 → 一组数据平均分成两份，中间的数
② 下四分位数Q1 → 是将序列平均分成四份，计算(n+1)/4与(n-1)/4两种，一般使用(n+1)/4
③ 上四分位数Q3 → 是将序列平均分成四份，计算(1+n)/4*3=6.75
④ 内限 → T形的盒须就是内限，最大值区间Q3+1.5IQR,最小值区间Q1-1.5IQR （IQR=Q3-Q1）
⑤ 外限 → T形的盒须就是内限，最大值区间Q3+3IQR,最小值区间Q1-3IQR （IQR=Q3-Q1）
⑥ 异常值 → 内限之外 - 中度异常，外限之外 - 极度异常

plt.plot.box(),plt.boxplot()
 
'''
fig,axes = plt.subplots(2,1,figsize=(10,6))
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
color = dict(boxes='DarkGreen', whiskers='DarkOrange', medians='DarkBlue', caps='Gray')
# 箱型图着色
# boxes → 箱线
# whiskers → 分位数与error bar横线之间竖线的颜色
# medians → 中位数线颜色
# caps → error bar横线颜色
df.plot.box(ylim=[0,1.2],
           grid = True,
           color = color,
           ax = axes[0])
# color：样式填充
df.plot.box(vert=False, 
            positions=[1, 4, 5, 6, 8],
            ax = axes[1],
            grid = True,
           color = color)
# vert：是否垂直，默认True
# position：箱型图占位

# pltboxplot(x, notch=None, sym=None, vert=None, whis=None, positions=None, widths=None, patch_artist=None, bootstrap=None, 
# usermedians=None, conf_intervals=None, meanline=None, showmeans=None, showcaps=None, showbox=None, showfliers=None, boxprops=None, 
# labels=None, flierprops=None, medianprops=None, meanprops=None, capprops=None, whiskerprops=None, manage_xticks=True, autorange=False, 
# zorder=None, hold=None, data=None)
df = pd.DataFrame(np.random.rand(10, 5), columns=['A', 'B', 'C', 'D', 'E'])
plt.figure(figsize=(10,4))
f = df.boxplot(sym = 'o',  # 异常点形状，参考marker
               vert = True,  # 是否垂直
               whis = 1.5,  # IQR，默认1.5，也可以设置区间比如[5,95]，代表强制上下边缘为数据95%和5%位置
               patch_artist = True,  # 上下四分位框内是否填充，True为填充
               meanline = False,showmeans=True,  # 是否有均值线及其形状
               showbox = True,  # 是否显示箱线
               showcaps = True,  # 是否显示边缘线
               showfliers = True,  # 是否显示异常值
               notch = False,  # 中间箱体是否缺口
               return_type='dict'  # 返回类型为字典
              ) 
plt.title('boxplot')

for box in f['boxes']:
    box.set( color='b', linewidth=1)        # 箱体边框颜色
    box.set( facecolor = 'b' ,alpha=0.5)    # 箱体内部填充颜色
for whisker in f['whiskers']:
    whisker.set(color='k', linewidth=0.5,linestyle='-')
for cap in f['caps']:
    cap.set(color='gray', linewidth=2)
for median in f['medians']:
    median.set(color='DarkBlue', linewidth=2)
for flier in f['fliers']:
    flier.set(marker='o', color='y', alpha=0.5)
# boxes, 箱线
# medians, 中位值的横线,
# whiskers, 从box到error bar之间的竖线.
# fliers, 异常值
# caps, error bar横线
# means, 均值的横线,

# 分组汇总
df = pd.DataFrame(np.random.rand(10,2), columns=['Col1', 'Col2'] )
df['X'] = pd.Series(['A','A','A','A','A','B','B','B','B','B'])
df['Y'] = pd.Series(['A','B','A','B','A','B','A','B','A','B'])
df.boxplot(by = 'X')
df.boxplot(column=['Col1','Col2'], by=['X','Y'])
# columns：按照数据的列分子图
# by：按照列分组做箱型图

# 按元素处理样式：style.applymap()
def color_neg_red(val):
    if val < 0:
        color = 'red'
    else:
        color = 'black'
    return('color:%s' % color)
df.style.applymap(color_neg_red)
# 创建样式方法，使得小于0的数变成红色
# style.applymap() → 自动调用其中的函数

# 按行/列处理样式：style.apply()
def highlight_max(s):
    is_max = s == s.max()
    #print(is_max)
    lst = []
    for v in is_max:
        if v:
            lst.append('background-color: yellow')
        else:
            lst.append('')
    return(lst)
df.style.apply(highlight_max, axis = 0, subset = ['b','c'])
# 创建样式方法，每列最大值填充黄色
# axis：0为列，1为行，默认为0
# subset：索引

df = pd.DataFrame(np.random.randn(10,4),columns=['a','b','c','d'])
df.style.format("{:+.2f}")
df.style.format({'b':"{:.2%}", 'c':"{:+.3f}", 'd':"{:.3f}"})

# 色彩映射
df = pd.DataFrame(np.random.rand(10,4),columns = list('ABCD'))
df.style.background_gradient(cmap='Greens',axis =1,low=0,high=1)
# cmap：颜色
# axis：映射参考，0为行，1以列
# low,high最低最浅，最高最深

# 条形图
df = pd.DataFrame(np.random.rand(10,4),columns = list('ABCD'))
df.style.bar(subset=['A', 'B'], color='#d65f5f', width=100)
# width：最长长度在格子的占比

             
             
def sinplot(flip=1):
    x = np.linspace(0, 14, 100)
    for i in range(1, 7):
        plt.plot(x, np.sin(x + i * .5) * (7 - i) * flip)
sinplot()
# 简单切换为seaborn图表统一风格
sns.set()

# 风格选择包括："white", "dark", "whitegrid", "darkgrid", "ticks"
data = np.random.normal(size=(20, 6)) + np.arange(6) / 2
sns.set_style("white")
sns.boxplot(data=data)

# 3、despine()
# 设置图表坐标轴
# seaborn.despine(fig=None, ax=None, top=True, right=True, left=False, 
# bottom=False, offset=None, trim=False)
# 设置风格
#sns.despine()# 删除了上、右坐标轴
#sns.despine(offset=10, trim=True)
# offset：与坐标轴之间的偏移
# trim：为True时，将坐标轴限制在数据最大最小值
#sns.despine(left=True, right = False)
# top, right, left, bottom：布尔型，为True时不显示

# 4、axes_style()
# 设置局部图表风格，可学习和with配合的用法
with sns.axes_style("darkgrid"):
    plt.subplot(211)
    sinplot()
sns.set_style("whitegrid")
plt.subplot(212)
sinplot()

# 5、set_context()
# 设置显示比例尺度
# 选择包括：'paper', 'notebook', 'talk', 'poster'
sns.set_context("talk")

# 1、color_palette()
# 默认6种颜色：deep, muted, pastel, bright, dark, colorblind 【前2个好看】
# seaborn.color_palette(palette=None, n_colors=None, desat=None)
current_palette = sns.color_palette()
sns.palplot(current_palette)#显示调色盘

# 其他颜色风格
# 风格内容：Accent, Accent_r, Blues, Blues_r, BrBG, BrBG_r, BuGn, BuGn_r, BuPu, 
# BuPu_r, CMRmap, CMRmap_r, Dark2, Dark2_r, GnBu, GnBu_r, Greens, Greens_r, Greys, Greys_r, OrRd, OrRd_r, Oranges, Oranges_r, PRGn, PRGn_r, 
# Paired, Paired_r, Pastel1, Pastel1_r, Pastel2, Pastel2_r, PiYG, PiYG_r, PuBu, PuBuGn, PuBuGn_r, PuBu_r, PuOr, PuOr_r, PuRd, PuRd_r, Purples,
# Purples_r, RdBu, RdBu_r, RdGy, RdGy_r, RdPu, RdPu_r, RdYlBu, RdYlBu_r, RdYlGn, RdYlGn_r, Reds, Reds_r, Set1, Set1_r, Set2, Set2_r, Set3, 
# Set3_r, Spectral, Spectral_r, Wistia, Wistia_r, YlGn, YlGnBu, YlGnBu_r, YlGn_r, YlOrBr, YlOrBr_r, YlOrRd, YlOrRd_r, afmhot, afmhot_r, 
# autumn, autumn_r, binary, binary_r, bone, bone_r, brg, brg_r, bwr, bwr_r, cool, cool_r, coolwarm, coolwarm_r, copper, copper_r, cubehelix, 
# cubehelix_r, flag, flag_r, gist_earth, gist_earth_r, gist_gray, gist_gray_r, gist_heat, gist_heat_r, gist_ncar, gist_ncar_r, gist_rainbow, 
# gist_rainbow_r, gist_stern, gist_stern_r, gist_yarg, gist_yarg_r, gnuplot, gnuplot2, gnuplot2_r, gnuplot_r, gray, gray_r, hot, hot_r, hsv, 
# hsv_r, icefire, icefire_r, inferno, inferno_r, jet, jet_r, magma, magma_r, mako, mako_r, nipy_spectral, nipy_spectral_r, ocean, ocean_r, 
# pink, pink_r, plasma, plasma_r, prism, prism_r, rainbow, rainbow_r, rocket, rocket_r, seismic, seismic_r, spectral, spectral_r, spring, 
# spring_r, summer, summer_r, terrain, terrain_r, viridis, viridis_r, vlag, vlag_r, winter, winter_r
sns.palplot(sns.color_palette("hls", 8))
# 这里颜色风格为 hls
# 颜色色块个数为8个
# 风格颜色反转(不是所有颜色都可以反转)：Blues/Blues_r
sns.palplot(sns.color_palette("Paired",8))# 分组颜色设置 - "Paired"
# 可用方法：
# ① husl_palette([n_colors, h, s, l])
# ② hls_palette([n_colors, h, l, s])
sns.palplot(sns.hls_palette(8, l=.3, s=.8))# l → 亮度；s → 饱和度

# 3、cubehelix_palette()
# 按照线性增长计算，设置颜色
sns.palplot(sns.cubehelix_palette(8, gamma=2))
sns.palplot(sns.cubehelix_palette(8, start=.5, rot=-.75))
sns.palplot(sns.cubehelix_palette(8, start=2, rot=0, dark=0, light=.95, reverse=True))
# n_colors → 颜色个数
# start → 值区间在0-3，开始颜色
# rot → 颜色旋转角度
# gamma → 颜色伽马值，越大颜色越暗
# dark，light → 值区间0-1，颜色深浅
# reverse → 布尔值，默认为False，由浅到深

# 4、dark_palette(color[, n_colors, reverse, ...]) / light_palette(color[, n_colors, reverse, ...])
# 颜色深浅

sns.palplot(sns.light_palette("green"))   # 按照“颜色”green做浅色调色盘
sns.palplot(sns.dark_palette("green", reverse=True))   # 按照blue做深色调色盘
#↑起始or结束为某个颜色中间值
sns.palplot(sns.color_palette("Greens"))  # 按照“风格”Greens做调色盘
# reverse → 转制颜色

# 5、diverging_palette()
# 创建分散颜色
# seaborn.diverging_palette(h_neg, h_pos, s=75, l=50, sep=10, n=6, 
# center='light', as_cmap=False)¶

sns.palplot(sns.diverging_palette(145, 280, s=85, l=25, n=7))
# h_neg, h_pos → 起始/终止颜色值
# s → 值区间0-100，饱和度
# l → 值区间0-100，亮度
# n → 颜色个数
# center → 中心颜色为浅色还是深色“light”，“dark”,默认为light

# 5、diverging_palette()
# 创建分散颜色

plt.figure(figsize = (8,6))
x = np.arange(25).reshape(5, 5)
cmap = sns.diverging_palette(200, 20, sep=20, as_cmap=True)
sns.heatmap(x, cmap=cmap)

with sns.color_palette("PuBuGn_d"):
    plt.subplot(211)
    sinplot()

sns.set_palette("husl")
plt.subplot(212)
sinplot()

# 1、直方图 - distplot()

rs = np.random.RandomState(10)  # 设定随机数种子
s = pd.Series(rs.randn(100) * 100)
sns.distplot(s
             ,bins = 10# bins → 箱数
             ,hist = True# hist、ked → 是否显示箱/密度曲线
             ,kde = True#True时相当于norm_hist也为True
             ,norm_hist=False# norm_hist → 是否标准化
             ,rug = True# rug → 是否显示数据下面的小数杠分布
             ,vertical = False
             #,color = 'y'
             ,label = 'distplot'# label → 图例
             ,axlabel = 'x'# axlabel → x轴标注
             #,rug_kws = {'color':'y'}# 设置数据频率分布颜色
             #,kde_kws={"color": "k", "lw": 1, "label": "KDE",'linestyle':'--'}## 设置密度曲线颜色，线宽，标注、线形
             #,hist_kws={"histtype": "bar", "linewidth": 1,"alpha": 0.7, "color": "blue"}
             )
plt.legend()
# 设置箱子的风格、线宽、透明度、颜色;
# 风格包括：'bar', 'barstacked', 'step', 'stepfilled'

# 2、密度图 - kdeplot()
# 单个样本数据密度分布图

sns.kdeplot(s,
           shade = False,  # 是否填充
           color = 'r',   # 设置颜色
           vertical = False  # 设置是否水平
           )

sns.kdeplot(s,bw=5, label="bw: 0.2",
            linestyle = '-',linewidth = 1.2,alpha = 0.5)
sns.kdeplot(s,bw=20, label="bw: 2",
            linestyle = '-',linewidth = 1.2,alpha = 0.5)
# bw → 控制拟合的程度，类似直方图的箱数

sns.rugplot(s,height = 0.1,color = 'k',alpha = 0.5)
# 数据频率分布图

# 2、密度图 - kdeplot()
# 两个样本数据密度分布图

rs = np.random.RandomState(2)  # 设定随机数种子
df = pd.DataFrame(rs.randn(100,2),
                 columns = ['A','B'])
sns.kdeplot(df['A'],df['B'],
           cbar = True,    # 是否显示颜色图例
           shade = True,   # 是否填充
           cmap = 'Reds',  # 设置调色盘
           shade_lowest=False,  # 最外围颜色是否显示
           n_levels = 10   # 曲线个数（如果非常多，则会越平滑）
           )
# 两个维度数据生成曲线密度图，以颜色作为密度衰减显示

sns.rugplot(df['A'], color="g", axis='x',alpha = 0.5)
sns.rugplot(df['B'], color="r", axis='y',alpha = 0.5)
# 注意设置x，y轴

# 2、密度图 - kdeplot()
# 两个样本数据密度分布图
# 多个密度图

rs1 = np.random.RandomState(2)  
rs2 = np.random.RandomState(5)  
df1 = pd.DataFrame(rs1.randn(100,2)+2,columns = ['A','B'])
df2 = pd.DataFrame(rs2.randn(100,2)-2,columns = ['A','B'])
# 创建数据

sns.kdeplot(df1['A'],df1['B'],cmap = 'Greens',
            shade = True,shade_lowest=False)
sns.kdeplot(df2['A'],df2['B'],cmap = 'Blues',
            shade = True,shade_lowest=False)
# 创建图表

# 1、综合散点图 - jointplot()
# 散点图 + 分布图
rs = np.random.RandomState(2)  
df = pd.DataFrame(rs.randn(200,2),columns = ['A','B'])
sns.jointplot(x=df['A'], y=df['B'],  # 设置xy轴，显示columns名称
              data=df,   # 设置数据
              color = 'k',   # 设置颜色
              s = 50, edgecolor="w",linewidth=1,  # 设置散点大小、边缘线颜色及宽度(只针对scatter）
              kind = 'scatter',   # 设置类型：“scatter”、“reg”、“resid”、“kde”、“hex”
              space = 0.2,  # 设置散点图和布局图的间距
              size = 8,   # 图表大小（自动调整为正方形）
              ratio = 5,  # 散点图与布局图高度比，整型
              marginal_kws=dict(bins=15, rug=True)  # 设置柱状图箱数，是否设置rug
              )  

# 1、综合散点图 - jointplot()
# 散点图 + 分布图
# 蜂窝图
df = pd.DataFrame(rs.randn(500,2),columns = ['A','B'])
with sns.axes_style("white"):
    sns.jointplot(x=df['A'], y=df['B'],data = df, kind="hex", color="k",
                 marginal_kws=dict(bins=20))
    
# 1、综合散点图 - jointplot()
# 散点图 + 分布图
# 密度图
rs = np.random.RandomState(15)
df = pd.DataFrame(rs.randn(300,2),columns = ['A','B'])
g = sns.jointplot(x=df['A'], y=df['B'],data = df,
                  kind="kde", color="k",
                  shade_lowest=False)
g.plot_joint(plt.scatter,c="w", s=30, linewidth=1, marker="+")
# 添加散点图

# 1、综合散点图 - JointGrid()
# 可拆分绘制的散点图
# plot_joint() + ax_marg_x.hist() + ax_marg_y.hist()

sns.set_style("white")
# 设置风格

tips = sns.load_dataset("tips")
print(tips.head())
# 导入数据

g = sns.JointGrid(x="total_bill", y="tip", data=tips)
# 创建一个绘图表格区域，设置好x、y对应数据

g.plot_joint(plt.scatter, color ='m', edgecolor = 'white')  # 设置框内图表，scatter
g.ax_marg_x.hist(tips["total_bill"], color="b", alpha=.6,
                 bins=np.arange(0, 60, 3))            # 设置x轴直方图，注意bins是数组
g.ax_marg_y.hist(tips["tip"], color="r", alpha=.6,
                 orientation="horizontal",
                 bins=np.arange(0, 12, 1))            # 设置x轴直方图，注意需要orientation参数

from scipy import stats
g.annotate(stats.pearsonr)    
# 设置标注，可以为pearsonr，spearmanr

plt.grid(linestyle = '--')

# 1、综合散点图 - JointGrid()
# 可拆分绘制的散点图
# plot_joint() + plot_marginals()

g = sns.JointGrid(x="total_bill", y="tip", data=tips)
# 创建一个绘图表格区域，设置好x、y对应数据

g = g.plot_joint(plt.scatter,color="g", s=40, edgecolor="white")   # 绘制散点图
plt.grid(linestyle = '--')

g.plot_marginals(sns.distplot, kde=True, color="g")                # 绘制x，y轴直方图

# 1、综合散点图 - JointGrid()
# 可拆分绘制的散点图
# plot_joint() + plot_marginals()
# kde - 密度图

g = sns.JointGrid(x="total_bill", y="tip", data=tips)
# 创建一个绘图表格区域，设置好x、y对应数据

g = g.plot_joint(sns.kdeplot,cmap = 'Reds_r')             # 绘制密度图
plt.grid(linestyle = '--')

g.plot_marginals(sns.kdeplot, shade = True, color="r")  # 绘制x，y轴密度图

# 2、矩阵散点图 - pairplot()

sns.set_style("white")
# 设置风格

iris = sns.load_dataset("iris")
print(iris.head())
# 读取数据

sns.pairplot(iris,
            kind = 'scatter',  # 散点图/回归分布图 {‘scatter’, ‘reg’}  
            diag_kind="hist",  # 直方图/密度图 {‘hist’, ‘kde’}
            hue="species",   # 按照某一字段进行分类
            palette="husl",  # 设置调色板
            markers=["o", "s", "D"],  # 设置不同系列的点样式（这里根据参考分类个数）
            size = 2,   # 图表大小
            )

# 2、矩阵散点图 - pairplot()
# 只提取局部变量进行对比

sns.pairplot(iris,vars=["sepal_width", "sepal_length"],
             kind = 'reg', diag_kind="kde", 
             hue="species", palette="husl")

# 2、矩阵散点图 - pairplot()
# 其他参数设置

sns.pairplot(iris, diag_kind="kde", markers="+",
             plot_kws=dict(s=50, edgecolor="b", linewidth=1),
             # 设置点样式
             diag_kws=dict(shade=True)
             # 设置密度图样式
            )

# 2、矩阵散点图 - PairGrid()
# 可拆分绘制的散点图
# map_diag() + map_offdiag()

g = sns.PairGrid(iris,hue="species",palette = 'hls',
                vars = ['sepal_length','sepal_width','petal_length','petal_width'],  # 可筛选
                )
# 创建一个绘图表格区域，设置好x、y对应数据，按照species分类

g.map_diag(plt.hist, 
           histtype = 'barstacked',   # 可选：'bar', 'barstacked', 'step', 'stepfilled'
           linewidth = 1, edgecolor = 'w')           
# 对角线图表，plt.hist/sns.kdeplot

g.map_offdiag(plt.scatter,
              edgecolor="w", s=40,linewidth = 1,   # 设置点颜色、大小、描边宽度
             )     
# 其他图表，plt.scatter/plt.bar...

g.add_legend()
# 添加图例

# 2、矩阵散点图 - PairGrid()
# 可拆分绘制的散点图
# map_diag() + map_lower() + map_upper()

g = sns.PairGrid(iris)
g.map_diag(sns.kdeplot, lw=3)   # 设置对角线图表
g.map_upper(plt.scatter, color = 'r')     # 设置对角线上端图表
g.map_lower(sns.kdeplot, cmap="Blues_d")      # 设置对角线下端图表

# 1、stripplot()
# 按照不同类别对样本数据进行分布散点图绘制

tips = sns.load_dataset("tips")
print(tips.head())
# 加载数据

sns.stripplot(x="day",          # x → 设置分组统计字段
              y="total_bill",   # y → 数据分布统计字段
              # 这里xy数据对调，将会使得散点图横向分布
              data=tips,        # data → 对应数据
              jitter = True,    # jitter → 当点数据重合较多时，用该参数做一些调整，也可以设置间距如：jitter = 0.1
              size = 5, edgecolor = 'w',linewidth=1,marker = 'o'  # 设置点的大小、描边颜色或宽度、点样式
              )

# 1、stripplot()
# 通过hue参数再分类

sns.stripplot(x="sex", y="total_bill", hue="day",
              data=tips, jitter=True)

# 1、stripplot()
# 设置调色盘

sns.stripplot(x="sex", y="total_bill", hue="day",
              data=tips, jitter=True,
              palette="Set2",  # 设置调色盘
              dodge=True,  # 是否拆分
             )

# 1、stripplot()
# 筛选分类类别

print(tips['day'].value_counts())
# 查看day字段的唯一值

sns.stripplot(x="day", y="total_bill", data=tips,jitter = True, 
              order = ['Sat','Sun'])
# order → 筛选类别

# 2、swarmplot()
# 分簇散点图

sns.swarmplot(x="total_bill", y="day", data=tips,
              size = 5, edgecolor = 'w',linewidth=1,marker = 'o',
              palette = 'Reds')
# 用法和stripplot类似

# 1、boxplot()
# 箱型图

sns.boxplot(x="day", y="total_bill", data=tips,
            linewidth = 2,   # 线宽
            width = 0.8,     # 箱之间的间隔比例
            fliersize = 3,   # 异常点大小
            palette = 'hls', # 设置调色板
            whis = 1.5,      # 设置IQR 
            notch = True,    # 设置是否以中值做凹槽
            order = ['Thur','Fri','Sat','Sun'],  # 筛选类别
           )
# 绘制箱型图

sns.swarmplot(x="day", y="total_bill", data=tips,color ='k',size = 3,alpha = 0.8)
# 可以添加散点图

# 1、boxplot()
# 通过hue参数再分类

sns.boxplot(x="day", y="total_bill", data=tips,
            hue = 'smoker', palette = 'Reds')
# 绘制箱型图

#sns.swarmplot(x="day", y="total_bill", data=tips,color ='k',size = 3,alpha = 0.8)
# 可以添加散点图

# 2、violinplot()
# 小提琴图

sns.violinplot(x="day", y="total_bill", data=tips,
            linewidth = 2,   # 线宽
            width = 0.8,     # 箱之间的间隔比例
            palette = 'hls', # 设置调色板
            order = ['Thur','Fri','Sat','Sun'],  # 筛选类别
            scale = 'area',  # 测度小提琴图的宽度：area-面积相同，count-按照样本数量决定宽度，width-宽度一样
            gridsize = 50,   # 设置小提琴图边线的平滑度，越高越平滑
            inner = 'box',   # 设置内部显示类型 → “box”, “quartile”, “point”, “stick”, None
            #bw = 0.8        # 控制拟合程度，一般可以不设置
           )
# 用法和boxplot类似

# 2、violinplot()
# 通过hue参数再分类

sns.violinplot(x="day", y="total_bill", data=tips,
               hue = 'smoker', palette="muted", 
               split=True,  # 设置是否拆分小提琴图
               inner="quartile")

# 2、violinplot()
# 结合散点图

sns.violinplot(x="day", y="total_bill", data=tips, palette = 'hls', inner = None)
sns.swarmplot(x="day", y="total_bill", data=tips, color="w", alpha=.5)
# 插入散点图

# 3、lvplot()
# LV图表

sns.lvplot(x="day", y="total_bill", data=tips, palette="mako",
           #hue = 'smoker',
           width = 0.8,           # 箱之间间隔比例
           linewidth = 12,
           #scale = 'area',        # 设置框的大小 → “linear”、“exonential”、“area”
           #k_depth = 'proportion',  # 设置框的数量 → “proportion”、“tukey”、“trustworthy”
          )
# 绘制LV图

sns.swarmplot(x="day", y="total_bill", data=tips,color ='k',size = 3,alpha = 0.8)
# 可以添加散点图

# 1、barplot()
# 柱状图 - 置信区间估计
# 置信区间：样本均值 + 抽样误差

titanic = sns.load_dataset("titanic")
print(titanic.head())
print('-----')
# 加载数据

sns.barplot(x="sex", y="survived", hue="class", data=titanic,
            palette = 'hls', 
            order = ['male','female'],  # 筛选类别
            capsize = 0.05,  # 误差线横向延伸宽度
            saturation=.8,   # 颜色饱和度
            errcolor = 'gray',errwidth = 2,  # 误差线颜色，宽度
            #ci = None    # 置信区间误差 → 0-100内值、'sd'、None
            )
print(titanic.groupby(['sex','class']).mean()['survived'])
print(titanic.groupby(['sex','class']).std()['survived'])
# 计算数据

# 1、barplot()
# 柱状图 - 置信区间估计（柱为均值）

sns.barplot(x="day", y="total_bill", hue="sex", data=tips,
            palette = 'Blues',edgecolor = 'w')
tips.groupby(['day','sex']).mean()
# 计算数据

# 1、barplot()
# 柱状图 - 置信区间估计

crashes = sns.load_dataset("car_crashes").sort_values("total", ascending=False)
print(crashes.head())
# 加载数据

f, ax = plt.subplots(figsize=(6, 15))
# 创建图表

sns.set_color_codes("pastel")
sns.barplot(x="total", y="abbrev", data=crashes,
            label="Total", color="b",edgecolor = 'w')
# 设置第一个柱状图

sns.set_color_codes("muted")
sns.barplot(x="alcohol", y="abbrev", data=crashes,
            label="Alcohol-involved", color="b",edgecolor = 'w')
# 设置第二个柱状图

ax.legend(ncol=2, loc="lower right")
sns.despine(left=True, bottom=True)

# 2、countplot()
# 计数柱状图

sns.countplot(x="class", hue="who", data=titanic,palette = 'magma')
#sns.countplot(y="class", hue="who", data=titanic,palette = 'magma')  
# x/y → 以x或者y轴绘图（横向，竖向）
# 用法和barplot相似

# 3、pointplot()
# 折线图 - 置信区间估计

sns.pointplot(x="time", y="total_bill", hue = 'smoker',data=tips,
              palette = 'hls',
              dodge = True,   # 设置点是否分开
              join = True,    # 是否连线
              markers=["o", "x"], linestyles=["-", "--"],  # 设置点样式、线型
              )
tips.groupby(['time','smoker']).mean()['total_bill']
# 计算数据
# # 用法和barplot相似

# 基本用法

tips = sns.load_dataset("tips")
print(tips.head())
# 加载数据

sns.lmplot(x="total_bill", y="tip", hue = 'smoker',data=tips,palette="Set1",
           ci = 70,   # 误差值
           size = 5,  # 图表大小
           markers = ['+','o'],  # 点样式
           )

# 拆分多个表格

sns.lmplot(x="total_bill", y="tip", col="smoker", data=tips)

# 多图表1

sns.lmplot(x="size", y="total_bill", hue="day", col="day",data=tips, 
           aspect=0.6,    # 长宽比
           x_jitter=.30,  # 给x或者y轴随机增加噪音点
           col_wrap=4,    # 每行的列数
          )

# 多图表2
# 多个变量
sns.lmplot(x="total_bill", y="tip", row="sex", col="time",data=tips, size=4)
# 行为sex字段，列为time字段
# x轴total_bill, y轴tip

#单个变量
sns.regplot(x="total_bill", y="tip", data=data)

# 非线性回归

sns.lmplot(x="total_bill", y="tip",data=tips,
           order = 2)

# 1、时间线图表 - tsplot()
# 简单示例

x = np.linspace(0, 15, 31)
data = np.sin(x) + np.random.rand(10, 31) + np.random.randn(10, 1)
print(data.shape)
print(pd.DataFrame(data).head())
# 创建数据

sns.tsplot(data=data,
           err_style="ci_band",   # 误差数据风格，可选：ci_band, ci_bars, boot_traces, boot_kde, unit_traces, unit_points
           interpolate=True,      # 是否连线
           ci = [40,70,90],       # 设置误差区间 
           color = 'g'            # 设置颜色
          )

# 1、时间线图表 - tsplot()
# 简单示例

sns.tsplot(data=data, err_style="boot_traces", 
           n_boot=300   # 迭代次数
          )

# 1、时间线图表 - tsplot()
# 参数设置

gammas = sns.load_dataset("gammas")
print(gammas.head())
print('数据量为：%i条' % len(gammas))
print('timepoint为0.0时的数据量为：%i条' % len(gammas[gammas['timepoint'] == 0]))
print('timepoint共有%i个唯一值' % len(gammas['timepoint'].value_counts()))
#print(gammas['timepoint'].value_counts())  # 查看唯一值具体信息
# 导入数据

sns.tsplot(time="timepoint",     # 时间数据，x轴
           value="BOLD signal",  # y轴value
           unit="subject",       # 类似index
           condition="ROI",      # 分类
           data=gammas)

# 2、热图 - heatmap()
# 简单示例

df = pd.DataFrame(np.random.rand(10,12))
# 创建数据 - 10*12图表

sns.heatmap(df,    # 加载数据
            vmin=0, vmax=1   # 设置图例最大最小值
            )

# 2、热图 - heatmap()
# 参数设置

flights = sns.load_dataset("flights")
flights = flights.pivot("month", "year", "passengers") 
print(flights.head())
# 加载数据
           
sns.heatmap(flights,
            annot = True,      # 是否显示数值
            fmt = 'd',         # 格式化字符串
            linewidths = 0.2,  # 格子边线宽度
            #center = 100,      # 调色盘的色彩中心值，若没有指定，则以cmap为主
            #cmap = 'Reds',     # 设置调色盘
            cbar = True,       # 是否显示图例色带
            #cbar_kws={"orientation": "horizontal"},   # 是否横向显示图例色带
            #annot_kws={"size": 6} #设置热力图矩阵上数字的大小颜色字体
            #square = True,     # 是否正方形显示图表
           )

# 2、热图 - heatmap()
# 绘制半边热图

sns.set(style="white")
# 设置风格

rs = np.random.RandomState(33)
d = pd.DataFrame(rs.normal(size=(100, 26)))
corr = d.corr()   # 求解相关性矩阵表格
# 创建数据

mask = np.zeros_like(corr, dtype=np.bool)
mask[np.triu_indices_from(mask)] = True
# 设置一个“上三角形”蒙版

cmap = sns.diverging_palette(220, 10, as_cmap=True)
# 设置调色盘

sns.heatmap(corr, mask=mask, cmap=cmap, vmax=.3, center=0,
            square=True, linewidths=0.2)
# 生成半边热图

# 1、基本设置
# 绘制直方图

tips = sns.load_dataset("tips")
print(tips.head())
# 导入数据

g = sns.FacetGrid(tips, col="time", row="smoker")
# 创建一个绘图表格区域，设置好row、col并分组

g.map(plt.hist, "total_bill",alpha = 0.5,color = 'k',bins = 10)
# 以total_bill字段数据分别做直方图统计

# 1、基本设置
# 绘制直方图

g = sns.FacetGrid(tips, col="day", 
                  size=4,    # 图表大小
                  aspect=.5) # 图表长宽比

g.map(plt.hist, "total_bill", bins=10,
      histtype = 'step',   #'bar', 'barstacked', 'step', 'stepfilled'
      color = 'k')

# 1、基本设置
# 绘制散点图

g = sns.FacetGrid(tips, col="time",  row="smoker"
                  ,size=4,aspect=1.2)
# 创建一个绘图表格区域，设置好row、col并分组

g.map(plt.scatter, 
      "total_bill", "tip",    # share{x,y} → 设置x、y数据
      edgecolor="w", s = 40, linewidth = 1)   # 设置点大小，描边宽度及颜色
g.add_legend()
# 添加图例

# 1、基本设置
# 分类

g = sns.FacetGrid(tips, col="time",  hue="smoker")
# 创建一个绘图表格区域，设置好col并分组，按hue分类

g.map(plt.scatter, 
      "total_bill", "tip",    # share{x,y} → 设置x、y数据
      edgecolor="w", s = 40, linewidth = 1)   # 设置点大小，描边宽度及颜色
g.add_legend()
# 添加图例

# 2、图表矩阵

attend = sns.load_dataset("attention")
print(attend.head())
# 加载数据

g = sns.FacetGrid(attend, col="subject", col_wrap=5,   # 设置每行的图表数量
                  size=1.5)
g.map(plt.plot, "solutions", "score", 
      marker="o",color = 'gray',linewidth = 2)
# 绘制图表矩阵

g.set(xlim = (0,4),
      ylim = (0,10),
      xticks = [0,1,2,3,4],
      yticks = [0,2,4,6,8,10]
      )


from bokeh.plotting import figure,show
#from bokeh.io import output_notebook
# 导入notebook绘图模块
#output_notebook()
# notebook绘图命令
p = figure(plot_width=400, plot_height=400)   # 创建图表，设置宽度、高度
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)
# 创建一个圆形散点图
show(p)

# 在spyder等非notebook中创建绘图空间
from bokeh.plotting import figure,show,output_file
# 导入图表绘制、图标展示模块
# output_file → 非notebook中创建绘图空间
output_file("line.html")
# notebook绘图命令，创建html文件
# 运行后会弹出html窗口
p = figure(plot_width=400, plot_height=400)   # 创建图表，设置宽度、高度
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="blue", alpha=0.5)
# 创建一个圆形散点图
show(p)

# 在spyder等非notebook中创建绘图空间

from bokeh.plotting import figure,show,output_file
# 导入图表绘制、图标展示模块
# output_file → 非notebook中创建绘图空间

import os
os.chdir(r'D:\在读')
# 创建工作目录

output_file("line.html")
# notebook绘图命令，创建html文件
# 运行后会弹出html窗口

p = figure(plot_width=400, plot_height=400)   # 创建图表，设置宽度、高度
p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="blue", alpha=0.5)
# 创建一个圆形散点图

show(p)
# 绘图

# 创建图表工具 
# figure()

df = pd.DataFrame(np.random.randn(100,2),columns = ['A','B'])
# 创建数据

p = figure(plot_width=600, plot_height=400,    # 图表宽度、高度
           tools = 'pan,wheel_zoom,box_zoom,save,reset,help',  # 设置工具栏，默认全部显示
           toolbar_location='above',     # 工具栏位置："above"，"below"，"left"，"right"
           x_axis_label = 'A', y_axis_label = 'B',    # X,Y轴label
           x_range = [-3,3], y_range = [-3,3],        # X,Y轴范围
           title="测试图表"                       # 设置图表title
          )
# figure创建图表，设置基本参数
# tool参考文档：https://bokeh.pydata.org/en/latest/docs/user_guide/tools.html

p.title.text_color = "white"
p.title.text_font = "times"
p.title.text_font_style = "italic"
p.title.background_fill_color = "black"
# 设置标题：颜色、字体、风格、背景颜色

p.circle(df['A'], df['B'], size=20,  alpha=0.5)
show(p)
# 创建散点图
# 这里.circle()是figure的一个绘图方法

# 颜色设置

p = figure(plot_width=600, plot_height=400)
# 创建绘图空间

p.circle(df.index, df['A'], color = 'green', size=10,  alpha=0.5)
p.circle(df.index, df['B'], color = '#FF0000', size=10,  alpha=0.5)
show(p)
# 颜色设置
# ① 147个CSS颜色，参考网址：http://www.colors.commutercreative.com/grid/
# ② RGB颜色值，参考网址：https://coolors.co/87f1ff-c0f5fa-bd8b9c-af125a-582b11

# 图表边框线参数设置

p = figure(plot_width=600, plot_height=400)
p.circle(df.index, df['A'], color = 'green', size=10,  alpha=0.5)
p.circle(df.index, df['B'], color = '#FF0000', size=10,  alpha=0.5)
# 绘制散点图
 
p.outline_line_width = 7         # 边框线宽
p.outline_line_alpha = 0.3       # 边框线透明度
p.outline_line_color = "navy"    # 边框线颜色
# 设置图表边框

show(p)

# 设置绘图空间背景

p = figure(plot_width=600, plot_height=400)
p.circle(df.index, df['A'], color = 'green', size=10,  alpha=0.5)
p.circle(df.index, df['B'], color = '#FF0000', size=10,  alpha=0.5)
# 绘制散点图

p.background_fill_color = "beige"    # 绘图空间背景颜色
p.background_fill_alpha = 0.5        # 绘图空间背景透明度
# 背景设置参数

show(p)

# 设置外边界背景

p = figure(plot_width=600, plot_height=400)
p.circle(df.index, df['A'], color = 'green', size=10,  alpha=0.5)
p.circle(df.index, df['B'], color = '#FF0000', size=10,  alpha=0.5)
# 绘制散点图

p.border_fill_color = "whitesmoke"    # 外边界背景颜色
p.min_border_left = 80                # 外边界背景 - 左边宽度
p.min_border_right = 80               # 外边界背景 - 右边宽度
p.min_border_top = 10                 # 外边界背景 - 上宽度
p.min_border_bottom = 10              # 外边界背景 - 下宽度

show(p)

# Axes - 轴线设置
# 轴线标签、轴线线宽、轴线颜色
# 字体颜色、字体角度

p = figure(plot_width=400, plot_height=400)
p.circle([1,2,3,4,5], [2,5,8,2,7], size=10)
# 绘制图表

p.xaxis.axis_label = "Temp"
p.xaxis.axis_line_width = 3
p.xaxis.axis_line_color = "red"
p.xaxis.axis_line_dash = [6,4]
# 设置x轴线：标签、线宽、轴线颜色

p.yaxis.axis_label = "Pressure"
p.yaxis.major_label_text_color = "orange"
p.yaxis.major_label_orientation = "vertical"
# 设置y轴线：标签、字体颜色、字体角度

p.axis.minor_tick_in = 5      # 刻度往绘图区域内延伸长度
p.axis.minor_tick_out = 3   # 刻度往绘图区域外延伸长度
# 设置刻度

p.xaxis.bounds = (2, 4)
# 设置轴线范围

show(p)

# Axes - 轴线设置
# 标签设置

p = figure(plot_width=400, plot_height=400)
p.circle([1,2,3,4,5], [2,5,8,2,7], size=10)

p.xaxis.axis_label = "Lot Number"
p.xaxis.axis_label_text_color = "#aa6666"
p.xaxis.axis_label_standoff = 30
# 设置标签名称、字体颜色、偏移距离

p.yaxis.axis_label = "Bin Count"
p.yaxis.axis_label_text_font_style = "italic"
# 设置标签名称、字体

show(p)

# Grid - 格网设置
# 线型设置

p = figure(plot_width=600, plot_height=400)
p.circle(df.index, df['A'], color = 'green', size=10,  alpha=0.5)
p.circle(df.index, df['B'], color = '#FF0000', size=10,  alpha=0.5)
# 绘制散点图

p.xgrid.grid_line_color = None
# 颜色设置，None时则不显示

p.ygrid.grid_line_alpha = 0.8
p.ygrid.grid_line_dash = [6, 4]
# 设置透明度，虚线设置
# dash → 通过设置间隔来做虚线

p.xgrid.minor_grid_line_color = 'navy'
p.xgrid.minor_grid_line_alpha = 0.1
# minor_line → 设置次轴线

show(p)

# Grid - 格网设置
# 颜色填充

p = figure(plot_width=600, plot_height=400)
p.circle(df.index, df['A'], color = 'green', size=10,  alpha=0.5)
p.circle(df.index, df['B'], color = '#FF0000', size=10,  alpha=0.5)
# 绘制散点图

p.xgrid.grid_line_color = None
# 设置颜色为空

p.ygrid.band_fill_alpha = 0.1
p.ygrid.band_fill_color = "navy"
# 设置颜色填充，及透明度

#p.grid.bounds = (-1, 1)
# 设置填充边界

show(p)

# Legend - 图例设置
# 设置方法 → 在绘图时设置图例名称 + 设置图例位置

p = figure(plot_width=600, plot_height=400)
# 创建图表

x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)
# 设置x，y

p.circle(x, y, legend="sin(x)")
p.line(x, y, legend="sin(x)")
# 绘制line1，设置图例名称

p.line(x, 2*y, legend="2*sin(x)",line_dash=[4, 4], line_color="orange", line_width=2)
# 绘制line2，设置图例名称

p.square(x, 3*y, legend="3*sin(x)", fill_color=None, line_color="green")
p.line(x, 3*y, legend="3*sin(x)", line_color="green")
# 绘制line3，设置图例名称

p.legend.location = "bottom_left"
# 设置图例位置："top_left"、"top_center"、"top_right" (the default)、"center_right"、"bottom_right"、"bottom_center"
# "bottom_left"、"center_left"、"center"

p.legend.orientation = "vertical"
# 设置图例排列方向："vertical" （默认）or "horizontal"

p.legend.label_text_font = "times"
p.legend.label_text_font_style = "italic"  # 斜体
p.legend.label_text_color = "navy"
p.legend.label_text_font_size = '12pt'
# 设置图例：字体、风格、颜色、字体大小

p.legend.border_line_width = 3
p.legend.border_line_color = "navy"
p.legend.border_line_alpha = 0.5
# 设置图例外边线：宽度、颜色、透明度

p.legend.background_fill_color = "gray"
p.legend.background_fill_alpha = 0.2
# 设置图例背景：颜色、透明度

show(p)

#总结一下：
#Line Properties → 线设置
#Fill Properties → 填充设置
#Text Properties → 字体设置
#
#1、Line Properties → 线设置
#（1）line_color，设置颜色
#（2）line_width，设置宽度
#（3）line_alpha，设置透明度
#（4）line_join，设置连接点样式：'miter' miter_join，'round' round_join，'bevel' bevel_join
#（5）line_cap，设置线端口样式，'butt' butt_cap，'round' round_cap，'square' square_cap
#（6）line_dash，设置线条样式，'solid'，'dashed'，'dotted'，'dotdash'，'dashdot'，或者整型数组方式（例如[6,4]）
#
#2、Fill Properties → 填充设置
#（1）fill_color，设置填充颜色
#（2）fill_alpha，设置填充透明度
#
#3、Text Properties → 字体设置
#（1）text_font，字体
#（2）text_font_size，字体大小，单位为pt或者em（ '12pt', '1.5em'）
#（3）text_font_style，字体风格，'normal' normal text，'italic' italic text，'bold' bold text
#（4）text_color，字体颜色
#（5）text_alpha，字体透明度
#（6）text_align，字体水平方向位置，'left', 'right', 'center'
#（7）text_baseline，字体垂直方向位置，'top'，'middle'，'bottom'，'alphabetic'，'hanging'
#
#4、可见性
#p.xaxis.visible = False
#p.xgrid.visible = False
#基本参数中都含有.visible参数，设置是否可见
             
# 辅助标注 - 线

from bokeh.models.annotations import Span
# 导入Span模块

x = np.linspace(0, 20, 200)
y = np.sin(x)
# 创建x，y数据

p = figure(y_range=(-2, 2))
p.line(x, y)
# 绘制曲线

upper = Span(location=1,           # 设置位置，对应坐标值
             dimension='width',    # 设置方向，width为横向，height为纵向  
             line_color='olive', line_width=4   # 设置线颜色、线宽
            )
p.add_layout(upper)
# 绘制辅助线1

lower = Span(location=-1, dimension='width', line_color='firebrick', line_width=4)
p.add_layout(lower)
# 绘制辅助线2

show(p)

# 辅助标注 - 矩形

from bokeh.models.annotations import BoxAnnotation
# 导入BoxAnnotation模块

x = np.linspace(0, 20, 200)
y = np.sin(x)
# 创建x，y数据

p = figure(y_range=(-2, 2))
p.line(x, y)
# 绘制曲线

upper = BoxAnnotation(bottom=1, fill_alpha=0.1, fill_color='olive')
p.add_layout(upper)
# 绘制辅助矩形1

lower = BoxAnnotation(top=-1, fill_alpha=0.1, fill_color='firebrick')
p.add_layout(lower)
# 绘制辅助矩形2

center = BoxAnnotation(top=0.6, bottom=-0.3, left=7, right=12,  # 设置矩形四边位置
                       fill_alpha=0.1, fill_color='navy'        # 设置透明度、颜色
                      )
p.add_layout(center)
# 绘制辅助矩形3

show(p)

# 绘图注释

from bokeh.models.annotations import Label
# 导入Label模块，注意是annotations中的Label

p = figure(x_range=(0,10), y_range=(0,10))
p.circle([2, 5, 8], [4, 7, 6], color="olive", size=10)
# 绘制散点图

label = Label(x=5, y=7,       # 标注注释位置
              x_offset=12,    # x偏移，同理y_offset
              text="Second Point",      # 注释内容
              text_font_size="12pt",    # 字体大小
              border_line_color="red", background_fill_color="gray", background_fill_alpha = 0.5   # 背景线条颜色、背景颜色、透明度
             )
p.add_layout(label)
# 绘制注释

show(p)

# 注释箭头

from bokeh.models.annotations import Arrow
from bokeh.models.arrow_heads import OpenHead, NormalHead, VeeHead   # 三种箭头类型
# 导入相关模块

p = figure(plot_width=600, plot_height=600)
p.circle(x=[0, 1, 0.5], y=[0, 0, 0.7], radius=0.1, color=["navy", "yellow", "red"], fill_alpha=0.1)
# 创建散点图

p.add_layout(Arrow(end=OpenHead(line_color="firebrick", line_width=4),  # 设置箭头类型，及相关参数：OpenHead, NormalHead, VeeHead
                   x_start=0, y_start=0, x_end=1, y_end=0))   # 设置箭头矢量方向
# 绘制箭头1

p.add_layout(Arrow(end=NormalHead(fill_color="orange"),
                   x_start=1, y_start=0, x_end=0.5, y_end=0.7))
# 绘制箭头2

p.add_layout(Arrow(end=VeeHead(size=35), line_color="red",
                   x_start=0.5, y_start=0.7, x_end=0, y_end=0))
# 绘制箭头3

show(p)

# 调色盘
# 颜色参考文档：http://bokeh.pydata.org/en/latest/docs/reference/palettes.html
# ColorBrewer：http://colorbrewer2.org/#type=sequential&scheme=BuGn&n=3

import bokeh.palettes as bp
from bokeh.palettes import brewer

print('所有调色板名称：\n',bp.__palettes__)
print('-------')
# 查看所有调色板名称

print('蓝色调色盘颜色：\n',bp.Blues)
print('-------')
# 查看蓝色调色盘颜色

n = 8
colori = brewer['YlGn'][n]   
print('YlGn调色盘解析为%i个颜色，分别为：\n' % n, colori)
# 调色盘解析 → 不同颜色解析最多颜色有限

# 1、基本散点图绘制

s = pd.Series(np.random.randn(80))
# 创建数据

p = figure(plot_width=600, plot_height=400)
p.circle(s.index, s.values,                  # x，y值，也可以写成：x=s.index, y = s.values
         size=25, color="navy", alpha=0.5,   # 点的大小、颜色、透明度（注意，这里的color是线+填充的颜色，同时线和填充可以分别上色，参数如下）
         fill_color = 'red',fill_alpha = 0.6, # 填充的颜色、透明度
         line_color = 'black',line_alpha = 0.8,line_dash = 'dashed',line_width = 2,   # 点边线的颜色、透明度、虚线、宽度
         # 同时还有line_cap、line_dash_offset、line_join参数    
         legend = 'scatter-circle',    # 设置图例
         #radius = 2   # 设置点的半径，和size只能同时选一个
        )
# 创建散点图，基本参数
# bokeh对line和fill是同样的设置方法

p.legend.location = "bottom_right"
# 设置图例位置

show(p)

# 2、散点图不同 颜色上色/散点大小 的方法
# ① 数据中有一列专门用于设置颜色 / 点大小

from bokeh.palettes import brewer

rng = np.random.RandomState(1)
df = pd.DataFrame(rng.randn(100,2)*100,columns = ['A','B'])
# 创建数据，有2列随机值

df['size'] = rng.randint(10,30,100)   
# 设置点大小字段

colormap1 = {1: 'red', 2: 'green', 3: 'blue'}    
df['color1'] = [colormap1[x] for x in rng.randint(1,4,100)]           # 调色盘1
#=df['color1'] = np.random.choice(['red','green','blue'],100)

n = 8
colormap2 = brewer['Blues'][n]
df['color2'] = [colormap2[x] for x in rng.randint(0,n,100)]           # 调色盘2
# 设置颜色字段
# 通过字典/列表，识别颜色str
# 这里设置了两个调色盘，第二个为蓝色渐变

p = figure(plot_width=600, plot_height=400)
p.circle(df['A'], df['B'],       # 设置散点图x，y值
         line_color = 'white',   # 设置点边线为白色
         fill_color = df['color2'],fill_alpha = 0.5,   # 设置内部填充颜色，这里用到了颜色字段
         size = df['size']       # 设置点大小，这里用到了点大小字段
        )

show(p)

# 2、散点图不同 颜色上色/散点大小 的方法
# ② 遍历数据分开做图

rng = np.random.RandomState(1)
df = pd.DataFrame(rng.randn(100,2)*100,columns = ['A','B'])
df['type'] = rng.randint(0,7,100)
print(df.head())
# 创建数据

colors = ["red", "olive", "darkred", "goldenrod", "skyblue", "orange", "salmon"]
# 创建颜色列表

p = figure(plot_width=600, plot_height=400,tools = "pan,wheel_zoom,box_select,lasso_select,reset")
for t in df['type'].unique():
    p.circle(df['A'][df['type'] == t], df['B'][df['type'] == t],       # 设置散点图x，y值
             size = 20,alpha = 0.5,
             color = colors[t])        
# 通过分类设置颜色

show(p)

# 3、不同符号的散点图
# asterisk(), circle(), circle_cross(), circle_x(), cross(), diamond(), diamond_cross(), inverted_triangle()
# square(), square_cross(), square_x(), triangle(), x()

p = figure(plot_width=600, plot_height=400,x_range = [0,3], y_range = [0,7])

p.circle_cross(1, 1, size = 30, alpha = 0.5, legend = 'circle_cross')
p.asterisk(1, 2, size = 30, alpha = 0.5, legend = 'asterisk')
p.circle_x(1, 3, size = 30, alpha = 0.5, legend = 'circle_x')
p.cross(1, 4, size = 30, alpha = 0.5, legend = 'cross')
p.diamond(1, 5, size = 30, alpha = 0.5, legend = 'diamond')
p.diamond_cross(1, 6, size = 30, alpha = 0.5, legend = 'diamond_cross')
p.inverted_triangle(2, 1, size = 30, alpha = 0.5, legend = 'inverted_triangle')
p.square(2, 2, size = 30, alpha = 0.5, legend = 'square')
p.square_cross(2, 3, size = 30, alpha = 0.5, legend = 'square_cross')
p.square_x(2, 4, size = 30, alpha = 0.5, legend = 'square_x')
p.triangle(2, 5, size = 30, alpha = 0.5, legend = 'triangle')
p.x(2, 6, size = 30, alpha = 0.5, legend = 'x')

p.legend.location = "bottom_right"
# 设置图例位置

show(p)
# 详细参数可参考文档：http://bokeh.pydata.org/en/latest/docs/reference/plotting.html#bokeh.plotting.figure.Figure.circle


# 1、折线图 - 单线图

from bokeh.models import ColumnDataSource
# 导入ColumnDataSource模块
# 将数据存储为ColumnDataSource对象
# 参考文档：http://bokeh.pydata.org/en/latest/docs/user_guide/data.html
# 可以将dict、Dataframe、group对象转化为ColumnDataSource对象

df = pd.DataFrame({'value':np.random.randn(100).cumsum()})
# 创建数据

df.index.name = 'index'
source = ColumnDataSource(data = df)
# 转化为ColumnDataSource对象
# 这里注意了，index和columns都必须有名称字段

p = figure(plot_width=600, plot_height=400)
p.line(x='index',y='value',source = source,     # 设置x，y值, source → 数据源
       line_width=1, line_alpha = 0.8, line_color = 'black',line_dash = [10,4])   # 线型基本设置
# 绘制折线图
p.circle(x='index',y='value',source = source, 
         size = 2,color = 'red',alpha = 0.8)
# 绘制折点

show(p)

df2 = pd. DataFrame (np.random.randn(100, 2), columns = ['A','B'])
source = ColumnDataSource(data = df2)
p = figure()
p.circle(x = 'A', y = 'B' , source = source) 
show (p)


# 1、折线图 - 多线图
# ① multi_line

df = pd.DataFrame({'A':np.random.randn(100).cumsum(),"B":np.random.randn(100).cumsum()})
# 创建数据

p = figure(plot_width=600, plot_height=400)
p.multi_line([df.index, df.index], [df['A'], df['B']],   # 注意x，y值的设置 → [x1,x2,x3,..], [y1,y2,y3,...]
             color=["firebrick", "navy"],    # 可同时设置 → color= "firebrick"
             alpha=[0.8, 0.6],     # 可同时设置 → alpha = 0.6
             line_width=[2,1],     # 可同时设置 → line_width = 2
            )
# 绘制多段线
# 这里由于需要输入具体值，故直接用dataframe，或者dict即可

show(p)  
             
             
# 1、折线图 - 多线图
# ② 多个line

x = np.linspace(0.1, 5, 100)
# 创建x值

p = figure(title="log axis example", y_axis_type="log",y_range=(0.001, 10**22))
# 这里设置对数坐标轴

p.line(x, np.sqrt(x), legend="y=sqrt(x)",
       line_color="tomato", line_dash="dotdash")
# line1

p.line(x, x, legend="y=x")
p.circle(x, x, legend="y=x")
# line2，折线图+散点图

p.line(x, x**2, legend="y=x**2")
p.circle(x, x**2, legend="y=x**2",fill_color=None, line_color="olivedrab")
# line3

p.line(x, 10**x, legend="y=10^x",line_color="gold", line_width=2)
# line4

p.line(x, x**x, legend="y=x^x",line_dash="dotted", line_color="indigo", line_width=2)
# line5

p.line(x, 10**(x**2), legend="y=10^(x^2)",line_color="coral", line_dash="dashed", line_width=2)
# line6

p.legend.location = "top_left"
p.xaxis.axis_label = 'Domain'
p.yaxis.axis_label = 'Values (log scale)'
# 设置图例及label

show(p)

# 2、面积图 - 单维度面积图

s = pd.Series(np.random.randn(100).cumsum())
s.iloc[0] = 0
s.iloc[-1] = 0
# 创建数据
# 注意设定起始值和终点值为最低点

p = figure(plot_width=600, plot_height=400)
p.patch(s.index, s.values,     # 设置x，y值
        line_width=1, line_alpha = 0.8, line_color = 'black',line_dash = [10,4],   # 线型基本设置
        fill_color = 'black',fill_alpha = 0.2
        )
# 绘制面积图
# .patch将会把所有点连接成一个闭合面

p.circle(s.index, s.values,size = 5,color = 'red',alpha = 0.8)
# 绘制折点

show(p)

# 2、面积图 - 面积堆叠图

from bokeh.palettes import brewer
# 导入brewer模块

N = 20
cats = 10
rng = np.random.RandomState(1)
df = pd.DataFrame(rng.randint(10, 100, size=(N, cats))).add_prefix('y')
# 创建数据，shape为（20，10）

df_top = df.cumsum(axis=1)   # 每一个堆叠面积图的最高点
df_bottom = df_top.shift(axis=1).fillna({'y0': 0})[::-1]    # 每一个堆叠面积图的最低点，并反向【顺时针画图】
df_stack = pd.concat([df_bottom, df_top], ignore_index=True)   # 数据合并，每一组数据都是一个可以围合成一个面的散点集合
# 得到堆叠面积数据

colors = brewer['Spectral'][df_stack.shape[1]]    # 根据变量数拆分颜色
x = np.hstack((df.index[::-1], df.index))         # 得到围合顺序的index，这里由于一列是20个元素，所以连接成面需要40个点

p = figure(x_range=(0, N-1), y_range=(0, 700))
p.patches([x] * df_stack.shape[1],                       # 得到10组index
          [df_stack[c].values for c in df_stack],     # c为df_stack的列名，这里得到10组对应的valyes
          color=colors, alpha=0.8, line_color=None)   # 设置其他参数

show(p)


# 1、单系列柱状图
# vbar

p = figure(plot_width=400, plot_height=400)
p.vbar(x=[1, 2, 3], width=0.5, bottom=0,top=[1.2, 2.5, 3.7],  # x：横轴坐标，width：宽度，bottom：底高度，top：顶高度
       #color = ['red','blue','green'], alpha = 0.8   # 整体颜色设置，也可单独设置 → color="firebrick"
       line_width = 1,line_alpha = 0.8,line_color = 'black', line_dash = [5,2],    # 单独设置线参数
       fill_color = 'red',fill_alpha = 0.6    # 单独设置填充颜色参数
      )
# 绘制竖向柱状图

show(p)

# 1、单系列柱状图
# hbar

p = figure(plot_width=400, plot_height=400)
p.hbar(y=[1, 2, 3], height=0.5, left=0,right=[1.2, 2.5, 3.7],  # y：纵轴坐标，height：厚度，left：左边最小值，right：右边最大值
       color = ['red','blue','green'])
# 绘制竖向柱状图

show(p)

# 1、单系列柱状图 - 分类设置标签
# ColumnDataSource

from bokeh.palettes import Spectral6
from bokeh.transform import factor_cmap
# 导入相关模块

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
counts = [5, 3, 4, 2, 4, 6]
source = ColumnDataSource(data=dict(fruits=fruits, counts=counts))
colors = [ "salmon", "olive", "darkred", "goldenrod", "skyblue", "orange"]
# 创建一个包含标签的data，对象类型为ColumnDataSource

p = figure(x_range=fruits, y_range=(0,9), plot_height=350, title="Fruit Counts",tools="")

p.vbar(x='fruits', top='counts', source=source,    # 加载数据另一个方式
       width=0.9, alpha = 0.8,
       color = factor_cmap('fruits', palette=Spectral6, factors=fruits),    # 设置颜色
       legend="fruits")
# 绘制柱状图，横轴直接显示标签
# factor_cmap(field_name, palette, factors, start=0, end=None, nan_color='gray')：颜色转换模块，生成一个颜色转换对象
# field_name：分类名称
# palette：调色盘
# factors：用于在调色盘中分颜色的参数
# 参考文档：http://bokeh.pydata.org/en/latest/docs/reference/transform.html

p.xgrid.grid_line_color = None
p.legend.orientation = "horizontal"
p.legend.location = "top_center"
# 其他参数设置

show(p)

# 2、多系列柱状图
# vbar

from bokeh.transform import dodge
from bokeh.core.properties import value
# 导入dodge、value模块

df = pd.DataFrame({'2015':[2, 1, 4, 3, 2, 4],'2016':[5, 3, 3, 2, 4, 6], '2017':[3, 2, 4, 4, 5, 3]},
                 index = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries'])
# 创建数据

fruits = df.index.tolist()   # 横坐标
years = df.columns.tolist()    # 系列名
data = {'index':fruits}
for year in years:
    data[year] = df[year].tolist()
print(data)
# 生成数据，数据格式为dict

source = ColumnDataSource(data=data)
# 将数据转化为ColumnDataSource对象

p = figure(x_range=fruits, y_range=(0, 10), plot_height=350, title="Fruit Counts by Year",tools="")

p.vbar(x=dodge('index', -0.25, range=p.x_range), top='2015', width=0.2, source=source,color="#c9d9d3", legend=value("2015"))
p.vbar(x=dodge('index',  0.0,  range=p.x_range), top='2016', width=0.2, source=source,color="#718dbf", legend=value("2016"))
p.vbar(x=dodge('index',  0.25, range=p.x_range), top='2017', width=0.2, source=source,color="#e84d60", legend=value("2017"))
# 绘制多系列柱状图
# dodge(field_name, value, range=None) → 转换成一个可分组的对象，value为元素的位置（配合width设置）
# value(val, transform=None) → 按照年份分为dict

p.xgrid.grid_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"
# 其他参数设置

show(p)

# 3、堆叠图

from bokeh.core.properties import value
# 导入value模块

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ["2015", "2016", "2017"]
colors = ["#c9d9d3", "#718dbf", "#e84d60"]
data = {'fruits' : fruits,
        '2015'   : [2, 1, 4, 3, 2, 4],
        '2016'   : [5, 3, 4, 2, 4, 6],
        '2017'   : [3, 2, 4, 4, 5, 3]}
source = ColumnDataSource(data=data)
# 创建数据

p = figure(x_range=fruits, plot_height=350, title="Fruit Counts by Year",tools="")
renderers = p.vbar_stack(years,          # 设置堆叠值，这里source中包含了不同年份的值，years变量用于识别不同堆叠层
                         x='fruits',     # 设置x坐标
                         source=source,
                         width=0.9, color=colors,
                         legend=[value(x) for x in years], name=years)
# 绘制堆叠图
# 注意第一个参数需要放years

p.xgrid.grid_line_color = None
p.axis.minor_tick_line_color = None
p.outline_line_color = None
p.legend.location = "top_left"
p.legend.orientation = "horizontal"
# 设置其他参数

show(p)

# 3、堆叠图

from bokeh.palettes import GnBu3, OrRd3
# 导入颜色模块

fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
years = ["2015", "2016", "2017"]
exports = {'fruits' : fruits,
           '2015'   : [2, 1, 4, 3, 2, 4],
           '2016'   : [5, 3, 4, 2, 4, 6],
           '2017'   : [3, 2, 4, 4, 5, 3]}
imports = {'fruits' : fruits,
           '2015'   : [-1, 0, -1, -3, -2, -1],
           '2016'   : [-2, -1, -3, -1, -2, -2],
           '2017'   : [-1, -2, -1, 0, -2, -2]}

p = figure(y_range=fruits, plot_height=350, x_range=(-16, 16), title="Fruit import/export, by year")

p.hbar_stack(years, y='fruits', height=0.9, color=GnBu3, source=ColumnDataSource(exports),
             legend=["%s exports" % x for x in years])      # 绘制出口数据堆叠图

p.hbar_stack(years, y='fruits', height=0.9, color=OrRd3, source=ColumnDataSource(imports),
             legend=["%s imports" % x for x in years])      # 绘制进口数据堆叠图，这里值为负值

p.y_range.range_padding = 0.2     # 调整边界间隔
p.ygrid.grid_line_color = None   
p.legend.location = "top_left"
p.axis.minor_tick_line_color = None
p.outline_line_color = None
# 设置其他参数

show(p)

# 4、直方图
# np.histogram + figure.quad()
# 不需要构建ColumnDataSource对象

df = pd.DataFrame({'value': np.random.randn(1000)*100})
df.index.name = 'index'
print(df.head())
# 创建数据

hist, edges = np.histogram(df['value'],bins=20)
print(hist[:5])
print(edges)
# 将数据解析成直方图统计格式
# 高阶函数np.histogram(a, bins=10, range=None, weights=None, density=None) 
# a：数据
# bins：箱数
# range：最大最小值的范围，如果不设定则为(a.min(), a.max())
# weights：权重
# density：为True则返回“频率”，为False则返回“计数”
# 返回值1 - hist：每个箱子的统计值（top）
# 返回值2 - edges：每个箱子的位置坐标，这里n个bins将会有n+1个edges

p = figure(title="HIST", tools="save",background_fill_color="#E8DDCB")
p.quad(top=hist, bottom=0, left=edges[:-1], right=edges[1:],   # 分别代表每个柱子的四边值
        fill_color="#036564", line_color="#033649")
# figure.quad绘制直方图

show(p)


# 1、轴线标签设置
# 设置字符串

df = pd.DataFrame({'score':[98,86,74,67,87]},index = ['小明','小王','小张','小红','小红帽'])
df.index.name = 'name'
#print(df)
# 创建数据

source = ColumnDataSource(df)
# 讲数据转化为ColumnDataSource对象

name = df.index.tolist()   # 提取name
p = figure(x_range=name, y_range=(60,100), plot_height=350, title="考试成绩",tools="")
# 通过x_range设置横轴标签，这里提取成list

p.circle(x = 'name', y = 'score', source = source,
         size = 20, line_color = 'black', line_dash = [6,4],
         fill_color = 'red',fill_alpha = 0.8)

show(p)

# 1、轴线标签设置
# 时间序列设置
# Dataframe DatetimeIndex + x_axis_type

from bokeh.sampledata.commits import data
print(data.head())
print(type(data.index))
# 导入数据，查看数据
# 这里index为时间序列

DAYS = ['Sun', 'Sat', 'Fri', 'Thu', 'Wed', 'Tue', 'Mon']
source = ColumnDataSource(data)
# 转化为ColumnDataSource对象

p = figure(plot_width=800, plot_height=600, 
           y_range=DAYS,                     # 设置图表的y轴刻度分类
           x_axis_type='datetime',           # 设置x轴类型 → 时间序列
           title="Commits by Time of Day (US/Central) 2012-2016")

p.circle(x='time', y='day',  source=source, alpha=0.2)
# 生成散点图

p.ygrid.grid_line_color = None
# 设置其他参数

show(p)

# 1、轴线标签设置
# 设置对数坐标轴

x = [0.1, 0.5, 1.0, 1.5, 2.0, 2.5, 3.0]
y = [10**xx for xx in x]
# 创建数据

p = figure(plot_width=400, plot_height=400, 
           y_axis_type="log")    
# y_axis_type="log" → 对数坐标轴

p.line(x, y, line_width=2)
p.circle(x, y, fill_color="white", size=8)

show(p)

# 2、浮动设置
# Jitter
# 参考文档：https://bokeh.pydata.org/en/latest/docs/reference/transform.html

from bokeh.transform import jitter

DAYS = ['Sun', 'Sat', 'Fri', 'Thu', 'Wed', 'Tue', 'Mon']
source = ColumnDataSource(data)
# 转化为ColumnDataSource对象

p = figure(plot_width=800, plot_height=600, 
           y_range=DAYS,                     # 设置图表的y轴刻度分类
           x_axis_type='datetime',           # 设置x轴类型 → 时间序列
           title="Commits by Time of Day (US/Central) 2012-2016")

p.circle(x='time', 
         y=jitter('day', width=0.6, range=p.y_range),
         source=source, alpha=0.3)
# jitter参数 → 'day'：第一参数，这里指y的值，width：间隔宽度比例，range：分类范围对象，这里和y轴的分类一致

p.ygrid.grid_line_color = None
# 设置其他参数

show(p)

# 3、多图表设置
# gridplot

from bokeh.layouts import gridplot
# 导入gridplot模块

x = list(range(11))
y0 = x
y1 = [10-xx for xx in x]
y2 = [abs(xx-5) for xx in x]
# 创建数据

s1 = figure(plot_width=250, plot_height=250, title=None)
s1.circle(x, y0, size=10, color="navy", alpha=0.5)
# 散点图1

s2 = figure(plot_width=250, plot_height=250, x_range=s1.x_range, y_range=s1.y_range, title=None)
s2.triangle(x, y1, size=10, color="firebrick", alpha=0.5)
# 散点图2，设置和散点图1一样的x_range/y_range → 图表联动

s3 = figure(plot_width=250, plot_height=250, x_range=s1.x_range, title=None)
s3.square(x, y2, size=10, color="olive", alpha=0.5)
# 散点图3，设置和散点图1一样的x_range/y_range → 图表联动

p = gridplot([[s1, s2, s3]])
#p = gridplot([[s1, s2], [None, s3]])
# 组合图表

show(p)

# 3、多图表设置
# gridplot

x = list(range(-20, 21))
y0 = [abs(xx) for xx in x]
y1 = [xx**2 for xx in x]
source = ColumnDataSource(data=dict(x=x, y0=y0, y1=y1))
# 创建数据

TOOLS = "box_select,lasso_select,help"

left = figure(tools=TOOLS, plot_width=300, plot_height=300, title=None)
left.circle('x', 'y0', source=source)    # 散点图1

right = figure(tools=TOOLS, plot_width=300, plot_height=300, title=None)
right.circle('x', 'y1', source=source)   # 散点图2
# 共用一个ColumnDataSource

p = gridplot([[left, right]])
# 组合图表

show(p)


# 工具栏 tools
# （1）设置位置

p = figure(plot_width=300, plot_height=300,
          toolbar_location="above")
# 工具栏位置："above"，"below"，"left"，"right"

p.circle(np.random.randn(100),np.random.randn(100))
show(p)

# 工具栏 tools
# （1）设置位置

p = figure(plot_width=300, plot_height=300,
           toolbar_location="below",
           toolbar_sticky=False)
# 工具栏位置设置为"below"时，可增加toolbar_sticky参数使得toolsbar不被遮挡
p.circle(np.random.randn(100),np.random.randn(100))
show(p)

# 工具栏 tools
# （2）移动、放大缩小、存储、刷新

TOOLS = '''
        pan, xpan, ypan,             
        box_zoom,
        wheel_zoom, xwheel_zoom, ywheel_zoom,   
        zoom_in, xzoom_in, yzoom_in,
        zoom_out, xzoom_out, yzoom_out,
        save,reset
        '''

p = figure(plot_width=800, plot_height=400,toolbar_location="above",
           tools = TOOLS)
# 添加toolbar
# 这里tools = '' 则不显示toolbar

p.circle(np.random.randn(500),np.random.randn(500))
show(p)

# 工具栏 tools
# （3）选择

TOOLS = '''
        box_select,lasso_select,
        reset
        '''

p = figure(plot_width=800, plot_height=400,toolbar_location="above",
           tools = TOOLS)
# 添加toolbar

p.circle(np.random.randn(500),np.random.randn(500))
show(p)

# 工具栏 tools
# （4）提示框、十字线

from bokeh.models import HoverTool
# 用于设置显示标签内容

df = pd.DataFrame({'A':np.random.randn(500)*100,
                  'B':np.random.randn(500)*100,
                  'type':np.random.choice(['pooh', 'rabbit', 'piglet', 'Christopher'],500),
                  'color':np.random.choice(['red', 'yellow', 'blue', 'green'],500)})
df.index.name = 'index'
source = ColumnDataSource(df)
print(df.head())
# 创建数据 → 包含四个标签

hover = HoverTool(tooltips=[
                            ("index", "$index"),
                            ("(x,y)", "($x, $y)"),
                            ("A", "@A"),
                            ("B", "@B"),
                            ("type", "@type"),
                            ("color", "@color"),
                        ])
# 设置标签显示内容
# $index：自动计算 → 数据index
# $x：自动计算 → 数据x值
# $y：自动计算 → 数据y值
# @A：显示ColumnDataSource中对应字段值

p1 = figure(plot_width=800, plot_height=400,toolbar_location="above",
            tools=[hover,'box_select,reset,wheel_zoom,pan,crosshair'])   # 注意这里书写方式
# 如果不设置标签，就只写hover，例如 tools='hover,box_select,reset,wheel_zoom,pan,crosshair'
p1.circle(x = 'A',y = 'B',source = source,size = 10,alpha = 0.3, color = 'color')
show(p1)

p2 = figure(plot_width=800, plot_height=400,toolbar_location="above",
           tools=[hover,'box_select,reset,wheel_zoom,pan'])
p2.vbar(x = 'index', width=1, top='A',source = source)
show(p2)
print(hover)


# 1、筛选数据 - 隐藏
# legend.click_policy

from bokeh.palettes import Spectral4
# 导入颜色模块

df = pd.DataFrame({'A':np.random.randn(500).cumsum(),
                  'B':np.random.randn(500).cumsum(),
                  'C':np.random.randn(500).cumsum(),
                  'D':np.random.randn(500).cumsum()},
                 index = pd.date_range('20180101',freq = 'D',periods=500))
# 创建数据

p = figure(plot_width=800, plot_height=400, x_axis_type="datetime")
p.title.text = '点击图例来隐藏数据'

for col,color in zip(df.columns.tolist(),Spectral4):
    p.line(df.index,df[col],line_width=2, color=color, alpha=0.8,legend = col)

p.legend.location = "top_left"
p.legend.click_policy="hide"
# 设置图例，点击隐藏

show(p)

# 1、筛选数据 - 消隐
# legend.click_policy

from bokeh.palettes import Spectral4
# 导入颜色模块

df = pd.DataFrame({'A':np.random.randn(500).cumsum(),
                  'B':np.random.randn(500).cumsum(),
                  'C':np.random.randn(500).cumsum(),
                  'D':np.random.randn(500).cumsum()},
                 index = pd.date_range('20180101',freq = 'D',periods=500))
# 创建数据

p = figure(plot_width=800, plot_height=400, x_axis_type="datetime")
p.title.text = '点击图例来隐藏数据'

for col,color in zip(df.columns.tolist(),Spectral4):
    p.line(df.index,df[col],line_width=2, color=color, alpha=0.8,legend = col,
           muted_color=color, muted_alpha=0.2)   # 设置消隐后的显示颜色、透明度

p.legend.location = "top_left"
p.legend.click_policy="mute"
# 设置图例，点击隐藏

show(p)

# 2、交互小工具
# 图表分页

from bokeh.models.widgets import Panel, Tabs
# 导入panel，tabs模块

p1 = figure(plot_width=500, plot_height=300)
p1.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)
tab1 = Panel(child=p1, title="circle")
# child → 页码
# title → 分页名称

p2 = figure(plot_width=500, plot_height=300)
p2.line([1, 2, 3, 4, 5], [4, 2, 3, 8, 6], line_width=3, color="navy", alpha=0.5)
tab2 = Panel(child=p2, title="line")

tabs = Tabs(tabs=[ tab1, tab2 ])
# 设置分页图表

show(tabs)

#各点之间的连线（lec1-intro）
income_values = np.linspace(0, 16000, 2000)
sns.scatterplot(data=df, x="Income", y="Debt")
sns.lineplot(income_values, rmodel.predict(income_values.reshape(-1, 1)), 
             color="palevioletred",label='MYCLASS')
plt.legend(['Prediction', 'Data'])
fig = plt.gcf()#Get the current figure.
fig.savefig("debt_vs_income_prediction_k1.png", dpi=300, bbox_inches = "tight")

ax = sns.scatterplot(data['total_bill'], data['tip'])
ax.set_ylim([0, 11])
ax.set_xlim([0, 53])
fig = ax.get_figure()
fig.savefig("no_fit.png", dpi=300, bbox_inches = "tight")

#小竖线
plt.vlines(np.array([10]), 0, 1,colors="r", label="Actual Value")