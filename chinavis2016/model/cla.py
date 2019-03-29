# -*- coding: utf-8 -*-
# @Time    : 2019/3/29 16:00
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : cla.py
# @Software: PyCharm
# https://blog.csdn.net/sinat_38682860/article/details/80421697


# 导入数据集预处理、特征工程和模型训练所需的库
from sklearn import model_selection, preprocessing, linear_model, naive_bayes, metrics, svm
from sklearn.feature_extraction.text import TfidfVectorizer, CountVectorizer
# from sklearn import decomposition, ensemble
#
# import xgboost, textblob, string
from keras.preprocessing import text, sequence
# from keras import layers, models, optimizers
import pandas
import numpy


# 加载数据集
data = open('../res/corpus').read()
labels, texts = [], []
for i, line in enumerate(data.split("\n")):
    content = line.split()
    labels.append(content[0])
    texts.append(content[1])
# print(texts)
# 创建一个dataframe，列名为text和label
trainDF = pandas.DataFrame()
trainDF['text'] = texts
trainDF['label'] = labels

# 将数据集分为训练集和验证集
train_x, valid_x, train_y, valid_y = model_selection.train_test_split(
    trainDF['text'], trainDF['label'])

# label编码为目标变量
encoder = preprocessing.LabelEncoder()
train_y = encoder.fit_transform(train_y)
valid_y = encoder.fit_transform(valid_y)

# 创建一个向量计数器对象
count_vect = CountVectorizer(analyzer='word', token_pattern=r'\w{1,}')
count_vect.fit(trainDF['text'])

# 使用向量计数器对象转换训练集和验证集
xtrain_count = count_vect.transform(train_x)
xvalid_count = count_vect.transform(valid_x)

# 词语级tf-idf
tfidf_vect = TfidfVectorizer(
    analyzer='word',
    token_pattern=r'\w{1,}',
    max_features=5000)
tfidf_vect.fit(trainDF['text'])
xtrain_tfidf = tfidf_vect.transform(train_x)
xvalid_tfidf = tfidf_vect.transform(valid_x)

# ngram 级tf-idf
tfidf_vect_ngram = TfidfVectorizer(
    analyzer='word',
    token_pattern=r'\w{1,}',
    ngram_range=(
        2,
        3),
    max_features=5000)
tfidf_vect_ngram.fit(trainDF['text'])
xtrain_tfidf_ngram = tfidf_vect_ngram.transform(train_x)
xvalid_tfidf_ngram = tfidf_vect_ngram.transform(valid_x)

# 词性级tf-idf
tfidf_vect_ngram_chars = TfidfVectorizer(
    analyzer='char', token_pattern=r'\w{1,}', ngram_range=(
        2, 3), max_features=5000)
tfidf_vect_ngram_chars.fit(trainDF['text'])
xtrain_tfidf_ngram_chars = tfidf_vect_ngram_chars.transform(train_x)
xvalid_tfidf_ngram_chars = tfidf_vect_ngram_chars.transform(valid_x)

# 加载预先训练好的词嵌入向量
embeddings_index = {}
for i, line in enumerate(open('data/wiki-news-300d-1M.vec')):
    values = line.split()
embeddings_index[values[0]] = numpy.asarray(values[1:], dtype='float32')

# 创建一个分词器
token = text.Tokenizer()
token.fit_on_texts(trainDF['text'])
word_index = token.word_index

# 将文本转换为分词序列，并填充它们保证得到相同长度的向量
train_seq_x = sequence.pad_sequences(
    token.texts_to_sequences(train_x), maxlen=70)
valid_seq_x = sequence.pad_sequences(
    token.texts_to_sequences(valid_x), maxlen=70)

# 创建分词嵌入映射
embedding_matrix = numpy.zeros((len(word_index) + 1, 300))
for word, i in word_index.items():
    embedding_vector = embeddings_index.get(word)
if embedding_vector is not None:
    embedding_matrix[i] = embedding_vector
