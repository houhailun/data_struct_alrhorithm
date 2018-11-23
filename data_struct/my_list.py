#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
模块功能：实现链表:内存不连续，快速插入删除
"""


class Node:
    """ 节点类 """
    def __init__(self, data):
        self.data = data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class LinkList:
    """ 链表类 """
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head

    def add(self, item):
        """ 头插法 """
        tmp_node = Node(item)
        tmp_node.set_next(self.head)
        self.head = tmp_node

    def size(self):
        count = 0
        cur_node = self.head
        while cur_node:
            cur_node = cur_node.get_next()
            count += 1
        return count

    def search(self, item):
        found = False
        cur_node = self.head
        while cur_node and not found:
            if cur_node.get_data() == item:
                found = True
                break
            else:
                cur_node = cur_node.get_next()
        return found

    def remove(self, ix):
        """ 删除指定位置节点 """
        pass


if __name__ == "__main__":
    link_list = LinkList()
    link_list.add(10)
    link_list.add(20)
    link_list.add(30)
    print(link_list.size())

    print(link_list.search(20))
