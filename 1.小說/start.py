# 第一步 發送請求
# 安裝送網路請求的套件 CTRL+'  <~
# pip install requests

import requests
# 過慮HTML  TAG
# 安裝 lxml ,   pip install lxml
# 引用模組 命名空間 lxml裏的etree
from lxml import etree
# 在CHROME 中裝擴充 xpath helper 用來過慮TAG



# 要抓的網站，注意小說內容不是另由JAVSSCRIPT 產生，
url= 'https://www.twking.cc/161_161329/56074098.html'

# 偽裝成瀏灠器 使用PYTHON字典格式，其他語言稱MAP或是其他的，就是一個KEY 對一個VALUE
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
# 發送請求
# resp=requests.get(url) 要加上 HEADER
resp=requests.get(url,headers=headers)
# PRINT
resp.encoding='utf-8'
# print(resp.text)
# html_txt=bytes(bytearray(resp.text,encoding='utf-8'))這會路出\XE7 等編碼
html_txt=resp.text
# print(html_txt)
e = etree.HTML(html_txt)
#  sss = e.xpath('//ARTICLE[@id="article"]')
# sss = e.xpath('//article')
# LSJ 註後面要加上/text()，不然會傳會節點的LIST==>[<Element article at 0x20b7adf4240>]
# sss = e.xpath('//*[@id="article"]/text()')
# 由於傳回值是列表 使用 '\n'.join() 是指每個元素用一個換行連結起來
sss = '\n'.join(e.xpath('//*[@id="article"]/text()'))
# 列表格式 取第一個列表
titl=e.xpath('//h1/text()')[0]
print(titl)
print(sss)
# 輸出有表示是一個列表
# print(html)
# 存文字檔  檔名       覆蓋寫入 \n\n 換行
with open('mytxt.txt', 'w',encoding='utf-8') as f:
    # Comment:
    f.write(titl+'\n'+sss+'\n')
# end overwrite file
