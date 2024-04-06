#以下程式未測試
from time import sleep
import datetime
import requests
from lxml import etree

def page_numbers(url):
    response = requests.get(url)
    html = etree.HTML(response.text)
    next_tag = html.xpath("//a[@rel='next']")[0] # 定位出下一頁
    final_page = next_tag.getparent().getprevious().find('a').text # 下一頁按鈕的前一個按鈕及為最後一頁的數字
    return int(final_page)
  
def get_title_url(html,target_date):
    element_list = html.xpath("//div[@class = 'qa-list']")
    answered_tag = "qa-condition  qa-condition--has-answer   qa-condition--had-answer  " # 已有最佳解答
    target_date = target_date.strftime("%Y-%m-%d")
    articles = {}
    for element in element_list:
        tags = [t.text for t in element.findall("./div[@class = 'qa-list__content']/div[@class='qa-list__tags']/a")] # 列出所有 Tag
        time = element.find("./div[@class = 'qa-list__content']/div[@class='qa-list__info']/a[1]").text # 定位出時間
        answer_status = element.find("./div[@class = 'qa-list__condition']/a[2]").get('class') # 找出回答標籤的 class 內容
        if answer_status != answered_tag and "python" in tags and time == target_date: # 若三個條件皆符合，則收入為目標問題
            articles[element.find("./div[@class = 'qa-list__content']/h3/a").text] = element.find("./div[@class = 'qa-list__content']/h3/a").get("href")
    return articles
  
  
target_url = "https://ithelp.ithome.com.tw/questions"
today = datetime.date.today()
target_date = today.replace(day=today.day -1)
last_page = page_numbers(target_url)
articles = {}

for page in range(last_page):
    response = requests.get(target_url,params = {'page':page+1})
    html = etree.HTML(response.text)
    articles = {**articles,**get_title_url(html,target_date)}
    last_question_date = html.xpath("//div[@class='qa-list__info']/a[1]")[-1].text
    if datetime.datetime.strptime(last_question_date,"%Y-%m-%d").date() < target_date:
        break