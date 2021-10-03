import requests
import re

domain = "https://www.dytt89.com/"
resp = requests.get(domain, verify=False)
resp.encoding = "gb2312"

obj1 = re.compile(r"2021必看热片.*?<ul>(?P<ul>.*?)</ul>", re.S)
obj2 = re.compile(r"a href='(?P<href>.*?)'", re.S)
obj3 = re.compile(r'◎片　　名(?P<movie>.*?)<.*?'
                  r'<td style="WORD-WRAP: break-word" bgcolor="#fdfddf"><a href="(?P<download>.*?)">', re.S)

result1 = obj1.finditer(resp.text)
child_href_list = []
for it1 in result1:
    ul = it1.group('ul')

    result2 = obj2.finditer(ul)
    for it2 in result2:
        child_href = domain + it2.group('href').strip("/")
        child_href_list.append(child_href)

for href in child_href_list:
    child_resp = requests.get(href, verify=False)
    child_resp.encoding = "gb2312"
    result3 = obj3.search(child_resp.text)
    print(result3.group("movie"))
    print(result3.group("download"))
