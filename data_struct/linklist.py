#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Time    : 2019/6/27 17:27
@Author  : Hou hailun
@File    : linklist.py
"""

print(__doc__)


class Node:
    """节点类"""
    def __init__(self, data):
        self.data = data  # 数据域
        self.next = None  # 指针域

    def get_next(self):
        return self.next

    def get_data(self):
        return self.data

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class LinkList:
    """链表类"""
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head

    def add(self, item):
        """头插法: 新节点插入最开始处"""
        tmp_node = Node(item)
        tmp_node.set_next(self.head)
        self.head = tmp_node

    def size(self):
        """链表中节点个数"""
        node_cnt = 0
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.get_next()
            node_cnt += 1
        return node_cnt

    def search(self, item):
        """链表中查找是否存在值为item的节点"""
        cur_node = self.head
        while cur_node:
            if cur_node.get_data() == item:
                return True
            cur_node = cur_node.get_next()
        return False

    def remove(self, ix):
        """链表中删除ix位置节点"""
        del_data = 0
        cur_node = self.head
        pre_node = None
        if 0 == ix:  # 删除头节点
            del_data = self.head.get_data()
            self.head = self.head.get_next()
            return del_data
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

    def print_link(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.get_next()


def link_list():
    link = LinkList()
    link.add(5)
    link.add(4)
    link.add(3)
    link.add(2)
    link.add(1)

    link.print_link()

    length = link.size()
    print(length)

    print(link.search(4))

    link.print_link()
    print(link.remove(3))


if __name__ == "__main__":
    link_list()