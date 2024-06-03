# 安裝套件 CTRL+~
# pip install pymongo
# from pymongo import MongoClient 這二個指令皆可
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
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

for x in rows:
    print(x)


x = mycol.find_one()
print(x)

for result in mycol.find(myquery):
    print('--'+result['name'])


# db.test.find({name:'HELLO'})
#

