# 發送=送請求地址
url='https://www.ip138.com/mobile.asp?mobile=16600116666&action=mobile'
# 前面一段和抓小說一樣# 第一步 發送請求
# 安裝送網路請求的套件 CTRL+'
# pip install requests

import requests

# 偽裝成瀏灠器 使用PYTHON字典格式，其他語言稱MAP或是其他的，就是一個KEY 對一個VALUE
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
# 發送請求
# resp=requests.get(url) 要加上 HEADER
resp=requests.get(url,headers=headers)

resp.encoding='utf-8'
# print(resp.text)

# 使用lxml 解析XPATH
# pip install lxml
from lxml import etree
e = etree.HTML(resp.text)
# datas = e.xpath('//tr/td[2]/*//text()')
datas = e.xpath('//tr/td[2]//a/text()') 
# 
# 以上XPATH ，原網站改了 用SPAN 不行的 XPATH 要改一改
# 註:text()方法
# 
print(datas)
# NEXT 將以上傳成函式
