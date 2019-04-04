# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 10:03
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : all_subject.py
# @Software: PyCharm

import csv
import jieba
import os.path

path = '../res/chinavis2016_data'
all_subject_txt = '../res/all_subject.txt'
# all_subject_txt = 'all_subject.txt'
stopwords = '../res/stop_words_eng.txt'
save_path = 'all_subject_words.txt'

def manual_clear_subject(str):

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
    return str


def save_subject(content):
    f = open(all_subject_txt, 'a', encoding='utf_8')
    f.write(content)
    f.write('\n')
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
                save_subject(content)


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
    # f = open(save_path, 'w', encoding='utf_8')  # 保存的txt
    for i, row in enumerate(words_list):
        print(i, row)
    return ''.join(words_list)


if __name__ == "__main__":
    read_all_sub_csv(all_subject_txt)
    # text = open(all_subject_txt, encoding='utf_8', errors='ignore').read()
    # text = clear(text, stopwords, save_path)  # 送值，分词，去停用词，加载自定义词典
