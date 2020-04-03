#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-27 20:34:30
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://okery.github.io/
# @Version : v1.0
# @Description : 输入数组 目标值 寻找数组中的三个数 和与目标值最接近


def three_sum_clostest_update(nums, targets):
    """
    方法一：
        暴力破解,遍历全部
        时间复杂度O(n^3)
    """
    result = 0
    nums_num = len(nums)
    sums = {}

    for i in range(nums_num):
        for j in range(i+1, nums_num):
            for k in range(j+1, nums_num):
                result = nums[i] + nums[j] + nums[k]
                sums[result] = result

    flag = True
    index = 0

    while(flag):
        if sums.__contains__(targets-index):
            result = sums[(targets-index)]
            flag = False
        elif sums.__contains__(targets+index):
            result = sums[(targets+index)]
            flag = False
        else:
            index += 1

    return result


def three_sum_clostest_update_2(num, target):
    """
    暴力优化,边计算边比较
    """
    result = 0
    nums_num = len(num)
    distance = 0

    if nums_num == 3:
        result = sum(num)
        return result

    for i in range(nums_num-3):
        for j in range(i+1, nums_num-2):
            for k in range(j+1, nums_num):
                current_res = num[i] + num[j] + num[k]
                current_dis = target - current_res
                if current_dis < 0:
                    current_dis = - current_dis
                if i == 0 and j == 1 and k == 2:
                    distance = current_dis
                    result = current_res
                else:
                    if distance > current_dis:
                        distance = current_res
                        result = current_res

    return result


def three_sum_clostest_update_3(num, target):
    """
    非暴力破解
    """


test_nums = [0, 1, 2]
test_target = 3

result = three_sum_clostest_update_2(test_nums, test_target)

print(result)
