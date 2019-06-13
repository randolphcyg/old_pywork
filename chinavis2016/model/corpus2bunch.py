# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 10:07
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : corpus2bunch.py
# @Software: PyCharm

import os
import re
import pickle
import numpy as np

from sklearn.datasets.base import Bunch
from sklearn.preprocessing import StandardScaler
from Tools import readfile

top100 = '../res/results/raw_modify_top100.txt'
person_words2array_path = '../res/test_corpus_seg'


def display_occur_to_array_single(filename):
    """这里我们打开分词后的内部员工名字对应的txt文档、top100关键词，
    尝试遍历第一个文件中，各top100关键词出现的次数
    :return:
    """
    # print('正在处理文件', filename, '：')
    with open(top100, encoding='utf8', errors='ignore') as fw:
        wordlist = fw.read().split('\n')  # top词汇表
        aim_array = []
        with open(filename, encoding='utf8', errors='ignore') as fw2:
            for content in fw2:
                for w in wordlist:
                    count = len(re.findall(w, content))
                    # print(w, '出现的次数是：', count)
                    aim_array.append(count)
        # print(aim_array)
        return aim_array


def corpus2bunch(wordbag_path, seg_path):
    catelist = os.listdir(seg_path)
    labellist = ['Financial', 'Technology', 'Technology', 'Human', 'Technology',
                 'Technology', 'Technology', 'Technology', 'Technology', 'Technology',
                 'Technology', 'Technology', 'Financial', 'Human', 'Technology',
                 'Technology', 'Technology', 'Technology', 'Technology', 'Technology']
    print(len(catelist))    # 20
    # 创建一个Bunch实例
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    bunch.target_name.extend(catelist)
    print(bunch)
    # extend(addlist)是python list中的函数，意思是用新的list（addlist）去扩充原来的list

    for mydir, c in zip(catelist, labellist):
        print(mydir)
        fullname = seg_path + mydir

        bunch.label.append(c)
        bunch.filenames.append(fullname)
        bunch.contents.append(readfile(fullname))
        # 这里我们的学习内容输入量改成99维度的数组

    # 将bunch存储到wordbag_path路径中
    with open(wordbag_path, "wb") as file_obj:
        pickle.dump(bunch, file_obj)
    print("构建文本对象结束！！！")


def corpus2bunch0(wordbag_path, seg_path, labellist, name_list, all_array):
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    bunch.target_name.append(name_list)
    bunch.label.append(labellist)
    bunch.contents.append(all_array)


def train_bunch():
    train_labellist = ['Technology', 'Technology', 'Technology', 'Technology', 'Technology', 'Technology', 'Technology',
                       'Technology',
                       'Human', 'Human', 'Human', 'Human', 'Human', 'Human',
                       'Financial', 'Financial', 'Financial', 'Financial', 'Financial', 'Financial']

    train_name_list = ['alberto_ornaghi_subject.txt', 'alberto_pelliccione_subject.txt',
                       'alessandro_scarafile_subject.txt', 'bruno_muschitiello_subject.txt',
                       'cristian_vardaro_subject.txt', 'daniel_martinez_moreno_subject.txt',
                       'diego_giubertoni_subject.txt', 'emanuele_placidi_subject.txt',

                       'antonella_capaldo_subject.txt', 'daniele_milan_subject.txt',
                       'giancarlo_russo_subject.txt', 'marco_bettini_subject.txt',
                       'massimiliano_luppi_subject.txt', 'valeriano_bedeschi_subject.txt',
                       'alberto_pelliccione_subject.txt', 'lucia_rana_subject.txt',
                       'mauro_romeo_subject.txt', 'sergio_rodriguez-sol¨ªs_y_guerrero_subject.txt',
                       'simonetta_gallucci_subject.txt', 'walter_furlan_subject.txt']

    all_array = []
    for i, f in enumerate(train_name_list):
        print(i + 1, f)
        filename = os.path.join(person_words2array_path, f)
        single_array = display_occur_to_array_single(filename)
        print(single_array)
        all_array.append(single_array)
    print(all_array)  # 训练集二维数组

    # data = np.random.uniform(0, 100, 10)[:, np.newaxis]
    # print(data)
    # ss = StandardScaler()

    # std_all_array = ss.fit_transform(all_array)
    # print(std_all_array)
    # # 对训练集进行Bunch化操作：
    # wordbag_path = "../res/train_word_bag/train_set.dat"  # Bunch存储路径
    # seg_path = "../res/train_corpus_seg/"  # 分词后分类语料库路径
    # corpus2bunch0(wordbag_path, seg_path, train_labellist, train_name_list, all_array)


def test_bunch():
    train_labellist = []

    train_name_list = []
    for i, f in enumerate(os.listdir(person_words2array_path)):
        filename = os.path.join(person_words2array_path, f)
        # print(f)
        train_name_list.append(f)
        # print(filename)

    all_array = []
    for i, f in enumerate(train_name_list):
        print(i + 1, f)
        filename = os.path.join(person_words2array_path, f)
        single_array = display_occur_to_array_single(filename)
        # print(single_array)
        all_array.append(single_array)
    print(all_array)  # 训练集二维数组
    # # 对训练集进行Bunch化操作：
    # wordbag_path = "../res/train_word_bag/train_set.dat"  # Bunch存储路径
    # seg_path = "../res/train_corpus_seg/"  # 分词后分类语料库路径
    # corpus2bunch0(wordbag_path, seg_path, train_labellist, train_name_list, all_array)


if __name__ == "__main__":
    train_bunch()
    test_bunch()

    # 对训练集进行Bunch化操作：
    wordbag_path = "../res/train_word_bag/train_set.dat"  # Bunch存储路径
    seg_path = "../res/train_corpus_seg/"  # 分词后分类语料库路径
    corpus2bunch(wordbag_path, seg_path)

    # 对测试集进行Bunch化操作：
    wordbag_path = "../res/test_word_bag/test_set.dat"  # Bunch存储路径
    seg_path = "../res/test_corpus_seg/"  # 分词后分类语料库路径
    corpus2bunch(wordbag_path, seg_path)
