#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-06 13:55:03
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://github.com/Okiii-lh
# @Version : v1.0
# @Description : 完全二叉树的节点个数


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0

        if not root.left and not root.right:
            return 1

        return self.countNodes(root.left) + self.countNodes(root.right) + 1
