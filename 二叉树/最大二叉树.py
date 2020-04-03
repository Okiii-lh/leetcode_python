#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-03 14:55:23
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://github.com/Okiii-lh
# @Version : v1.0
# @Description : 最大二叉树


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def constructMaximumBinaryTree(self, nums: List[int]) -> TreeNode:
        if nums == []:
            return None
        max_num = max(nums)
        max_index = nums.index(max_num)
        left_nums = nums[0: max_index]
        right_nums = nums[max_index+1: ]

        root = TreeNode(max_num)

        root.left = self.constructMaximumBinaryTree(left_nums)
        root.right = self.constructMaximumBinaryTree(right_nums)

        return root
