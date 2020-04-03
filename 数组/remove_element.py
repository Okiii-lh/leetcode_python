#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-28 15:29:08
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://okery.github.io/
# @Version : v1.0
# @Description :给定一个数组 nums 和一个值 val，你需要原地移除所有数值等于 val 的元素，返回移除后数组的新长度。不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1) 额外空间的条件下完成。元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。


def remove_element(nums, val):

    nums_len = len(nums)
    index = 0

    while(index != nums_len):
        if(nums[index] == val):
            del(nums[index])
            nums_len -= 1
        else:
            index += 1

    return nums_len


nums = [3,2,2,3]
val = 3

result = remove_element(nums, val)
print(result)
