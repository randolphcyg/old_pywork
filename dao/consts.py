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

DB_URI = 'mysql://{}:{}@{}/{}'.format(
    USERNAME, PASSWORD, HOSTNAME, DATABASE, CHARSET
)