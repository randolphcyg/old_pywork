# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 15:38
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : display_inner_staff_list.py
# @Software: PyCharm

import pandas as pd
import os.path

path = '../res/chinavis2016_data'
save_file = '../res/display_list.txt'


def getnamelist(source_set):
    namelist = []
    for name in source_set:
        list_name = name.split(';')
        for item in list_name:
            namelist.append(item)
    return namelist


def core():
    open_save_file = open(save_file, 'w', encoding='utf_8', errors='ignore')
    employees = []
    for i, f in enumerate(os.listdir(path)):
        file = os.path.join('../res/chinavis2016_data/', f)
        print('正在处理第', i + 1, '个文件', file, '：')
        data = pd.read_csv(file, encoding='utf-8', error_bad_lines=False)
        data.fillna(value='0', inplace=True)

        from_result = data.loc[data['from (address)'].str.contains(
            'o=hackingteam' or '@hackingteam.it' or '@hackingteam.com', na=False)]
        from_set = set(from_result['from (display)'])

        fromlist = getnamelist(from_set)
        fromlist = set(fromlist)
        print(len(fromlist))

        namelist = []
        for name in fromlist:
            name = name.replace('\'', '')
            namelist.append(name)
        namelist = set(namelist)
        print(len(namelist))

        clear_namelist = []
        for name in namelist:
            if '@hackingteam.it' in name:
                name = name.replace('@hackingteam.it', '')
                clear_namelist.append(name)
            elif '@hackingteam.com' in name:
                name = name.replace('@hackingteam.com', '')
                clear_namelist.append(name)
            elif ' hackingteam.it' in name:
                name = name.replace(' hackingteam.it', '')
                clear_namelist.append(name)
            else:
                clear_namelist.append(name)

        clear_namelist = set(clear_namelist)
        print(len(clear_namelist))

        # for name in clear_namelist:
        #     print(name)

        for name in clear_namelist:
            if name in employees:
                pass
            # elif name == "mauro.romeo hackingteam":
            #     print('>>>>>>>>>>>>>>>>>>>', file, '<<<<<<<<<<<<<<<<<<')
            else:
                employees.append(name)
        print(len(employees))

    # if '.com' in name:
    #     name = name.split(' ')[0]
    #     employees.append(name)
    # elif 'hackingteam' in name:
    #     name = name.split(' ')[0]
    #     employees.append(name)
    # else:
    #     name = ' '.join(name.split('.'))
    #     employees.append(name)

    ## 修正列表

    # for employee in employees:
    #     if '.com' in employees:
    #             employee = employee.split(' ')[0]
    #             open_save_file.write(employee + '\n')
    #     elif 'hackingteam' in employees:
    #         employee = employee.split(' ')[0]
    #         open_save_file.write(employee + '\n')
    #
    #     ' '.join(employee.split('.'))
    #     open_save_file.write(employee + '\n')

    for employee in employees:
        open_save_file.write(employee + '\n')
    open_save_file.close()
if __name__ == "__main__":
    core()
