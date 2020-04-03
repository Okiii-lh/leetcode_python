#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-09 20:43:08
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://okery.github.io/
# @Version : v1.0
# @Description : map、zip函数学习


a = [1, 2, 3]
print(list(map(str, a)))
print(list(map(float, a)))


a = [
    [1, 2, 3],
    [4, 5, 6]
]
print(list(map(sum, a)))


a = [1, 2, 3, 4, 5]

print(list(map(lambda x: x**2, [1, 2, 3, 4, 5])))


a = [1, 2, 3]
b = [4, 5, 6]

print(list(zip(a, b)))

print(list(zip(*(a, b))))


test_matrix = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
    ]


print(list(zip(*test_matrix)))

print(list(map(list, zip(*test_matrix))))
