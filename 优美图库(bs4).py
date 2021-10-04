import requests
import time
from bs4 import BeautifulSoup

# 获取网站首页源码
url = "https://www.umei.cc/bizhitupian/weimeibizhi/"
resp = requests.get(url)
resp.encoding = "utf-8"

# 获取经BeautifulSoup解析后的页面
main_page = BeautifulSoup(resp.text, "html.parser")
# 获取图片子页面链接后缀(a)
alist = main_page.find("div", class_="TypeList").find_all("a")

for a in alist:
    # 拼接网址，获取图片子页面链接(href)
    href = "https://www.umei.cc/" + a.get('href')
    # 获取图片子页面源码
    child_page_resp = requests.get(href)
    child_page_resp.encoding = "utf-8"
    # 获取经BeautifulSoup解析后的页面
    child_page = BeautifulSoup(child_page_resp.text, "html.parser")
    # 获取图片下载路径(src)
    p = child_page.find("p", align="center")
    img = p.find("img")
    src = img.get("src")
    # 下载图片
    img_resp = requests.get(src)  # 通过get方法可以直接拿到属性值
    img_name = src.split("/")[-1]
    with open("img/" + img_name, mode="wb") as f:
        f.write(img_resp.content)
    print(img_name + " has downloaded.")
    time.sleep(1)  # 减缓下载频率，防止被服务器制裁
print("all img have downloaded.")

resp.close()
