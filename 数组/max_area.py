#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-25 21:56:06
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://okery.github.io/
# @Version : v1.0
# @Description : 给定 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 
# (i, ai) 。在坐标内画 n 条垂直线，垂直线i的两个端点分别为 (i, ai) 和 (i, 0)。找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

import time


# 方法1 暴力破解 时间复杂度O(n^2)  在大数据时超出时间限制
def max_area(height_list):
    height_num = len(height_list)
    max_area = 0

    for i in range(height_num):
        current_val = height_list[i]
        for j in range(i+1, height_num):
            if current_val <= height_list[j]:
                area = current_val * (j-i)
            else:
                area = height_list[j] * (j-i)
            if max_area < area:
                max_area = area

    return max_area


# 方法2 双指针 头尾指针移动
def max_area_hash(height_list):
    list_length = len(height_list)

    rear_pointer = list_length - 1
    head_pointer = 0

    max_area = 0

    while(rear_pointer != head_pointer):
        if height_list[rear_pointer] >= height_list[head_pointer]:
            current_width = rear_pointer - head_pointer
            current_area = height_list[head_pointer] * current_width
            if max_area < current_area:
                max_area = current_area
            head_pointer += 1
        else:
            current_width = rear_pointer - head_pointer
            current_area = height_list[rear_pointer] * current_width
            if max_area < current_area:
                max_area = current_area
            rear_pointer -= 1

    return max_area


print(time.time())
result = max_area(
    [1, 8, 6, 2, 5, 4, 8, 3, 7]
)

print(result)

print(time.time())
