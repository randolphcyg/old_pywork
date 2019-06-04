# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 19:38
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : prehaddle.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import os.path
import json
from collections import Counter

path0 = '../res/传感器布置表.csv'
path1 = '../res/传感器日志数据/day1.csv'
path2 = '../res/传感器日志数据/day2.csv'
path3 = '../res/传感器日志数据/day3.csv'

# # 入口位置
# area_entrance_port = [11300, 11502, 11504, 11507]
# # 出口位置
# area_exit_port = [10019, 11505, 11515, 11517]
# # 签到处
# area_check_in_desk = [11202, 11203, 11204, 11205, 11302, 11303, 11304, 11305]
# # 展厅
# area_exhibition_hall = [10215, 10216, 10217, 10218, 10315, 10316, 10317, 10318,
#                         10415, 10416, 10417, 10418, 10515, 10516, 10517, 10518,
#                         10615, 10616, 10617, 10618, 10715, 10716, 10717, 10718,
#                         10815, 10816, 10817, 10818, 10915, 10916, 10917, 10918,
#                         11015, 11016, 11017, 11018, 11115, 11116, 11117, 11118]
# # 主会场
# area_main_venue = [10219, 10220, 10221, 10222, 10223, 10224,
#                    10319, 10320, 10321, 10322, 10323, 10324, 10325, 10326, 10327,
#                    10419, 10420, 10421, 10422, 10423, 10424, 10425, 10426, 10427,
#                    10519, 10520, 10521, 10522, 10523, 10524, 10525, 10526, 10527,
#                    10619, 10620, 10621, 10622, 10623, 10624, 10625, 10626, 10627,
#                    10719, 10720, 10721, 10722, 10723, 10724, 10725, 10726, 10727,
#                    10819, 10820, 10821, 10822, 10823, 10824, 10825, 10826, 10827,
#                    10919, 10920, 10921, 10922, 10923, 10924, 10925, 10926, 10927,
#                    11019, 11020, 11021, 11022, 10423, 11024, 11025, 11026, 11027,
#                    11119, 11120, 11121, 11122, 10423, 11124, 11125, 11126, 11127]
# # 服务台
# area_service_desk = [11419, 11420, 11519, 11520]
# # 房间
# area_room1 = [10610, 10611, 10710, 10711, 10810, 10811, 10910, 10911]
# area_room2 = [11010, 11011, 11110, 11111]
# area_room3 = [11421, 11422, 11423, 11424, 11521, 11522, 11523, 11524]
# area_room4 = [11425, 11426, 11525, 11526]
# area_room5 = [21001, 21002, 21003, 21004, 21101, 21102, 21103, 21104]
# area_room6 = [20610, 20611, 20710, 20711]
# # 厕所
# area_toilet1 = [10410, 10411, 10510, 10511]
# area_toilet2 = [11427, 11428, 11527, 11528]
# area_toilet3 = [20410, 20411, 20510, 20511]
# # 海报区
# area_poster_area = [10307, 10308, 10407, 10408, 10507, 10508, 10607,
#                     10608, 10707, 10708, 10807, 10808, 10907, 10908]
# # 分会场
# area_venue_a = [10201, 10202, 10203, 10204, 10301, 10302, 10303, 10304]
# area_venue_b = [10401, 10402, 10403, 10404, 10501, 10502, 10503, 10504]
# area_venue_c = [10601, 10602, 10603, 10604, 10701, 10702, 10703, 10704]
# area_venue_d = [10801, 10802, 10803, 10804, 10901, 10902, 10903, 10904]
# # 扶梯
# area_escalator_first_north = [10110, 10111]
# area_escalator_first_south = [11410, 11411]
# area_escalator_second_north = [20110, 20111]
# area_escalator_second_south = [21410, 21411]
# # 餐厅
# area_restaurant = [20202, 20203, 20204, 20205, 20302, 20303, 20304, 20305,
#                    20402, 20403, 20404, 20405, 20502, 20503, 20504, 20505,
#                    20602, 20603, 20604, 20605, 20702, 20703, 20704, 20705,
#                    20802, 20803, 20804, 20805, 20902, 20903, 20904, 20905]
# # 休息区
# area_lounge_area = [21300, 21301, 21302, 21303, 21304, 21305,
#                     21400, 21401, 21402, 21403, 21404, 21405,
#                     21500, 21501, 21502, 21503, 21504, 21505]
# # 所有区域的name对应的sid
# place_all = {
#     'entrance_port': area_entrance_port,
#     'exit_port': area_exit_port,
#     'check_in_desk': area_check_in_desk,
#     'exhibition_hall': area_exhibition_hall,
#     'main_venue': area_main_venue,
#     'service_desk': area_service_desk,
#     'room1': area_room1,
#     'room2': area_room2,
#     'room3': area_room3,
#     'room4': area_room4,
#     'room5': area_room5,
#     'room6': area_room6,
#     'toilet1': area_toilet1,
#     'toilet2': area_toilet2,
#     'toilet3': area_toilet3,
#     'poster_area': area_poster_area,
#     'venue_a': area_venue_a,
#     'venue_b': area_venue_b,
#     'venue_c': area_venue_c,
#     'venue_d': area_venue_d,
#     'escalator_first_north': area_escalator_first_north,
#     'escalator_first_south': area_escalator_first_south,
#     'escalator_second_north': area_escalator_second_north,
#     'escalator_second_south': area_escalator_second_south,
#     'restaurant': area_restaurant,
#     'lounge_area': area_lounge_area
# }

