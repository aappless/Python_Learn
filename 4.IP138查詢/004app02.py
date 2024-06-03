# 將所需的模組 放到上面
# 一個WEB 服務 模組
# 安裝送網路請求的套件 CTRL+'
# pip install flask
# pip install requests
# pip install lxml
import requests
from lxml import etree
# 提供WEB 服務
from flask import Flask,render_template

app=Flask(__name__) #建立一個WEB的物件


def get_mobile(phone):

    # 發送=送請求地址
    url=f'https://www.ip138.com/mobile.asp?mobile={phone}&action=mobile'
    # 前面一段和抓小說一樣# 第一步 發送請求

    # 偽裝成瀏灠器 使用PYTHON字典格式，其他語言稱MAP或是其他的，就是一個KEY 對一個VALUE
    headers={'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36'}
    # 發送請求
    # resp=requests.get(url) 要加上 HEADER
    resp=requests.get(url,headers=headers)

    resp.encoding='utf-8'
    # print(resp.text)

    # 使用lxml 解析XPATH


    e = etree.HTML(resp.text)
    # datas = e.xpath('//tr/td[2]/*//text()')
    datas = e.xpath('//tr/td[2]//a/text()')
    #
    # 以上XPATH ，原網站改了 用SPAN 不行的 XPATH 要改一改
    # 註:text()方法
    #
    print(datas)
    # NEXT 將以上傳成函式


#get_mobile(18811018888)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search_phone')
def search_phone():
    return "Hello"
app.run(debug=True) # 啟動服務，修程式 自動重啟
