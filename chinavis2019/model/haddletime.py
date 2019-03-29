# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 15:32
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : haddletime.py
# @Software: PyCharm


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
    print(current_time)
    return current_time


if __name__ == "__main__":
    t1 = 25240
    t2 = 45164
    seconds2current_time(t1)
    seconds2current_time(t2)
