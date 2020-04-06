#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-06 13:55:43
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://github.com/Okiii-lh
# @Version : v1.0
# @Description : 修剪二叉搜索树


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if not root:
            return None

        if root.val < L and root.right:
            return self.trimBST(root.right, L, R)
        if root.val < L and not root.right:
            return None
        if root.val > R and root.left:
            return self.trimBST(root.left, L, R)
        if root.val > R and not root.left:
            return None

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)

        return root

