import pymongo
import plotly
import plotly.graph_objs as go

# 通过地址和端口号,获得MongoDB连接对象
client = pymongo.MongoClient(host='localhost', port=27017)
# 连接数据库
db = client['test']
# 选择集合
collection = db['second_classroom']


def count_time(start_time, end_time):
    """
    @Author Silence
    @Date 2021/11/16 16:00
    @Description 计算活动持续的小时数
    """
    hour = int(end_time[0:2]) - int(start_time[0:2])
    minute = int(end_time[3:5]) - int(start_time[3:5])

    if minute < 0:
        minute += 60
        hour -= 1

    return hour + minute / 60


def bar_2():
    """
    @Author Silence
    @Date 2021/11/16 16:32
    @Description 最值活动top50
    """

    data = collection.find({})

    dic = {}
    # 虽然这样很浪费空间，但我一时想不到更好的方法来获得排序后的映射关系了……
    dic_time = {}
    dic_durtime = {}
    for ac in data:
        durtime = count_time(ac['活动开始时间'], ac['活动结束时间'])
        # 去掉时长小于15分钟的活动
        if durtime > 0.25:
            dic.update({ac['活动名称']: ac['学时'] / durtime})
            dic_time.update({ac['活动名称']: ac['学时']})
            dic_durtime.update({ac['活动名称']: durtime})

    dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=True))
    list_time = []
    list_durtime = []
    for item in dic:
        list_time.append(dic_time.get(item))
        list_durtime.append(dic_durtime.get(item))

    bar_1 = go.Bar(
        x=list(dic)[0:50],
        y=list(dic.values())[0:50],
        name='性价比'
    )

    bar_2 = go.Bar(
        x=list(dic)[0:50],
        y=list_time[0:50],
        name='学时'
    )

    bar_3 = go.Bar(
        x=list(dic)[0:50],
        y=list_durtime[0:50],
        name='活动时长'
    )

    layout = go.Layout(
        title={'text': '最值活动top50', 'x': 0.5},
    )

    trace = [bar_1, bar_2, bar_3]
    figure = go.Figure(data=trace, layout=layout)

    figure.show()
    plotly.offline.plot(figure, filename='output/最值活动top50.html')


def bar_3():
    """
    @Author Silence
    @Date 2021/11/16 21:02
    @Description 最亏活动top50
    """

    data = collection.find({})

    dic = {}
    dic_time = {}
    dic_durtime = {}
    for ac in data:
        durtime = count_time(ac['活动开始时间'], ac['活动结束时间'])
        if durtime > 0.25:
            dic.update({ac['活动名称']: ac['学时'] / durtime})
            dic_time.update({ac['活动名称']: ac['学时']})
            dic_durtime.update({ac['活动名称']: durtime})

    dic = dict(sorted(dic.items(), key=lambda item: item[1], reverse=False))
    list_time = []
    list_durtime = []
    for item in dic:
        list_time.append(dic_time.get(item))
        list_durtime.append(dic_durtime.get(item))

    bar_1 = go.Bar(
        x=list(dic)[0:50],
        y=list(dic.values())[0:50],
        name='性价比'
    )

    bar_2 = go.Bar(
        x=list(dic)[0:50],
        y=list_time[0:50],
        name='学时'
    )

    bar_3 = go.Bar(
        x=list(dic)[0:50],
        y=list_durtime[0:50],
        name='活动时长'
    )

    layout = go.Layout(
        title={'text': '最亏活动top50', 'x': 0.5},
    )

    trace = [bar_1, bar_2, bar_3]
    figure = go.Figure(data=trace, layout=layout)

    figure.show()
    plotly.offline.plot(figure, filename='output/最亏活动top50.html')


def pie_1():
    """
    @Author Silence
    @Date 2021/11/17 10:14
    @Description 性价比占比
    """

    data = collection.find({})

    dic = {}
    dic_cnt = {}
    for ac in data:
        durtime = count_time(ac['活动开始时间'], ac['活动结束时间'])
        if durtime > 0.25:
            cost = ac['学时'] / durtime
            dic.update({ac['活动名称']: cost})
            # 统计性价比出现频率
            dic_cnt[cost] = dic_cnt.get(cost, 0) + 1

    for key in list(dic_cnt.keys()):
        if dic_cnt.get(key) <= 3:
            dic_cnt.pop(key)

    pie = go.Pie(
        labels=list(dic_cnt.keys()),
        values=list(dic_cnt.values())
    )

    layout = go.Layout(
        title={'text': '性价比占比', 'x': 0.5}
    )

    figure = go.Figure(data=pie, layout=layout)

    figure.show()
    plotly.offline.plot(figure, filename='output/性价比占比.html')


if __name__ == '__main__':
    print('start...')
    # -------------------------------------------------------
    # bar_2()
    # bar_3()
    pie_1()
    # -------------------------------------------------------
    print('finish!')
