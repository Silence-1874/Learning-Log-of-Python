import numpy
import pymongo
import plotly
import plotly.graph_objs as go

# 通过地址和端口号,获得MongoDB连接对象
client = pymongo.MongoClient(host='localhost', port=27017)
# 连接数据库
db = client['test']
# 选择集合
collection = db['second_classroom']


def scatter():
    """
    @Author Silence
    @Date 2021/11/17 19:23
    @Description 活动地点使用频率top10
    """
    data = collection.find({}, {'_id': 0, '活动名称': 1, '活动地点': 1})

    dic_loc = {}
    for ac in data:
        loc = ac['活动地点']
        # 排除线上活动
        if loc.find('线上') == -1 and loc.find('无') == -1 and loc.find('江南大学') == -1:
            dic_loc[loc] = dic_loc.get(loc, 0) + 1

    # 找出使用频率前十的地点
    dic_loc = dict(sorted(dic_loc.items(), key=lambda item: item[1], reverse=True))
    list_loc = list(dic_loc.keys())[0:10]

    # 再根据这些地点找活动
    dic = {}
    data.rewind()
    for ac in data:
        if ac['活动地点'] in list_loc:
            dic.update({ac['活动名称']: ac['活动地点']})

    scatter = go.Scatter(
        x=list(dic.keys()),
        y=list(dic.values()),
        mode='markers',
        marker=dict(
            color=numpy.random.randn(len(list(dic.keys()))),
            colorscale='sunset'
        )
    )

    layout = go.Layout(
        title={'text': "活动地点使用频率top10", 'x': 0.5}
    )

    figure = go.Figure(data=scatter, layout=layout)

    figure.show()
    plotly.offline.plot(figure, filename='output/活动地点使用频率top10.html')


if __name__ == '__main__':
    print('start...')
    # -------------------------------------------------------
    scatter()
    # -------------------------------------------------------
    print('finish!')