# 签到处
check_in_desk = [[11302, 11301], [11302, 11401], [11302, 11402], [11302, 11403],
                 [11303, 11402], [11303, 11403], [11303, 11404],
                 [11304, 11403], [11304, 11404], [11304, 11405],
                 [11305, 11404], [11305, 11405], [11305, 11406], [11305, 11306], [11305, 11206],
                 [11205, 11106], [11205, 11206], [11205, 11306]]
# 海报区
poster_area = [[10307, 10406], [10307, 10306], [10307, 10206], [10307, 10207], [10307, 10208],
               [10308, 10207], [10308, 10208], [10308, 10209], [10308, 10309], [10308, 10409],
               [10407, 10306], [10407, 10406], [10407, 10506],
               [10507, 10406], [10507, 10506], [10507, 10606],
               [10607, 10506], [10607, 10606], [10607, 10706],
               [10707, 10606], [10707, 10706], [10707, 10806],
               [10807, 10706], [10807, 10806], [10807, 10906],
               [10907, 10806], [10907, 10906], [10907, 11006], [10907, 11007], [10907, 11008],
               [10908, 11007], [10908, 11008], [10908, 11009], [10908, 10909], [10908, 10809],
               [10808, 10909], [10808, 10809], [10808, 10709],
               [10708, 10809], [10708, 10709], [10708, 10609],
               [10608, 10709], [10608, 10609], [10608, 10509],
               [10508, 10609], [10508, 10509], [10508, 10409],
               [10408, 10509], [10408, 10409], [10408, 10309]]
# 展厅
exhibition_hall = [[11116, 11216], [11117, 11217], [10218, 10219]]
# 服务台
service_desk = [[11419, 11418], [11419, 11318], [11419, 11319], [11419, 11320],
                [11420, 11319], [11420, 11320], [11420, 11321]]
# 主会场
main_venue = [[11121, 11221], [11123, 11223],
              [11125, 11225], [10219, 10218], [10219, 10119]]
