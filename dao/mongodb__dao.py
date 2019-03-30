# -*- coding: utf-8 -*-
# @Time    : 2019/3/30 22:57
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : mongodb__dao.py
# @Software: PyCharm

import pymongo
from consts import HOSTNAME, MONGODBPORT, MONGODB_URI


# con = pymongo.MongoClient(MONGODB_URI)
con = pymongo.MongoClient(host=HOSTNAME, port=MONGODBPORT)  # 连接
db = con.cyg  # 数据库

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
