# -*- coding: utf-8 -*-
# @Time    : 2019/3/18 17:45
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : subject.py
# @Software: PyCharm

import pandas as pd
import csv
import jieba
import imageio
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

# subject_dict = ''
font_path = 'C:/Windows/Fonts/simkai.ttf'
back_coloring_path = "../res/bg.png"
img = "../res/result.png"
stopwords = '../res/stop_words_eng.txt'
path = '../res/a.bassi.csv'
text_path = '../res/subject.txt'

# def subject_to_txt(subject_txt, path):
#     f = open(subject_txt, 'w', encoding='utf_8')    # 保存的txt
#     with open(path, encoding='utf_8', errors='ignore') as csvfile:  # 处理的csv
#         reader = csv.DictReader(csvfile)    # 读成字典
#         for row in reader:
#             f.write(row['Subject'])
#             f.write("\n")
# subject_to_txt(subject_txt, path)

def clear(text_path, stopwords):
    # jieba.load_userdict(subject_dict)
    mywordlist = []
    seg_list = jieba.cut(text_path, cut_all=False)
    liststr = "/ ".join(seg_list)
    print(liststr)
    f_stop = open(stopwords, encoding='utf_8', errors='ignore')
    try:
        f_stop_text = f_stop.read()
    finally:
        f_stop.close()
    f_stop_seg_list = f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not (myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
            mywordlist.append(myword)
    # for row in mywordlist:
    #     print(row)
    return ''.join(mywordlist)

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

if __name__ == "__main__":
    subject_word_cloud()
