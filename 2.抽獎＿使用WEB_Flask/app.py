# 第二個練習
# 使用Flask框架 按下CTRL+~ 出現TERMINAL
# pip install flask 注意要在(.venv)下
from flask import Flask
# 建立flask 物件
app=Flask(__name__)

# app.run() # 將服務啟動
app.run(debug=True) # 將服務啟動並可DEBUG，就是不用一直啟動

#執行後 開啟 CHROME 會沒有網頁，因為沒有建立