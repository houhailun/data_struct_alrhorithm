#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Time    : 2019/7/12 18:33
@Author  : Hou hailun
@File    : AVL.py
"""

print(__doc__)

"""
平衡二叉树
概念: 一种特殊的二叉排序树，它或者为空树，或者每个结点的左右子树都是平衡二叉树，也就是每个结点的左右子树的高度之差只能是-1,0,1三种情况；
    AVL树由平衡因子Balance Factor来衡量；平衡因子定义为当前结点的左子树高度减去右子树的高度之差，其可能取值只有-1,0,1。叶结点的BF都是0。如果能维持平衡二叉树的结构，检索操作就能在O(log n)时间内完成。

红黑树：
Red-Black Tree, 是不严格的平衡二叉树，即不满足左右子树相差最大为1
定义：红黑树是一种含有红黑结点并能自平衡的二叉查找树。它必须满足下面性质:
    1、节点要么是黑色，要么是白色
    2、根节点是黑色的
    3、每个叶子节点都是黑色的空节点，即叶子节点不存储数据
    4、每个红色结点的两个子结点一定都是黑色。
    5、每个节点，从该节点到达其可达叶子节点的所有路径，包含相同数目的黑色节点
    5.1 第5点可以推出：如果一个结点存在黑子结点，那么该结点肯定有两个子结点
"""


class Node:
    # 树节点类
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class RedBlackTree:
    # 红黑树类
    def __init__(self):
        self.root = None

    def search(self, node, data):
        """
        查找操作
        由于查找并不会改变树结构，因此和二叉搜索树查找操作一样
        :param data: 待查找的数据
        :return: Tree Node
        """
        if node is None:
            return None
        if node.data == data:
            return node
        if node.data > data:
            return self.search(node.left, data)
        else:
            return self.search(data.right, data)

    def search_loop(self, node, data):
        if node is None:
            return None
        while node:
            if data == node.data:
                return node
            elif data < node.data:
                node = node.left
            else:
                node = node.right
        return None

    def insert(self, data):
        """
        插入操作，
        :param data:
        :return:
        """