room1 = [[10710, 10709], [10910, 10909]]
room2 = [[11110, 11109]]
room3 = [[11422, 11322], [11424, 11324]]
room4 = [[11425, 11325]]
room5 = [[21005, 21006], [21105, 21106]]
room6 = [[20610, 20609], [20710, 20709]]
toilet1 = [[10410, 10409], [10510, 10509]]
toilet2 = [[11427, 11327], [11428, 11328]]
toilet3 = [[20410, 20409], [20510, 20509]]
# 分会场
venue_a = [[10205, 10206], [10305, 10306]]
venue_b = [[10405, 10406], [10505, 10506]]
venue_c = [[10605, 10606], [10705, 10706]]
venue_d = [[10805, 10806], [10905, 10906]]
# 南北扶梯
escalator_north = [[10111, 10210], [10111, 10211], [10111, 10112],
                   [20111, 20211], [20111, 20210]]
escalator_south = [[11411, 11310], [11411, 11311], [11411, 11312], [11411, 11412],
                   [21411, 21311], [21411, 21310]]
restaurant = [[20205, 20206], [20505, 20506], [20805, 20806]]
# 休息区
lounge_area = [[21405, 21406]]
# 签到周围 误差好大
around_check_in_desk = [[11301, 11300], [11301, 11302],
                        [11401, 11302], [11401, 11502], [11402, 11300], [11402, 11302], [11402, 11502],
                        [11403, 11302], [11403, 11303], [11403, 11304], [11403, 11502], [11403, 11504],
                        [11404, 11303], [11404, 11304], [11404, 11305], [11404, 11504], [11404, 11505],
                        [11405, 11304], [11405, 11305], [11405, 11504], [11405, 11505],
                        [11406, 11305], [11406, 11505], [11406, 11507], [11408, 11507],
                        [11306, 11305], [11306, 11205],
                        [11206, 11305], [11206, 11205], [11407, 11507],
                        [11106, 11205], [11106, 11006], [11106, 11007],
                        [11107, 11006], [11107, 11007], [11107, 11008],
                        [11108, 11007], [11108, 11008], [11108, 11009],
                        [11109, 11110], [11109, 11009], [11109, 11008], [11109, 11210],
                        [11209, 11210], [11209, 11310],
                        [11309, 11210], [11309, 11310],
                        [11409, 11310]]
# 前走廊 有一个没出去
front_main_venue = [[11225, 11125], [11223, 11123], [11221, 11121], [11217, 11117], [11216, 11116],
                    [11327, 11427], [11326, 11426], [11325, 11425], [11324, 11424], [11322, 11422],
                    [11321, 11420], [11320, 11420], [11320, 11419], [11319, 11420], [11319, 11419], [11318, 11419],
                    [11418, 11419], [11417, 11517], [11415, 11515], [11412, 11411], [11312, 11411], [11311, 11411],
                    [11310, 11411], [11310, 11309], [11310, 11209], [11310, 11409],
                    [11210, 11109], [11210, 11209], [11210, 11309]]
# 差了57个，但是建模都正常啊
around_poster_area = [[10406, 10307], [10306, 10307], [10206, 10307], [10207, 10307], [10208, 10307],
                      [10207, 10308], [10208, 10308], [10209, 10308], [10309, 10308], [10409, 10308],
                      [10306, 10407], [10406, 10407], [10506, 10407], [10406, 10507], [10506, 10507],
                      [10606, 10507], [10506, 10607], [10606, 10607], [10706, 10607], [10606, 10707],
                      [10706, 10707], [10806, 10707], [10706, 10807], [10806, 10807], [10906, 10807],
                      [10806, 10907], [10906, 10907], [11006, 10907], [11007, 10907], [11008, 10907],
                      [11007, 10908], [11008, 10908], [11009, 10908], [10909, 10908], [10809, 10908],
                      [10909, 10808], [10809, 10808], [10709, 10808], [10809, 10708], [10709, 10708],
                      [10609, 10708], [10709, 10608], [10609, 10608], [10509, 10608], [10609, 10508],
                      [10509, 10508], [10409, 10508], [10509, 10408], [10409, 10408], [10309, 10408],
                      [10206, 10205], [10306, 10305], [10406, 10405], [10506, 10505], [10606, 10605],
                      [10706, 10705], [10806, 10805], [10906, 10905], [10409, 10410], [10509, 10510],
                      [10709, 10710], [10909, 10910],
                      [10209, 10210], [10209, 10310], [10309, 10310], [10309, 10210],
                      [11006, 11106], [11006, 11107],
                      [11007, 11106], [11007, 11107], [11007, 11108],
                      [11008, 11107], [11008, 11108], [11008, 11109],
                      [11009, 11108], [11009, 11109]]
