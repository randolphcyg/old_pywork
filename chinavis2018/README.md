# 20190314
## 0.参考资料
* [Python + wordcloud + jieba 十分钟学会用任意中文文本生成词云](https://blog.csdn.net/fontthrone/article/details/72782971)
* [Python词云 wordcloud 十五分钟入门与进阶](https://blog.csdn.net/fontthrone/article/details/72775865)
* [Python中文分词 jieba 十五分钟入门与进阶](https://blog.csdn.net/fontthrone/article/details/72782499)
* [jieba·PyPI](https://pypi.org/project/jieba/)
## 1.将email.csv的subject绘制词云，观察文本分布情况，可以首先筛除垃圾邮件;
看到包含“ALARM”，“RECOVER”，“互联网资产监控报警”，“安全邮件崩溃”字样的邮件主题，这些我们明显不需要：

![](/res/wrong_result1.png)
![](/res/wrong_result2.png)

## 2.再者根据前二十高频词汇，也能尽量找到无用记录：
```
HOST 0.7083569789095852
邮件 0.5233368348207466
崩溃 0.4402549631286797
ALARM 0.3615879377571882
RECOVER 0.34676904115239693
安全 0.32229094578948253
文档 0.24175923428257629
报警 0.13963687165883418
葡京 0.13448404268243297
监控 0.12412264358465147
互联网 0.11885318218949696
澳門 0.11210220857513435
38 0.10455554826713877
com 0.09368149682334513
116498 0.09124598372394656
群號 0.08414526243415073
资产 0.0841363421215404
会计核算 0.08324108391702387
需求 0.07141084949166569
项目 0.06777019155158302
```
## 3.清理代码
```
def clean(target_csv, clean_csv):
    read_data = pd.read_csv(target_csv)  # 读取原始Email.csv
    # print(read_data)
    read_data = read_data[~ read_data['subject'].str.contains('邮件')]  # 删除某列包含特殊字符的行
    read_data = read_data[~ read_data['subject'].str.contains('崩溃')]  
    read_data = read_data[~ read_data['subject'].str.contains('HOST')]
    read_data = read_data[~ read_data['subject'].str.contains('ALARM')]
    read_data = read_data[~ read_data['subject'].str.contains('RECOVER')]
    read_data = read_data[~ read_data['subject'].str.contains('报警')]
    read_data = read_data[~ read_data['subject'].str.contains('葡京')]
    read_data = read_data[~ read_data['subject'].str.contains('澳門')]
    read_data = read_data[~ read_data['subject'].str.contains('38')]
    read_data = read_data[~ read_data['subject'].str.contains('群號')]
    # print(read_data)
    read_data.to_csv(clean_csv, index=False)  # 将数据重新写入Email.csv
```
## 4.剔除后前二十高频词和词云，达到了要求：
清理数据后的高频词汇
```
文档 0.6547430658567895
会计核算 0.22543719023105152
需求 0.19339802539646225
项目 0.18353823431754343
财务 0.17090855224163862
税务 0.1634438203477047
用户手册 0.160830880914214
api 0.15635222762432255
配置 0.15598272665734156
分析 0.15424798424972375
系统配置 0.15022076771748638
初验 0.1482698486562203
终验 0.14520411870280223
软件开发 0.13839853942736494
设计 0.13572664266454468
概要 0.12885281438319748
测试数据 0.12789329858039522
传输 0.12710249619060948
子系统 0.1265628142423125
```
可以看到，借助词云和高频词我们已经基本剔除了无用数据，至此简单清洗数据工作完成

![](/res/result1.png)
![](/res/result2.png)
