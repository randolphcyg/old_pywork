# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 19:38
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : prehaddle.py
# @Software: PyCharm

import pandas as pd
import numpy as np

path0 = '../res/传感器布置表.csv'
path1 = '../res/传感器日志数据/day1.csv'
path2 = '../res/传感器日志数据/day2.csv'
path3 = '../res/传感器日志数据/day3.csv'
# 入口位置
entrance_sid = [11300, 11502, 11504, 11507]
# 出口位置
exit_sid = [10019, 11505, 11515, 11517]
# 签到处
check_in_desk = [11202, 11203, 11204, 11205,
                 11302, 11303, 11304, 11305]
# 展厅
exhibition_hall = [10215, 10216, 10217, 10218,
                   10315, 10316, 10317, 10318,
                   10415, 10416, 10417, 10418,
                   10515, 10516, 10517, 10518,
                   10615, 10616, 10617, 10618,
                   10715, 10716, 10717, 10718,
                   10815, 10816, 10817, 10818,
                   10915, 10916, 10917, 10918,
                   11015, 11016, 11017, 11018,
                   11115, 11116, 11117, 11118]
# 主会场，11228为主会场出入口
main_venue = [10219, 10220, 10221, 10222, 10223, 10224,
              10319, 10320, 10321, 10322, 10323, 10324, 10325, 10326, 10327,
              10419, 10420, 10421, 10422, 10423, 10424, 10425, 10426, 10427,
              10519, 10520, 10521, 10522, 10523, 10524, 10525, 10526, 10527,
              10619, 10620, 10621, 10622, 10623, 10624, 10625, 10626, 10627,
              10719, 10720, 10721, 10722, 10723, 10724, 10725, 10726, 10727,
              10819, 10820, 10821, 10822, 10823, 10824, 10825, 10826, 10827,
              10919, 10920, 10921, 10922, 10923, 10924, 10925, 10926, 10927,
              11019, 11020, 11021, 11022, 10423, 11024, 11025, 11026, 11027,
              11119, 11120, 11121, 11122, 10423, 11124, 11125, 11126, 11127]
# 服务台
service_desk = [11419, 11420,
                11519, 11520]
# 房间
room1 = [10610, 10611,
         10710, 10711,
         10810, 10811,
         10910, 10911]
room2 = [11010, 11011,
         11110, 11111]
room3 = [11421, 11422, 11423, 11424,
         11521, 11522, 11523, 11524]
room4 = [11425, 11426,
         11525, 11526]
room5 = [21001, 21002, 21003, 21004,
         21101, 21102, 21103, 21104]
room6 = [20610, 20611]
# 厕所
toilet1 = [10410, 10411,
           10510, 10511]
toilet2 = [11427, 11428,
           11527, 11528]
toilet3 = [20410, 20411,
           20510, 20511]
# 海报区
poster_area = [10307, 10308,
               10407, 10408,
               10507, 10508,
               10607, 10608,
               10707, 10708,
               10807, 10808,
               10907, 10908]
# 分会场
breakout_venue_a = [10201, 10202, 10203, 10204,
                    10301, 10302, 10303, 10304]
breakout_venue_b = [10401, 10402, 10403, 10404,
                    10501, 10502, 10503, 10504]
breakout_venue_c = [10601, 10602, 10603, 10604,
                    10701, 10702, 10703, 10704]
breakout_venue_d = [10801, 10802, 10803, 10804,
                    10901, 10902, 10903, 10904]
# 扶梯
escalator_first_north = [10110, 10111]
escalator_first_south = [11410, 11411]
escalator_second_north = [20110, 20111]
escalator_second_south = [21410, 21411]
# 餐厅
restaurant = [20202, 20203, 20204, 20205,
              20302, 20303, 20304, 20305,
              20402, 20403, 20404, 20405,
              20502, 20503, 20504, 20505,
              20602, 20603, 20604, 20605,
              20702, 20703, 20704, 20705,
              20802, 20803, 20804, 20805,
              20902, 20903, 20904, 20905]
# 休息区
lounge_area = [21300, 21301, 21302, 21303, 21304, 21305,
               21400, 21401, 21402, 21403, 21404, 21405,
               21500, 21501, 21502, 21503, 21504, 21505]


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


def writefile(path):
    f = open(path, 'a', encoding='utf_8')  # 保存的txt
    return f


def core(path):
    # df1 = pd.read_csv(path0, encoding='utf-8', error_bad_lines=False)
    # 读第一天的所有人经过的所有位置
    df_y = pd.read_csv(path, encoding='utf-8', error_bad_lines=False,
                       usecols=[0, 1, 2])  # pd.dataframe
    train_data = np.array(df_y)  # np.ndarray()
    train_x_list = train_data.tolist()  # list
    # print(train_x_list[0][1])
    # print(type(train_x_list))
    return train_x_list


def analysis_place():
    for i, sid in enumerate(core(path1)):

        # if sid[:][1] in entrance_sid:
        #     print(i, '参会者', sid[:][0], seconds2current_time(sid[:][2]), '进入会场')
        # if sid[:][1] in exit_sid:
        #     print(i, '参会者', sid[:][0], seconds2current_time(sid[:][2]), '出会场')
        # if sid[:][1] in check_in_desk:
        #     print('参会者', sid[:][0], seconds2current_time(sid[:][2]), '签到')
        # if sid[:][1] in exhibition_hall:
        #     print('参会者', sid[:][0], seconds2current_time(sid[:][2]), '进入展厅')

        # # 主会场人员规律
        # main_venue_path = '../res/main_venue.txt'
        # if sid[:][1] in main_venue:
        #     print('参会者', sid[:][0], seconds2current_time(sid[:][2]), '主会场')
        #     content1 = str(sid[:][0])
        #     content2 = str(seconds2current_time(sid[:][2]))
        #     writefile(main_venue_path).write('参会者：' + content1 + ' 进出时间：' + content2 + '\n')

        # # 餐厅人流规律
        # restaurant_path = '../res/restaurant.txt'
        # if sid[:][1] in restaurant:
        #     print('参会者', sid[:][0], seconds2current_time(sid[:][2]), '餐厅')
        #     content1 = str(sid[:][0])
        #     content2 = str(seconds2current_time(sid[:][2]))
        #     writefile(restaurant_path).write('参会者：' + content1 + ' 进出时间：' + content2 + '\n')

        # # 厕所1
        # toilet1_path = '../res/toilet1.txt'
        # if sid[:][1] in toilet1:
        #     print('参会者', sid[:][0], seconds2current_time(sid[:][2]), '厕所1')
        #     content1 = str(sid[:][0])
        #     content2 = str(seconds2current_time(sid[:][2]))
        #     writefile(toilet1_path).write('参会者：' + content1 + ' 进出时间：' + content2 + '\n')

        pass


per16111_path = '../res/16111.txt'


def analysis_person():
    for i, sid in enumerate(core(path1)):
        if sid[:][0] == 16111:
            print(sid[:][1], seconds2current_time(sid[:][2]))
            c1 = str(sid[:][1])
            c2 = str(seconds2current_time(sid[:][2]))
            writefile(per16111_path).write(c1 + ' ' + c2 + '\n')



if __name__ == "__main__":
    # analysis_place()
    analysis_person()
