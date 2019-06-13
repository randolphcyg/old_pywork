# 0.通过chinavis2016挑战赛2熟悉机器学习流程
## 熟悉机器学习
机器学习分为输入、算法、输出

输入：*输入是训练和算法需要的数据集*:从源代码到统计数据，数据集可以包含任何东西。因为需要这些输入来训练机器学习算法，因此发现和生成高质量的数据集是当今机器学习面临的最大挑战之一。

算法：如何处理和分析数据

*算法能将数据转化为观点*

机器学习算法使用数据来执行特定任务。 最常见的算法类型有：

1.监督学习使用已经标注和结构化的训练数据。通过指定一组输入和所需的输出，机器将学习如何成功识别并将其映射。

2.无监督学习是使用非结构化数据来发现模式和结构的过程。监督学习可能使用excel表格作为其数据输入，而无监督学习可能用来理解书籍或博客。

输出:*输出是最终结果*:输出可能是识别红色符号的模式，可能是判断网页论调正面或负面的情感分析，或者是有置信区间的一个预测分数。

在机器学习中，输出可以是任何事物。产生输出的几种方法包括：

分类：为数据集中的每一项生成输出值

回归：通过已有数据来预测所考虑变量的最可能值

聚类：将数据分组成相似模式

>原文：https://blog.csdn.net/ejinxian/article/details/78411327 


# 1.数据准备
## 0源文件标准化

输入：2016年挑战赛61个name.csv文件

处理：format_file_data.py（修改源csv文件从ANSI为utf8、m.luppi.csv打开重保存、文件内文本小写化处理）

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

输出：矩阵向量

## 2.4 喂入分类器

输入：bunch数据，bunch = Bunch(target_name=[], label=[], filenames=[], contents=[])

处理：NBayes_Predict.py  （多项式贝叶斯算法、随机森林算法）

输出：为数据集中的每一项内部员工生成输出类别

问题是这个类别如何去定义？

这个label是选取2成人后手工给上标签和对应向量；

## 3.0 总结

还需衔接0.0
