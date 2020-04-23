#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/4/15 15:10
# Author: Hou hailun

# 链表:
# 链式存储
# 查询O(N), 插入/删除O(1)


class Node:
    def __init__(self, data):
        self.data = data  # 数据
        self.next = None  # 指针


class LinkList:
    def __init__(self):
        self.head = None  # 头节点

    def add_tail(self, data):
        # 尾插法
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            self.head.next = node

    def add_head(self, data):
        # 头插法
        node = Node(data)
        node.next = self.head
        self.head = node

    def size(self):
        # 链表中节点数
        cnt = 0
        cur_node = self.head
        if cur_node:
            cur_node = cur_node.next
            cnt += 1
        return cnt

    def search(self, item):
        # 在链表中查找值为item的节点
        if self.head is None:
            return False
        cur_node = self.head
        while cur_node:
            if cur_node.data == item:
                return True
            cur_node = cur_node.next
        return False

    def remove(self, ix):
        # 删除ix位置的节点
        del_date = 0
        pre_node = None
        cur_node = self.head
        i = 0  # 标记节点位置
        if 0 == ix:  # 删除头节点
            del_date = cur_node.data
            self.head = self.head.next
            return del_date
        i = 0
        while cur_node:
            print('i:', i)
            if i == ix:
                pre_node.next = cur_node.get_next()
                del_data = cur_node.get_data()
                break
            elif i < ix:
                pre_node = cur_node
                cur_node = cur_node.get_next()
                i += 1
        if i > ix:
            del_data = -1
        return del_data


