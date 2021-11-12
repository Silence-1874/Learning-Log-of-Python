> 本人对人工智能方向并不感兴趣，更喜欢写一些小爬虫和自动化脚本这类相对更实用的工具。
> 之前正好写了一个第二课堂抢课脚本（repo地址：https://github.com/Silence-Zoe/JNU-Auto-SecondClassroom），不过其中用到的爬虫代码比较简单，于是打算把第二课堂的数据全部爬取下来，进行数据可视化与分析（也更方便决定以后要抢哪些二课）。

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
