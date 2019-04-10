# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 10:10
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : corpus2segment.py
# @Software: PyCharm

import os
import jieba

stopwords = '../res/stop_words_eng.txt'


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


def save_subject(save, content):
    """
    保存数据
    :param save: 保存路径
    :param content: 保存某字符串
    :return:
    """
    f = open(save, 'a', encoding='utf_8')
    if content is None:
        pass
    else:
        f.write(content + ' ')
    f.close()


def clear(text_path, stopwords, save_path):    # , save_path
    words_list = []
    seg_list = jieba.cut(text_path, cut_all=False)
    str_list = '/'.join(seg_list)
    f_stop = open(stopwords, encoding='utf_8', errors='ignore')     # 停用词
    try:
        f_stop_text = f_stop.read()
    finally:
        f_stop.close()
    f_stop_seg_list = f_stop_text.split('\n')
    for word in str_list.split('/'):
        if not (word.strip() in f_stop_seg_list) and len(word.strip()) > 1:
            words_list.append(word)
    # 保存 位置
    for i, row in enumerate(words_list):
        print(i, row)
        save_subject(save_path, manual_clear_subject(row))

    return ''.join(words_list)


def corpus_segment(corpus_path, seg_path):
    catelist = os.listdir(corpus_path)  # 获取corpus_path下的所有子目录
    print("分词中...")

    # 获取每个目录（类别）下所有的文件
    for i, mydir in enumerate(catelist):
        class_path = corpus_path + mydir
        seg_dir = seg_path + mydir
        print('正在分词第', i+1, '个文件', class_path)

        # print(seg_dir)

        text = open(class_path, encoding='utf_8', errors='ignore').read()   # 读 corpus
        clear(text, stopwords, seg_dir)  # 传seg

    print("英文语料分词结束")


if __name__ == "__main__":
    # 对训练集进行分词
    # corpus_path = "../res/train_corpus/"  # 未分词分类语料库路径
    # seg_path = "../res/train_corpus_seg/"  # 分词后分类语料库路径
    # corpus_segment(corpus_path, seg_path)

    # 对测试集进行分词
    corpus_path = "../res/test_corpus/"  # 未分词分类语料库路径
    seg_path = "../res/test_corpus_seg/"  # 分词后分类语料库路径
    corpus_segment(corpus_path, seg_path)
