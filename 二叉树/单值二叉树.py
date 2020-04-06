#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-06 14:33:32
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://github.com/Okiii-lh
# @Version : v1.0
# @Description : 单值二叉树


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:
        if not root:
            return True

        if root.left and root.right:
            if root.val == root.left.val and root.val == root.right.val:
                return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
            else:
                return False
        if root.left and not root.right:
            if root.val == root.left.val:
                return self.isUnivalTree(root.left)
            else:
                return False
        if not root.left and root.right:
            if root.val == root.right.val:
                return self.isUnivalTree(root.right)
            else:
                return False

        return True

