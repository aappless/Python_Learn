# re --- 正規表示式 (regular expression) 將符合規則的字串篩選出來。
# 在python 有三種方式，match,search,findall
# 一、re.match(四配规,被匹配字符)
# 從被匹配字符 【從開頭開始進行匹配】,匹配成功返回匹配對象(包含匹配的信息),匹配不成功返回空。
# s = 'python itheima python itheima python itheima'
# result = re.match('python', s) ，有二個傳回 result.span()  result.group()
# 二、re.search('python', s) 找字串中所有的文字，只找到一個就不找了。
# 三、findall 可找出全部，返回LIST
# 字符 .除了換行以外所有的字
#      ^開頭
#      #尾部
#      +
#      ?
#      []
#
import re
import requests
from lxml import etree
#  A[@href='/zh_hant/book/68288/32062481.html']
url= 'https://m.bqg9527.net/zh_hant/book/68288/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
resp=requests.get(url,headers=headers)
resp.encoding='utf-8'
print(resp.text)