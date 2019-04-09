# -*- coding: utf-8 -*-
# @Time    : 2019/3/28 16:25
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : test.py
# @Software: PyCharm

# 文本向量化，将文本转换为向量形式
# 两种方式TF词频方式、TF-IDF词频逆词频方式

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer

word_file = '../res/word_list.txt'

f_word_list = open(word_file, encoding='utf_8', errors='ignore').read()

word_list = f_word_list.split(' ')  # 单词分割进列表
clear_word_list = []
# 再次洗主题
for word in word_list:
    if word.isdigit() or word.split('.')[0].isdigit():
        pass
    else:
        clear_word_list.append(word)
print(clear_word_list)


def subject_to_txt(subject_txt, path):
    f = open(subject_txt, 'w', encoding='utf_8')    # 保存的txt
    with open(path, encoding='utf_8', errors='ignore') as csvFile:  # 处理的csv
        reader = csv.DictReader(csvFile)    # 读成字典
        for row in reader:
            f.write(row['subject'])
            f.write("\n")


# 主题向量化
vectorizer = CountVectorizer()  # min_df=0.005
count = vectorizer.fit_transform(clear_word_list)   # 将文本中的词语转换为词频矩阵
print(vectorizer.get_feature_names())
print(vectorizer.vocabulary_)
print(count.toarray())

transformer = TfidfTransformer()
tfidf_matrix = transformer.fit_transform(count)
print(tfidf_matrix.toarray())


# 稀疏矩阵
# clear_word_list = [
#     'sample',
#     'hackers',
#     'china',
#     'suspected',
#     'breach',
#     'multibrowser',
#     ]


# CountVectorizer是通过fit_transform函数将文本中的词语转换为词频矩阵
## get_feature_names()可看到所有文本的关键字
## vocabulary_可看到所有文本的关键字和其位置
## toarray()可看到词频矩阵的结果

# TfidfTransformer是统计CountVectorizer中每个词语的tf-idf权值

# TfidfVectorizer可以把CountVectorizer, TfidfTransformer合并起来，直接生成tfidf值
## 参数：max_df（描述单词在文档中的最高出现率） min_df（单词至少在20%文档中出现）
## ngram_range(观察一元模型)