# re --- 正規表示式 (regular expression) 將符合規則的字串篩選出來。
# 在python 有三種方式，match,search,findall
# 一、re.match(四配规,被匹配字符)
# 從被匹配字符 【從開頭開始進行匹配】,匹配成功返回匹配對象(包含匹配的信息),匹配不成功返回空。
# s = 'python itheima python itheima python itheima'
# result = re.match('python', s) ，有二個傳回 result.span()  result.group()
# 二、re.search('python', s) 找字串中所有的文字，只找到一個就不找了。
# 三、findall 可找出全部，返回LIST
# 字符 .除了換行以外所有的字
#      ^開頭 就是NOT 的意思，[^0-9]==>非數字 ，
#      內定符號 \d 表示[0-9], \D => [^0-9]
#      \w 任意字母，數字。\W 非任意字母及數字
#      \s 空格 ,\S 非空格
#       yes|no ==>yes OR NO
#       ? 是出0次或1前都可以
#       * 是沒出現或出現很多次都可以
#      #尾部
#      +
#      # ?
#      []
#
import re
# pip install requests
import requests
# pip install lxml
from lxml import etree
#  A[@href='/zh_hant/book/68288/32062481.html']
# 以下是取得目錄
url= 'https://m.bqg9527.net/zh_hant/book/68288/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
resp=requests.get(url,headers=headers)
resp.encoding='utf-8'
#print(resp.text)
# xpath 不會顯示全部 (影片上的範例說的)
# 取得目錄 使用正則，抓出符合規則的文字 <a href="/zh_hant/book/68288/32064907.html">
# .* 代表除了換行字元之外所有的字元
info_list=re.findall('<li><a href="(.*)">(.*)<span></span></a></li>',resp.text)
print(info_list)
#  tuple 使用() list 使用[] , tuple 是不能改的。list 是可以改的open('title.txt', 'w',encoding='utf-8')
f = open('title.txt', 'w',encoding='utf-8')

for info in info_list:
    # comment:
    url=info[0]
    title=info[1]
    print(url,title)
    f.write(title+' '+url+'\n')
   # with open('title.txt', 'w',encoding='utf-8') as f:
    #    f.write(title+' '+url+'\n')
    # Comment:

# end for
f.close()
print('數量:',len(info_list))
# 二個問題，一，會多抓預覽的章節，二抓JS非同步不會有文章(有些網頁)
