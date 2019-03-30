# -*- coding: utf-8 -*-
# @Time    : 2019/3/30 21:27
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : consts.py
# @Software: PyCharm


HOSTNAME = 'localhost'
DATABASE = 'world'
USERNAME = 'root'
PASSWORD = '3588'
CHARSET = 'utf8'

MYSQL_URI = 'mysql://{}:{}@{}/{}'.format(HOSTNAME,
                                         DATABASE, USERNAME, PASSWORD)

MONGODBPORT = 27017

# 'mongodb://127.0.0.1:27017/'
MONGODB_URI = 'mongodb://{}:{}'.format(HOSTNAME, MONGODBPORT)

print(MONGODB_URI)
