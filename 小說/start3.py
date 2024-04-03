# re --- 正規表示式 (regular expression) 將符合規則的字串篩選出來。
import re
# pip install requests
import requests
# pip install lxml
from lxml import etree
from lxml import html
#  A[@href='/zh_hant/book/68288/32062481.html']
# 以下是取得目錄
url= 'https://m.bqg9527.net/zh_hant/book/68288/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
resp=requests.get(url,headers=headers)
resp.encoding='utf-8'
# 使用XPATH 方式抓出範圍
html_txt=resp.text
tree = etree.HTML(html_txt)
# urls = e.xpath("//ul[@class='chapter']/li/a/@href")
# texts = e.xpath("//ul[@class='chapter']/li/a/text()")
# 這二個分開 會不會有對不上的情況??萬一有一個沒有URL會不會有錯?
# print(urls)
# print(texts)
# 先將章節裏的東西用xpath 抓出來
# 這有二段要排除第一段的 直接指定第2 段這個可用
# chapter_elements = tree.xpath("//ul[@class='chapter'][2]/*")
# 直接排除
chapter_elements = tree.xpath("//ul[@class='chapter' and not(@id='last12')]/*")

print(chapter_elements)
#將各元素轉成XML
new_html = ""
for element in chapter_elements:
    new_html += html.tostring(element, encoding='unicode')

#print(new_html)
# 以下指令是將 二個LIST 組合在一起，zip的使用是texts對應 urls
#result = [(url, text) for url, text in zip(urls, texts)]

#print(result)
# .* 代表除了換行字元之外所有的字元
info_list=re.findall('<li><a href="(.*)">(.*)<span></span></a></li>',new_html)
print(info_list)
#  tuple 使用() list 使用[] , tuple 是不能改的。list 是可以改的open('title.txt', 'w',encoding='utf-8')
f = open('title_N.txt', 'w',encoding='utf-8')

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
