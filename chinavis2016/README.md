# 1.数据准备
## 0源文件标准化

输入：2016年挑战赛61个name.csv文件

处理：format_file_data.py（修改源csv文件为utf8，小写化处理）

输出：convert_name.csv

## 1.0主题数据清洗：

输入：../res/chinavis2016_data/目录下所有convert_name.csv文件

处理：get_all_subject.py

read_all_sub_csv()读取 

manual_clear_subject() 去无用字符

is_number()判断是否为数字 

save_subject()保存 主题句子间保持一个换行

输出：../res/results/all_subject.txt（36.0MB）

## 1.1分词（只进行一次，运算需要半小时）

输入：../res/results/all_subject.txt（36.0MB）

处理：get_all_subject.py

clear()用 jieba分词

save_subject() 保存 词汇间保持一个空格

输出：all_subject_words.txt（29.3MB）


## 1.2 清理分词后数据再清理

输入：all_subject_words.txt（29.3MB）

处理：get_all_subject.py

save_subject()

manual_clear_subject()

输出：../res/results/all_subject_words_clear.txt（27.5MB）



# 2.0 所有主题清洗后根据人组成文章

输入：../res/results/display_list.txt

处理：display_per_subject_txt.py	每个人对应的主题文章

输出：../res/corpus_file/name_subject.txt

## 2.1 训练集与测试集分词

输入：../res/train_corpus/	分词前 每个员工的主题清洗后文件

处理：corpus2segment.py	(训练集分词处理)

输出：../res/train_corpus_seg/	目录下的分词清理后文件

## 2.2 bunch化操作，将数据塞入我们scikit的bunch化数据

输入：../res/train_corpus_seg/	目录下的分词清理后文件

处理：corpus2bunch.py		(Bunch化处理)

输出：Scikit-Learn库的bunch类型数据

Bunch和字典结构类似，也是由键值对组成，和字典区别：其键值可以被实例对象当作属性使用：

## 2.3  tf-idf词向量空间实例创建

输入：

../res/train_word_bag/train_set.dat

../res/train_word_bag/tfdifspace.dat

../res/test_word_bag/test_set.dat

../res/test_word_bag/testspace.dat

../res/train_word_bag/tfdifspace.dat

训练集测试的bunch数据

处理：tfidf_space.py

输出：

## 2.4 喂入分类器

这时候我们可以在此喂入各种分类器，计算召回率等

输入：

导入训练集bunch数据：trainpath = "../res/train_word_bag/tfdifspace.dat"

导入测试集bunch数据：testpath = "../res/test_word_bag/testspace.dat"

处理：NBayes_Predict.py  （多项式贝叶斯算法、随机森林算法）

输出：控制台~

name1_subject.txt : 实际类别: finacial  -->预测类别: finacial

name2_subject.txt : 实际类别: technology  -->预测类别: technology

name3_subject.txt : 实际类别: personel  -->预测类别: personel

name4_subject.txt : 实际类别: personel  -->预测类别: technology   (假装错误)

...

预测完毕!!!

精度:0.951

召回:0.959

f1-score:0.943

