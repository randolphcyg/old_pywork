# -*- coding: utf-8 -*-
# @Time    : 2019/4/2 18:27
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : 1.py
# @Software: PyCharm

import multiprocessing


tmp_catalog = 'C:/Users/randolph/Desktop/cnews/'
file_list = [tmp_catalog+'cnews.train.txt', tmp_catalog+'cnews.test.txt']
write_list = [tmp_catalog+'train_token.txt', tmp_catalog+'test_token.txt']

# def tokenFile(file_path, write_path):
#     word_divider = WordCut()
#     with open(write_path, 'w') as w:
#         with open(file_path, 'r') as f:
#             for line in f.readlines():
#                 line = line.decode('utf-8').strip()
#                 token_sen = word_divider.seg_sentence(line.split('\t')[1])
#                 w.write(line.split('\t')[0].encode('utf-8') + '\t' + token_sen.encode('utf-8') + '\n')
#     print(file_path + ' has been token and token_file_name is ' + write_path)
#
# pool = multiprocessing.Pool(processes=4)
# for file_path, write_path in zip(file_list, write_list):
#     pool.apply_async(tokenFile, (file_path, write_path, ))
# pool.close()
# pool.join() # 调用join()之前必须先调用close()
# print("Sub-process(es) done.")


def constructDataset(path):
    """
    path: file path
    rtype: lable_list and corpus_list
    """
    label_list = []
    corpus_list = []
    with open(path, 'r',encoding='utf8',errors='ignore') as p:
        for line in p.readlines():
            label_list.append(line.split('\t')[0])
            corpus_list.append(line.split('\t')[1])
    return label_list, corpus_list


tmp_catalog = 'C:/Users/randolph/Desktop/cnews/'
file_path = 'cnews.val.txt'
val_label, val_set = constructDataset(tmp_catalog + file_path)
print(len(val_set))

from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer

tmp_catalog = 'C:/Users/randolph/Desktop/cnews/'
write_list = [tmp_catalog + 'cnews.train.txt', tmp_catalog + 'cnews.test.txt']

tarin_label, train_set = constructDataset(write_list[0])  # 50000
test_label, test_set = constructDataset(write_list[1])  # 10000
# 计算tf-idf
corpus_set = train_set + val_set + test_set  # 全量计算tf-idf
print("length of corpus is: " + str(len(corpus_set)))
vectorizer = CountVectorizer(min_df=1e-5)  # drop df < 1e-5,去低频词
transformer = TfidfTransformer()
tfidf = transformer.fit_transform(vectorizer.fit_transform(corpus_set))
words = vectorizer.get_feature_names()
print("how many words: {0}".format(len(words)))
print("tf-idf shape: ({0},{1})".format(tfidf.shape[0], tfidf.shape[1]))


from sklearn import preprocessing

# encode label
corpus_label = tarin_label + val_label + test_label
encoder = preprocessing.LabelEncoder()
corpus_encode_label = encoder.fit_transform(corpus_label)
train_label = corpus_encode_label[:50000]
val_label = corpus_encode_label[50000:55000]
test_label = corpus_encode_label[55000:]
# get tf-idf dataset
train_set = tfidf[:50000]
val_set = tfidf[50000:55000]
test_set = tfidf[55000:]


from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report
# from sklearn.metrics import confusion_matrix

# LogisticRegression classiy model
lr_model = LogisticRegression()
lr_model.fit(train_set, train_label)
print("val mean accuracy: {0}".format(lr_model.score(val_set, val_label)))
y_pred = lr_model.predict(test_set)
print(classification_report(test_label, y_pred))
