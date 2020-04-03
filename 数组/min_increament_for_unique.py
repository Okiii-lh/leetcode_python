#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-12-02 21:03:53
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://okery.github.io/
# @Version : v1.0
# @Description :给定整数数组 A，每次 move 操作将会选择任意 A[i]，并将其递增 1。返回使 A 中的每个值都是唯一的最少操作次数。


def min_increament_for_unique(A):
    """
    hash存储，找相邻的空位置相加
    """
    A_len = len(A)
    A_dic = {}
    repeates = []
    repeate_done = {}
    move_sum = 0

    for i in range(A_len):
        if A[i] in A_dic:
            A_dic[A[i]] += 1
            repeates.append(A[i])
        else:
            A_dic[A[i]] = 1

    for x in repeates:
        done_flag = False
        if x in repeate_done:
            current_move_count = repeate_done[x]+1
        else:
            current_move_count = 1
        while not done_flag:
            if (x+current_move_count) not in A_dic:
                A_dic[x+current_move_count] = 1
                repeate_done[x] = current_move_count
                move_sum += current_move_count
                done_flag = True
            else:
                current_move_count += 1
                move_sum += 1

    return move_sum


test_A = [2, 2, 2, 1]

result = min_increament_for_unique(test_A)

print(result)

print(test_A[1: 3])

print(type(test_A))

