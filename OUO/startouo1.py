# re --- 正規表示式 (regular expression) 將符合規則的字串篩選出來。
import re
# pip install requests
import requests
# pip install lxml
from lxml import etree
from lxml import html
# 以下是取得目錄
url= 'https://ouo.io/Wv4Aute'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
resp=requests.get(url,headers=headers)
resp.encoding='utf-8'
# 使用XPATH 方式抓出範圍
html_txt=resp.text
tree = etree.HTML(html_txt)
print(html_txt)
# 以下沒有了~ 有空再來做
