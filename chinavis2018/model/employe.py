# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 23:49
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : employe.py
# @Software: PyCharm

import os
import csv
import sys
import re
import pandas as pd
from jieba.analyse import *

def merge(path, csv_name, target_csv):
    # i = 0
    files = os.listdir(path)
    with open(target_csv, 'w+', newline='', encoding='UTF-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['time','proto','sip','sport','dip','dport','from','to','subject'])
        for f in files:  # f是倒数第二级文件夹eg:2017-11-01的列表
            # i = i + 1
            # print(f)
            if (os.path.isdir(path + '/' + f)):  # 判断是否是文件夹
                if (f[0] == '.'):  # 排除隐藏文件夹
                    pass
                else:  # 添加非隐藏文件
                    for filenames in os.listdir(path + '/' + f):  # filenames是3三级文件的一个列表
                        # print(filenames)
                        path_1 = os.path.join(path, f, filenames)  # 路径合成
                        if (filenames == csv_name):
                            with open(path_1, 'r+',encoding='gb18030',errors='ignore') as fr:
                                reader = csv.reader(fr, dialect='excel', delimiter=',')  # 读取文件到list中
                                try:
                                    for row in reader:
                                        #print(row)
                                        if 'sport' in row:
                                            pass
                                        else:
                                            if ';' in row[7]:  # 判断是否符合划分
                                                a = re.split(';', row[7])  # 拆分的值存储起来
                                                # print (a)
                                                for i in a:
                                                    row[7] = i
                                                    # print (row[7])
                                                    writer.writerow(
                                                        [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                                                         row[8]])
                                            else:
                                                writer.writerow(
                                                    [row[0], row[1], row[2], row[3], row[4], row[5], row[6], row[7],
                                                     row[8]])
                                    else:
                                        continue
                                except csv.Error as e:
                                    sys.exit('file {}, line {}: {}'.format(csv_name, reader.line_num, e))
def clean(target_csv, clean_csv):
    read_data = pd.read_csv(target_csv)  # 读取原始Email.csv
    # print(read_data)
    read_data = read_data[~ read_data['subject'].str.contains('邮件')]  # 删除某列包含特殊字符的行
    read_data = read_data[~ read_data['subject'].str.contains('崩溃')]
    read_data = read_data[~ read_data['subject'].str.contains('HOST')]
    read_data = read_data[~ read_data['subject'].str.contains('ALARM')]
    read_data = read_data[~ read_data['subject'].str.contains('RECOVER')]
    read_data = read_data[~ read_data['subject'].str.contains('报警')]
    read_data = read_data[~ read_data['subject'].str.contains('葡京')]
    read_data = read_data[~ read_data['subject'].str.contains('澳門')]
    read_data = read_data[~ read_data['subject'].str.contains('38')]
    read_data = read_data[~ read_data['subject'].str.contains('群號')]
    # print(read_data)
    read_data.to_csv(clean_csv, index=False)  # 将数据重新写入Email.csv
def subject_to_txt(clean_txt, clean_csv):
    f = open(clean_txt, 'a', encoding='utf_8')

    with open(clean_csv, encoding='utf_8', errors='ignore') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            # print(row['subject'])
            # 将写入文件中
            f.write(row['subject'])
            # 换行
            f.write("\n")
def word_analysis(clean_txt):
    # read_data = pd.read_csv(clean_csv_path)  # 读取清洗后的邮件数据
    with open(clean_txt, encoding='utf-8') as f:
        data = f.read()
    for keyword, weight in extract_tags(data, withWeight=True):
        print('%s %s' % (keyword, weight))
def subject_word_cloud(clean_txt):
    pass
if __name__ == "__main__":

    # email文件整合
    path = "../res/chinavis2018_data"
    source_csv = "email.csv"
    target_csv = "../res/Email.csv"
    print("step1: 合并邮件")
    merge(path, source_csv, target_csv)
    print("step1: 合并邮件完成")

    # 去除杂项
    clean_csv = "../res/Email.csv"
    print("step2: 清理垃圾记录")
    clean(target_csv, clean_csv)
    print("step2: 清理垃圾记录完成")

    # 清洁主题输出到txt
    clean_txt = "../res/Email.txt"
    print("step3: 主题转txt")
    subject_to_txt(clean_txt, clean_csv)
    print("step3: 主题转txt完成")

    # 词频分析
    print("step4.1: 主题词频统计")
    word_analysis(clean_txt)
    print("step4.1: 主题词频统计完成")
    #
    # # 词云
    # print("step4.2: 主题词云分析")
    # subject_word_cloud(clean_txt)
    # print("step4.2: 主题词云分析完成")