本人对人工智能方向并不感兴趣，更喜欢写一些小爬虫和自动化脚本这类相对更实用的工具。
之前正好写了一个[第二课堂抢课脚本](https://github.com/Silence-Zoe/JNU-Auto-SecondClassroom)，不过其中用到的爬虫代码比较简单，于是打算把第二课堂的数据全部爬取下来，进行数据可视化与分析（也更方便决定以后要抢哪些二课）。

主要用到的lib：

- 爬虫——requests

    >  因为学校的网站结构比较简单，也没有什么反爬机制，所以requests库就够用了

- 数据持久化存储——pymongo

    > 这次爬取的数据结构其实是固定的，用MySQL或许会更好，这里用MongoDB纯粹是因为之前爬虫存储数据用的是MongoDB，pymongo比较熟了，懒得再学PyMySQL了

- 数据可视化——plotly

    > 之前用过matplotlib，还是更喜欢plotly

使用工具：

- Python IDE——PyCharm 2020.1
- 数据库可视化管理工具——Navicat Premium 15.0.9

# 获得数据集（crawler.py）

## 1.分析网页结构

### (1)概览

打开第二课堂网页

![image-20211114090706835](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/1.png) 

这种数据一般都是Ajax加载的，不过还是先看下页面源码

![image-20211114090646780](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/2.png) 

显然没有我要的数据，按F12打开Developer Tools，选择Network中的Fetch/XHR，刷新页面，开始抓包

![image-20211114093216154](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/3.png)

捕获一些XHR请求，逐个查看

- 第一个me：左边的信息栏![image-20211114091846148](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/4.png) 

- adbr?_o=https://miao.baidu.com/abdr?_o=http%3A%2F%2Fdekt.jiangnan.edu.cn 没什么用

    ![image-20211114093323681](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/5.png) 

- 第二个me：首页的个人信息

    ![image-20211114093341875](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/6.png)  

    ![image-20211114092840813](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/7.png) 

- list?开头的XHR：各种活动信息，显然，这就是我要找的

    ![image-20211114093430017](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/8.png) 

- list：各个组织的相关信息![image-20211114093457578](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/9.png) 

### (2)深入查看list?开头XHR的Response

`data`中的`total`对应活动总条目数

![image-20211114094308883](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/10.png) 

`list`对应一个个活动

![image-20211114094428023](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/11.png) 

每一个list值记录了对应活动的详细信息

![image-20211114094614413](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/12.png) 

共计56个键值对，从中挑选出了主要的16个，对应如下

```json
{
	'bmjssj': 报名结束时间,
	'bmkssj':报名开始时间,
	'bmrs':报名人数,
	'createTime':创建时间,
	'hddd':活动地点,
	'hdjbf':活动举（主）办方,
	'hdjj':活动简介,
	'hdlxr':活动联系人,
	'hdmc':活动名称,
	'id':活动id,
	'jssj':（活动）结束时间,
	'kssj':（活动）开始时间,
	'lxdh':联系电话,
	'xn':学年,
	'sq':学期,
	'xs':学时,
	'xyId':学院Id,
	'zmrs':招募人数,
	'zzmc':组织名称（所属部落）
}
```

## 2 确定数据爬取接口

这个比较简单，查看XHR的请求头就行

![image-20211114101721928](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/13.png)  

其中，请求参数(Query String Parameters)对应如下

```json
{
    'hdmc': 活动名称，保持为空即可,
    'orgId': 组织Id，保持为空即可,
    'size': 每页显示的条目数,
    'page': 页码,
    'userId': 学号,
    'xyId': 学院Id,
    'grade': 年级,
    'type': 活动类型，参数对应如下：1-预热中 2-招募中 3-进行中 4-已结束 5-全部活动
}
```

## 3 保持登录状态

在XHR中找到Authorization和Cookie![image-20211114102047963](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/14.png) 

## 4 爬取数据并存储到MongoDB中

运行代码

![image-20211114111950686](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/15.png) 

打开Navicat，查看MongoDB，发现数据已全部抓取

![image-20211114112251447](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/16.png) 

代码详见`crawler.py`



# 数据可视化与分析（main.py）

## 1 数据预处理

- 活动名称去重

    ```python
    for ac in collection.distinct('活动名称'):
        repeating = collection.find_one({'活动名称': ac})
        collection.delete_many({'活动名称': ac})
        collection.insert_one(repeating)
    ```
    
- 删除不含实际内容的“学时补录”的相关记录![image-20211115162928150](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/17.png) 

    ```python
    collection.delete_many({'活动名称': {'$regex': '学时补录'}})
    ```

- 将活动地点统一为大写

    ![image-20211115165833880](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/18.png) 

    ```python
    all = collection.find({})
    for ac in all:
        new = ac['活动地点'].upper()
        collection.update_one({'_id': ac['_id']}, {'$set': {'活动地点': new}})![image-20211115201627691](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211115201627691.png) 
    ```

- 去除“活动联系人”字段前面的学号![image-20211115204256680](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/19.png) 

	```python
	all = collection.find({})
	for ac in all:
    	name = re.sub(r'[0-9]', '', ac['活动联系人'])
    	collection.update_one({'_id': ac['_id']}, {'$set': {'活动联系人': name}})
	```

## 2.分析与可视化

### (1)学时总排名（`visualize_1.py`）

![image-20211116153327593](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/20.png) 

### (2)活动性价比——学时/小时(`visualize_2.py`)

#### ①最值活动top50（`bar_2()`）

![image-20211116212749008](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/21.png) 

#### ②最亏活动top50（`bar_3()`）![image-20211117095839825](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/22.png) 

#### ③性价比占比（`pie_1()`）

![image-20211117111527580](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/23.png) 

可以看出，近四分之一的活动都是一个小时一个学时，近三分之二的活动性价比在1-2之间。

### (3)时间区间（`visualize_3.py`）

![image-20211117164714405](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/24.png)

气泡的大小和颜色反映了频率。
可以发现大多数活动的开始时间在下午14点到16点之间，以及18点到20点之间，而结束时间则大都在16点到18点之间，20点到22点之间，这与前面所得出的结论一致。

### (4)兵家必争之地——活动地点使用频率top10（`visualize_4.py`）

![image-20211117201018042](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/25.png) 

### (5)大慈善家——活动主办方发布的活动总数/学时总数（`visualize_5.py`）

![image-20211117212129329](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/26.png)  

我们学院虽然去年才成立，但发布活动数量和总学时还是相当多的。

### (6)多事之秋——各学期活动总数（`visualize_6.py`）

![image-20211118122244076](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/27.png) 

每年的4月5月，11月12月是活动的高峰期，活动总数也在逐年上升。

### (7)活动狂热者——发布活动数top10的创建人（`visualize_7.py`）

![image-20211118163957131](https://github.com/Silence-Zoe/Learning-Log-of-Python/blob/main/2021Fall%20'Python%20Programming'%20Course%20Design/img/28.png) 


# 实验小结（碎碎念）
敲了差不多一个星期代码，终于完成了7个小专题的可视化，其实本人是主攻**Java**的，Python写的很少，在开头也说了，平时只是写一些小爬虫和小脚本。书也只读过一本，今年暑假看的蟒蛇书（《Python编程：从入门到实践》），也是从这本书里，稍微体验了一下用matplotlib和plotly进行数据可视化，感觉很有趣，稍稍入了点门。

这次的实验我有意识地尽量多尝试不同类型的图，所以柱状图、直方图、条形图、折线图、饼图、环形图、散点图、气泡图都写了一下。

事实上，我连Python的基础语法都没有系统学过，虽然跟着蟒蛇书粗略过了一遍，但几个月没敲就忘光光了。虽然基础语法都不太熟，但并不影响我写代码，网页开着手册，现用现查，写Python的时候，在浏览器上的时间比在IDE上的时间还多。Python的库真的很丰富，封装性很高，轮子全都造好了，直接拿来用就行，这也是我不太喜欢Python的原因之一，感觉Python更像是一个强大的工具，而不是编程语言（当然，用起来还是很香的）。

得益于plotly的高度封装性，可视化部分的代码逻辑其实并不复杂，核心代码都很简单，主要比较难的地方还是数据的前期处理，如何筛选出想要统计的数据。list/dict/tuple的增删改查以及相互转换，这些操作的频率很高，即使基础语法并不太熟，写完七个小专题后，也差不多全都写熟练了，正如老师说的，学习一门语言最好的方法就是多用多敲，但本人并不准备专攻Python，所以我还是现用现查吧……

Python写多了，得了后遗症，感觉自己“越来越懒”了，有时候一些功能感觉比较简单，嫌自己写的不够*elegant*，也怕重复造轮子，不够就想着去找现成的api，结果找了半天，花的时间都够自己造好几个轮子了，虽然写出来的都不太优雅。
