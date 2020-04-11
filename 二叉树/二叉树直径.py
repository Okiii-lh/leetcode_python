#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-11 08:38:11
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://github.com/Okiii-lh
# @Version : v1.0
# @Description : 二叉树直径

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def __init__(self):
        self.max = 0

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.depth(root)

        return self.max

    def depth(self, root):
        if not root:
            return 0
        l = self.depth(root.left)
        r = self.depth(root.right)

        self.max = max(self.max, l+r)

        return max(l, r) + 1
