#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Time    : 2019/6/28 10:04
@Author  : Hou hailun
@File    : test.py
"""

print(__doc__)


class MyQueue(object):
    """队列类: 队尾入，对头出; 本质就是列表"""
    def __init__(self):
        self.queue = []

    def enquene(self, data):
        """入队列"""
        self.queue.append(data)

    def dequene(self):
        """出队列"""
        if not self.is_empty():
            return self.queue.pop(0)

    def is_empty(self):
        """检查是否空队列"""
        return self.queue == []

    def size(self):
        return len(self.queue)


class MyDeque(object):
    """双端队列: 头尾都可以插入、删除元素"""
    def __init__(self):
        self.deque = []

    def is_empty(self):
        return self.deque == []

    def add_front(self, data):
        """队列头部插入数据"""
        self.deque.insert(0, data)

    def add_tail(self, data):
        """队列尾部插入数据"""
        self.deque.append(data)

    def del_front(self):
        """删除队列头部数据"""
        if not self.is_empty():
            return self.deque.pop(0)

    def del_tail(self):
        """删除队列尾部数据"""
        if not self.is_empty():
            return self.deque.pop()

    def size(self):
        return len(self.deque)


class MyStack(object):
    """栈类"""
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return self.stack == []

    def push(self, data):
        self.stack.append(data)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def print_stack(self):
        """栈打印"""
        if self.is_empty():
            print("栈为空!")
            return
        for i in range(len(self.stack)):
            print(self.stack[i])


class Search(object):
    """查找类: 顺序查找、二分查找、树查找(二叉搜索树)、hash查找、插值差值、斐波那契查找、分块查找"""
    def __init__(self, data):
        self.data = data

    def sequence_search(self, key):
        """
        顺序查找: 从头到尾依次查找
        时间复杂度: O(N)
        """
        found = False
        for val in self.data:
            if val == key:
                found = True
                break
        return found

    def binary_search(self, key):
        """
        二分查找: 首先检查中间元素是否等于key，如果小于key则在右半子数组查找；否则在左半子数组查找；递归
        前提: 序列有序或者基本有序
        时间复杂度: O(logN)
        """
        array = self.data.copy()
        array.sort()
        start = 0
        end = len(array)-1
        found = False
        while start < end:
            mid = (start + end) // 2
            if key == array[mid]:
                found = True
                break
            elif key < array[mid]:  # 左子序列
                end = mid - 1
            else:
                start = mid + 1     # 右子序列
        return found

    def insert_search(self, key):
        """
        插值查找:仅仅是把二分查找中的mid更换为mid = start + (end - start) * (key - array[start]) // (array[end] - array[start])
        """
        pass

    def Fibnacio_search(self, key):
        """
        斐波那契查找
        斐波那契数列: O(n) = O(n-1) + O(n-2)
        """
        pass


class HashTable(object):
    """
    哈希表: 一种key-value对的数据存储结构，查找时只需要输入key，在O(1)时间内找到对应value
    算法思想: 常用列表、字典来实现
        列表实现: key是整数，把key作为列表下标，value作为列表元素
        字典实现: key可以是任意类型，key作为字典的key，value作为字典的value
    算法流程
　　  1）用给定的哈希函数构造哈希表；
　　  2）根据选择的冲突处理方法解决地址冲突；常见的解决冲突的方法：拉链法和线性探测法。
　　  3）在哈希表的基础上执行哈希查找。
    哈希函数：一种映射关系，根据key通过一定的函数关系，计算出该元素存储位置的函数；
    常用的哈希函数有：
        直接定址法：即取关键字或关键字的线性函数计算地址，表示为：Hash(key)=key或Hash(key)=a*key+b
        除留余数法：取关键字被某个不大于哈希表长度m的数p求余，表示为：hash(key)=key % p, p<=m
        数字分析法、平方取中法、折叠法、随机数法等
    复杂度分析: 单纯论查找复杂度：对于无冲突的Hash表而言，查找复杂度为O(1)（注意，在查找之前我们需要构建相应的Hash表）
    """
    def __init__(self, size):
        self.elem = [None] * size  # 哈希表
        self.count = size           # 最大表长

    def hash(self, key):
        """哈希函数，这里用除留余数法"""
        return key % self.count

    def insert_hash(self, key):
        """插入key到hash table"""
        address = self.hash(key)
        while self.elem[address]:  # 冲突，采用线性探测法解决
            address = (address + 1) % self.count
        self.elem[address] = key

    def search_hash(self, key):
        """查找key，前提是已经创建hash table，必须和创建时用同一个hash函数"""
        start = self.hash(key)
        while self.elem[start] != key:
            address = (start + 1) % self.count
            if address == start or not self.elem[address]:  # 循环一遍没有找到
                return False
        return True


class TNode(object):
    """二叉树节点"""
    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BinaryTree(object):
    """二叉树: 除叶子节点外，其他节点有左孩子、右孩子节点"""
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root == None

    def insert_node(self, key):
        bt = self.root
        if not bt:
            self.root = TNode(key)
            return


if __name__ == "__main__":
    # queue_test()

    deque_test()

