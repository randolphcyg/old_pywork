# -*- coding: utf-8 -*-
# @Time    : 2019/4/8 10:07
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : corpus2bunch.py
# @Software: PyCharm

import os
import pickle

from sklearn.datasets.base import Bunch
from Tools import readfile


def corpus2bunch(wordbag_path, seg_path):
    catelist = os.listdir(seg_path)
    # 创建一个Bunch实例
    bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])
    bunch.target_name.extend(catelist)
    # print(bunch)
    # extend(addlist)是python list中的函数，意思是用新的list（addlist）去扩充原来的list

    for mydir in catelist:
        print(mydir)
        fullname = seg_path + mydir

        bunch.label.append(mydir)
        bunch.filenames.append(fullname)
        bunch.contents.append(readfile(fullname))  # 读取文件内容
        # append(element)是python list中的函数，意思是向原来的list中添加element，注意与extend()函数的区别

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
