# # 抓網必需
# import requests
# # 分析網頁必需
# from lxml import etree
# # 時間
# from time import sleep 
# 函式寫法def 函式名 傳入html 未定義 看起來 html 是 etree 物件
#以「下一頁」做為目標，不斷的讀取該標籤的 URL 往下爬
# def page_numbers(html):
#     next_tag = html.xpath("//a[@rel='next']")[0] # 定位出下一頁 
#     final_page = next_tag.getparent().getprevious().find('a').text 
#     # 下一頁按鈕的前一個按鈕及為最後一頁的數字
#     return int(final_page)
 
 #擷取每個分類的文章網址
 # 以下程式未完成DEBUG 只是網站所抓
from time import sleep
import requests
from lxml import etree

def page_numbers(html):
    print(html)
    next_tag = html.xpath("//a[@rel='next']") # 定位出下一頁
    final_page = next_tag.getparent().getprevious().find('a').text # 下一頁按鈕的前一個按鈕及為最後一頁的數字
    return int(final_page)
  
def get_article_url(url, last_page):
    urls = set()
    for i in range(last_page):
        response = requests.get(url, params = {'page':i+1})
        html = etree.HTML(response.text)
        urls = urls.union(set(html.xpath("//a[@class = 'qa-list__title-link']/@href")))
        sleep(100) # 做隻有禮貌的蟲
    return urls

def article_parse(link):
    response = requests.get(link)
    html = etree.HTML(response.text)
    mk = html.xpath("//div[@class='markdown__style']")[0]
    header = html.xpath("//h2[@class = 'qa-header__title']/text()")[0]
    return {header : etree.tostring(mk, method='text', encoding='unicode', pretty_print=True).strip()}
  
target_url = ["https://ithelp.ithome.com.tw/questions",
             "https://ithelp.ithome.com.tw/questions?tab=hot",
             "https://ithelp.ithome.com.tw/questions?tab=solved"]
article_urls = set()

for url in target_url:
    response = requests.get(url) # 這裏少參數呀
    html = etree.HTML(response.text)
    last_page =  page_numbers(html)
    article_urls = article_urls.union(get_article_url(url,last_page))

article = {}
for url in article_urls:
    article = {**article,**article_parse(url)}
    sleep(100) # 做隻有禮貌的蟲