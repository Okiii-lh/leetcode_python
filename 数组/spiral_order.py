#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-30 11:08:43
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://okery.github.io/
# @Version : v1.0
# @Description :给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。


def spriral_order(matrix):
    """
    输入:
    [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]
    ]
    输出: [1,2,3,6,9,8,7,4,5]
    """
    res = []
    while matrix:
        res += matrix.pop(0)
        print("==================")
        print(matrix)
        print("-----------------")
        matrix = list(map(list, zip(*matrix)))[::-1]
        print("转置后")
        print(matrix)
        print("****************")
    return res


test_matrix = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
    ]

print(spriral_order(test_matrix))


def T(matrix):
    """
    转置
    """
    return list(map(list, zip(*matrix)))


test_matrix = [
     [1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]
    ]

# print(T(test_matrix))
