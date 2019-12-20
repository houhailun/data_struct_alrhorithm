#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2019/12/13 16:45
# Author: Hou hailun

"""
堆：一种特殊的完全二叉树；堆中的每个节点值都大于等于(小于等于)其左右子节点值
堆的存储：
    完全二叉树适合用数组来存储，用数组存储完全二叉树是非常节省空间的，因为不需要存储左右子节点的指针，
    单纯通过数组下标就可以找到节点的左右子节点和父节点
    某节点下标为i，其左子节点下标为2*i，右子节点下标为2*i+1，父节点下标为i/2
"""


class Heap:
    # 堆类，默认为大顶堆
    def __init__(self, capacity):
        self.heap = [None] * (capacity+1)  # 数组，从下标1开始存储数据
        self.capacity = capacity   # 堆可以存储的最大数据个数
        self.size = 0  # 堆中已经存储的数据个数

    def insert(self, data):
        """
        插入操作
        思路：
            1、把数据插入到最末尾
            2、如果不满足大顶堆性质就调整，直到满足堆的特征(堆化 heapify)
        :param data: 待插入的数据
        :return: 插入操作是否成功
        """
        # 堆满了
        if self.size >= self.capacity:
            return False
        self.size += 1
        self.heap[self.size] = data
        i = self.size
        while (i // 2 > 0) and (self.heap[i] > self.heap[i // 2]):  # 自下往上堆化
            self.heap[i//2], self.heap[i] = self.heap[i], self.heap[i//2]
            i = i // 2
        return True

    def delete_heap_top(self):
        """
        删除堆顶元素
        堆顶元素是最大值或最小值
        对于大顶堆，删除第一个节点，然后把最后一个节点放到堆顶，然后对比是否满足堆性质，对于不满足的要堆化
        :return:
        """
        # 空堆
        if self.size == 0:
            return None

        # 把最后一个节点放到堆顶
        self.heap[1] = self.heap[self.size]
        self.heap[self.size] = None
        self.size -= 1

        # 自上往下堆化heapify
        return self.heapify(self.size, 1)

    def heapify(self, n, i):
        """
        堆化操作
        :param n: 当前堆的节点数
        :param i: 从i处开始堆化
        :return:
        """
        while True:
            max_ix = i
            # 在左右子节点中查找大值
            if i * 2 <= n and self.heap[i] < self.heap[i * 2]:
                max_ix = i * 2
            if i * 2 + 1 <= n and self.heap[max_ix] < self.heap[i * 2 + 1]:
                max_ix = i * 2 + 1
            if max_ix == i:  # 循环终止条件：当前节点值已经大于等于其左右子节点值
                break
            self.heap[max_ix], self.heap[i] = self.heap[i], self.heap[max_ix]
            i = max_ix  # 递归往下执行

    def heapify_nums(self, nums, n, i):
        """
        堆化操作
        :param nums: 要堆化的数组
        :param n: 当前堆的节点数
        :param i: 从i处开始堆化
        :return:
        """
        while True:
            max_ix = i
            # 在左右子节点中查找大值
            if i * 2 <= n and nums[i] < nums[i * 2]:
                max_ix = i * 2
            if i * 2 + 1 <= n and nums[max_ix] < nums[i * 2 + 1]:
                max_ix = i * 2 + 1
            if max_ix == i:  # 循环终止条件：当前节点值已经大于等于其左右子节点值
                break
            nums[max_ix], nums[i] = nums[i], nums[max_ix]
            i = max_ix

    def create_heap(self, nums):
        """
        创建堆(大顶堆), 在数组原地创建堆
        方法1：从下往上堆化，到达下标1处即可
        方法2：从上往下堆化，到达最后一个父节点即可
        :param nums: 数组
        :return:
        """
        n = len(nums)-1
        for i in range(n//2, 0, -1):  # 只对父节点堆化
            self.heapify_nums(nums, len(nums)-1, i)

    def sort(self, nums):
        # 排序
        self.create_heap(nums)
        k = len(nums) - 1
        while k > 1:
            nums[1], nums[k] = nums[k], nums[1]  # 交换最大、最小元素
            k -= 1
            self.heapify_nums(nums, k, 1)  # 对剩余的k-1个元素重新堆化


class HeapApply:
    # 堆的应用
    def __init__(self, capacity=0):
        self.heap = [None] * (capacity + 1)  # 数组，从下标1开始存储数据
        self.capacity = capacity  # 堆可以存储的最大数据个数
        self.size = 0  # 堆中已经存储的数据个数

    def topK(self):
        # topk问题
        # case1：静态数据，如何在一个包含n个数据的数组中，查找前K大的数据
        # 方法：维护一个大小为K的小顶堆，顺序变量数组，从数组中取出元素与堆顶元素比较，如果比堆顶元素大，就把堆顶元素删除，并把这个元素插入到堆中；
        #       如果比堆顶元素小， 则不做处理；变量完成后，堆中的元素就是前K大元素
        # 时间复杂度：变量数组需要O(n), 一次堆化需要O(logK), 最坏情况下，n个元素都需要入堆，时间复杂度为O(NlogK)
        # case2：动态数据，求得topK问题, 也就是实时的topK
        # 方法：维护一个大小为k的小顶堆，当有数据被添加到集合中时，我们就拿它与堆顶的元素对比。如果比堆顶元素大，我们就把堆顶元素删除，并且将这个元素插入到堆中；
        #       如果比堆顶元素小，则不做处理。这样，无论任何时候需要查询当前的前K大数据，我们都可以里立刻返回给他
        pass

    def prioruty_queue(self):
        # 优先级队列
        # 队列是先进先出的，优先级队列则是根据优先级大小来决定出队顺序
        # 往优先级队列插入
        # 元素，就相当于往堆中插入元素；从优先级队列中取出优先级最高的元素，就相当于取出堆顶元素
        import queue
        queue.PriorityQueue()

    def get_median(self):
        # 求中位数


if __name__ == "__main__":
    obj = Heap(capacity=10)
    print(' 插入元素 '.center(40, '*'))
    obj.insert(19)
    obj.insert(10)
    obj.insert(6)
    obj.insert(25)
    obj.insert(40)
    obj.insert(26)
    print(obj.heap)

    print(' 删除堆顶元素 '.center(40, '*'))
    obj.delete_heap_top()
    print(obj.heap)

    print(' 创建heap '.center(40, '*'))
    nums = [None, 10, 20, 30, 40, 50, 60]
    obj.create_heap(nums)
    print(nums)

    print(' 堆排序 '.center(40, '*'))
    nums = [None, 10, 20, 30, 40, 50, 60]
    obj.sort(nums)
    print(nums)
