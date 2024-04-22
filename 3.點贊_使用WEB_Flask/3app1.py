# 第三個練習
# 前面先抄第二個練習的資料(抽獎)
from flask import Flask,render_template,request
# 建立flask 物件
app=Flask(__name__)
# 建立一些資料
data =[
    {'id': 0,'name':'中秋節','num':0},
    {'id': 1,'name':'端午節','num':0},
    {'id': 2,'name':'中元節','num':0},
]

@app.route('/')
def index0():
    return render_template('index.html',data=data)

@app.route('/index')
def index():
    return render_template('index.html',data=data)

@app.route('/clickx')
def clickx():
    id = request.args.get('id')
    print(f'給{{id}}')
    data[int(id)]['num']+=1
    #return '點贊成功'
    return render_template('index.html',data=data)


app.run(debug=True) # 將服務啟動修改後會自動重新啟動
# http://127.0.0.1:5000/index