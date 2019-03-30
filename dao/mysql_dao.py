# -*- coding: utf-8 -*-
# @Time    : 2019/3/30 19:55
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : mysql_dao.py
# @Software: PyCharm

import pymysql
from consts import HOSTNAME, DATABASE, USERNAME, PASSWORD, CHARSET


try:
    con = pymysql.connect(host=HOSTNAME,
                          db=DATABASE,
                          user=USERNAME,
                          password=PASSWORD,
                          charset=CHARSET,
                          cursorclass=pymysql.cursors.DictCursor)   # 游标
    cur = con.cursor(cursor=pymysql.cursors.DictCursor)
    cur.execute("SELECT VERSION()")
    ver = cur.fetchone()
    print('Database version:%s' % ver)

except pymysql.Error as e:
    print('Error %d:%s' % (e.args[0], e.args[1]))
    exit(1)


def find_country(cursor):
    country_str = input('输入要查询的国家：')   # 'Kabul'
    sql = "SELECT * FROM city where NAME =" + "'" + country_str + "';"
    try:
        cursor.execute(sql)
        result = cursor.fetchall()
        print(type(result))
        print(result)
    except pymysql.Error:
        print('Error:cannot get data!')


def modify_country(cursor, db):

    sql = "UPDATE `world`.`city` SET `Population` = '1780000' WHERE (`ID` = '1');"

    try:
        cursor.execute(sql)
        # 提交操作
        db.commit()
    except pymysql.Error:
        print('Error:rollback')
        # 发生错误则回滚事务
        db.rollback()


if __name__ == "__main__":
    # find_country(cur)
    # modify_country(cur, con)  # 传全局游标
    con.close()  # 关闭数据库放在操作后
