#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2019/12/9 10:48
# Author: Hou hailun

# 跳表
# 在单链表上增加多级索引的数据结构，称为跳表
# 时间复杂度为O(logN)
# 使用场景：
#   Redis中的有序集合使用跳表实现
#   实际上Redis的有序集合数据结构形式为：一份数据，多层指针
# 跳跃表有如下特点：
# (1) 每个跳跃表由很多层结构组成；
# (2) 每一层都是一个有序链表，且第一个节点是头节点；
# (3) 最底层的有序链表包含所有节点；
# (4) 每个节点可能有多个指针，这与节点所包含的层数有关；
# (5) 跳跃表的查找、插入、删除的时间复杂度均为O(log N)

MAX_LEVEL = 5


# 跳跃表结点类
class Node:
    def __init__(self, level, key, value):
        """
        跳表节点初始化
        :param level: 节点的层数
        :param key: 查询关键字
        :param value: 存储的信息
        """
        self.key = key
        self.value = value
        self.forward = [None] * level


class SkipList:
    def __init__(self):
        """
        跳表初始化 层数为0 初始化头部节点
        """
        self.level = 0
        self.header = Node(MAX_LEVEL, None, None)
        self.size = 0

    def search(self, key):
        """
        跳表搜索操作
        :param key: 查找的关键字
        :return: 节点的 key & value & 节点所在的层数(最高的层数)
        """
        i = self.level - 1
        q = self.header
        while i >= 0:
            while q.forward[i] and q.forward[i].key <= key:
                if q.forward[i].key == key:
                    return q.forward[i].key, q.forward[1].value, i
                q = q.forward[i]
            i -= 1
        return None, None, None

    def insert(self, key, value):
        """
        跳表插入操作
        :param key: 节点索引值
        :param value: 节点内容
        :return: Boolean 用于判断插入成功或失败
        """
        # 更新的最大层数为 MAX_LEVEL 层
        update = [None] * MAX_LEVEL

        i = self.level - 1
        q = None
        # 遍历所有的层数, 找到插入的位置
        while i >= 0:
            q = self.header
            while q.forward[i] and q.forward[i].key < key:
                q = q.forward[i]
            update[i] = q
            i -= 1

        if q and q.key == key:
            return False

        k = randomLevel()
        # 如果随机数大于当前层数，采取加1层策略
        if k > self.level:
            i = self.level
            update[i] = self.header
            self.level += 1
            k = self.level

        q = Node(k, key, value)
        i = 0
        while i < k:
            q.forward[i] = update[i].forward[i]
            update[i].forward[i] = q
            i += 1

        self.size += 1

        return True

