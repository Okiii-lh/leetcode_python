#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-03 14:34:51
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://github.com/Okiii-lh
# @Version : v1.0
# @Description : 合并二叉树

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if t1 is None and t2 is None:
            return
        if t1 is None and t2 is not None:
            return t2
        if t1 is not None and t2 is not None:
            t1.val = t1.val + t2.val
            t1.left = self.mergeTrees(t1.left, t2.left)
            t2.right = self.mergeTrees(t1.right, t2.right)
        return t1
