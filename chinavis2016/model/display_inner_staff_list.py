# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 15:38
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : display_inner_staff_list.py
# @Software: PyCharm

import pandas as pd
import re

# name1 = '../res/chinavis2016_data/a.bassi.csv'
# name1 = '../res/test.csv'
name1 = '../res/a.bassi.csv'

data = pd.read_csv(name1, encoding='gb18030')
# gbk gb18030   # ISO-8859-1编码会导致俄文符号错误显示
data.fillna(value='0', inplace=True)

# from的display  # , na=False给个缺失值标志
from_result = data.loc[data['From (address)'].str.contains('O=HACKINGTEAM' or '@hackingteam.it' or '@hackingteam.com', na=False)]
to_result = data.loc[data['To (address)'].str.contains('O=HACKINGTEAM' or '@hackingteam.it' or '@hackingteam.com', na=False)]
cc_result = data.loc[data['Cc (address)'].str.contains('O=HACKINGTEAM' or '@hackingteam.it' or '@hackingteam.com', na=False)]
bcc_result = data.loc[data['Bcc (address)'].str.contains('O=HACKINGTEAM' or '@hackingteam.it' or '@hackingteam.com', na=False)]

# 集合去重得到每个address对应的display
from_set = set(from_result['From (display)'])
to_set = set(to_result['To (display)'])
cc_set = set(cc_result['Cc (display)'])
bcc_set = set(bcc_result['Bcc (display)'])  # 缺失值给字符串
result_set = to_set.union(from_set).union(cc_set).union(bcc_set)
# 四个集合取并集得到全量display
# result_set = set(result_set)

# print(from_set)
# print(to_set)
# print(cc_set)
# print(bcc_set)
# print(len(result_set))
def getnamelist(set):
    namelist = []
    for name in set:
        # p1 = re.compile(r";")
        # lll = p1.findall(name)
        # print(lll)
        list_name = name.split(';')
        for item in list_name:
            namelist.append(item)
    #print(namelist)
    return namelist
resultlist = getnamelist(from_set) + getnamelist(to_set) + getnamelist(cc_set) + getnamelist(bcc_set)
# resultlist = getnamelist(from_set).extend(getnamelist(to_set)).extend(getnamelist(cc_set)).extend(getnamelist(bcc_set))
resultlist = set(resultlist)
#print(resultlist)
print(len(resultlist))
for name in resultlist:
    print(name)

# namelist 就是名单
# 写文件存起来
# f = open('../res/display_list', 'w', encoding='utf_8', errors='ignore')
# for name in result_set:
#     f.write(name+'\n')
# f.close()

# for name in result_set:
#     print(name)


# from_set = set(from_result['From (address)'])
# to_set = set(to_result['To (address)'])
# cc_set = set(cc_result['Cc (address)'])
# bcc_set = set(bcc_result['Bcc (address)'])  # 缺失值给字符串
# result_set = to_set.union(from_set).union(cc_set).union(bcc_set)
#
# print(len(result_set))
#
# for name in from_set:
#     print(name)