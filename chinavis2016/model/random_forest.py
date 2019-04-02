# -*- coding: utf-8 -*-
# @Time    : 2019/3/27 14:29
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : check.py
# @Software: PyCharm

# https://www.jianshu.com/p/dc00a5d597ed

from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing
from sklearn.feature_extraction.text import TfidfTransformer
import pandas as pd
import numpy as np
import multiprocessing
from sklearn.feature_extraction.text import CountVectorizer


text_path = '../res/word_list.txt'


# 计算tf-idf

# 矢量对象<class 'sklearn.feature_extraction.text.CountVectorizer'>
v = CountVectorizer(min_df=1e-5)    # 去低频词
data = open(text_path, encoding='utf-8', errors='ignore').read()
print(data)
corpus = []
corpus.append(data)
print(type(corpus))
print(corpus)
print(type(data))
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


# 标签数字化，抽取数据


# encode label
# corpus_label = tarin_label + val_label + test_label
# encoder = preprocessing.LabelEncoder()
# corpus_encode_label = encoder.fit_transform(corpus_label)
# train_label = corpus_encode_label[:50000]
# val_label = corpus_encode_label[50000:55000]
# test_label = corpus_encode_label[55000:]
# get tf-idf dataset
# train_set = tfidf[:500]
# val_set = tfidf[500:1000]
# test_set = tfidf[1000:]


# 载入随机森林分类器


# rf_model = RandomForestClassifier(n_estimators=200, random_state=1080)
# rf_model.fit(train_set, train_label)
# print("val mean accuracy: {0}".format(rf_model.score(val_set, val_label)))
# y_pred = rf_model.predict(test_set)
# print(classification_report(test_label, y_pred))
