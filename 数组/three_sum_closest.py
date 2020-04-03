#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-26 20:33:59
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://okery.github.io/
# @Version : v1.0
# @Description :


def absolute_value(x):
    """
    辅助函数 转换成绝对值
    """
    if(x < 0):
        x = -x

    return x


# 使用字典存放距离
def three_sum_clostest(nums, target):
    """
    给定一个包括n个整数的数组nums和一个目标值target。
    找出nums中的三个整数,使得它们的和与target最接近。返回这三个数的和。
    假定每组输入只存在唯一答案。
    """
    result_sum = 0
    pre_distance = {}
    if target < 0:
        max_width = len(nums) - target
    else:
        max_width = len(nums) + target
    current_nums_num = 0
    break_flag = False

    for x in nums:
        # print(x)
        current_dis = (target - x)

        if current_dis < 0:
            current_dis = - current_dis

        if pre_distance.__contains__(x) and current_dis != 0:
            pre_distance[x] += current_dis
        elif pre_distance.__contains__(x) and current_dis == 0:
            pre_distance[x] += 1
        elif current_dis != 0:
            pre_distance[x] = current_dis
        elif current_dis == 0:
            pre_distance[x] = 1

    print(pre_distance)

    if pre_distance.__contains__(target):
        if pre_distance[target] >= 3:
            result_sum = 3 * target
            break_flag = True
        elif pre_distance[target] < 3:
            result_sum = pre_distance[target] * target
            current_nums_num = pre_distance[target]

    for i in range(1, max_width):
        if break_flag:
            break
        if current_nums_num == 3:
            break
        if pre_distance.__contains__((target-i)):
            distance = pre_distance[(target-i)]
            if distance == i:
                result_sum += (target-i)
                current_nums_num += 1
            elif (distance/i) >= (3-current_nums_num):
                result_sum += (3-current_nums_num) * (target-i)
                break
            elif (distance/i) < (3-current_nums_num):
                for j in range(1, (3-current_nums_num)):
                    if current_nums_num == 3:
                        break
                    result_sum += (target-i)
                    current_nums_num += 1

        if pre_distance.__contains__((target+i)):
            distance = pre_distance[(target+i)]
            print(distance)
            if distance == i:
                result_sum += (target+i)
                current_nums_num += 1
            elif (distance/i) >= (3-current_nums_num):
                result_sum += (3-current_nums_num) * ((target+i))
                break
            elif (distance/i) < (3-current_nums_num):
                for j in range(1, (3-current_nums_num)):
                    if current_nums_num == 3:
                        break
                    result_sum += (target+i)
                    current_nums_num += 1

    return result_sum


print("test section")
nums = [0, 2, 1, -3]
target = 1
result_sum = three_sum_clostest(nums, target)

print("result_sum")
print(result_sum)

