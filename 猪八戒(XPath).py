import requests
from lxml import etree

# 获取页面源码
url = "https://jiangsu.zbj.com/search/f/?kw=saas"
resp = requests.get(url)

# 解析页面
html = etree.HTML(resp.text)
# 获取所有个服务商的div
divs = html.xpath("/html/body/div[6]/div/div/div[2]/div[5]/div[1]/div[@class!='search-module-insert "
                  "insert-module-rank']")
# 获取每一个服务商的具体信息
info = []
for div in divs:
    price = div.xpath('./div/div/a[2]/div[2]/div[1]/span[1]/text()')[0].strip("¥")
    title = "SaaS".join(div.xpath('./div/div/a[2]/div[2]/div[2]/p/text()'))
    company = div.xpath('./div/div/a[1]/div[1]/p/text()')[1].strip("\n")
    address = div.xpath('./div/div/a[1]/div[1]/div/span/text()')[0]
    info.append([price, title, company, address])

print(info)
resp.close()
