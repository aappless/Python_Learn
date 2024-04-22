# re --- 正規表示式 (regular expression) 將符合規則的字串篩選出來。
import re
# pip install requests
import requests
# pip install lxml
from lxml import etree
from lxml import html
# 以下是取得目錄
url= 'https://m.bqg9527.net/zh_hant/book/68288/'
headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
resp=requests.get(url,headers=headers)
resp.encoding='utf-8'
# 使用XPATH 方式抓出範圍
html_txt=resp.text
tree = etree.HTML(html_txt)
#取書名，作者
# bookname=tree.xpath("//div[@class='block_txt2']/h2/*/text()")[0]
bookname=''.join(tree.xpath("//div[@class='block_txt2']/h2/*/text()"))
print(bookname)
author=''.join(tree.xpath("//div[@class='block_txt2']/p[1]/*/text()"))
print(author)
# -----------------
# 以書名作者建目錄
import os
print(os.getcwdb())
dir = os.getcwd() + "\\" + bookname + "_" + author
print(dir)
if not os.path.exists(dir):
    os.mkdir(dir)

# 這有二段要排除第一段的 直接指定第2 段這個可用
# chapter_elements = tree.xpath("//ul[@class='chapter'][2]/*")
# 直接排除
chapter_elements = tree.xpath("//ul[@class='chapter' and not(@id='last12')]/*")
#將各元素轉成XML 注意這裏使用HTML物件 轉和上面的用etree物件轉相同
new_html = ""
for element in chapter_elements:
    new_html += html.tostring(element, encoding='unicode')

# .* 代表除了換行字元之外所有的字元 將二個()裏的東西 存入成一組 LIST(元組)，也就是每個LIST有二個東西，
info_list=re.findall('<li><a href="(.*)">(.*)<span></span></a></li>',new_html)
#  tuple 使用() list 使用[] , tuple 是不能改的。list 是可以改的open('title.txt', 'w',encoding='utf-8')
i =0
for info in info_list:
    i += 1
    urlx ='https://m.bqg9527.net'+info[0]
    titlex = info[1]
    #4碼補0 + 章節名
    fn = str(i).zfill(4) +'_'+ info[1]+'.txt'
    print(urlx,titlex)

    # 取得內容
    resp=requests.get(urlx,headers=headers)
    resp.encoding='utf-8'
    #print(resp.text)
    html_data = etree.HTML(resp.text)
    # div 一定要小寫
    chapter=''.join(html_data.xpath("//div[@id='nr_title']/text()"))
    chapter='    '+chapter.lstrip()
    print(chapter)
    txt_list =''.join(html_data.xpath('//div[@id="nr1"]/text()'))
    #文字取代有幾種方式，正則也可以
    txt_list=txt_list.replace('“','「')
    txt_list=txt_list.replace('”','」')
    print(txt_list)

    with open(dir+'\\'+fn, 'w',encoding='utf-8') as f:
        f.write(chapter+'\n'+txt_list+'\n')

print('數量:',len(info_list))
