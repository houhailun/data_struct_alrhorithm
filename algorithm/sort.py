#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
模块功能：讲述各种排序算法
冒泡、选择、插入、堆、希尔、归并、快排

如何评估算法呢
    1、排序算法的执行效率
        1.1 最好情况、最坏情况、平均情况时间复杂度
        1.2 时间复杂度的系数、常数、低阶
        1.3 比较次数和交换次数
    2、排序算法的稳定性
    3、排序算法内存消耗
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

    def bubble_sort_v2(self):
        # 每次把较大的放到后面
        array = self.data.copy()
        length = len(array)
        for i in range(length):
            for j in range(length-i-1):
                if array[j] > array[j+1]:
                    array[j], array[j+1] = array[j+1], array[j]
        return array
    # 是否原地排序：冒泡算法是原地排序，空间复杂度为O(1)
    # 是否稳定排序：冒泡算法中只有交换才能改变元素的前后顺序，为了保证稳定性，在相邻元素相等时候不做交换，相同大小的元素的位置在排序前后
    #     不会改变，所以冒泡算法是稳定排序算法
    # 时间复杂度：
    #   最好情况：数组本身就是有序的，这种只需要排序一次即可，时间复杂度为O(N)
    #   最坏情况：数组是倒序的，这种需要n次冒泡排序，时间复杂度为O(N*N)
    #   平均情况：

    def select_sort(self):
        """
        选择排序：每次在当前未完成排序的数组中找当前最小值，写到当前数组最前面
        O(n*n)

        直接选择排序的基本思想是在未排序序列中找到最小（或最大）元素，存放到排序序列的起始位置。

        第一趟排序
        初始数组：[23, 12, 09, 67, 43, 32, 20, 18, 3]
        找到整个数组中的最小元素 3，并与第一个元素 23 交换位置。
        结果：[3, 12, 09, 67, 43, 32, 20, 18, 23]
        第二趟排序
        从第二个元素开始查找最小元素 9，并与第二个元素 12 交换位置。
        结果：[3, 09, 12, 67, 43, 32, 20, 18, 23]
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
    # 原地排序
    # 非稳定排序：每次在当前未完成排序的数组中找当前最小值，和前面交换位置，破坏了稳定性

    def insert_sort(self):
        """
        直接插入法：操作是将一个记录插入到已经排好序的有序表中，从而得到一个新的、记录数增1的有序表 O(n*n)
        插入排序包含两种操作：
            一种是元素的比较，当插入元素时需要把待插入元素和已有元素比较，确定插入位置
            一种是元素的移动，把插入点之后的元素后移，这样才能腾出位置来插入元素

        直接插入排序的基本思想是从第二个元素开始，将每个元素插入到已排序序列的适当位置，以保持已排序序列的有序性
        第一趟排序
        初始数组：[23, 12, 09, 67, 43, 32, 20, 18, 3]
        第一个元素 23 已经默认为有序。
        将 12 插入到已排序序列中，与 23 比较后交换位置。
        结果：[12, 23, 09, 67, 43, 32, 20, 18, 3]
        第二趟排序
        接下来将 09 插入到已排序序列中。
        09 与 12 和 23 比较后，交换位置。
        结果：[09, 12, 23, 67, 43, 32, 20, 18, 3]
        """
        array = self.data.copy()
        length = len(array)
        for i in range(1, length):
            if array[i] < array[i-1]:
                tmp = array[i]  # 待插入元素
                j = i - 1
                while j >= 0 and array[j] > tmp:  # 后移
                    array[j + 1] = array[j]
                    j -= 1
                array[j+1] = tmp

        return array
    # 是否原地排序：是原地排序，空间复杂度为O(1)
    # 是否稳定排序: 对于值相同的元素，把后面出现的元素，插入到前面出现元素的后面，因此是稳定排序
    # 时间复杂度：O(N*N)
    # 对小规模数据 或 基本有序数据较为高效

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

    def bucket_sort(self):
        # 桶排序
        # 思想：把数据分到有序的桶中，对桶内元素应该快排排序, 最后由于桶是有序的，直接根据桶的序号即可获取最终有序数组
        # 前提: 1、数据能够划分到桶中  2、数据能够平均划分到桶中
        # 解决方法：对数据多的桶继续划分
        data = self.data.copy()
        max_num = max(data)
        bucket = [0] * (max_num + 1)  # 创建元素全是0的桶

        # 把元素放到桶中，下标为val，数据为val的次数
        for val in data:
            bucket[val] += 1

        # 存储排序好的元素
        sort_nums = []
        for j in range(len(bucket)):  # 根据桶号查找
            if bucket[j] != 0:        # 该桶有元素
                for y in range(bucket[j]):  # 取指定个数的元素j
                    sort_nums.append(j)
        return sort_nums


if __name__ == "__main__":
    sort_class = Sort()
    # print(sort_class.bubble_sort())
    # print(sort_class.bubble_sort_v2())
    # print(sort_class.insert_sort())
    # print(sort_class.select_sort())
    # print(sort_class.shell_sort())
    # print(sort_class.heap_sort())
    # print(sort_class.merge_sort(sort_class.data))
    # print(sort_class.quick_sort(sort_class.data, 0, len(sort_class.data)-1))