# 后走廊 没毛病
back_main_venue = [[10119, 10019], [10119,10219], [10118, 10019], [10112, 10111], [10211, 10111], [10210, 10111],
                   [10210, 10209], [10210, 10309], [10310, 10209], [10310, 10309], [10310, 10409]]
place_all = {
    'check_in_desk': check_in_desk,
    'poster_area': poster_area,
    'exhibition_hall': exhibition_hall,
    'service_desk': service_desk,
    'main_venue': main_venue,
    'room1': room1,
    'room2': room2,
    'room3': room3,
    'room4': room4,
    'room5': room5,
    'room6': room6,
    'toilet1': toilet1,
    'toilet2': toilet2,
    'toilet3': toilet3,
    'venue_a': venue_a,
    'venue_b': venue_b,
    'venue_c': venue_c,
    'venue_d': venue_d,
    'escalator_north': escalator_north,
    'escalator_south': escalator_south,
    'restaurant': restaurant,
    'lounge_area': lounge_area
}
lobby = {
    'around_check_in_desk': around_check_in_desk,
    'front_main_venue': front_main_venue,
    'around_poster_area': around_poster_area,
    'back_main_venue': back_main_venue
}

def core(path):
    """
    打开三天文件，转成np列表
    :param path:三天的日志
    :return:
    """
    df_y = pd.read_csv(path, encoding='utf-8', error_bad_lines=False,
                       usecols=[0, 1, 2])  # pd.dataframe
    log_data = np.array(df_y)  # np.ndarray()
    log_list = log_data.tolist()  # list
    # print(train_x_list[0][1])
    # print(type(train_x_list))
    return log_list


def write(save_path, save_content):
    with open(save_path, 'a', newline='') as f:
        df = pd.DataFrame(save_content)
        df.to_csv(f, index=False, sep=',', header=['id', 'sid', 'time'])


def s2t(second_time):
    """
    秒数转时间函数
    :param second_time: 25240
    :return: 07:00:40
    """
    m, s = divmod(second_time, 60)
    h, m = divmod(m, 60)
    return '%02d:%02d:%02d' % (h, m, s)


def split_time(n):
    """
    设置从07:00:00 18:10:00 20:01:31 20:10:00 72600
    :param n:几分钟统计一次,给整数
    :return:
    """
    time_slice = n * 60
    time_index = (72600 - 25200) // time_slice
    time_range = []
    for i in range(time_index + 1):
        moment = 25200 + i * time_slice
        time_range.append(moment)
    return time_range


def analysis_person(path, person_id):
    """
    分析某个人员行动轨迹
    :param person_id:
    :return:
    """
    save_path = '../res/test/' + str(person_id) + '.csv'
    go_list = []
    for i, sid in enumerate(core(path)):
        if sid[:][0] == person_id:
            print(sid[:][0], sid[:][1], sid[:][2])
    #         go_list.append(sid[:][:])
    # write(save_path, go_list)


def analysis_place(path, place, place_name):
    """
    分析各区域内部人员id，位置sid，时间time
    :param place:
    :param place_name:
    :return:
    """
    save_path = '../res/place/' + place_name + '.csv'
    sensor_list = []
    for i, sid in enumerate(core(path)):
        if sid[:][1] in place:
            sensor_list.append(sid[:][:])
    write(save_path, sensor_list)


