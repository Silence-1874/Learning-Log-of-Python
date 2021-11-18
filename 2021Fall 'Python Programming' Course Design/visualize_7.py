import pymongo
import plotly
import plotly.graph_objs as go

# 通过地址和端口号,获得MongoDB连接对象
client = pymongo.MongoClient(host='localhost', port=27017)
# 连接数据库
db = client['test']
# 选择集合
collection = db['second_classroom']


def bar_4():
    """
    @Author Silence
    @Date 2021/11/18 12:32
    @Description 发布活动数量top10的创建人
    """
    data = collection.find({})
    dic_p = {}
    dic_time = {}
    for ac in data:
        p = ac['活动联系人']
        if p != '':
            dic_p[p] = dic_p.get(p, 0) + 1
            dic_time[p] = dic_time.get(p, 0) + ac['学时']

    dic_p = dict(sorted(dic_p.items(), key=lambda item: item[1], reverse=True))
    dic_time = dict(sorted(dic_time.items(), key=lambda item: item[1], reverse=True))

    colors_1 = ['pink'] * 10
    colors_1[0] = 'crimson'

    list_x_1 = list(dic_p.values())[0:10]
    list_y = list(dic_p.keys())[0:10]
    bar_1 = go.Bar(
        x=list_x_1,
        y=list_y,
        orientation='h',
        marker_color=colors_1,
        name='活动总数'
    )

    colors_2 = ['skyblue'] * 10
    colors_2[7] = 'blue'

    list_x_2 = []
    for p in list_y:
        list_x_2.append(dic_time.get(p))

    bar_2 = go.Bar(
        x=list_x_2,
        y=list_y,
        orientation='h',
        marker_color=colors_2,
        name='学时总数'
    )

    layout = go.Layout(
        title={'text': '发布活动数量top10的创建人', 'x': 0.5},
    )

    trace = [bar_1, bar_2]
    figure = go.Figure(data=trace, layout=layout)

    figure.show()
    plotly.offline.plot(figure, filename='output/发布活动数量top10的创建人.html')


if __name__ == '__main__':
    print('start...')
    # -------------------------------------------------------
    bar_4()
    # -------------------------------------------------------
    print('finish!')
