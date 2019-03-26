# -*- coding: utf-8 -*-
# @Time    : 2019/3/24 0:00
# @Author  : Randolph
# @Email   : cyg0504@outlook.com
# @File    : grammer_down_class.py
# @Software: PyCharm

## 字符串与字节
# python3唯一可以保存文本信息的数据类型-str 不可变序列、保存的是unicode码位
# str bytes bytearray  区别
print(bytearray([102, 111, 111]))
print(bytes([102, 111, 111]))
print(list(b'foo bar'))
print(tuple(b'foo bar'))

print(type('some string'))
print(type(b'some string'))

# 拼接字符串推荐join方法
joint_str = ','.join(['some', 'comma', 'separated', 'values'])
print(joint_str)

## 集合类型

evens1 = []
for i in range(10):
    if i % 2 == 0:
        evens1.append(i)
print(evens1)

# 列表推导推荐此方法：高效、简短、涉及更少语法元素
evens2 = [i for i in range(10) if i % 2 ==0]
print(evens2)
# 枚举方法enumerate提供索引值
for i, girl in enumerate(['steve', 'kulipa', 'zhizhu']):
    print(i+1, girl)

# 合并等长可迭代对象内部元素用zip方法
for item in zip([1, 2, 3], [4, 5, 6]):
    print(item)
# 再次调用，恢复原状
for item in zip(*zip([1, 2, 3], [4, 5, 6])):
    print(item)

# 序列解包
first, second, third = '1', '2', '3'
print(second)
# 带星号表达式
first, second, *rest = 1, 2, 3, 4
print(rest)
# 带星号表达式
first, *second, rest = 1, 2, 3, 4
print(second)
# 嵌套解包
(a, b), (c, d) = (1, 2),(3, 4)
print(c)