def grid_realtime_num(path, n, sid):
    a_list = core(path)
    b_list = []
    for c in a_list:
        if sid == c[1]:
            b_list.append(c)
    print(b_list)
    sorted_b_list = sorted(b_list, key=lambda x: x[0])
    print(sorted_b_list)

    time_list = split_time(n)
    time_range = []
    id_list = []

    for front, back in zip(time_list[::1], time_list[1::1]):
        id_single = []
        for content in sorted_b_list:
            if front <= content[2] < back:
                time_range.append(str(s2t(front)) + '-' + str(s2t(back)))
                id_single.append(content[0])
                id_list.append(id_single)


    # print(len(time_range))
    # print(len(id_list))
    # print(time_range)
    # print(id_list)
    which_day = path.split('/')[3].split('.')[0]
    result = [time_range, id_list]
    result_dict = {which_day: result}
    print(result_dict)
    return result_dict
    pass


def area_realtime_num(day, n, k, v):
    # 两个函数传入待处理的数据，一个是时间按整数分割出的时间列表；第二个是区域进出列表（id:time）
    time_list = split_time(n)
    (in_list, out_list) = area_in_out_count(day, v, k)
    sorted_in_list = sorted(in_list, key=lambda x: x[1])    # 改为时间排序
    sorted_out_list = sorted(out_list, key=lambda x: x[1])

    # print(sorted_in_list)
    # for ii in sorted_in_list:
    #     print(ii[1])
    # time_list = [50000, 53000, 56000, 59000, 62000, 65000]
    # in_list = [[10020, 50526], [10019, 54981], [10019, 59851], [10062, 59491], [10091, 55701]]
    # out_list = [[10020, 53945], [10019, 58429], [10019, 63013], [10062, 62439], [10091, 57781]]
    # sorted_in_list = sorted(in_list, key=lambda x: x[1])  # 改为时间排序
    # sorted_out_list = sorted(out_list, key=lambda x: x[1])

    # 处理进出列表，将数据整理为{time_range：[id1, id2]，...}
    time_range = []
    id_list = []
    for content in sorted_in_list:
        # print(content)
        for front, back in zip(time_list[::1], time_list[1::1]):
            # print(front, back)
            if front <= content[1] < back:
                # print(content[1])
                time_range.append(str(s2t(front)) + '-' + str(s2t(back)))
                id_list.append(content[0])

    sorted_time_range = sorted(list(set(time_range)))

    in_dict = {}
    for t_point in sorted_time_range:
        per_range_person_list = []
        for a, b in zip(time_range, id_list):
            # print(a, b)
            if a == t_point:
                # print(a)
                per_range_person_list.append(b)
        # print(per_range_person_list)
        # test = {str(t_point): per_range_person_list}
        in_dict[t_point] = per_range_person_list
    # print(in_dict)
    # print(len(in_dict))

    # 还没想好出入处理如何放在一起 一个in_dict,out_dict
    time_range1 = []
    id_list1 = []
    for content in sorted_out_list:
        # print(content)
        for front, back in zip(time_list[::1], time_list[1::1]):
            # print(front, back)
            if front <= content[1] < back:
                # print(content[1], '在', front, back, '区间内，此时间区间列表加入content[0]')
                time_range1.append(str(s2t(front)) + '-' + str(s2t(back)))
                id_list1.append(content[0])

    sorted_time_range1 = sorted(list(set(time_range1)))
    # print(time_range1)
    # print(sorted_time_range1)
    out_dict = {}
    for t_point in sorted_time_range1:
        per_range_person_list1 = []
        for a, b in zip(time_range1, id_list1):
            # print(a, b)
            if a == t_point:
                # print(a)
                per_range_person_list1.append(b)
        # print(per_range_person_list)
        # test = {str(t_point): per_range_person_list}
        out_dict[t_point] = per_range_person_list1
    # print(out_dict)
    # print(len(out_dict))
    # 生成分割时间的字符串，用来遍历进出字典的keys
    ttt = []
    for front, back in zip(time_list[::1], time_list[1::1]):
        ttt.append(str(s2t(front)) + '-' + str(s2t(back)))

    # print(in_dict)
    # print(len(in_dict))
    # print(out_dict)
    # print(len(out_dict))
    # 将进出的字典中每个时间段记录的人员id替换成数目，出来的人加-号
    mount_in_dict = {}
    mount_out_dict = {}
    for ccc, ddd in zip(in_dict.keys(), in_dict.values()):
        mount_in_dict[ccc] = len(ddd)
    # print(mount_in_dict)
    # print(len(mount_in_dict))

    for ccc, ddd in zip(out_dict.keys(), out_dict.values()):
        mount_out_dict[ccc] = -len(ddd)
    # print(mount_out_dict)
    # print(len(mount_out_dict))
    # 将出入字典合并成计数字典
    mount_dict = {}
    for a in ttt:
        if a in mount_in_dict.keys() and a in mount_out_dict.keys():
            mount_dict[a] = mount_in_dict[a] + mount_out_dict[a]
        elif a in mount_in_dict.keys() and a not in mount_out_dict.keys():
            mount_dict[a] = mount_in_dict[a]
        elif a not in mount_in_dict.keys() and a in mount_out_dict.keys():
            mount_dict[a] = mount_out_dict[a]
    # print(len(mount_dict))
    # print(mount_dict)
    # print(sum(mount_dict.values()))

    # 叠加每个时间段的人数变量的到每个时间段的人数
    count_sum = []
    count_sum_time = []
    for t, c in zip(mount_dict.keys(), mount_dict.values()):
        count_sum.append(c)
        count_sum_time.append(t)
    count_sum_num = []
    for i, con in enumerate(count_sum):
        count_sum_num.append(sum(count_sum[:i + 1]))
    # print(len(count_sum_num))
    # print(count_sum_num)
    # print(count_sum_time)
    # result = {}
    # for a, b in zip(count_sum_time, count_sum_num):
    #     result[a] = b
    result = [count_sum_time, count_sum_num]
    # print(result)
    which_day = day.split('/')[3].split('.')[0]
    result_dict = {which_day: result}
    # print(result_dict)
    return result_dict


