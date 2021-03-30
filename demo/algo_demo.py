#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/9/17 13:35
# Author: Hou hailun

class Search:
    def __init__(self, nums):
        self.nums = nums
        self.found = False

    def sequence_search(self, key):
        for ix, num in enumerate(self.nums):
            if key == num:
                self.found = True
                return ix
        return -1

    def binary_search(self, key):
        nums = self.nums.copy()
        nums.sort()
        if not nums:
            self.found = False
            return None
        start, end = 0, len(nums)-1
        while start <= end:
            mid = start + (end - start) // 2
            if nums[mid] == key:
                self.found = True
                return mid
            elif nums[mid] < key:
                start = mid + 1
            elif nums[mid] > key:
                end = mid - 1
            else:
                pass
        self.found = False
        return None


class HashTable:
    # 哈希表是键值对存储
    def __init__(self, size):
        self.elem = [None] * size  # 哈希表
        self.count = size          # 最大表长

    def hash(self, key):
        # 哈希函数：除数留余法
        return key % self.count

    def insert(self, key):
        address = self.hash(key)
        while self.elem[address]:  # 冲突
            address = (address + 1) % self.count  # 线性探测法解决冲突问题
        self.elem[address] = key

    def search(self, key):
        # 哈希表中查找key
        start = address = self.hash(key)
        while self.elem[address] != key:
            address = (address + 1) % self.count
            # 没有找到 或者 循环了一圈
            if not self.elem[address] or start == address:
                return False
        return True


class BinarySearchConvert:
    def __init__(self):
        self.nums = [1,1,2,2,2,2,3,5,6]

    def find_first_key(self, key):
        if not self.nums:
            return None
        start, end = 0, len(self.nums)-1
        while start <= end:
            mid = start + (end - start) // 2
            if self.nums[mid] == key:
                if self.nums[mid-1] != key or mid == 0:
                    return mid
                else:
                    end = mid - 1
            elif self.nums[mid] > key:
                end = mid - 1
            else:
                start = mid + 1
        return None

    def find_last_key(self, key):
        if not self.nums:
            return None
        start, end = 0, len(self.nums)-1
        while start <= end:
            mid = start + (end - start) // 2
            if self.nums[mid] == key:
                if mid == len(self.nums)-1 or self.nums[mid+1] != key:
                    return mid
                else:
                    start = mid + 1
            elif self.nums[mid] > key:
                end = mid - 1
            else:
                start = mid + 1

    def find_first_num_large_equal_key(self, key):
        # 找出第一个大于等于key的元素
        if not self.nums:
            return None
        start, end = 0, len(self.nums)-1
        while start <= end:
            mid = start + (end - start) // 2
            if self.nums[mid] >= key:
                # 找到第一个元素 or 前面的元素小于key
                if mid == 0 or self.nums[mid-1] < key:
                    return mid
                else:
                    end = mid - 1
            else:
                start = mid + 1


class SortAlgo:
    def __init__(self, nums):
        self.nums = nums

    def bubble_sort(self):
        # 冒泡：相邻两两比较
        # O(N*N) 稳定算法
        nums = self.nums.copy()
        if not nums:
            return None
        nums_len = len(nums)
        # 遍历一次，把最小元素放到队首
        for i in range(nums_len-1):
            for j in range(i+1, nums_len):
                if nums[i] > nums[j]:
                    nums[i], nums[j] = nums[j], nums[i]
        return nums

    def select_sort(self):
        # 选择排序: 每次在当前未完成排序的数组中找当前最小值，写到当前数组最前面
        # O(N*N)  非稳定
        nums = self.nums.copy()
        nums_len = len(nums)
        for i in range(nums_len):
            mininum = i  # 标记最小为i，然后遍历剩余的元素，标记当前的最小值
            for j in range(i+1, nums_len):
                if nums[j] < nums[mininum]:
                    mininum = j
            nums[i], nums[mininum] = nums[mininum], nums[i]
        return nums

    def insert_sort(self):
        # 插入排序: 操作是将一个记录插入到已经排好序的有序表中，从而得到一个新的、记录数增1的有序表
        # O(N*N)  稳定
        nums = self.nums.copy()
        nums_len = len(nums)
        for i in range(1, nums_len):
            if nums[i] < nums[i-1]:  # 后面的小于前面的
                tmp = nums[i]
                j = i-1
                # 前面大于待插入值的元素后移
                while j >= 0 and nums[j] > tmp:
                    nums[j+1] = nums[j]
                    j -= 1
                nums[j + 1] = tmp
        return nums

    def shell_sort(self):
        # 希尔排序：增量递减排序，属于插入排序的改进版
        nums = self.nums.copy()
        increment = nums_len = len(nums)
        while increment > 1:  # 终止条件: 增量为1
            increment = increment // 3 + 1
            for i in range(increment, nums_len):
                if nums[i] < nums[i - increment]:
                    tmp = nums[i]
                    j = i - increment
                    while j >= 0 and nums[j] > tmp:
                        nums[j+increment] = nums[j]
                        j -= increment
                    nums[j+increment] = tmp
        return nums

    def merge_sort(self, arr):
        # 归并排序：利用归并思想，两两划分-> 两两排序合并
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.merge_sort(arr[: mid])
        right = self.merge_sort(arr[mid:])
        return self.merge(left, right)

    def merge(self, left_arr, right_arr):
        # 合并两个子数组
        tmp = []
        i = j = 0
        len_left, len_right = len(left_arr), len(right_arr)
        while i < len_left and j < len_right:
            if left_arr[i] <= right_arr[j]:
                tmp.append(left_arr[i])
                i += 1
            else:
                tmp.append(right_arr[j])
                j += 1
        tmp += left_arr[i:]
        tmp += right_arr[j:]
        return tmp

    def quick_sort(self, arr, start, end):
        # 通过一趟排序将待排记录分割成独立的两部分，其中一部分记录的关键字均比另一部分记录的关键字小，然后分别对这两部分继续进行排序，以达到整个记录集合的排序目的
        if end > start:
            index = self.partitions(arr, start, end)
            self.quick_sort(arr, start, index-1)  # 递归左子序列
            self.quick_sort(arr, index+1, end)    # 递归右子序列
        return arr

    def partitions(self, arr, start, end):
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
    # obj = Search([1,3,4,7,9, 14])
    # print(obj.sequence_search(9))
    # print(obj.binary_search(9))
    #
    # obj = BinarySearchConvert()
    # print(obj.find_first_key(2))
    # print(obj.find_last_key(2))

    obj = SortAlgo([5, -3, 9, 4, 1, -18])
    # print(obj.bubble_sort())
    # print(obj.select_sort())
    # print(obj.insert_sort())
    # print(obj.shell_sort())
    # print(obj.merge_sort([5, -3, 9, 4, 1, -18]))
    print(obj.quick_sort([5, -3, 9, 4, 1, -18], 0, 5))
