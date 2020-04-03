#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-11 15:53:13
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://okery.github.io/
# @Version : v1.0
# @Description : 300 最长上升子序列 给定一个无序的整数数组，找到其中最长上升子序列的长度。


def length_of_LIS(nums):
    """
    实现1 单指针
    指针对当前位置元素值与前者元素值进行判断，若为上升序，后指针向后移动，当前序列长度加一，若不是，双指针同时向后移动，比对当前序列长度与最长长度
    """
    nums_len = len(nums)
    current_point = 1
    max_length = 0
    current_length = 0

    while current_point < nums_len and nums_len != 0:
        if nums[current_point] > nums[current_point-1]:
            current_length += 1
            current_point += 1
        else:
            if max_length < current_length:
                max_length = current_length
            current_length = 0
            current_point += 1

    return max_length


def length_of_LIS_DP(nums):
    """
    动态规划
    """
    nums_len = len(nums)
    max_length = list(1 for _ in range(nums_len))

    if nums_len == 1:
        return 1

    # 转移方程
    for i in range(nums_len):
        max_length[i]


test_nums = [10, 9, 2, 5, 3, 7, 101, 18]

print(length_of_LIS_DP(test_nums))
