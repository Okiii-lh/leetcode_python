#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-11 15:23:42
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://okery.github.io/
# @Version : v1.0
# @Description :假设你正在爬楼梯。需要 n 阶你才能到达楼顶。每次你可以爬 1 或 2 个台阶。你有多少种不同的方法可以爬到楼顶呢？


def climb_stair(n):
    """
    动态规划方法，easy级别
    """
    # 开数组
    step = list(0 for _ in range(n+1))
    step[1] = 1
    step[2] = 2

    if n == 1:
        return 1

    for i in range(3, n+1):
        step[i] = step[i-1] + step[i-2]

    return step[n]


test_n = 3
print(climb_stair(test_n))
