#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2021/3/11 10:22
# Author: Hou hailun


# 算法之排序
class Sort:
    # 排序类
    def __init__(self):
        self.data = [10, 6, 12, 7, 9, -1, 20, 45]

    def bubble_sort(self):
        # 冒泡排序
        # 思想：两两对比，把小的放到前面
        # O(N*N)  稳定排序 原址排序
        arr = self.data.copy()
        arr_len = len(arr)
        for i in range(arr_len):
            for j in range(arr_len):
                if arr[i] < arr[j]:  # 后面大于前面元素，交换
                    arr[i], arr[j] = arr[j], arr[i]
        return arr

    def bubble_sort_better(self):
        # 减小比较次数
        arr = self.data.copy()
        arr_len = len(arr)
        for i in range(arr_len):
            for j in range(0, arr_len-1-i):
                if arr[j] > arr[j+1]:
                    arr[i], arr[j+1] = arr[j+1], arr[i]
        return arr

    def select_sort(self):
        # 选择排序
        # 思想：每轮选择当前最小元素放到前面
        # O(N*N)  非稳定排序 原址排序
        arr = self.data.copy()
        arr_len = len(arr)
        for i in range(arr_len):
            min_ix = i
            for j in range(i+1, arr_len):  # 在
                if arr[j] < arr[min_ix]:
                    min_ix = j
            if min_ix != i:
                arr[i], arr[min_ix] = arr[min_ix], arr[i]
        return arr

    def insert_sort(self):
        # 插入排序
        # 思想：操作是将一个记录插入到已经排好序的有序表中，从而得到一个新的、记录数增1的有序表 O(n*n)
        #         插入排序包含两种操作：
        #             一种是元素的比较，当插入元素时需要把待插入元素和已有元素比较，确定插入位置
        #             一种是元素的移动，把插入点之后的元素后移，这样才能腾出位置来插入元素
        arr = self.data.copy()
        arr_len = len(arr)
        for i in range(1, arr_len):  # 从位置1开始
            if arr[i] < arr[i-1]:    # 后面比前面小，则后移前面的元素，确定i元素插入的位置
                tmp = arr[i]
                j = i - 1
                while j >= 0 and arr[j] > tmp:  # 把前面大于待插入元素的数据后移
                    arr[j+1] = arr[j]
                    j -= 1
                arr[j+1] = tmp
        return arr

    def shell_sort(self):
        # 希尔排序  插入排序的改进版
        # 思想：设置一个间隔，使得数组逻辑上隔离为多个子数组，对每个子数组使用插入排序
        arr = self.data.copy()
        arr_len = len(arr)
        increment = arr_len
        while increment > 1:
            increment = increment // 3 + 1
            for i in range(increment, arr_len):
                if arr[i] < arr[i-increment]:
                    tmp = arr[i]
                    j = i - increment
                    while j >= 0 and arr[j] > tmp:
                        arr[j+increment] = arr[j]
                        j -= increment
                    arr[j+increment] = tmp
        return arr

    def quick_sort(self, arr, start, end):
        if start >= end:
            return
        index = self.partitions(arr, start, end)
        self.quick_sort(arr, start, index - 1)  # 递归左子序列
        self.quick_sort(arr, index + 1, end)    # 递归右子序列
        return arr

    def partitions(self, arr, start, end):
        # 一轮后，小于key的在前面，大于key的在后，返回key的位置
        key = arr[start]
        while start < end:
            while start < end and arr[end] >= key:
                end -= 1
            arr[start], arr[end] = arr[end], arr[start]
            while start < end and arr[start] <= key:
                start += 1
            arr[start], arr[end] = arr[end], arr[start]
        return start

    def merge_sort(self, arr):
        if not arr or len(arr) <= 1:
            return arr
        # 两两划分为多个子序列，然后合并子序列
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])  # 递归划分
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left_arr, right_arr):
        i = j = 0
        tmp = []
        while i < len(left_arr) and j < len(right_arr):
            if left_arr[i] < right_arr[j]:
                tmp.append(left_arr[i])
                i += 1
            else:
                tmp.append(right_arr[j])
                j += 1
        tmp += left_arr[i:]
        tmp += right_arr[j:]
        return tmp


class Search:
    # 搜索算法类
    def __init__(self):
        self.data = [10, -3, 34, 56, 97, 100]

    def sequent_search(self, key):
        # 顺序搜索
        for num in self.data:
            if num == key:
                return True
        return False

    def binary_search(self, key):
        # 二分搜索，前提是数据有序
        arr = self.data.copy()
        arr.sort()
        start, end = 0, len(arr)-1
        while start <= end:
            mid = start + (end - start) // 2
            if arr[mid] > key:
                end = mid - 1
            elif arr[mid] < key:
                start = mid + 1
            else:
                return True
        return False


