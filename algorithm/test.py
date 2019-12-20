#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2019/9/10 10:11
# Author: Hou hailun


class MySearch(object):
    # 查找算法类
    def __init__(self):
        self.data = [10, -3, 34, 56, 97, 100]

    def sequence_search(self, key):
        # 顺序查找: 从列表开始处依次往后查找; 时间复杂度O(N)
        _is_find = False
        for val in self.data:
            if key == val:
                _is_find = True
                break
        return _is_find, key

    def binary_search(self, key):
        # 二分查按：从列表中间处开始查找，如果中间值小于key，则往右半区间查找，否则往左半区间查找
        # 前提：数据有序   时间复杂度O(logN)
        array = self.data.copy()
        array.sort()
        start = 0
        end = len(array) - 1
        _is_find = False
        while start < end:
            mid = (start + end) // 2
            if key > array[mid]:  # 右半区间查找
                start = mid + 1
            elif key < array[mid]:  # 作伴区间查找
                end = mid - 1
            else:
                _is_find = True
                break
        return _is_find, key

    def insert_search(self, key):
        # 插值查找：和二分查找类似，mid=low+(high-low)*(key-a[low])/(a[high]-a[low])
        _is_find = False
        array = self.data.copy()
        array.sort()
        low = 0
        high = len(array) - 1
        while low < high:
            mid = low + (high - low) * ((key - array[low]) // (array[high] - array[low]))
            if key < array[mid]:
                high = mid - 1
            elif key > array[mid]:
                low = mid + 1
            else:
                _is_find = True
                break
        return _is_find, key

    def fibnacio_search(self, key):
        # 斐波那契查找：利用斐波性质: a[i] = a[i-1] + a[i-2], 其中a[0]=1,a[1] = 1
        pass


class Node:
    # 二叉树节点类
    def __init__(self, data, left=None, right=None):
        self.left = left
        self.right = right
        self.data = data


class BTree(object):
    # 二叉树类
    def __init__(self, node=None):
        self.root = node  # 根节点

    def add_node_complete_tree(self, item=None):
        # 构建完全二叉树
        node = Node(item)
        if self.root is None:  # 空树，添加到根节点
            self.root = node
            return
        # 不为空，则按照 左右顺序 添加节点,这样构建出来的是一棵有序二叉树，且是完全二叉树
        my_queue = []
        my_queue.append(self.root)
        while True:
            curr_node = my_queue.pop(0)
            if curr_node.left is None:
                curr_node.left = node
                return
            elif curr_node.right is None:
                curr_node.right = node
                return
            else:
                my_queue.append(curr_node.left)
                my_queue.append(curr_node.right)

    def add_node_tree(self, item):
        # 构建一搬二叉树
        node = Node(item)
        if self.root is None:  # 空树，添加到根节点
            self.root = node
            return
        # 不为空，则按照 左右顺序 添加节点,这样构建出来的是一棵有序二叉树，且是完全二叉树
        my_queue = []
        my_queue.append(self.root)
        while True:
            curr_node = my_queue.pop(0)
            # 如果当前节点为空节点则跳过它，起到占位的作用
            if curr_node.data is None:
                continue
            if curr_node.left is None:
                curr_node.left = node
                return
            elif curr_node.right is None:
                curr_node.right = node
                return
            else:
                my_queue.append(curr_node.left)
                my_queue.append(curr_node.right)

    def pre_order(self, node):
        # 前序遍历: 根-左-右
        if node is None:
            print('This Tree is None')
            return
        print(node.data)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def mid_order(self, node):
        # 中序遍历：左-根-右
        if node is None:
            return
        self.mid_order(node.left)
        print(node.data)
        self.mid_order(node.right)

    def post_order(self, node):
        # 后序遍历：左-右-根
        if node is None:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.data)

    @staticmethod
    def bread_travel(node):
        # 层次遍历（广度优先遍历）：利用队列实现
        if node is None:
            return
        _my_queue = list()
        _my_queue.append(node)
        while _my_queue:
            curr_node = _my_queue.pop(0)
            print(curr_node.data, end=', ')
            if curr_node.left is not None:
                _my_queue.append(curr_node.left)
            if curr_node.right is not None:
                _my_queue.append(curr_node.right)


