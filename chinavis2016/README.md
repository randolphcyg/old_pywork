# 0.几个问题
## 为什么机器学习？
机器学习需要我们提供数据让计算机学会分辨；

这里我们输入的内容主要是文本，这是最初的数据，刚开始会疑问，文本数据怎么做机器学习？ 

实际上初始数据都需要数字化，也就是转为矩阵，这个过程是数据准备，会针对数据类型和内容的不同有各种转换的方法，卡方、tf-idf等比较常用；

往内讲，文本数据又包括英文，中文，因此这里我们会遇到一些分词工具jieba等，jieba对比其他的比较好用；

再往外讲，除了文本数据，图像、声音、视频、纯数字...只要有区别的东西都可以通过转换做机器学习。就此思考2019年的纯数字，比较好用

2019从最初开始思考，我们告诉计算机的是这个ID经常在会场里呆着，那么这个ID类似行为的人都聚类为同一类：学者、演讲的、听演讲的。这里涉及到的一个ID和一个

主要的SID也就是位置传感器传过来的位置参数。

也可以有其他的思考，同样可以去做聚类，让计算机通过输入这个人 的ID，经常待的SID和时间去让计算机熟悉这样一个习惯的人是什么身份，或者对会议的参与度之类的。。

## 遇到的问题？

数据量比较小，几十个的话确实可以归类于数据偏颇的机器学习，“不平衡数据”

理解上：有些话，自己经历了才知道代表处理过程中的哪一步

现在自己很明确了，之前那个有一些错误，现在改回来，一天可以搞得定

1.根据发出地址address是否是hackingteam的邮箱后缀，来筛选出对应的display内部员工的名字

2.回到数据集中，筛选出每个员工对应的主题，并清洗组成文章

a.提取所有数据中频数最大的 100 个主题，为每个员工构建一个 100 维的向量，分别存储该员工收发该主题邮件的频数。

b.随机选取 40 名员工，基于邮件主题人工赋予其所属部门的标签，构建为训练集，并进行随机森林训练。

c. 利用训练好的随机森林将剩余的 259 名员工分类。我们发现财务部门有 24 名员工，人力资源部门有 18 员工，研发部门有 257 名员工

我提取所有邮件中频数最大的100个主题，向量的建立？

根据每个员工对应的主题txt，去遍历txt涉及这100主题的次数，给排个序


修改原先做好的机器学习流程的训练集与测试集



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

