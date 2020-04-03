#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-01 10:33:37
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://okery.github.io/
# @Version : v1.0
# @Description :给定一个非空整数数组，除了某个元素只出现一次以外，其余每个元素均出现两次。找出那个只出现了一次的元素。


def num_only_once_dic(nums):
    """
    使用额外空间实现
    使用字典存储元素以及元素出现次数
    查询字典中出现次数为1的元素
    """
    nums_dic = {}

    for num in nums:
        if num in nums_dic:
            nums_dic[num] += 1
        else:
            nums_dic[num] = 1

    for vec in nums_dic:
        if nums_dic[vec] == 1:
            return vec

    return None


def num_only_once(nums):
    """
    不使用额外空间实现
    先排序
    再使用双指针移动检查，指针移动步长为2
    检查前后指针所指元素是否相同，不相同返回前指针所指元素
    """
    pre_point = 0
    check_point = 1
    nums_len = len(nums)

    nums.sort()

    while check_point != nums_len and nums_len != 0:
        if nums[pre_point] == nums[check_point]:
            pre_point += 2
            check_point += 2
        else:
            return nums[pre_point]

    return nums[nums_len-1]


test_nums = [2, 2, 1]
num_only_once(test_nums)
