import pymongo
import plotly
import plotly.graph_objs as go

# 通过地址和端口号,获得MongoDB连接对象
client = pymongo.MongoClient(host='localhost', port=27017)
# 连接数据库
db = client['test']
# 选择集合
collection = db['second_classroom']


def line():
    """
    @Author Silence
    @Date 2021/11/18 8:44
    @Description 各月份活动总数
    """
    data = collection.find({}).sort('活动开始日期', 1)

    # 生成年份与月份字典
    key_month = list(range(1, 13))
    dic_month = dict(zip(key_month, [0] * len(key_month)))

    key_year = list(range(2017, 2022))
    value_year = [dic_month.copy(), dic_month.copy(), dic_month.copy(), dic_month.copy(), dic_month.copy()]
    dic_year = dict(zip(key_year, value_year))

    for ac in data:
        year = dic_year.get(int(ac['活动开始日期'][0:4]))  # 没想到这里还要先转换成int，debug了好久……
        month = int(ac['活动开始日期'][5:7])  # 去除前导零
        year[month] = year.get(month) + 1
    print(dic_year)

    line_1 = go.Scatter(
        x=list(dic_year[2017].keys()),
        y=list(dic_year[2017].values()),
        mode='lines + markers',
        name='2017'
    )

    line_2 = go.Scatter(
        x=list(dic_year[2018].keys()),
        y=list(dic_year[2018].values()),
        mode='lines + markers',
        name='2018'
    )
    line_3 = go.Scatter(
        x=list(dic_year[2019].keys()),
        y=list(dic_year[2019].values()),
        mode='lines + markers',
        name='2019'
    )

    line_4 = go.Scatter(
        x=list(dic_year[2020].keys()),
        y=list(dic_year[2020].values()),
        mode='lines + markers',
        name='2020'
    )

    line_5 = go.Scatter(
        x=list(dic_year[2021].keys()),
        y=list(dic_year[2021].values()),
        mode='lines + markers',
        name='2021'
    )

    layout = go.Layout(
        title={'text': '各月份活动总数', 'x': 0.5},
        xaxis_title='月份',
        yaxis_title='活动总数'
    )

    trace = [line_1, line_2, line_3, line_4, line_5]
    figure = go.Figure(data=trace, layout=layout)

    figure.show()
    plotly.offline.plot(figure, filename='output/各月份活动总数.html')


if __name__ == '__main__':
    print('start...')
    # -------------------------------------------------------
    line()
    # -------------------------------------------------------
    print('finish!')
