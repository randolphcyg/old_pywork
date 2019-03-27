# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 19:38
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : prehaddle.py
# @Software: PyCharm

import pandas as pd
import numpy as np

path1 = '../res/传感器布置表.csv'
path2 = '../res/传感器日志数据/day1.csv'


def seconds2current_time(t):
    hours = t // 3600
    minutes = (t - t // 3600 * 3600) // 60
    seconds = t % 3600 % 60
    # print(hours,'时',minutes,'分',seconds,'秒')
    if hours < 10:
        hours = str('0' + str(hours))
    if minutes < 10:
        minutes = str('0' + str(minutes))
    if seconds < 10:
        seconds = str('0' + str(seconds))

    current_time = str(str(hours) + ':' + str(minutes) + ':' + str(seconds))
    # print(current_time)
    return current_time


def core():
    # df1 = pd.read_csv(path1, encoding='utf-8', error_bad_lines=False)

    # 入口位置sid
    entrance_sid = [11300, 11502, 11504, 11507]
    # 出口位置sid
    exit_sid = [10019, 11505, 11515, 11517]
    # 读第一天的所有人经过的所有位置
    df_y = pd.read_csv(path2, encoding='utf-8', error_bad_lines=False,
                       usecols=[0, 1, 2])  # pd.dataframe

    train_data = np.array(df_y)  # np.ndarray()
    train_x_list = train_data.tolist()  # list
    print(train_x_list[0][1])
    # print(type(train_x_list))

    for sid in train_x_list:
        if sid[:][1] in entrance_sid:
            print('参会者', sid[:][0], seconds2current_time(sid[:][2]), '进入会场')
        if sid[:][1] in exit_sid:
            print('参会者', sid[:][0], seconds2current_time(sid[:][2]), '出会场')


if __name__ == "__main__":
    core()