def area_in_out_count(path, place, place_name):
    """房间实时进出人员列表统计
    :param path:
    :param place:
    :param place_name:
    :return:
    """
    import itertools
    new_merged_list = list(itertools.chain(*place))
    all_list = core(path)       # 待分析三元组列表(whichday)
    clear_list = []
    for c in all_list:
        if c[1] in new_merged_list:
            clear_list.append(c)
    sort_clear_list = sorted(clear_list, key=lambda x: x[0])

    # clear_list = [[10001, 11121, 1], [10001, 11221, 2], [10001, 11121, 3],
    #               [10002, 11223, 4], [10002, 11123, 5], [10002, 11223, 6]]
    # sort_clear_list = sorted(clear_list, key=lambda x: x[0])
    # print(sort_clear_list)

    a_id = [id[0] for id in sort_clear_list]
    a_sid = [sid[1] for sid in sort_clear_list]
    a_time = [time[2] for time in sort_clear_list]
    ana_id_list = sorted(list(set(a_id)))
    # 数据筛选准备完成
    area_in_person_list = []
    area_out_person_list = []
    for con in ana_id_list:
        print('分析人员：', con)
        for i, conn in enumerate(a_id):
            if conn == con and i + 1 < len(a_sid):
                print(conn)
                print(a_sid[i], a_sid[i + 1])
                front = a_sid[i]
                f_id = a_id[i]
                f_time = a_time[i]
                back = a_sid[i + 1]
                b_time = a_time[i + 1]
                b_id = a_id[i + 1]

                if [back, front] in place:
                    print('进')
                    area_in_person_list.append([f_id, f_time])
                if [front, back] in place:
                    print('出')
                    area_out_person_list.append([b_id, b_time])
    print(area_in_person_list)
    print(len(area_in_person_list))
    print(area_out_person_list)
    print(len(area_out_person_list))
    return area_in_person_list, area_out_person_list


