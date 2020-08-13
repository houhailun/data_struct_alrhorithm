#!/usr/bin/env python
# -*- coding:utf-8 -*-

class FindAlgorithm:
    # 查找算法类
    def __init__(self, data):
        self.data = data

    def sequence_find(self, key):
        # 顺序查找
        # 时间复杂度O(N)
        flag = False
        for num in self.data:
            if num == key:
                flag = True
                break
        return flag, key

    def binary_find(self, key):
        # 二分查找, 前提是数据有序或基本有序
        # 时间复杂度O(logN)
        flag = False
        start, end = 0, len(self.data)
        while start < end:
            mid = (start + end) >> 1
            if self.data[mid] > key:
                end = mid - 1
            elif self.data[mid] < key:
                start = mid + 1
            else:
                flag = True
                break
        return flag, key

# obj = FindAlgorithm([1,2,3,4,5,6,7,8])
# print(obj.binary_find(3))


# 二叉搜索树查找
class BSTNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BSTree:
    def __init__(self):
        self.root = None

    def is_empty(self):
        return self.root is None

    def insert(self, key):
        bt = self.root
        if bt is None:  # 根结点为空
            self.root = BSTNode(key)
            return
        while True:
            entry = bt.data
            if key < entry:  # 插入左节点
                if bt.left is None:
                    bt.left = BSTNode(key)
                    return
                bt = bt.left
            elif key > entry:
                if bt.right is None:
                    bt.right = BSTNode(key)
                    return
                bt = bt.right
            else:
                bt.data = key

    def iter(self, node):
        # 中序遍历可得到有序数组
        _stack = []
        if node:
            self.iter(node.left)
            _stack.append(node.data)
            self.iter(node.right)
        return _stack

    def search(self, key):
        if self.root is None:
            return False
        bt = self.root
        while bt:
            if key == bt.data:
                return True
            elif key < bt.data:
                bt = bt.left
            else:
                bt = bt.right
        return False


class HashTable:
    def __init__(self, size):
        self.item = [None] * size
        self.size = size

    def hash(self, key):
        # 哈希函数采用除留余数法
        return key % self.size

    def linear_detection(self, address):
        # 线性探测法解决冲突
        return (address + 1) % self.size

    def insert(self, key):
        address = self.hash(key)
        while self.item[address]:  # 冲突
            address = self.linear_detection(address)
        self.item[address] = key

    def search(self, key):
        start = address = self.hash(key)
        while self.item[address] != key:  # 冲突
            address = self.linear_detection(address)
            if address == start or self.item[address] is None:  # 找了一圈没有找到 or 线性探测下一地址空数据
                return False
        return True


# obj = HashTable(5)
# obj.insert(3)
# obj.insert(4)
# obj.insert(2)
# obj.insert(1)
# obj.insert(6)
# print(obj.item)
# print(obj.search(6))


class BinarySearchConvert:
    def __init__(self):
        self.array = [1, 2, 2, 3, 3, 4, 5, 6, 7, 8]

    def find_first_key(self, key):
        # 在可能有重复元素的数组中，查找第一个等于key的元素
        array = self.array.copy()
        start, end = 0, len(array)-1
        while start <= end:
            mid = start + (end - start) >> 1
            if key == array[mid]:
                if array[mid-1] != key or mid == 0:  # 左边元素不等于key 或者 已经找到最左边了
                    return mid
                end = mid - 1
            elif key < array[mid]:
                end = mid - 1
            else:
                start = mid + 1
        return None

# obj = BinarySearchConvert()
# print(obj.find_first_key(2))


