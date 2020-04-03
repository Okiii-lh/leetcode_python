#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-04 21:43:57
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://okery.github.io/
# @Version : v1.0
# @Description :给定一个整数数组 a，其中1 ≤ a[i] ≤ n （n为数组长度）, 其中有些元素出现两次而其他元素出现一次。找到所有出现两次的元素。你可以不用到任何额外空间并在O(n)时间复杂度内解决这个问题吗？


def find_duplicates(nums):
    """
    排序，然后双指针验证
    """
    duplicate_num = []
    nums_len = len(nums)
    pre_pointer = 0
    rear_pointer = 1

    nums.sort()

    while(pre_pointer <= nums_len-2 and nums_len != 0 and nums_len != 1):
        if nums[pre_pointer] == nums[rear_pointer]:
            duplicate_num.append(nums[pre_pointer])
            pre_pointer += 2
            rear_pointer += 2
        else:
            pre_pointer += 1
            rear_pointer += 1

    return duplicate_num


def find_duplicates_ex(nums):
    """
    交换法，将元素放到数组对应的索引位置上
    """
    repeates_num = []
    index = 0

    while index < len(len(nums)):
        if nums[index] != nums[nums[index]-1]:
            tmp = nums[index]
            nums[nums[index]-1] = nums[index]
            nums[index] = tmp
        else:
            index += 1

    return repeates_num


test_nums = [1, 2, 3, 3, 4]
find_duplicates(test_nums)
