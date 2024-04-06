# 使用Flask框架 按下CTRL+~ 出現TERMINAL
# pip install flask 注意要在(.venv)下
from flask import Flask
# 建立flask 物件
app=Flask(__name__)

# 建一個路徑 
# @是一個函式的修飾器，要用在定義函式之前
# ---------------- 
# @裝飾器
# def 函式名():
#     函式內部
# ----------------
#以上是會先執行裝飾器的程式碼，再去執行裏面的程式碼
#也就是說@app.route('/index')這一個是已在flas裏定好的裝飾器函式
# 會先去執行app.route('/index') 再去執行 index()
# 看起來是app.route 的固定寫法~ 

@app.route('/index')
def index():
    return 'Hello'
# 以上執行開啟  http://127.0.0.1:5000/index


# app.run() # 將服務啟動
app.run(debug=True) # 將服務啟動並可DEBUG，就是程式碼有變會自動重啟服務