class SortAlgorithm:
    def __init__(self):
        self.data = [10, 6, 12, 7, 9, -1, 20, 45]

    def bubble_sort(self):
        # 冒泡排序: 相邻的两个元素两两比较排序  O(N*N) 稳定
        array = self.data.copy()
        _len = len(array)
        for i in range(_len):
            for j in range(i+1, _len):
                if array[i] > array[j]:
                    array[i], array[j] = array[j], array[i]
        return array

    def select_sort(self):
        # 选择排序: 每次迭代会选择一个当前最小元素放到前面，用以减小交换次数 O(N*N)  非稳定
        array = self.data.copy()
        _len = len(array)
        for i in range(_len):
            min_num = i
            for j in range(i+1, _len):
                if array[min_num] > array[j]:
                    min_num = j
            if min_num != i:
                array[min_num], array[i] = array[i], array[min_num]
        return array

    def insert_sort(self):
        # 插入排序：把一个元素插入到已排好序的数组，使得整个数组有序
        # 1. 比较：和已有的元素（实际上只比较前一个元素即可）比较大小
        # 2. 后移：已有元素后移，以便插入到合适位置
        array = self.data.copy()
        _len = len(array)
        for i in range(1, _len):
            if array[i] < array[i-1]:
                # 前面的值后移
                tmp = array[i]  # 待插入元素
                j = i - 1
                while j >= 0 and array[j] > tmp:  # 后移
                    array[j + 1] = array[j]
                    j -= 1
                array[j + 1] = tmp
        return array

    def shell_sort(self):
        # 希尔排序: 增量排序，插入排序的改进版本
        array = self.data.copy()
        _len = len(array)
        increment = _len
        while increment > 1:
            increment = increment // 3 + 1
            for i in range(increment, _len):
                if array[i] < array[i-increment]:
                    tmp = array[i]
                    j = i - increment
                    while j >= 0 and array[j] > tmp:
                        array[j + increment] = array[j]
                        j -= increment
                    array[j + increment] = tmp
        return array

    def merge_sort(self, arr):
        # 归并排序
        # 归并思想: 把数组递归划分为以前的一半，直到划分为单个元素为止
        # 合并: 相邻两个子数组排序
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left, right):
        # 从小到大排序left，right子数组，合并为一个大数组
        i = j = 0
        res = []
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                res.append(left[i])
                i += 1
            else:
                res.append(right[j])
                j += 1
        res.extend(left[i:])
        res.extend(right[j:])
        return res

    def quick_sort(self, arr, start, end):
        if start < end:
            ix = self.partition(arr, start, end)
            self.quick_sort(arr, start, ix - 1)  # 递归左子序列
            self.quick_sort(arr, ix + 1, end)  # 递归右子序列
        return arr

    def partition(self, arr, start, end):
        pivot = arr[start]
        while start < end:
            while start < end and arr[end] >= pivot:
                end -= 1
            arr[start], arr[end] = arr[end], arr[start]

            while start < end and arr[start] <= pivot:
                start += 1
            arr[start], arr[end] = arr[end], arr[start]
        return start

    def heap_sort(self):
        # 堆排序
        # 堆是具有下列性质的完全二叉树：
        #   每个分支节点的值都大于或等于其左右孩子的值，称为大顶堆；
        #   每个分支节点的值都小于或等于其左右孩子的值，称为小顶堆；
        # 思想：把待排序数组构造成大订堆，此时，整个序列最大值位于根节点；把根节点和末尾元素交换；把剩余的n - 1
        # 的元素重新构造成大顶堆，反复执行即可
        # 时间复杂度：O(N * logN)
        array = self.data.copy()
        length = len(array)
        k = length // 2
        while k >= 0:  # 将原始序列构造成大顶堆，从带有子节点的父节点开始，到根节点结束
            self.heap_adjust(array, k, length - 1)
            k -= 1
        # 逆序遍历序列，不断去除根节点的值
        j = length - 1
        while j > 0:
            array[0], array[j] = array[j], array[0]  # 交换根节点最大值与末尾值
            self.heap_adjust(array, 0, j - 1)  # 剩余的n-1个元素重新构造为大顶堆
            j -= 1
        return array

    def heap_adjust(self, arr, start, end):
        tmp = arr[start]
        i = start * 2  # start节点的左右子孩子节点
        while i <= end:
            if i < end and arr[i] < arr[i + 1]:  # 找到左右子孩子中的大值
                i += 1
            if arr[i] <= tmp:
                break
            arr[i], arr[start] = arr[start], arr[i]  # 交换父节点和左右子孩子的大值
            start = i  # 递归往下执行
            i *= 2
        arr[start] = tmp

