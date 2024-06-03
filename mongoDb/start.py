# 安裝套件 CTRL+~
# pip install pymongo
# from pymongo import MongoClient 這二個指令皆可
import pymongo
myclient = pymongo.MongoClient("mongodb://localhost:27017/")
# 先定一個不存在的資料庫
mydb=myclient["book"]
# 然後在資料庫中加資料 就會新增這個資料庫 及資料
mydb['test'].insert_one({"name":"HELLO","age":5})
print(mydb)
dblst = myclient.list_database_names()
print(dblst)
#-----------------------