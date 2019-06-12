# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 15:38
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : display_inner_staff_list.py
# @Software: PyCharm

import pandas as pd
import os.path

path = '../res/chinavis2016_data'
save_file = '../res/results/display_list.txt'

# 分离分号组成的名字元素
# def getnamelist(source_set):
#     namelist = []
#     for name in source_set:
#         list_name = name.split(';')
#         for item in list_name:
#             namelist.append(item)
#     return namelist


def core():
    open_save_file = open(save_file, 'w', encoding='utf_8', errors='ignore')
    employees = []
    for i, f in enumerate(os.listdir(path)):
        file = os.path.join('../res/chinavis2016_data/', f)
        print('正在处理第', i + 1, '个文件', file, '：')
        data = pd.read_csv(file, encoding='utf-8', error_bad_lines=False)
        data.fillna(value='0', inplace=True)    # 缺失值处理
        # 筛选发出邮箱
        from_result = data.loc[data['from (address)'].str.contains(
            'o=hackingteam' or '@hackingteam.it' or '@hackingteam.com', na=False)]

        from_display = set(from_result['from (display)'])

        # fromlist = getnamelist(from_display)  # 这个函数处理貌似用不上了
        fromlist = set(from_display)

        print(len(fromlist))
        # print(fromlist)
        # 所有文件的名字都放到namelist，并去重
        namelist = []
        for name in fromlist:
            name = name.replace('\'', '')
            namelist.append(name)
        namelist = set(namelist)
        print(len(namelist))
        # 做简单清理操作 去掉含有.com hackingteam support的名字
        # 别忘记做重要度检验，别把重要任务给直接过滤掉了
        clear_namelist = []
        for name in namelist:
            # clear_namelist.append(name)
            if 'hackingteam' in name:
                name = name.split(' ')[0]
                for basic_name in namelist:
                    if name in basic_name:
                        pass
            elif name.isalpha():
                pass
            elif '.com' in name:
                pass
            elif 'support' in name:
                pass
            else:
                clear_namelist.append(name)

        clear_namelist = set(clear_namelist)
        print(len(clear_namelist))

        # for name in clear_namelist:
        #     print(name)

        for name in clear_namelist:
            if name in employees:
                pass
            # 临时检验有问题的display来自哪个文件
            # elif name == "fdalessio capitolmp.com":
            #     print('>>>>>>>>>>>>>>>>>>>', file, '<<<<<<<<<<<<<<<<<<')
            else:
                employees.append(name)
        print(len(employees))
        print(employees)

    for employee in employees:
        open_save_file.write(employee + '\n')
    open_save_file.close()


if __name__ == "__main__":
    core()
