#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2019/12/23 18:49
# Author: Hou hailun

# 分治算法
# 如何理解分治算法
#   1、核心思想就是分而治之，也就是把原问题划分成N个规模较小，并且结构与原问题相似的子问题，递归地解决这些子问题，然后再合并其结果，就得到原问题的解
#   2、分治和递归的区别：
#       分治算法是一种处理问题的思想，递归则是具体的编程技巧。实际上分治法一般适合用递归来实现
#   3、分治法的条件：
#       3.1 原问题和分解成的小问题具有相同的模式
#       3.2 原问题分解成的小问题可以独立求解，子问题之间没有相关性，这个动态规划不同
#       3.3 具有分解终止条件
#       3.4 可以将子问题合并成原问题


class Solution:
    def __init__(self):
        self.count = 0

    def mergeSortCounting(self, nums, low, high):
        # 归并排序
        if low >= high:
            return

        mid = (low + high) // 2
        self.mergeSortCounting(nums, low, mid)
        self.mergeSortCounting(nums, mid+1, high)
        self.merge(nums, low, mid, high)

    def merge(self, nums, low, mid, high):
        i = low
        j = mid + 1
        k = 0
        tmp = [None] * (high-low+1)
        while i <= mid and j <= high:
            if nums[i] <= nums[j]:  # 左半数组比右半数组小，则当前没有逆序对
                tmp[k] = nums[i]
                k += 1
                i += 1
            else:  # 统计 mid-low之间，比nums[j]大的元素个数
                self.count += (mid - i + 1)
                tmp[k] = nums[j]
                k += 1
                j += 1

        while i <= mid:
            tmp[k] = nums[i]
            k += 1
            i += 1

        while j <= high:
            tmp[k] = nums[j]
            k += 1
            j += 1

        for i in range(high-low):  # 从tmp拷贝回nums
            nums[low+i] = tmp[i]


if __name__ == "__main__":
    obj = Solution()
    obj.mergeSortCounting([1, 5, 6, 2, 3, 4], 0, 5)
    print(obj.count)