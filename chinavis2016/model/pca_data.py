# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 15:37
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : pca_data.py
# @Software: PyCharm

import pandas as pd
import numpy as np
import jieba
import csv
import imageio
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from jieba.analyse import *
from sklearn.feature_extraction.text import CountVectorizer


file = '../res/convert_a.bassi.csv'
font_path = 'C:/Windows/Fonts/simkai.ttf'
back_coloring_path = "../res/bg.png"
img = "../res/select_result.png"
stopwords = '../res/stop_words_eng.txt'
path = '../res/convert_a.bassi.csv'
text_path = '../res/select_subject.txt'


def core():
    df = pd.read_csv(file, encoding='utf-8', error_bad_lines=False,
                     usecols=[0, 1, 2])
    df.fillna(value='0', inplace=True)
    # 用numpy将datafarame转换成list
    train_data = np.array(df)  # np.ndarray()
    train_x_list = train_data.tolist()  # list

    for i, subject in enumerate(train_x_list):
        # 选择内部邮箱
        mail_list = []
        subject_list = []
        f = open(text_path, 'a', encoding='utf_8')  # 保存的txt
        if 'o=hackingteam' in subject[:][:][2] or \
                '@hackingteam.it' in subject[:][:][2] or \
                '@hackingteam.com' in subject[:][:][2]:
            # print(subject[:][:][2])   # 地址
            # print(subject[0][:][:])  # 主题
            # print(subject[:][1][:])  # 邮箱
            mail = subject[:][1][:]
            mail_list.append(mail)

            string = subject[0][:][:]
            if ']: ' in string:
                string = string.split(']: ')[1]
            if 'r: ' in string:
                string = string.split('r: ')[1]
            if 're: ' in string:
                string = string.split('re: ')[1]
            if '] ' in string:
                string = string.split('] ')[1]
            # print(string)  # 主题
            subject_list.append(string)
            # text = subject_list
            # print(text)
        else:
            pass
        # 写入文件
        # for s in subject_list:
        #     print('正在写入', s)
        #     f.write(s + '\n')
        # f.close()

        print(mail_list)
        print(subject_list)


word_file = '../res/word_list.txt'


def clear(text_path, stopwords):
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
    # for row in words_list:
    #     print(row)
    print(''.join(words_list))  # 去停用次 词汇表
    # print(type(''.join(words_list)))  # str
    f = open(word_file, 'a', encoding='utf_8')  # 保存的txt
    f.write(''.join(words_list))
    f.close()
    return ''.join(words_list)


def subject_word_cloud():
    back_coloring = imageio.imread(back_coloring_path)
    # 设置词云属性
    wc = WordCloud(background_color="white",
                   font_path=font_path,
                   max_words=100,
                   mask=back_coloring,
                   max_font_size=80,
                   random_state=42,
                   width=1000, height=860, margin=2,
                   )
    text = open(text_path, encoding='utf_8', errors='ignore').read()
    text = clear(text, stopwords)

    wc.generate(text)
    image_colors = ImageColorGenerator(back_coloring)
    plt.figure()
    plt.imshow(wc.recolor(color_func=image_colors))
    plt.axis("off")
    plt.show()
    wc.to_file(img)


def select_subject():
    text = open(text_path, encoding='utf_8', errors='ignore').read()
    text = clear(text, stopwords)  # 送值，分词，去停用词，加载自定义词典
    for keyword, weight in extract_tags(text, withWeight=True):
        print('%s %s' % (keyword, weight))

pca_data_path = '../res/pca_data.txt'
def pca():
    f = open(pca_data_path, 'a', encoding='utf_8')  # 保存的txt
    # 加载数据集
    from sklearn import datasets
    digits = datasets.load_digits()
    digits = list(digits.values())
    for d in digits:
        for data in d:
            print(data)
            # f.write(data)
        # print(d)

        # print(digits)
    # print(type(digits))
    # print(digits['data'])
    # 五列： data target target_names images DESCR


    f.close()



    # x = digits.data
    # print(type(x))  # <class 'numpy.ndarray'>
    # print(x)
    # y = digits.target
    # print(y)
    # 调用pca
    # from sklearn import decomposition
    # pca = decomposition.PCA()
    # pca.fit(x)

    # 绘图
    # import matplotlib.pyplot as plt
    # plt.figure()
    # plt.plot(pca.explained_variance_, 'k', linewidth=2)
    # plt.xlabel('n_components', fontsize=16)
    # plt.ylabel('explained_variance_', fontsize=16)
    # plt.show()


if __name__ == "__main__":
    #　subject_word_cloud()
    # select_subject()
    # pca()
    # core()

    text = open(text_path, encoding='utf_8', errors='ignore').read()
    text = clear(text, stopwords)

