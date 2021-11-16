import pymongo
import re


# 通过地址和端口号,获得MongoDB连接对象
client = pymongo.MongoClient(host='localhost', port=27017)
# 连接数据库
db = client['test']
# 选择集合
collection = db['second_classroom'

]
def pretreat():
    """
    @Author Silence
    @Date 2021/11/14 19:03
    @Description 数据预处理
    """

    collection.delete_many({'活动名称': {'$regex': '学时补录'}})

    all = collection.find({})
    for ac in all:
        # 将活动地点统一为大写
        new = ac['活动地点'].upper()
        # 去除活动联系人前的学号
        name = re.sub(r'[0-9]', '', ac['活动联系人'])

        collection.update_one({'_id': ac['_id']}, {'$set': {'活动地点': new, '活动联系人': name}})
        collection.update_one({'_id': ac['_id']}, {'$set': {}})