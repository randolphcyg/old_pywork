# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 15:38
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : display_inner_staff_list.py
# @Software: PyCharm

import pandas as pd

name1 = '../res/chinavis2016_data/a.bassi.csv'

data = pd.read_csv(name1, encoding='ISO-8859-1')
print(data['Subject'])

print(data['From (address)'])

result = data.loc[data['From (address)'].str.contains('O=HACKINGTEAM')]

print(result)

# NAN的处理

# 缺失值形成的原因：能否解决去读出来？？？
# 读取不出来的话，会对计算结果产生影响么