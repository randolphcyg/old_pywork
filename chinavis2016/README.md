# 0.说明
# 1.目标：套用18年东北师范大学随机森林算法，处理16年挑战赛数据，将员工分配至各个部门，找到部门领导；
## 1.根据答案，用pandas库读取筛选出87名内部员工及其多个邮箱地址：

1.	内部员工列表：

Display和address字段都有可能反映人员信息，下面我们分别进行讨论：

(1).以display字段为例，如果display对应的address字段中含有“o=hackingteam…”、“@hackingteam.it”、“@hackingteam.com”，则认为该display为内部员工的display。Path: final_Res/C2.1/inner_staff/display_inner_staff_list.txt

(2).以address字段为例，如果address字段含有“o=hackingteam…”、“@hackingteam.it”、“@hackingteam.com”，则认为这是一个内部邮箱地址，可以初步将每个邮箱假设为一名员工。（答案的后续部分基于address字段进行分析）Path: final_Res/C2.1/inner_staff/hackingteam_mail_inner_staff.txt

(3).在address字段中有59个形如“o=hackingteam…”的地址可以还原成邮件地址，详见Path: final_Res/OHackingString2dotCom_format.txt

(4).每个员工可能有多个内部邮件地址。通过整理，可以初步确认共87个内部员工，见下表

## 20190318 今天务必筛选出正确的员工列表
* [pandas找列中包含某数据](https://www.jianshu.com/p/805f20ac6e06)
* [缺失值处理](https://blog.csdn.net/lwgkzl/article/details/80948548)
* [缺失值处理思路](https://blog.csdn.net/silence2015/article/details/65643125 )
>用pandas来做csv的缺失值处理时候发现奇怪BUG，就是excel打开csv文件，明明有的格子没有任何东西，
>当然，我就想到用pandas的dropna()或者fillna()来处理缺失值。但是pandas读取csv文件后发现那个空的地方isnull()竟然是false，
>就是说那个地方有东西。。。后来经过排查发现看似什么都没有的地方有空字符串，故pandas认为那儿不是缺失值，所以就不能用dropna()或者fillna()来处理。
>解决思路：先用正则将空格匹配出来，然后全部替换为NULL，再在用pandas读取csv时候指定 read_csv（na_values='NULL'）
>就是将NULL认为是nan处理，接下来就可以用dropna()或者fillna()来处理了

* [缺失值处理小例子](https://blog.csdn.net/u010924297/article/details/80060229)

## 20190319英文词云，观察词云处理数据
![](/chinavis2016/res/result.png)

