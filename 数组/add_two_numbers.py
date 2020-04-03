#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date    : 2019-11-25 21:32:03
# @Author  : LiuHe (liuh131@163.com)
# @Link    : https://okery.github.io/
# @Version : v1.0
# @Description : 两数相加


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


def add_two_numbers(l1, l2):
    """
    l1: ListNode
    l2: ListNode
    问题描述：
    给出两个非空的链表用来表示两个非负的整数。
    其中，它们各自的位数是按照逆序的方式存储的，并且它们的每个节点只能存储一位数字。
    如果，我们将这两个数相加起来则会返回一个新的链表来表示它们的和。
    """
    head_note = None
    while(l1 or l2 != 0):

