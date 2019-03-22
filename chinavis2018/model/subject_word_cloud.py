# -*- coding: utf-8 -*-
# @Time    : 2019/3/15 23:52
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : subject_word_cloud.py
# @Software: PyCharm

import jieba
import imageio
import matplotlib.pyplot as plt
from wordcloud import WordCloud, ImageColorGenerator

# 公共路径
back_coloring_path = "../res/bg.png"  # 设置背景图片路径
font_path = 'C:/Windows/Fonts/simkai.ttf'  # 为matplotlib设置中文字体路径
img = "../res/result.png"  # 保存图片(颜色按背景图颜色布局生成)
stopwords = '../res/stopwords.txt'  # 停用词词表
subject_dict = '../res/subject_dict.txt'  # 自定义词典
text_path = '../res/Email.txt'  # 待分析文本路径


def class_clear_custom(path, subject_dict, stopwords):
    """
    分词&去停用词&加载自定义词典
    :param path: 待分析文本打开
    :param subject_dict: 自定义词典设置主词典
    :param stopwords: 停用词词典
    :return:
    """
    jieba.load_userdict(subject_dict)
    mywordlist = []
    seg_list = jieba.cut(path, cut_all=False)
    liststr = "/ ".join(seg_list)
    f_stop = open(stopwords, encoding='utf_8', errors='ignore')
    try:
        f_stop_text = f_stop.read()
    finally:
        f_stop.close()
    f_stop_seg_list = f_stop_text.split('\n')
    for myword in liststr.split('/'):
        if not(myword.strip() in f_stop_seg_list) and len(myword.strip()) > 1:
            mywordlist.append(myword)
    # for row in mywordlist:
    #     print(row)
    return ''.join(mywordlist)


def subject_word_cloud():
    """
    调分词函数，二次处理主题，生成词云
    :return:
    """
    back_coloring = imageio.imread(back_coloring_path)  # 设置背景图片（图转数组）
    # 设置词云属性
    wc = WordCloud(background_color="white",    # 背景
                   font_path=font_path,   # 字体
                   max_words=100,    # 最大词数
                   mask=back_coloring,  # 背景图
                   max_font_size=80,  # 字体最大值
                   random_state=42,
                   width=1000, height=860, margin=2,  # 设置图片默认的大小,
                   # 但是如果使用背景图片的话,那么保存的图片大小将会按照其大小保存,margin为词语边缘距离
                   )
    text = open(text_path, encoding='utf_8', errors='ignore').read()
    text = class_clear_custom(
        text,
        subject_dict,
        stopwords)  # 送值，分词，去停用词，加载自定义词典

    wc.generate(text)   # 生成词云 用generate输入全部文本
    image_colors = ImageColorGenerator(back_coloring)   # 从背景图片生成颜色值
    plt.figure()
    plt.imshow(wc.recolor(color_func=image_colors))  # 显示图片
    plt.axis("off")
    plt.show()  # 绘制词云
    wc.to_file(img)    # 保存图片


if __name__ == "__main__":
    subject_word_cloud()
