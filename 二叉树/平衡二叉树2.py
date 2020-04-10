#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-10 19:34:20
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://github.com/Okiii-lh
# @Version : v1.0
# @Description : 平衡二叉树

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        if not root:
            return True
        if abs(self.deepOfTree(root.left)-self.deepOfTree(root.right)) > 1:
            return False

        return self.isBalanced(root.left) and self.isBalanced(root.right)

    def deepOfTree(self, root: TreeNode):
        if not root:
            return 0
        if not root.left and not root.right:
            return 1

        return max(self.deepOfTree(root.left), self.deepOfTree(root.right))+1
