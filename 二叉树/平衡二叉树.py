#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2020-04-02 13:34:03
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://github.com/Okiii-lh
# @Version : v1.0
# @Description : leetcode 刷题 平衡二叉树

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


def is_balance_tree(root):
    # 树节点要做的事情
    if root.left is not None and root.left.left is not None and root.right is None:
        return False
    elif root.left is not None and root.left.right is not None and root.right is None:
        return False
    elif root.right is not None and root.right.left is not None and root.left is None:
        return False
    elif root.right is not None and root.right.right is not None and root.left is None:
        return False
    elif root.right is not None and root.left is not None:
        if abs(deep_of_tree(root.left) - deep_of_tree(root.right)) > 1:
            return False
    else:
        return True

    return is_balance_tree(root.left) and is_balance_tree(root.right)


# 树深度
def deep_of_tree(root):
    if not root:
        return 0
    if not root.left and root.right:
        return 1

    return max(deep_of_tree(root.left), deep_of_tree(root.right))+1
