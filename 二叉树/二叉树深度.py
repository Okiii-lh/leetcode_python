#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-03 15:13:09
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://github.com/Okiii-lh
# @Version : v1.0
# @Description : 求二叉树深度


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        if not root.left and root.right:
            return 1

        return max(self.maxDepth(root.left), self.maxDepth(root.right)) + 1
