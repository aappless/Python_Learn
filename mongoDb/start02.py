# 安裝套件 CTRL+~
# pip install pymongo

# ====讀取 INI==========================
print('INI READE')
import configparser
import os
current_directory = os.path.dirname(os.path.abspath(__file__))
config_path = os.path.join(current_directory, 'config.ini') #字串相加

config = configparser.ConfigParser()
# config.read('config.ini', encoding='utf-8')
config.read(config_path, encoding='utf-8')
# config.read('config.ini')
eform=''
try:
    eform=config['SYSTEM']['EFORM_SERVER']
except:
    print('發生錯誤')

print(eform)
print('INI READE END')

if eform=='':
   eform="mongodb://localhost:27017/"

# from pymongo import MongoClient 這二個指令皆可
import pymongo
myclient = pymongo.MongoClient(eform)
# 先定一個不存在的資料庫
mydb=myclient["book"]
# 然後在資料庫中加資料 就會新增這個資料庫 及資料
# mydb['test'].insert_one({"name":"HELLO","age":5})
# print(mydb)
dblst = myclient.list_database_names()
print(dblst)
# 查資料-----------------------
if "book" in dblst:
  print("book資料庫有存在")

collst = mydb.list_collection_names()
if "test" in collst:
    print("test集合有存在")
mycol = mydb["test"]

rows=mycol.find({"name":"HELLO"})
print(rows)

rows=mycol.find({"age":5})
print(rows)

myquery ={"name":"HELLO"}
rows=mycol.find(myquery)
# 轉成LIST
mylist=list(rows)
print(len(mylist))
print(mylist)
for x in rows:
    print(x)


x = mycol.find_one()
print(x)

for result in mycol.find(myquery):
    print('--'+result['name'])
    print(result)

myquery ={"name":"HEXLO"}
mylist=list(mycol.find(myquery))
print(len(mylist))
print(mylist)
# {$gte:ISODate(“2020-03-01”),$lt:ISODate(“2021-03-31”)}}