# 贪心算法
# 0/1 背包问题
#  具体实例：一个背包，最多能承载重量为 W=150 的物品，现在有 7 个物品（物品不能分割成任意大小），编号为 1~7，
#       重量分别是 wi=[35、30、60、50、40、10、25]，价值分别是 pi=[10、40、30、50、35、40、30]，
#       现在从这 7 个物品中选择一个或多个装入背包，要求在物品总重量不超过 W 的前提下，所装入的物品总价值最高。

# 分析
# 1、目标函数：sum(Pi)最大，即装入的物品总价值最高
# 2、约束条件：不能超过背包的承载重量
# 3、贪心策略：选择重量最轻的、选择价值最高的、选择单位价值最高的
from copy import deepcopy
class Good:
    # 商品类
    def __init__(self, weight, value, status):
        self.weight = weight
        self.value = value
        self.status = status  # 标记商品是否被选择


class Greddy:
    def greddy(self, goods, W, strategory='strategy_max_unit_value'):
        """
        0/1背包问题
        :param goods: 列表，包含商品重量，价值，是否被选择
        :param W: 背包承载总重量
        :param strategory: 贪心策略
        :return:
        """
        result = []  # 记录所选择的物品
        sum_weight = sum_value = 0.0
        goodsMat = deepcopy(goods)
        while True:
            # 每种策略 一次只选择当前最合适的一个物品
            if strategory == 'strategy_min_weight':
                s = self.strategy_min_weight(goodsMat, W)
            elif strategory == 'strategy_max_value':
                s = self.strategy_max_value(goodsMat, W)
            else:
                s = self.strategy_max_unit_value(goodsMat, W)

            if s == -1:
                break

            sum_weight += goodsMat[s].weight    # 累计重量总和，价值总和
            sum_value += goodsMat[s].value
            result.append(goodsMat[s].weight)
            W = W - goodsMat[s].weight  # 更新当前背包剩余的承载重量
            goodsMat[s].status = 1      # 标记物品s已被选择

        return result, sum_weight, sum_value

    def strategy_max_unit_value(self, goodsMat, W):
        # 最大单位价值策略
        index = -1
        max_unit_value = -float('inf')
        for i in range(len(goodsMat)):
            goods = goodsMat[i]
            if goods.status == 0 and goods.weight <= W and goods.value / goods.weight > max_unit_value:
                index = i
                max_unit_value = goods.value / goods.weight

        return index


    def strategy_min_weight(self, goodsMat, W):
        # 最小重量贪心
        index = -1
        min_weight = float('inf')
        for i in range(len(goodsMat)):
            # 该商品没有被选择 & 该商品重量小于等于背包承载重量 & 该商品重量小于最小重量
            if goodsMat[i].status == 0 and goodsMat[i].weight <= W and min_weight > goodsMat[i].weight:
                index = i
                min_weight = goodsMat[i].weight

        return index

    def strategy_max_value(self, goodsMat, W):
        # 最大价值贪心
        index = -1
        max_value = -float('inf')
        for i in range(len(goodsMat)):
            goods = goodsMat[i]
            # 该商品没有被选择 & 该商品价值大于最大价值 & 该商品重量小于等于背包承载重量
            if goods.status == 0 and goods.value > max_value and goods.weight <= W:
                index = i
                max_value = goods.value

        return index

if __name__ == "__main__":
    # obj = Sort()
    # print(obj.bubble_sort())
    # print(obj.bubble_sort_better())
    # print(obj.select_sort())
    # print(obj.insert_sort())
    # print(obj.shell_sort())
    # print('quick_sort')
    # print(obj.quick_sort(obj.data.copy(), 0, len(obj.data)-1))
    # print('merge_sort')
    # print(obj.merge_sort(obj.data))

    # obj = Search()
    # print(obj.sequent_search(97))
    # print(obj.binary_search(97))
    #
    # goods = [Good(35, 10, 0), Good(30, 40, 0), Good(60, 30, 0), Good(50, 50, 0),
    #          Good(40, 35, 0), Good(10, 40, 0), Good(25, 30, 0)]
    # greedy = Greddy()
    # print(greedy.greddy(goods, 150, strategory='strategy_max_unit_value'))
    # print(greedy.greddy(goods, 150, strategory='strategy_min_weight'))
    # print(greedy.greddy(goods, 150, strategory='strategy_max_value'))