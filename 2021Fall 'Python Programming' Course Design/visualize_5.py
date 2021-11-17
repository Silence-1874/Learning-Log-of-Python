import pymongo
import plotly
import plotly.graph_objs as go
from plotly.subplots import make_subplots

# 通过地址和端口号,获得MongoDB连接对象
client = pymongo.MongoClient(host='localhost', port=27017)
# 连接数据库
db = client['test']
# 选择集合
collection = db['second_classroom']


def pie_2():
    """
    @Author Silence
    @Date 2021/11/17 21:26
    @Description 活动主办方发布的活动总数/学时总数
    """
    map = {
        '10100': '食品学院',
        '10400': '化学与材料工程学院',
        '10500': '物联网工程学院',
        '10600': '环境与土木工程学院',
        '10700': '商学院',
        '10800': '理学院',
        '10900': '机械学院/君远学院',
        '11000': '设计学院',
        '11100': '药学院',
        '11200': '医学院',
        '11400': '人文学院',
        '11500': '外国语学院',
        '11600': '法学院',
        '11800': '体育部',
        '11900': '国际教育学院/北美学院',
        '12100': '纺织科学与工程学院',
        '12200': '人工智能与计算机学院',
        '30100': '图书馆与档案馆',
        '30200': '信息化建设与管理中心',
        '40700': '团委',
        '51900': '招生就业处',
        '60100': '至善学院',
    }

    data = collection.find({})

    dic_ac_cnt = {}
    dic_time_total = {}
    for ac in data:
        host = map.get(ac['学院Id'], 'ohter')
        time = ac['学时']
        # 统计各个组织方发布的活动总数/学时总数
        dic_ac_cnt[host] = dic_ac_cnt.get(host, 0) + 1
        dic_time_total[host] = dic_time_total.get(host, 0) + time

    pie_1 = go.Pie(
        labels=list(dic_ac_cnt.keys()),
        values=list(dic_ac_cnt.values()),
        hole=0.4,
        pull=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3],
        textinfo='percent+label',
        marker_colors=['rgb(33, 75, 99)', 'rgb(79, 129, 102)', 'rgb(151, 179, 100)',
                       'rgb(175, 49, 35)', 'rgb(36, 73, 147)']
    )

    pie_2 = go.Pie(
        labels=list(dic_time_total.keys()),
        values=list(dic_time_total.values()),
        hole=0.4,
        pull=[0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.3],
        textinfo='percent+label',
        marker_colors=['rgb(33, 75, 99)', 'rgb(79, 129, 102)', 'rgb(151, 179, 100)',
                       'rgb(175, 49, 35)', 'rgb(36, 73, 147)']
    )

    # 在一个页面里显示两个饼图
    figure = make_subplots(
        rows=1,
        cols=2,
        specs=[[{'type': 'domain'},
                {'type': 'domain'}]]
    )
    figure.add_trace(pie_1, 1, 1)
    figure.add_trace(pie_2, 1, 2)
    figure.update_layout(
        title={
            # 强行对齐标题……
            'text': '发布的活动总数                                                                                 发布的学时总数',
            'x': 0.275,
            'y': 0.5
        }
    )

    figure.show()
    plotly.offline.plot(figure, filename='output/性价比占比.html')


if __name__ == '__main__':
    print('start...')
    # -------------------------------------------------------
    pie_2()
    # -------------------------------------------------------
    print('finish!')
