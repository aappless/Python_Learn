from flask import Flask,render_template
#二、亂數
from random import randint
# 建立flask 物件
app = Flask(__name__)


hero = [
    "亞歷斯塔",
    "亞菲利歐",
    "伊澤瑞爾",
    "伊瑞莉雅",
    "伊羅旖",
    "伊芙琳",
    "伊莉絲",
    "克雷德",
    "克黎思妲",
    "凱爾",
    "凱特琳",
    "凱能",
    "凱莎",
    "剎雅",
    "剛普朗克",
    "加里歐",
    "努努和威朗普",
    "劫",
    "勒布朗",
    "卡力斯",
    "卡桑帝",
    "卡爾瑟斯",
    "卡特蓮娜",
    "卡瑪",
    "卡莎碧雅",
    "卡薩丁",
    "卡蜜兒",
    "厄薩斯",
    "古拉格斯",
    "史加納",
    "史瓦妮",
    "史矛德",
    "吉茵珂絲",
    "吶兒",
    "嘉文四世",
    "圖奇",
    "埃可尚",
    "埃爾文",
    "塔莉雅",
    "塔里克",
    "塔隆",
    "墨菲特",
    "夜曲",
    "奈德麗",
    "奧莉安娜",
    "好運姐",
    "妮可",
    "姍娜",
    "姬亞娜",
    "威寇茲",
    "娜米",
    "娜菲芮",
    "婕莉",
    "安妮",
    "寇格魔",
    "崔絲塔娜",
    "巴德",
    "布蕾爾",
    "布蘭德",
    "布郎姆",
    "布里茨",
    "希格斯",
    "希瓦娜",
    "希維爾",
    "庫奇",
    "弗力貝爾",
    "弗拉迪米爾",
    "悟空",
    "悠咪",
    "慎",
    "慨影",
    "拉克絲",
    "拉姆斯",
    "提摩",
    "斯溫",
    "易大師",
    "星朵拉",
    "札克",
    "李星",
    "杰西",
    "枷蘿",
    "柔依",
    "極靈",
    "歐拉夫",
    "汎",
    "沃維克",
    "法洛士",
    "波比",
    "泰達米爾",
    "派克",
    "淣菈",
    "漢默丁格",
    "潘森",
    "烏爾加特",
    "烏迪爾",
    "煞蜜拉",
    "燼",
    "特朗德",
    "犽凝",
    "犽宿",
    "珍娜",
    "瑟菈紛",
    "瑟雷西",
    "睿娜妲．格萊斯克",
    "科加斯",
    "米里歐",
    "約瑞科",
    "納帝魯斯",
    "納瑟斯",
    "索娜",
    "索拉卡",
    "維克特",
    "維爾戈",
    "維迦",
    "翱銳龍獸",
    "艾克",
    "艾妮維亞",
    "艾希",
    "茂凱",
    "莉莉亞",
    "菲歐拉",
    "菲艾",
    "葛雷夫",
    "葵恩",
    "蒙多醫生",
    "蓋倫",
    "薇可絲",
    "薩科",
    "藍寶",
    "貝爾薇斯",
    "貪啃奇",
    "費德提克",
    "賈克斯",
    "賽勒斯",
    "賽恩",
    "賽特",
    "赫克林",
    "赫威",
    "趙信",
    "路西恩",
    "辛吉德",
    "逆命",
    "達瑞文",
    "達瑞斯",
    "鄂爾",
    "銳兒",
    "銳空",
    "鏡爪",
    "關",
    "阿卡莉",
    "阿姆姆",
    "阿璃",
    "阿祈爾",
    "雷尼克頓",
    "雷歐娜",
    "雷玟",
    "雷珂煞",
    "雷茲",
    "雷葛爾",
    "露璐",
    "飛斯",
    "馬爾札哈",
    "魔甘娜",
    "魔鬥凱薩",
    "麗珊卓",
    "黛安娜",
    "齊勒斯",
]




# 建一個路徑
# @是一個函式的修飾器，要用在定義函式之前
# ----------------
# @裝飾器
# def 函式名():
#     函式內部
# ----------------
# 以上是會先執行裝飾器的程式碼，再去執行裏面的程式碼
# 也就是說@app.route('/index')這一個是已在flas裏定好的裝飾器函式
# 會先去執行app.route('/index') 再去執行 index()
# 看起來是app.route 的固定寫法~


@app.route("/index")
def index():
    return render_template('index.html',hero=hero)
# 一、亂數抽獎 建立一個網頁
@app.route("/getrandom")
def getrandom():
    # 亂數由0開始
    num=randint(0,len(hero)-1)
    return render_template('index.html',hero=hero,h=hero[num])
# 以上執行開啟  http://127.0.0.1:5000/index


# app.run() # 將服務啟動
app.run(debug=True)  # 將服務啟動並可DEBUG，就是不用一直啟動
