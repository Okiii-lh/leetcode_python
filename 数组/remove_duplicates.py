#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-28 11:30:38
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://okery.github.io/
# @Version : v1.0
# @Description : 给定一个排序数组，你需要在原地删除重复出现的元素，使得每个元素只出现一次，返回移除后数组的新长度。不要使用额外的数组空间，你必须在原地修改输入数组并在使用 O(1)额外空间的条件下完成。


def remove_duplicates(nums):
    """
    不能使用额外数组
    双指针移动
    """
    reslut_len = len(nums)
    move_pointer = 0
    check_pointer = 1

    while (check_pointer != reslut_len and reslut_len != 0):
        if(nums[check_pointer] == nums[move_pointer]):
            del(nums[check_pointer])
            reslut_len -= 1
        else:
            move_pointer += 1
            check_pointer += 1

    return reslut_len


nums = [1, 1, 2]
result = remove_duplicates(nums)
print(result)
