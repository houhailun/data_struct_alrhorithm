#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
模块功能：讲述各种排序算法
"""


class Sort(object):
    """排序算法类"""
    def __init__(self):
        self.data = [10, 6, 12, 7, 9, -1, 20, 45]

    def bubble_sort(self):
        """冒泡排序：相邻的两个比较，较小的放在前面 O（n*n）"""
        array = self.data.copy()  # 避免更改self.data
        length = len(array)
        for i in range(length):
            for j in range(length):
                if array[j] > array[i]:
                    array[i], array[j] = array[j], array[i]  # 交换

        return array

    def select_sort(self):
        """
        选择排序：每次在当前未完成排序的数组中找当前最小值，写到当前数组最前面
        O(n*n)
        """
        array = self.data.copy()
        length = len(array)
        for i in range(length):
            mininum = i
            for j in range(i+1, length):
                if array[mininum] > array[j]:
                    mininum = j
            if mininum != i:
                array[mininum], array[i] = array[i], array[mininum]

        return array

    def insert_sort(self):
        """直接插入法：操作是将一个记录插入到已经排好序的有序表中，从而得到一个新的、记录数增1的有序表 O(n*n)"""
        array = self.data.copy()
        length = len(array)
        for i in range(1, length):
            if array[i] < array[i-1]:
                tmp = array[i]
                j = i - 1
                while j >= 0 and array[j] > tmp:  # 后移
                    array[j + 1] = array[j]
                    j -= 1
                array[j+1] = tmp

        return array

    def shell_sort(self):
        """
        希尔排序：又称增量减小法，是插入排序的改进版本
        其核心思想是将原数据集合分割成若干个子序列，然后再对子序列分别进行直接插入排序，使子序列基本有序，最后再对全体记录进行一次直接插入排序
        这里最关键的是跳跃和分割的策略，也就是我们要怎么分割数据，间隔多大的问题。通常将相距某个“增量”的记录组成一个子序列，这样才能保证在子序列内分别进行直接插入排序后得到的结果是基本有序而不是局部有序。
        一般都是：increment = increment/3+1 来确定“增量”的值
        时间复杂度：O(n^(3/2))
        """
        array = self.data.copy()
        length = len(array)
        increment = length
        while increment > 1:
            increment = increment // 3 + 1
            for i in range(increment, length):
                if array[i] < array[i - increment]:
                    tmp = array[i]
                    j = i - increment
                    while j >= 0 and array[j] > tmp:
                        array[j+increment] = array[j]
                        j -= increment
                    array[j + increment] = tmp

        return array

    def heap_adjust(self, arr, start, end):
        tmp = arr[start]
        i = start * 2  # start节点的左右子孩子节点
        while i <= end:
            if i < end and arr[i] < arr[i+1]:  # 找到左右子孩子中的大值
                i += 1
            if arr[i] <= tmp:
                break
            arr[i], arr[start] = arr[start], arr[i]  # 交换父节点和左右子孩子的大值
            start = i  # 递归往下执行
            i *= 2
        arr[start] = tmp

    def heap_sort(self):
        """
        推排序：利用堆进行排序
        堆是具有下列性质的完全二叉树：
            每个分支节点的值都大于或等于其左右孩子的值，称为大顶堆；
            每个分支节点的值都小于或等于其左右孩子的值，称为小顶堆；
        思想：把待排序数组构造成大订堆，此时，整个序列最大值位于根节点；把根节点和末尾元素交换；把剩余的n-1的元素重新构造成大顶堆，反复执行即可
        时间复杂度：O(N*logN)
        """
        array = self.data
        length = len(array)
        k = length // 2
        # 将原始序列构造成大顶堆，从带有子节点的父节点开始，到根节点结束
        while k >= 0:
            self.heap_adjust(array, k, length-1)
            k -= 1
        # 逆序遍历序列，不断去除根节点的值
        j = length - 1
        while j > 0:
            array[0], array[j] = array[j], array[0]  # 交换根节点最大值与末尾值
            self.heap_adjust(array, 0, j-1)          # 剩余的n-1个元素重新构造为大顶堆
            j -= 1

        return array

    def merge_sort(self, arr):
        """
        归并排序：分而治之思想，把序列分割为n个子序列，达到子序列有序，然后两两合并排序
        时间复杂度：O(N*logN) 递归拆分的时间复杂度是logN 然而，进行两个有序数组排序的方法复杂度是N该算法的时间复杂度是N*logN
        合并方法：需要辅助序列tmp，相邻两个序列，首先比较第一个元素，把较小值放到tmp，然后在进行比较
        """
        # print(arr)
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[:mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, start, end):
        tmp = []
        i = j = 0
        len_start = len(start)
        len_end = len(end)
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
        """
        快速排序核心思想：通过一趟排序将待排记录分割成独立的两部分，其中一部分记录的关键字均比另一部分记录的关键字小，然后分别对这两部分继续进行排序，以达到整个记录集合的排序目的
        时间复杂度:O(N*logN)
        """
        if end > start:
            index = self.partitions(arr, start, end)
            self.quick_sort(arr, start, index-1)  # 递归左子序列
            self.quick_sort(arr, index+1, end)    # 递归右子序列
        return arr

    def partitions(self, arr, start, end):
        """快排的核心函数"""
        key = arr[start]
        while start < end:
            while start < end and arr[end] >= key:
                end -= 1
            arr[start], arr[end] = arr[end], arr[start]

            while start < end and arr[start] <= key:
                start += 1
            arr[start], arr[end] = arr[end], arr[start]

        return start


if __name__ == "__main__":
    sort_class = Sort()
    print(sort_class.bubble_sort())
    print(sort_class.insert_sort())
    print(sort_class.select_sort())
    print(sort_class.shell_sort())
    print(sort_class.heap_sort())
    print(sort_class.merge_sort(array))
    print(sort_class.quick_sort(array, 0, len(array)-1))


