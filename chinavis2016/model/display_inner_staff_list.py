# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 15:38
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : display_inner_staff_list.py
# @Software: PyCharm

import pandas as pd

# name1 = '../res/chinavis2016_data/a.bassi.csv'
# name1 = '../res/a.bassi.csv'
name1 = '../res/a.bassi.csv'

data = pd.read_csv(name1, encoding='ISO-8859-1')
# print(data.columns)

# print(data['From (display)']) # display
# print(data['From (address)'])   # address
# print(data['To (display)'])   # display
# print(data['To (address)'])   # address
# print(data['Cc (display)'])   # d就第一行不是空
# print(data['Cc (address)'])   # 就第一行不是空
# print(data['Bcc (display)'])
# print(data['Bcc (address)'])
# print(data['Attachment Names'])
# 判断有缺失值的列 False的话就说明都赋值了
# print(data.isnull().any())
# NAN的处理：替换（改变文件）、删除（行或列）
# data.dropna() # 删除有缺失值的记录
# 缺失值给0，, inplace=True
# 不给零
#data.fillna(value=0, inplace=True)
# 这里给字符串0处理缺失值
data.fillna(value='0', inplace=True)
print(data.isnull().any())

# from的display  # , na=False给个缺失值标志

from_result = data.loc[data['From (address)'].str.contains('O=HACKINGTEAM' or '@hackingteam.it' or '@hackingteam.com', na=False)]
to_result = data.loc[data['To (address)'].str.contains('O=HACKINGTEAM' or '@hackingteam.it' or '@hackingteam.com', na=False)]
cc_result = data.loc[data['Cc (address)'].str.contains('O=HACKINGTEAM' or '@hackingteam.it' or '@hackingteam.com', na=False)]

bcc_result = data.loc[data['Bcc (address)'].str.contains('O=HACKINGTEAM' or '@hackingteam.it' or '@hackingteam.com', na=False)]
# 出错的原因是我们给缺失值赋值了0，然后在一堆0里面匹配字符串是错误的
# print(data.loc[data['To (address)'].str.contains('O=HACKINGTEAM', na=False)])

# 集合去重得到每个address对应的display

from_set = set(from_result['From (display)'])
to_set = set(to_result['To (display)'])
cc_set = set(cc_result['Cc (display)'])

# 个别出错
bcc_set = set(bcc_result['Bcc (display)'])

result_set = to_set.union(from_set).union(cc_set).union(bcc_set)
# 四个集合取并集得到全量display
print(len(from_set))
print(len(to_set))
print(len(cc_set))
print(len(result_set))

# print(from_result['From (address)'])
# print(from_result['From (address)'])


#print(result.loc[:]['From (display)'])
#print(result1.loc[:]['From (display)'])
#print(result2.loc[:]['From (display)'])

