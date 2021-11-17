import pymongo
import plotly
import plotly.graph_objs as go

# 通过地址和端口号,获得MongoDB连接对象
client = pymongo.MongoClient(host='localhost', port=27017)
# 连接数据库
db = client['test']
# 选择集合
collection = db['second_classroom']


def get_interval(time):
    """
    @Author Silence
    @Date 2021/11/17 15:50
    @Description 以2小时为间隔，计算time所属区间
    """
    h = time[0:2]
    # 一开始这里的条件判断我写的都是 "h >= x and h < y"，经PyCharm提示才知道python可以写在一起
    if '06' <= h < '08':
        return '[6, 8)'
    elif '08' <= h < '10':
        return '[8, 10)'
    elif '10' <= h < '12':
        return '[10, 12)'
    elif '12' <= h < '14':
        return '[12, 14)'
    elif '14' <= h < '16':
        return '[14, 16)'
    elif '16' <= h < '18':
        return '[16, 18)'
    elif '18' <= h < '20':
        return '[18, 20)'
    elif '20' <= h < '22':
        return '[20, 22)'
    elif h >= '22':
        return '[22, 24)'
    else:
        return 'exclude'


def bubble():
    data = collection.find({}, {'_id': 0, '活动创建时间': 1, '报名开始时间': 1, '报名结束时间': 1, '活动开始时间': 1, '活动结束时间': 1})

    dic_time_1 = {
        '[6, 8)': 0, '[8, 10)': 0, '[10, 12)': 0, '[12, 14)': 0, '[14, 16)': 0, '[16, 18)': 0, '[18, 20)': 0,
        '[20, 22)': 0, '[22, 24)': 0, 'exclude': 0
    }
    dic_time_2 = dic_time_1.copy()
    dic_time_3 = dic_time_1.copy()
    dic_time_4 = dic_time_1.copy()
    dic_time_5 = dic_time_1.copy()
    # 统计时间区间频率
    for ac in data:
        time_1 = get_interval(ac['活动创建时间'][11:13])
        time_2 = get_interval(ac['报名开始时间'])
        time_3 = get_interval(ac['报名结束时间'])
        time_4 = get_interval(ac['活动开始时间'])
        time_5 = get_interval(ac['活动结束时间'])
        dic_time_1[time_1] = dic_time_1.get(time_1) + 1
        dic_time_2[time_2] = dic_time_2.get(time_2) + 1
        dic_time_3[time_3] = dic_time_3.get(time_3) + 1
        dic_time_4[time_4] = dic_time_4.get(time_4) + 1
        dic_time_5[time_5] = dic_time_5.get(time_5) + 1

    dic_time_1.pop('exclude')
    dic_time_2.pop('exclude')
    dic_time_3.pop('exclude')
    dic_time_4.pop('exclude')
    dic_time_5.pop('exclude')

    scatter_1 = go.Scatter(
        x=list(dic_time_1.keys()),
        y=['活动创建时间'] * 9,
        mode='markers',
        marker=dict(
            color=list(dic_time_1.values()),
            size=list(dic_time_1.values()),
            colorscale='plotly3',
            showscale=True,
            sizeref=3
        ),
        name='活动创建时间'
    )

    scatter_2 = go.Scatter(
        x=list(dic_time_2.keys()),
        y=['报名开始时间'] * 9,
        mode='markers',
        marker=dict(
            color=list(dic_time_2.values()),
            size=list(dic_time_2.values()),
            colorscale='plotly3',
            sizeref=3
        ),
        name='报名开始时间'
    )
    scatter_3 = go.Scatter(
        x=list(dic_time_3.keys()),
        y=['报名结束时间'] * 9,
        mode='markers',
        marker=dict(
            color=list(dic_time_3.values()),
            size=list(dic_time_3.values()),
            colorscale='plotly3',
            sizeref=3
        ),
        name='报名结束时间'
    )
    scatter_4 = go.Scatter(
        x=list(dic_time_4.keys()),
        y=['活动开始时间'] * 9,
        mode='markers',
        marker=dict(
            color=list(dic_time_4.values()),
            size=list(dic_time_4.values()),
            colorscale='plotly3',
            sizeref=3
        ),
        name='活动开始时间'
    )
    scatter_5 = go.Scatter(
        x=list(dic_time_5.keys()),
        y=['活动结束时间'] * 9,
        mode='markers',
        marker=dict(
            color=list(dic_time_5.values()),
            size=list(dic_time_5.values()),
            colorscale='plotly3',
            sizeref=3
        ),
        name='活动结束时间'
    )

    layout = go.Layout(
        title={'text': '时间区间', 'x': 0.5}
    )

    trace = [scatter_1, scatter_2, scatter_3, scatter_4, scatter_5]
    figure = go.Figure(data=trace, layout=layout)

    figure.show()
    plotly.offline.plot(figure, filename='output/时间区间.html')


if __name__ == '__main__':
    print('start...')
    # -------------------------------------------------------
    bubble()
    # -------------------------------------------------------
    print('finish!')
