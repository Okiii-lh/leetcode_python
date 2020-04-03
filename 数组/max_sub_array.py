#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-30 11:08:43
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://okery.github.io/
# @Version : v1.0
# @Description :给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。


def max_sub_array(nums):
    """
    动态规划
    """
    result_sum = nums[0]
    current_sum = 0

    for num in nums:
        if current_sum > 0:
            current_sum += num
        else:
            current_sum = num
        result_sum = max(result_sum, current_sum)

    return result_sum


test_num = [1, 2, 3]


