#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-02 10:56:12
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://okery.github.io/
# @Version : v1.0
# @Description :给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。如果你最多只允许完成一笔交易（即买入和卖出一支股票），设计一个算法来计算你所能获取的最大利润。

# 输入: [7,1,5,3,6,4]
# 输出: 5
# 解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
#      注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
from time import time


def max_profit_vio(nums):
    """
    暴力枚举
    没考虑输入数组为空 但是测试用例没有提出相关测试
    最大测试用例运行十七秒
    """
    nums_len = len(nums)
    print(nums_len)
    max_profit = 0

    for i in range(nums_len-1):
        for j in range(i+1, nums_len):
            if nums[j] > nums[i]:
                current_profit = nums[j] - nums[i]
                if max_profit < current_profit:
                    max_profit = current_profit

    return max_profit


def max_profit_o_n(nums):
    """
    当数据量为万级以上时，暴力破解方法使用时间过长
    当前最大值减去当前最小值即为当前情况下最大利润
    只遍历一遍即可
    时间复杂度O(n)
    """
    nums_len = len(nums)
    max_profit = 0

    if nums_len == 0:
        return max_profit
    else:
        current_max_value = nums[0]
        current_min_value = nums[0]


    for i in range(1, nums_len):
        if current_min_value > nums[i]:
            current_max_value = nums[i]
            current_min_value = nums[i]
        else:
            if current_max_value < nums[i]:
                current_max_value = nums[i]
                current_profit = current_max_value - current_min_value
                if current_profit > max_profit:
                    max_profit = current_profit

    return max_profit


print(time())

test_nums = [7, 1, 5, 3, 6, 4]

print(max_profit_o_n(test_nums))

print(time())