def analysis_person_stay():
    """
    判断每个人停留时间长度较长的点
    :return:
    """
    take_part_in_person_list = []
    read_path = '../res/person/'
    for i, f in enumerate(os.listdir(read_path)):
        handle_path = '../res/person/' + f
        print(i, handle_path)

        with open(handle_path, 'r') as file:
            data = pd.read_csv(file)
            for i in range(len(data)):
                if i + 1 < len(data):   # 错误处理，防止i+1超过迭代数目
                    if data['time'].iloc[i + 1] - \
                            data['time'].iloc[i] > 60:    # 两时间类型数据可以相减
                        for k, v in zip(place_all.keys(), place_all.values()):
                            if data['sid'].iloc[i] in v:    # 判断停留所在的地点, 停留时间
                                print(k, data['sid'].iloc[i], s2t(
                                    data['time'].iloc[i + 1] - data['time'].iloc[i]))

                                # 主会场分析
                                if k == 'main_venue':
                                    print(
                                        data['id'].iloc[i], '与会人员', data['sid'].iloc[i])
                                    if data['id'].iloc[i] not in take_part_in_person_list:
                                        take_part_in_person_list.append(
                                            data['id'].iloc[i])
    print(len(take_part_in_person_list))


def analysis_some_person_stay(person_id):
    """
    判断mou个人停留时间长度较长的点
    :return:
    """
    handle_path = '../res/test/' + str(person_id) + '.csv'
    print(handle_path)
    with open(handle_path, 'r') as file:
        data = pd.read_csv(file)
        for i in range(len(data)):
            if i + 1 < len(data):   # 错误处理，防止i+1超过迭代数目
                if data['time'].iloc[i + 1] - data['time'].iloc[i] > 20:
                    for k, v in zip(place_all.keys(), place_all.values()):
                        if data['sid'].iloc[i] in v:    # 判断停留所在的地点, 停留时间
                            print(k, data['sid'].iloc[i], s2t(
                                data['time'].iloc[i + 1] - data['time'].iloc[i]))


def get_all_id():
    all_emm = core(path1) + core(path2) + core(path3)
    all_id_list = [x[0] for x in all_emm]
    set_list = list(set(all_id_list))
    print(len(set_list))
    all_id = dict()
    all_id['id'] = set_list
    print(all_id)
    # # 写入json
    # with open("../res/results/all_id.json", 'a') as outfile:
    #     json.dump(all_id, outfile, ensure_ascii=False)
    #     outfile.write('\n')


if __name__ == "__main__":
    # grid_realtime_num(path1, n=1, sid=10119)
    # result_list = area_realtime_num(day=path2, n=1, k='restaurant', v=restaurant)
    # print(result_list)

    # all_results = {}
    # for k, v in zip(place_all.keys(), place_all.values()):
    #     print(k, v)
    #
    #     result_list_day1 = area_realtime_num(day=path1, n=1, k=k, v=v)
    #     result_list_day2 = area_realtime_num(day=path2, n=1, k=k, v=v)
    #     result_list_day3 = area_realtime_num(day=path3, n=1, k=k, v=v)
    #     result_list = {}
    #     result_list.update(result_list_day1)
    #     result_list.update(result_list_day2)
    #     result_list.update(result_list_day3)
    #     single_results = {k: result_list}
    #     all_results.update(single_results)
    #     print(all_results)
    #
    # # 写入json
    # with open("../res/results/place_real_time_person_num.json", 'a') as outfile:
    #     json.dump(all_results, outfile, ensure_ascii=False)
    #     outfile.write('\n')

    result_list_day = area_realtime_num(day=path1, n=1, k='around_check_in_desk', v=around_check_in_desk)
    print(result_list_day)
    # a_l = core(path1)
    # for c in a_l:
    #     if c[1] == 11201:
    #         print(c)