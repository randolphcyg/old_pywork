# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 10:03
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : all_subject.py
# @Software: PyCharm

import csv
import jieba
from jieba.analyse import *
import os.path
from collections import Counter

path = '../res/chinavis2016_data'
all_subject_txt = '../res/all_subject.txt'
stopwords = '../res/stop_words_eng.txt'
all_subject_txt_words = '../res/all_subject_words.txt'
all_subject_txt_words2 = '../res/all_subject_words.txt'
all_subject_txt_words_100 = '../res/all_subject_words_100.txt'


def is_number(s):
    """
    判断是否为数字
    :param s:
    :return:
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
    :param str:
    :return:
    """
    while 're: ' in str or 'r: ' in str:
        str = ' '.join(str.split(' ')[1:])
    # print('第一步，去掉re：' + str)

    if '[vtmis]' in str:
        str = ' '.join(str.split(' ')[1:])
    #　print('第二步，去掉[vtmis]' + str)

    if '[!' in str or '[!' in str:
        str = ' '.join(str.split(' ')[1:])
    # print('第三步，去掉[*]:' + str)
    # print(str)
    if str == 'r:':
        pass
    if is_number(str):
        pass
    return str


def save_subject(save, content):
    """
    保存数据
    :param save: 保存路径
    :param content: 保存某字符串
    :return:
    """
    f = open(save, 'a', encoding='utf_8')
    f.write(content +' ')
    f.close()


def read_all_sub_csv(save_path):
    """a模式，拿到所有模板化csv主题，只可以运行一次
    :param save_path:保存路径
    :return:
    """
    for i, source_file in enumerate(os.listdir(path)):
        print('正在读取第', i + 1, '个文件', source_file, '：')
        source_path = os.path.join(path, source_file)
        f = open(save_path, 'a', encoding='utf_8')  # 保存的txt
        with open(source_path, encoding='utf_8', errors='ignore') as csvFile:  # 处理的csv
            reader = csv.DictReader(csvFile)  # 读成字典
            for i, row in enumerate(reader):
                subject = row['subject']
                # 调用手动清理函数和文件写入函数
                content = manual_clear_subject(subject)
                save_subject(all_subject_txt, content)


def clear(text_path, stopwords, save_path):
    # jieba.load_userdict(subject_dict)
    words_list = []
    seg_list = jieba.cut(text_path, cut_all=False)
    str_list = "/ ".join(seg_list)
    # print(str_list)
    f_stop = open(stopwords, encoding='utf_8', errors='ignore')
    try:
        f_stop_text = f_stop.read()
    finally:
        f_stop.close()
    f_stop_seg_list = f_stop_text.split('\n')
    for word in str_list.split('/'):
        if not (word.strip() in f_stop_seg_list) and len(word.strip()) > 1:
            words_list.append(word)

    for i, row in enumerate(words_list):
        print(i, row)
        save_subject(save_path, row)

    return ''.join(words_list)


def word_analysis():
    word_dict = {}
    words = open(all_subject_txt_words, encoding='utf_8', errors='ignore').read()
    # print(words)
    if words in word_dict:
        word_dict[words] += 1
    else:
        word_dict[words] = 1

    count = Counter(word_dict)
    for l in count.most_common()[:10]:
        # print(type(l))
        for con in l:
            print(count.most_common()[:10])
        # save_subject(all_subject_txt_words_100, l)
    # print(count.most_common()[:10])


if __name__ == "__main__":
    # 主题清洗保存 all_subject
    # read_all_sub_csv(all_subject_txt)
    # 主题分词 all_subject_words
    text = open(all_subject_txt, encoding='utf_8', errors='ignore').read()
    text = clear(text, stopwords, all_subject_txt_words)  # 送值，分词，去停用词，加载自定义词典
    # word_analysis()