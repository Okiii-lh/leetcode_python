#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-03 15:28:07
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://github.com/Okiii-lh
# @Version : v1.0
# @Description : 镜像二叉树


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def mirrorTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        if root.left is None and root.right is None:
            return root

        tmp = root.left
        root.left = root.right
        root.right = tmp

        self.mirrorTree(root.left)
        self.mirrorTree(root.right)

        return root
