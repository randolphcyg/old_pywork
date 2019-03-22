# -*- coding: utf-8 -*-
# @Time    : 2019/3/22 15:07
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : format_file_data.py
# @Software: PyCharm

import os.path

path = '../res/chinavis2016_data'
source_encoding = 'ISO-8859-1'


def modify_utf8(
        source_file,
        target_file,
        source_encoding,
        target_encoding='UTF-8'):
    """
    读取文件编码统一utf-8
    所有数据小写化处理
    :param source_file:源文件
    :param target_file:目标文件
    :param source_encoding:读时解码
    :param target_encoding:写入编码
    :return:
    """
    with open(source_file, 'r', encoding=source_encoding) as fr:  # 打开源文件
        with open(target_file, 'w', encoding=target_encoding) as fw:    # 打开新文件
            for line in fr:
                fw.write(line[:-1].lower() + '\n')  # 小写化
    os.remove(source_file)


def convert():
    for i, source_file in enumerate(os.listdir(path)):
        print('正在处理第', i + 1, '个文件', source_file, '：')
        target_file = 'convert_' + source_file
        source_file = os.path.join(path, source_file)
        target_file = os.path.join(path, target_file)
        print(target_file)
        modify_utf8(source_file, target_file, source_encoding)


# 以下为个例测试

# source_file = '../res/a.bassi.csv'
# target_file = '../res/convert_a.bassi.csv'
#
#
# def modify_utf8(
#         source_file,
#         target_file,
#         source_encoding,
#         target_encoding='UTF-8'):
#     with open(source_file, 'r', encoding=source_encoding) as fr:  # 打开源文件
#         with open(target_file, 'w', encoding=target_encoding) as fw:    # 打开新文件
#             for line in fr:
#                 #print(line[:-1].lower())
#                 fw.write(line[:-1].lower() + '\n')
#     # os.remove(source_file)
#
#
# modify_utf8(source_file, target_file, source_encoding)


if __name__ == "__main__":
    convert()