# obj = SortAlgorithm()
# print(obj.bubble_sort())
# print(obj.select_sort())
# print(obj.insert_sort())
# print(obj.shell_sort())
# print(obj.merge_sort(obj.data))
# print(obj.quick_sort(obj.data, 0, len(obj.data)-1))

from copy import deepcopy

# 0/1背包问题
# 3种策略: 最大价值，最小重量，最大单位价值
class Good:
    def __init__(self, weight, value, status):
        self.weight = weight
        self.value = value
        self.status = status  # 标记是否放入背包


class Greedy:
    def greedy(self, goods, W, strategory='strategy_max_unit_value'):  # goods是物品的集合，W是背包的空闲重量):
        result = []
        sum_weight = sum_value = 0
        goodsMat = deepcopy(goods)
        while True:
            if strategory == 'strategy_min_weight':
                s = self.strategy_min_weight(goodsMat, W)
            elif strategory == 'strategy_max_value':
                s = self.strategy_max_value(goodsMat, W)
            else:
                s = self.strategy_max_unit_value(goodsMat, W)
            if -1 == s:
                break
            result.append(goodsMat[s])
            sum_weight += goodsMat[s].weight
            sum_value += goodsMat[s].value
            W = W - goodsMat[s].weight
            goodsMat[s].status = 1
            goodsMat.pop(s)
        return result, sum_weight, sum_value

    def strategy_min_weight(self, goodsMat, W):
        # 最小重量策略
        index = -1
        min_weight = goodsMat[0].weight
        for i in range(len(goodsMat)):
            cur_goods = goodsMat[i]
            # 选择当前未选择的物品 && 物品的重量小于当前背包剩余重要 && 当前物品的重量小于最小重量的物品重量
            if cur_goods.status == 0 and cur_goods.weight <= W and cur_goods.weight < min_weight:
                index = i
                min_weight = cur_goods.weight
        return index

    def strategy_max_value(self, goodsMat, W):
        # 最大价值策略
        index = -1
        max_value = goodsMat[0].weight
        for i in range(len(goodsMat)):
            cur_goods = goodsMat[i]
            if cur_goods.status == 0 and cur_goods.weight <= W and cur_goods.value > max_value:
                index = i
                max_value = cur_goods.value
        return index

    def strategy_max_unit_value(self, goodsMat, W):
        # 最大单位价值策略
        index = -1
        max_unit_value = goodsMat[0].value / goodsMat[0].weight
        for i in range(len(goodsMat)):
            cur_goods = goodsMat[i]
            if cur_goods.status == 0 and cur_goods.weight <= W and cur_goods.value / cur_goods.weight > max_unit_value:
                index = i
                max_unit_value = cur_goods.value / cur_goods.weight
        return index


goods = [Good(35, 10, 0), Good(30, 40, 0), Good(60, 30, 0), Good(50, 50, 0), Good(40, 35, 0), Good(10, 40, 0), Good(25, 30, 0)]
g = Greedy()
result, sum_weight, sum_value = g.greedy(goods, 150, 'strategy_min_weight')
print("--------------按照取最小重量的贪心策略--------------")
print("最终总重量为：" + str(sum_weight))
print("最终总价值为：" + str(sum_value))
print("重量选取依次为：", end='')
print(result)

print("--------------按照取最大价值贪心策略--------------")
result, sum_weight, sum_value = g.greedy(goods, 150, 'strategy_max_value')
print("最终总重量为：" + str(sum_weight))
print("最终总价值为：" + str(sum_value))
print("重量选取依次为：", end='')
print(result)

print("--------------按照取单位重量的最大价值贪心策略--------------")
result, sum_weight, sum_value = g.greedy(goods, 150)
print("最终总重量为：" + str(sum_weight))
print("最终总价值为：" + str(sum_value))
print("重量选取依次为：", end='')
print(result)