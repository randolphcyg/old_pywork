# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 14:29
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : check.py
# @Software: PyCharm

from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
import numpy as np
import multiprocessing
from sklearn.feature_extraction.text import CountVectorizer


# text_path = '../res/word_list.txt'
text_path = '../res/results/all_subject_words_clear.txt'


# 计算tf-idf

# 矢量对象<class 'sklearn.feature_extraction.text.CountVectorizer'>
v = CountVectorizer(min_df=1e-5)    # 去低频词
data = open(text_path, encoding='utf-8', errors='ignore').read()
# print(data)
corpus = []
corpus.append(data)
# print(type(corpus))
# print(corpus)
# print(type(data))
X = v.fit_transform(corpus)
print(type(X.toarray()))
print(X.toarray())
df = X.toarray()
# 用numpy将datafarame转换成list
# train_data = np.array(df)  # np.ndarray()
# train_x_list = train_data.tolist()  # list
# for line in train_x_list:
#     print(line)


transformer = TfidfTransformer()
words = v.get_feature_names()
tfidf = transformer.fit_transform(v.fit_transform(corpus))
print("how many words: {0}".format(len(words)))
print("tf-idf shape: ({0},{1})".format(tfidf.shape[0], tfidf.shape[1]))
