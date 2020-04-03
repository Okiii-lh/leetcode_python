#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-28 23:24:00
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://okery.github.io/
# @Version : v1.0
# @Description :给定一个排序数组和一个目标值，在数组中找到目标值，并返回其索引。如果目标值不存在于数组中，返回它将会被按顺序插入的位置。


def search_insert(nums, target):
    """
    单指针移动
    当指针所指元素大于或等于目标值时，将指针返回
    """
    nums_len = len(nums)
    index = 0

    while index != nums_len and nums_len != 0:
        if nums[index] == target or nums[index] > target:
            return index
        else:
            index += 1

    return nums_len


print(5/2)
