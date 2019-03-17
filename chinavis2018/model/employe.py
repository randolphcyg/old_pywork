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
import jieba
import imageio
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

# 公共路径
back_coloring_path = "../res/bg.png"  # 设置背景图片路径
font_path = 'C:/Windows/Fonts/simkai.ttf'  # 为matplotlib设置中文字体路径
img = "../res/result.png"  # 保存图片(颜色按背景图颜色布局生成)
stopwords = '../res/stopwords.txt'  # 停用词词表
subject_dict = '../res/subject_dict.txt'  # 自定义词典
text_path = '../res/Email.txt'  # 待分析文本路径

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
    f = open(clean_txt, 'w', encoding='utf_8')

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
def class_clear_custom(path, subject_dict, stopwords):
    '''
    分词&去停用词&加载自定义词典
    :param path: 待分析文本打开
    :param subject_dict: 自定义词典设置主词典
    :param stopwords: 停用词词典
    :return:
    '''
    jieba.load_userdict(subject_dict)
    mywordlist = []
    seg_list = jieba.cut(path, cut_all=False)
    liststr="/ ".join(seg_list)
    f_stop = open(stopwords, encoding='utf_8', errors='ignore')
    try:
        f_stop_text = f_stop.read( )
    finally:
        f_stop.close( )
    f_stop_seg_list=f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip())>1:
            mywordlist.append(myword)
    # for row in mywordlist:
    #     print(row)
    return ''.join(mywordlist)

def subject_word_cloud():
    '''
    调分词函数，二次处理主题，生成词云
    :param back_coloring_path:
    :param font_path:
    :param path:
    :param subject_dict:
    :param stopwords:
    :param img:
    :return:
    '''
    back_coloring = imageio.imread(back_coloring_path)# 设置背景图片（图转数组）
    # 设置词云属性
    wc = WordCloud(background_color="white",    # 背景
                   font_path=font_path,   # 字体
                   max_words=100,    # 最大词数
                   mask=back_coloring,  # 背景图
                   max_font_size=80,  # 字体最大值
                   random_state=42,
                   width=1000, height=860, margin=2,  # 设置图片默认的大小,
                   # 但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
    )
    text = open(text_path, encoding='utf_8', errors='ignore').read()
    text = class_clear_custom(text, subject_dict, stopwords) # 送值，分词，去停用词，加载自定义词典

    wc.generate(text)   # 生成词云 用generate输入全部文本
    image_colors = ImageColorGenerator(back_coloring)   # 从背景图片生成颜色值
    plt.figure()
    plt.imshow(wc.recolor(color_func=image_colors))  # 显示图片
    plt.axis("off")
    plt.show()  # 绘制词云
    wc.to_file(img)    # 保存图片

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

    # 词云
    print("step4.2: 主题词云分析")
    subject_word_cloud()
    print("step4.2: 主题词云分析完成")