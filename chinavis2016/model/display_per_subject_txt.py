# -*- coding: utf-8 -*-
# @Time    : 2019/4/7 21:12
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : display_per_subject_txt.py
# @Software: PyCharm


import pandas as pd
import numpy as np
import os.path

path = '../res/chinavis2016_data'
save_path = '../res/corpus_file/'


def is_number(s):
    """
    判断是否为数字
    :param s:字符串
    :return:T OR F
    """
    try:
        float(s)
        return True
    except ValueError:
        pass
    try:
        import unicodedata
        unicodedata.numeric(s)
        return True
    except (TypeError, ValueError):
        pass
    return False


def manual_clear_subject(str):
    """
    传主题 反清洗过主题
    :param str:字符串
    :return:字符串
    """
    while 're: ' in str or 'r: ' in str or 'i:' in str:
        str = ' '.join(str.split(' ')[1:])
    if '[vtmis]' in str:
        str = ' '.join(str.split(' ')[1:])
    if '[!' in str:
        str = ' '.join(str.split(' ')[1:])
    # 忽略空回复、数字、空
    if str == 'r:' or is_number(str) or str.isspace():
        pass
    else:
        return str


def get_display_subject():
    for i, f in enumerate(os.listdir(path)):
        file = os.path.join('../res/chinavis2016_data/', f)
        print('正在处理第', i + 1, '个文件', file, '：')
        data = pd.read_csv(file, encoding='utf-8', error_bad_lines=False)
        data.fillna(value='0', inplace=True)    # 缺失值处理
        # 筛选发出邮箱
        from_result = data.loc[data['from (address)'].str.contains(
            'o=hackingteam' or '@hackingteam.it' or '@hackingteam.com', na=False)]

        from_display = set(from_result['from (display)'])
        # 文森特CEO发的邮件主题 清洗后都在这里了
        mmm = 0
        if 'simonetta gallucci' in from_display:
            # 用numpy将datafarame转换成list
            train_data = np.array(from_result['subject'])  # np.ndarray()
            train_x_list = train_data.tolist()  # list

            for line in train_x_list:
                # print(line)
                mmm += 1


if __name__ == "__main__":
    get_display_subject()