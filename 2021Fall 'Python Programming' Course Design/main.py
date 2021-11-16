import pymongo
import re


# 通过地址和端口号,获得MongoDB连接对象
client = pymongo.MongoClient(host='localhost', port=27017)
# 连接数据库
db = client['test']
# 选择集合
collection = db['second_classroom' ]


def pretreat():
    """
    @Author Silence
    @Date 2021/11/14 19:03
    @Description 数据预处理
    """

    # 活动名称去重
    for ac in collection.distinct('活动名称'):
        repeating = collection.find_one({'活动名称': ac})
        collection.delete_many({'活动名称': ac})
        collection.insert_one(repeating)

    # 删除不含实际内容的“学时补录”
    collection.delete_many({'活动名称': {'$regex': '学时补录'}})

    all = collection.find({})
    for ac in all:
        # 将活动地点统一为大写
        new = ac['活动地点'].upper()
        # 去除活动联系人前的学号
        name = re.sub(r'[0-9]', '', ac['活动联系人'])

        collection.update_one({'_id': ac['_id']}, {'$set': {'活动地点': new, '活动联系人': name}})
        collection.update_one({'_id': ac['_id']}, {'$set': {}})


# 找了很久，没找到类似功能的API，只能自己实现了……
def ListField(cursor, field):
    """
    @Author Silence
    @Date 2021/11/16 9:46
    @Description 获得查询结果指定字段的所有值，并以列表的形式返回
    """

    # 刷新游标
    cursor.rewind()
    # 存储字段值
    ret = []
    # 遍历结果集
    for x in cursor:
        ret.append(x[field])
    return ret


def bar_1():
    """
    @Author Silence
    @Date 2021/11/16 14:53
    @Description 学时总排名
    """
    data = collection.find({}).sort('学时', -1)

    bar = go.Bar(
        x=ListField(data, '活动名称'),
        y=ListField(data, '学时')
    )

    layout = go.Layout(
        title={'text': '学时排行榜', 'x': 0.5}
    )

    figure = go.Figure(data=bar, layout=layout)

    figure.show()
    plotly.offline.plot(figure, filename='output/学时总排名.html')
