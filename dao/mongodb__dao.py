# -*- coding: utf-8 -*-
# @Time    : 2019/3/30 22:57
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : mongodb__dao.py
# @Software: PyCharm

import pymongo
import pymysql
from consts import HOSTNAME, MONGODBPORT, MONGODB_URI, DATABASE, USERNAME, PASSWORD, CHARSET
import json


json_path = 'res/herolist.json'

# con = pymongo.MongoClient(MONGODB_URI)
con = pymongo.MongoClient(host=HOSTNAME, port=MONGODBPORT)  # 连接
db = con.cyg  # 数据库


def test():
    # 增
    db.col.insert({"accout": 21, "user_name": "xiao"})
    # 删
    # db.col.remove({"user_name": "xiao"})
    # 改
    # db.col.update({"user_name": "xiao"}, {
    #               "$set": {"email": "jeiker@126.com", "password": "123456"}})
    # 查
    for item in db.col.find():
        print(item)


def csv2mongodb():
    # 创建集合
    emp = db.data
    # 根据情况清空数据库
    emp.remove(None)

    f = open(json_path, 'r', encoding='utf-8-sig')
    for line in f:
        print(line)
        # everyline = json.loads(line)
        # emp.insert_one(everyline)
        # <<<<<<<<loading>>>>>>>>>
    f.close()


def mysql2json2mongodb():
    con = pymysql.connect(host=HOSTNAME,
                          db=DATABASE,
                          user=USERNAME,
                          password=PASSWORD,
                          charset=CHARSET,
                          cursorclass=pymysql.cursors.DictCursor)
    cur = con.cursor(cursor=pymysql.cursors.DictCursor)
    sql = "SELECT * FROM city"
    cur.execute(sql)
    result = cur.fetchall()
    # 拿到数据库表格内容
    print('从mysql表中拿到的数据格式为：', type(result))
    list_a = result
    print(list_a)
    # 列表转成json
    list_b = json.dumps(list_a)
    print('用json.dumps函数将列表转换为：', type(list_b))
    print(list_b)

    # json写入mongdb
    con = pymongo.MongoClient(host=HOSTNAME, port=MONGODBPORT)  # 连接
    db = con.cyg  # 数据库

    # 先删除文档
    # <<<<<<<<<loading>>>>>>>>>>

    # mongodb条件操作符
    # (>) 大于 - $gt
    # (<) 小于 - $lt
    # (>=) 大于等于 - $gte
    # (<= ) 小于等于 - $lte

    # 删除ID小于5000的(每次新增前先删除)
    db.col.delete_many({"ID": {"$lt": 5000}})
    # 删除等于21的accont
    # db.col.delete_many({"accout": {"$gte": 21}})

    # 列表转成Bson格式
    for i in range(len(list_a)):
        print('插入第', i, '条记录：', list_a[i], '中...')
        db.col.insert_one(list_a[i])

    # 查看是否存进信息
    # print('mongdb数据库中现有：', db.col.find())

    # 示例

    # list_a = [{'ID': 1,
    #            'Name': 'Kabul',
    #            'CountryCode': 'AFG',
    #            'District': 'Kabol',
    #            'Population': 1780000},
    #           {'ID': 2,
    #               'Name': 'Qandahar',
    #               'CountryCode': 'AFG',
    #               'District': 'Qandahar',
    #               'Population': 237500}]
    #
    # print(type(list_a))
    # print(list_a)
    #
    # list_b = json.dumps(list_a)
    # print(type(list_b))
    # print(list_b)
    #
    # list_c = json.loads(list_b)
    # print(type(list_c))
    # print(list_c)


if __name__ == "__main__":
    # csv2mongodb()
    mysql2json2mongodb()
