import pymongo
import re
import visualize_1
import visualize_2
import visualize_3
import visualize_4
import visualize_5
import visualize_6
import visualize_7

# 通过地址和端口号,获得MongoDB连接对象
client = pymongo.MongoClient(host='localhost', port=27017)
# 连接数据库
db = client['test']
# 选择集合
collection = db['second_classroom']


def pretreat():
    """
    @Author Silence
    @Date 2021/11/14 19:03
    @Description 数据预处理
    """
    # 删除不含实际内容的“学时补录”
    collection.delete_many({'活动名称': {'$regex': '学时补录'}})

    # 活动名称去重
    for ac in collection.distinct('活动名称'):
        repeating = collection.find_one({'活动名称': ac})
        collection.delete_many({'活动名称': ac})
        collection.insert_one(repeating)

    all = collection.find({})
    for ac in all:
        # 将活动地点统一为大写
        new = ac['活动地点'].upper()
        # 去除活动联系人前的学号
        name = re.sub(r'[0-9]', '', ac['活动联系人'])

        collection.update_one({'_id': ac['_id']}, {'$set': {'活动地点': new, '活动联系人': name}})
        collection.update_one({'_id': ac['_id']}, {'$set': {}})


if __name__ == '__main__':
    print('start...')
    # -------------------------------------------------------
    pretreat()
    visualize_1.bar_1()
    visualize_2.bar_2()
    visualize_2.bar_3()
    visualize_2.pie_1()
    visualize_3.bubble()
    visualize_4.scatter()
    visualize_5.pie_2()
    visualize_6.line()
    visualize_7.bar_4()
    # -------------------------------------------------------
    print('finish!')
