# -*- coding: utf-8 -*-
# @Time    : 2019/3/11 14:29
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : worker_list.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import os.path

path = "../res/chinavis2016_data"

# 遍历所有文件找出所有创建者姓名
worker = []
i = 0
for file in os.listdir(path):
    i += 1
    print(i,file)
    data = pd.read_csv(os.path.join(path,file),
                       usecols= ['Creator Name'], encoding='ISO-8859-1')
    worker.append(data['Creator Name'][0])
    print(data['Creator Name'][0])
print(worker)

# 打开文件，用来存创建者名单
f = open('../res/creater_name_list', 'w', encoding='utf_8', errors='ignore')
for name in worker:
    f.write(name+'\n')
f.close()


