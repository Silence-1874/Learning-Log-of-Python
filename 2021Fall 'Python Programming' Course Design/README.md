本人对人工智能方向并不感兴趣，更喜欢写一些小爬虫和自动化脚本这类相对更实用的工具。
之前正好写了一个第二课堂抢课脚本（repo地址：https://github.com/Silence-Zoe/JNU-Auto-SecondClassroom），不过其中用到的爬虫代码比较简单，于是打算把第二课堂的数据全部爬取下来，进行数据可视化与分析（也更方便决定以后要抢哪些二课）。

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

# 1.获得数据集（crawler.py）

## 1.1 分析网页结构

### 1.1.1 概览

打开第二课堂网页

![image-20211114090706835](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211114090706835.png) 

这种数据一般都是Ajax加载的，不过还是先看下页面源码

![image-20211114090646780](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211114090646780.png) 

显然没有我要的数据，按F12打开Developer Tools，选择Network中的Fetch/XHR，刷新页面，开始抓包

![image-20211114093216154](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211114093216154.png)

捕获一些XHR请求，逐个查看

- 第一个me：左边的信息栏![image-20211114091846148](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211114091846148.png) 

- adbr?_o=https://miao.baidu.com/abdr?_o=http%3A%2F%2Fdekt.jiangnan.edu.cn：没什么用

    ![image-20211114093323681](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211114093323681.png) 

- 第二个me：首页的个人信息

    ![image-20211114093341875](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211114093341875.png)  

    ![image-20211114092840813](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211114092840813.png) 

- list?开头的XHR：各种活动信息，显然，这就是我要找的

    ![image-20211114093430017](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211114093430017.png) 

- list：各个组织的相关信息![image-20211114093457578](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211114093457578.png) 

### 1.1.2 深入查看list?开头XHR的Response

`data`中的`total`对应活动总条目数

![image-20211114094308883](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211114094308883.png) 

`list`对应一个个活动

![image-20211114094428023](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211114094428023.png) 

每一个list值记录了对应活动的详细信息

![image-20211114094614413](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211114094614413.png) 

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

## 1.2 确定数据爬取接口

这个比较简单，查看XHR的请求头就行

![image-20211114101721928](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211114101721928.png)  

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

## 1.3 保持登录状态

在XHR中找到Authorization和Cookie![image-20211114102047963](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211114102047963.png) 

## 1.4 爬取数据并存储到MongoDB中

运行代码

![image-20211114111950686](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211114111950686.png) 

打开Navicat，查看MongoDB，发现数据已全部抓取

![image-20211114112251447](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211114112251447.png) 

代码详见`crawler.py`



# 2.数据可视化与分析（main.py）

## 2.1 数据预处理

- 删除不含实际内容的“学时补录”的相关记录![image-20211115162928150](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211115162928150.png) 

    ```python
    collection.delete_many({'活动名称': {'$regex': '学时补录'}})
    ```

- 将活动地点统一为大写

    ![image-20211115165833880](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211115165833880.png) 

    ```python
    all = collection.find({})
    for ac in all:
        new = ac['活动地点'].upper()
        collection.update_one({'_id': ac['_id']}, {'$set': {'活动地点': new}})![image-20211115201627691](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211115201627691.png) 
    ```

- 去除“活动联系人”字段前面的学号![image-20211115204256680](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211115204256680.png) 

    初步处理完毕，效果如下：

    ![image-20211115204522717](C:\Users\22458\AppData\Roaming\Typora\typora-user-images\image-20211115204522717.png) 

    ```python
    all = collection.find({})
    for ac in all:
        name = re.sub(r'[0-9]', '', ac['活动联系人'])
        collection.update_one({'_id': ac['_id']}, {'$set': {'活动联系人': name}})
    ```
