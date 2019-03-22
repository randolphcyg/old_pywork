# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 15:38
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : display_inner_staff_list.py
# @Software: PyCharm

import pandas as pd

# name1 = '../res/chinavis2016_data/a.bassi.csv'
# name1 = '../res/test.csv'
name1 = '../res/chinavis2016_data/a.capaldo.csv'

data = pd.read_csv(name1, encoding='ISO-8859-1')
# gbk gb18030   # ISO-8859-1编码会导致俄文符号错误显示
data.fillna(value='0', inplace=True)

# from的display  # , na=False给个缺失值标志
from_result = data.loc[data['From (address)'].str.contains(
    'O=HACKINGTEAM' or '@hackingteam.it' or '@hackingteam.com', na=False)]
to_result = data.loc[data['To (address)'].str.contains(
    'O=HACKINGTEAM' or '@hackingteam.it' or '@hackingteam.com', na=False)]
cc_result = data.loc[data['Cc (address)'].str.contains(
    'O=HACKINGTEAM' or '@hackingteam.it' or '@hackingteam.com', na=False)]
bcc_result = data.loc[data['Bcc (address)'].str.contains(
    'O=HACKINGTEAM' or '@hackingteam.it' or '@hackingteam.com', na=False)]

# 集合去重得到每个address对应的display
from_set = set(from_result['From (display)'])
to_set = set(to_result['To (display)'])
cc_set = set(cc_result['Cc (display)'])
bcc_set = set(bcc_result['Bcc (display)'])  # 缺失值给字符串


def getnamelist(set):
    namelist = []
    for name in set:
        list_name = name.split(';')
        for item in list_name:
            namelist.append(item)
    return namelist


resultlist0 = getnamelist(from_set) + getnamelist(to_set) + \
    getnamelist(cc_set) + getnamelist(bcc_set)
resultlist0 = set(resultlist0)
print(len(resultlist0))
# for name in resultlist0:
#     print(name)
resultlist = []
for name in resultlist0:
    name = name.replace('\'', '')
    resultlist.append(name)
    # print(name)
resultlist = set(resultlist)
print(len(resultlist))
# for name in resultlist:
#     print(name)
clear_resultlist = []
for name in resultlist:
    if '@hackingteam.it' in name:
        name = name.replace('@hackingteam.it', '')
        clear_resultlist.append(name)
    elif '@hackingteam.com' in name:
        name = name.replace('@hackingteam.com', '')
        clear_resultlist.append(name)
    elif ' hackingteam.it' in name:
        name = name.replace(' hackingteam.it', '')
        clear_resultlist.append(name)
    else:
        clear_resultlist.append(name)

clear_resultlist = set(clear_resultlist)
print(len(clear_resultlist))

for name in clear_resultlist:
    print(name)


f = open('../res/display_list', 'w', encoding='utf_8', errors='ignore')
for name in clear_resultlist:
    pass
f.close()