class BSTree:
    # 二叉搜索树: 左孩子节点值小于其父节点值，右孩子节点值大于其父节点值
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def search(self, key):
        # 利用二叉搜索树的性质：左节点值 < 父节点值 < 右节点值
        bt = self.root
        while bt:
            if key > bt.data:
                bt = bt.right
            elif key < bt.data:
                bt = bt.left
            else:
                return bt
        return None

    def insert(self, key):
        # 插入值为key的节点
        pass


class MySort:
    # 排序算法类
    def __init__(self, data=None):
        self.data = [4, 6, 3, -10, 85, 43]

    def bubble_sort(self):
        # 冒泡排序
        # 思想: 相邻元素两两比较，前面元素大于后面元素则交换
        # 空间复杂度O(1)  时间复杂度O(N*N)   稳定排序算法
        data = self.data.copy()
        length = len(data)
        for i in range(length):
            # 内循环一次，把最大元素放到尾部
            for j in range(length - i - 1):
                if data[j] > data[j+1]:
                    data[j], data[j+1] = data[j+1], data[j]

        return data

    def insert_sort(self):
        # 插入排序
        # 思想：在已排序数组中插入一个新元素，得到一个长度加1的有序数组
        # 1、确定插入位置  2、插入位置后面元素后移
        # 空间复杂度O(1)  时间复杂度O(N*N)  稳定排序算法
        data = self.data.copy()
        length = len(data)
        # 从1开始，第一个元素认为已排序数组
        for i in range(1, length):
            if data[i] < data[i-1]:  # 确定插入位置i
                value = data[i]  # 待插入元素
                j = i - 1        # 待插入位置前一个元素位置
                while j >= 0 and data[j] > value:  # 后移
                    data[j+1] = data[j]
                    j -= 1
                data[j + 1] = value
        return data

    def select_sort(self):
        # 选择排序
        # 思想: 每次在当前未完成排序的数组中找当前最小值，写到当前数组最前面
        # 空间复杂度O(1)  时间复杂度O(N*N)  非稳定排序(交换破坏了稳定性)
        data = self.data.copy()
        length = len(data)
        for i in range(length):
            mininum = i
            for j in range(i+1, length):
                if data[mininum] > data[j]:
                    mininum = j
            if mininum != i:
                data[mininum], data[i] = data[i], data[mininum]
        return data

    def merge_sort(self, arr):
        if len(arr) <= 1:
            return arr
        # 递归拆分,O(logN)
        mid = len(arr) // 2
        left = self.merge_sort(arr[: mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, start, end):
        # 合并子数组O(N)
        tmp = []
        i = j = 0
        len_start, len_end = len(start), len(end)
        while i < len_start and j < len_end:
            if start[i] < end[j]:
                tmp.append(start[i])
                i += 1
            else:
                tmp.append(end[j])
                j += 1

        tmp += start[i:]
        tmp += end[j:]
        return tmp

    def quick_sort(self, arr, start, end):
        if end > start:
            index = self.partition(arr, start, end)
            self.quick_sort(arr, start, index-1)
            self.quick_sort(arr, index+1, end)
        return arr

    def partitions(self, arr, start, end):
        key = arr[start]  # 设置分区点
        while start < end:
            # 从后往前，直至小于key
            while start < end and arr[end] >= key:
                end -= 1
            arr[start], arr[end] = arr[end], arr[start]

            # 从前往后，直至大于key
            while start < end and arr[start] <= key:
                start += 1
            arr[start], arr[end] = arr[end], arr[start]
        return start


if __name__ == "__main__":
    obj = MySearch()
    print(' sequence search '.center(40, '*'))
    print(obj.sequence_search(34))
    print(' binary search '.center(40, '*'))
    print(obj.binary_search(34))
    print(' insert search '.center(40, '*'))
    print(obj.insert_search(34))