# -*- coding: utf-8 -*-
# @Time    : 2019/4/4 10:03
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : all_subject.py
# @Software: PyCharm

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import csv
import jieba
from jieba.analyse import *
import os.path
from collections import Counter

path = '../res/chinavis2016_data'
stopwords = '../res/stop_words_eng.txt'

all_subject_txt = '../res/results/all_subject.txt'
all_subject_txt_words = '../res/results/all_subject_words.txt'
all_subject_txt_words_clear = '../res/results/all_subject_words_clear.txt'

all_subject_txt_words_clear_100 = '../res/results/all_subject_words_clear_100.txt'


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
        #　f.write(content + '\n')     # 1.拿主题，手清理
        f.write(content + ' ')      # 2.主题分词，词汇空一格即可
    f.close()


def read_all_sub_csv(save_path):
    """a模式，拿到所有模板化csv主题，只可以运行一次
    :param save_path:保存路径
    :return:
    """
    for i, source_file in enumerate(os.listdir(path)):
        print('正在处理第', i + 1, '个文件', source_file, '：')
        source_path = os.path.join(path, source_file)
        f = open(save_path, 'a', encoding='utf_8')
        with open(source_path, encoding='utf_8', errors='ignore') as csvFile:
            reader = csv.DictReader(csvFile)
            for i, row in enumerate(reader):
                subject = row['subject']
                # 调用手动清理函数和文件写入函数
                content = manual_clear_subject(subject)
                save_subject(all_subject_txt, content)


def clear(text_path, stopwords):    # , save_path
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
    # 保存
    # for i, row in enumerate(words_list):
    #     print(i, row)
    #     save_subject(save_path, row)

    return ''.join(words_list)


txt = '../res/results/test.txt'
txt_result = '../res/results/test_result.txt'


def top_100_subject():
    with open(all_subject_txt_words_clear, 'r') as fr:  # 读入已经去除停用词的文件
        data = jieba.cut(fr.read())
    data = dict(Counter(data))

    with open(all_subject_txt_words_clear_100, 'a', encoding='utf_8') as fw:
        # print(sorted(data.values(), reverse=True))
        for i, (k, v) in enumerate(
                sorted(data.items(), key=lambda data: data[1], reverse=True)):
            if i < 100:
                fw.write('%d,%s,%d\n' % (i + 1, k, v))
            else:
                pass
        fw.close()


def tf_idf():
    # 计算tf-idf
    # 矢量对象<class 'sklearn.feature_extraction.text.CountVectorizer'>
    v = CountVectorizer(min_df=1)  # 去低频词
    data = open(
        all_subject_txt_words_clear,
        encoding='utf-8',
        errors='ignore').read()
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
    print("共多少词汇: {0}".format(len(words)))
    print("tf-idf shape: ({0},{1})".format(tfidf.shape[0], tfidf.shape[1]))

    print(tfidf)


if __name__ == "__main__":
    # 1.主题清洗保存 all_subject
    # read_all_sub_csv(all_subject_txt)

    # 2.主题分词 all_subject_words
    # text = open(all_subject_txt, encoding='utf_8', errors='ignore').read()
    # text = clear(text, stopwords, all_subject_txt_words)

    # 3.清洗分词后的文件再次去数字等
    # text = open(all_subject_txt_words, encoding='utf_8', errors='ignore').read()
    # word_list = text.split(' ')
    # print(word_list)
    # for i, word in enumerate(word_list):
    #     print(i, word)
    #     save_subject(all_subject_txt_words_clear, manual_clear_subject(word))

    # 4.提取数据中频数最大的 100 个主题
    # top_100_subject()

    # 5.
    # tf_idf()
    pass
