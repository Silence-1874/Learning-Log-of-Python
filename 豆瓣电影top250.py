import requests
import re
import csv

url = "https://movie.douban.com/top250"
head = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36 Edg/94.0.992.310"
}
resp = requests.get(url, headers=head)
page_content = resp.text

obj = re.compile(r'<li>.*?<div class="item">.*?<span class="title">(?P<name>.*?)</span>.*?'
                 r'<p class="">.*?<br>(?P<year>.*?)&nbsp.*?<span class="rating_num" property="v:average">'
                 r'(?P<score>.*?)</span>.*?<span>(?P<num>.*?)人评价</span>', re.S)

result = obj.finditer(page_content)
f = open("豆瓣电影top250.csv", mode="w", encoding="utf-8")
csvwriter = csv.writer(f)
for it in result:
    print(it.group("name"))
    print(it.group("score"))
    print(it.group("num"))
    print(it.group("year").strip())
    dic = it.groupdict()
    dic['year'] = dic['year'].strip()
    csvwriter.writerow(dic.values())

f.close()
resp.close()
print("over!")