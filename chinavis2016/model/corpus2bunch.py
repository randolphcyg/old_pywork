# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 10:07
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : corpus2bunch.py
# @Software: PyCharm

import os
import re
import pickle

from sklearn.datasets.base import Bunch
from Tools import readfile

# top100 = '../res/results/test_top100.txt'
#
#
# def display_occur_to_array_single(filename):
#     """这里我们打开分词后的内部员工名字对应的txt文档、top100关键词，
#     尝试遍历第一个文件中，各top100关键词出现的次数
#     :return:
#     """
#     # for i, f in enumerate(os.listdir(path2)):
#     file = os.path.join('../res/test_corpus_seg/', filename)
#     print('正在处理文件', file, '：')
#     with open(top100, encoding='utf8', errors='ignore') as fw:
#         wordlist = fw.read().split('\n')  # top词汇表
#         aim_array = []
#         with open(file, encoding='utf8', errors='ignore') as fw2:
#             for content in fw2:
#                 for w in wordlist:
#                     count = len(re.findall(w, content))
#                     # print(w, '出现的次数是：', count)
#                     aim_array.append(count)
#         print(aim_array)
#         return aim_array


def corpus2bunch(wordbag_path, seg_path):
    catelist = os.listdir(seg_path)
    labellist = ['Financial', 'Human', 'Technology', 'Human', 'Human',
                'Financial', 'Technology', 'Technology', 'Technology', 'Technology',
                'Technology', 'Technology', 'Financial', 'Human', 'Technology',
                'Technology', 'Technology', 'Financial', 'Technology', 'Technology']
    print(len(catelist))    # 20
    # 创建一个Bunch实例
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    bunch.target_name.extend(catelist)
    print(bunch)
    # extend(addlist)是python list中的函数，意思是用新的list（addlist）去扩充原来的list

    for mydir, c in zip(catelist, labellist):
        # for c in labellist:
        print(mydir)
        fullname = seg_path + mydir

        #　bunch.label.append(mydir)
        bunch.label.append(c)
        bunch.filenames.append(fullname)
        # bunch.contents.append(display_occur_to_array_single(mydir))  # 读取文件内容
        bunch.contents.append(readfile(fullname))
        # 这里我们的学习内容输入量改成99维度的数组

    # 将bunch存储到wordbag_path路径中
    with open(wordbag_path, "wb") as file_obj:
        pickle.dump(bunch, file_obj)
    print("构建文本对象结束！！！")


if __name__ == "__main__":
    # 对训练集进行Bunch化操作：
    wordbag_path = "../res/train_word_bag/train_set.dat"  # Bunch存储路径
    seg_path = "../res/train_corpus_seg/"  # 分词后分类语料库路径
    corpus2bunch(wordbag_path, seg_path)

    # 对测试集进行Bunch化操作：
    wordbag_path = "../res/test_word_bag/test_set.dat"  # Bunch存储路径
    seg_path = "../res/test_corpus_seg/"  # 分词后分类语料库路径
    corpus2bunch(wordbag_path, seg_path)
