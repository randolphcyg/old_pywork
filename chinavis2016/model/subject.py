# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 17:45
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : subject.py
# @Software: PyCharm

import csv
import jieba
import imageio
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator
from jieba.analyse import *

# subject_dict = ''
font_path = 'C:/Windows/Fonts/simkai.ttf'
back_coloring_path = "../res/bg.png"
img = "../res/result.png"
stopwords = '../res/stop_words_eng.txt'
path = '../res/convert_a.bassi.csv'
text_path = '../res/test_corpus/david_vincenzetti_subject.txt'


def subject_to_txt(subject_txt, path):
    f = open(subject_txt, 'w', encoding='utf_8')    # 保存的txt
    with open(path, encoding='utf_8', errors='ignore') as csvFile:  # 处理的csv
        reader = csv.DictReader(csvFile)    # 读成字典
        for row in reader:
            f.write(row['subject'])
            f.write("\n")


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


def word_analysis():
    text = open(text_path, encoding='utf_8', errors='ignore').read()
    text = clear(text, stopwords)  # 送值，分词，去停用词，加载自定义词典
    for keyword, weight in extract_tags(text, withWeight=True):
        print('%s %s' % (keyword, weight))


if __name__ == "__main__":
    # subject_to_txt(text_path, path)
    # subject_word_cloud()
    word_analysis()
