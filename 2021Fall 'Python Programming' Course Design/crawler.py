import requests
import pymongo

# 通过地址和端口号,获得MongoDB连接对象
client = pymongo.MongoClient(host='localhost', port=27017)
# 连接数据库
db = client['test']
# 选择集合
collection = db['second_classroom']

# 请求头
Headers = {
    'Authorization': '',
    'Cookie': '',
    'Referer': 'http://dekt.jiangnan.edu.cn/admin/index.html',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.72 Safari/537.36'
}

# 请求参数
Qurey_String_Parameters = {
    'hdmc': '',  # 原请求就是空的，保持为空
    'orgId': '',  # 原请求就是空的，保持为空
    'size': '100',  # 每页显示的条目数
    'page': '1',  # 页码
    'userId': '1191200522',  # 学号
    'xyId': '12200',  # 学院Id
    'grade': '2020',  # 年级
    'type': '5'  # 活动类型，5表示“招募中”(经试验，参数对应如下：1-预热中 2-招募中 3-进行中 4-已结束 5-全部活动)
}


# 核心代码
def crawl():
    """
    @Author Silence
    @Date 2021/11/14 8:59
    @Description 获得数据集
    """
    session = requests.session()
    # 请求活动列表
    response = session.request(method='get',
                               url='http://dekt.jiangnan.edu.cn/biz/activity/student/list',
                               params=Qurey_String_Parameters,
                               headers=Headers)
    # 解析列表
    response.encoding = response.apparent_encoding
    # 转换成json格式
    data = response.json()
    # 获得活动总数
    cnt = data['data']['total']
    # 获得总页数
    page_cnt = (cnt - 1) // 100 + 1
    for i in range(0, page_cnt):
        Qurey_String_Parameters['page'] = i + 1
        response = session.request(method='get',
                                   url='http://dekt.jiangnan.edu.cn/biz/activity/student/list',
                                   params=Qurey_String_Parameters,
                                   headers=Headers)
        response.encoding = response.apparent_encoding
        data = response.json()
        for active in data['data']['list']:
            active = {
                '_id': active['id'],
                '活动名称': active['hdmc'],
                '活动简介': active['hdjj'],
                '活动地点': active['hddd'],
                '学时': active['xs'],
                '活动开始日期': active['kssj'][0:10],
                '活动开始时间': active['kssj'][11:16],
                '活动结束日期': active['kssj'][0:10],
                '活动结束时间': active['jssj'][11:16],
                '报名开始日期': active['bmkssj'][0:10],
                '报名开始时间': active['bmkssj'][11:16],
                '报名结束日期': active['bmjssj'][0:10],
                '报名结束时间': active['bmjssj'][11:16],
                '招募人数': active['zmrs'],
                '报名人数': active['bmrs'],
                '活动联系人': active['hdlxr'],
                '联系电话': active['lxdh'],
                '活动创建时间': active['createTime'],
                '活动主办方': active['hdjbf'],
                '所属部落': active['zzmc'],
                '学院Id': active['xyId'],
                '学年': active['xn'],
                '学期': active['xq']
            }
            # print(active)
            collection.insert_one(active)


if __name__ == '__main__':
    print("start...")
    crawl()
    print("finish.")
