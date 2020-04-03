#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-22 23:19:24
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://okery.github.io/
# @Version : 给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。


def two_sum_vio(nums, target):
    num_len = len(nums)
    results = []
    for i in range(0, num_len):
        flage = False
        remainder = target - nums[i]
        for j in range(0, num_len):
            if(nums[j] == remainder and j != i):
                results.append(i)
                results.append(j)
                flage = True
                break
        if flage:
            break

    return results


def two_sum_hash(nums, target):
    nums_len = len(nums)
    num_dict = {}
    results = []
    for i in range(0, nums_len):
        if num_dict.__contains__(nums[i]):
            num_dict[nums[i]] += i
        else:
            num_dict[nums[i]] = i
    for i in range(0, nums_len):
        remainder = target - nums[i]
        if num_dict.__contains__(remainder) and num_dict[remainder] != i:
            print(remainder)
            if remainder == nums[i]:
                print("相等")
                results.append(i)
                results.append(num_dict[nums[i]]-i)
            else:
                print(i)
                print(num_dict[remainder])
                results.append(i)
                results.append(num_dict[remainder])
            break

    return results


nums = [3, 2, 4]
target = 6
results = two_sum_vio(nums, target)
print(nums[0])
print(results)
results2 = two_sum_hash(nums, target)
print(results2)
