# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 15:38
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : display_inner_staff_list.py
# @Software: PyCharm

import pandas as pd

# name1 = '../res/chinavis2016_data/a.bassi.csv'
name1 = '../res/a.bassi.csv'

data = pd.read_csv(name1, encoding='ISO-8859-1')
print(data.columns)

# data.fillna(0, inplace=True)

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
print(data.isnull().any())
data.dropna()
result = data.loc[data['Subject'].str.contains('error')]
print(result)

# NAN的处理：替换（改变文件）、删除（行或列）
