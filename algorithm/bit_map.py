#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/1/4 10:17
# Author: Hou hailun

# 位图：常用的数据结构，比如用于Bloom Filter中、用于无重复整数的排序等等。bitmap通常基于数组来实现，数组中每个元素可以看成是一系列二进制数，所有元素组成更大的二进制集合。对于Python来说，整数类型默认是有符号类型，所以一个整数的可用位数为31位。
# 位图适合数字的范围不是很大的情况；
# 如果数字范围很大，需要使用布隆过滤器: 位图+hash

class BitMap:
    # 类图
    def __init__(self, max):
        """ 初始化BitMap """
        self.size = self.calc_elem_index(max, True)  # 位数max / 31，向上取整
        self.array = [0] * self.size                 # 确定数组大小后，创建数组

    def calc_elem_index(self, num, up=False):
        """
        计算num位于数组的第x个元素上
        如果要将一个整数保存进这个数组，首先需要知道保存在这个数组的第几个元素之上，然后要知道是在这个元素的第几位上。因此计算索引分为：
            计算在数组中的索引
            计算在数组元素中的位索引
        up为True则为向上取整, 否则为向下取整
        """
        if up:
            return int((num + 31 - 1) / 31)  # 向上取整
        return num // 31  # 向下取整

    def calc_bit_index(self, num):
        # 计算在数组元素中的位索引
        return num % 31

    def set(self, num):
        # 置1操作，将某位置为1则表示在此为存储了数据
        elem_index = self.calc_elem_index(num)
        byte_index = self.calc_bit_index(num)
        elem = self.array[elem_index]
        self.array[elem_index] = elem | (1 << byte_index)

    def clean(self, i):
        # 清0操作，即丢弃已存储的数据
        elem_index = self.calc_elem_index(i)
        byte_index = self.calc_bit_index(i)
        elem = self.array[elem_index]
        self.array[elem_index] = elem & (~(1 << byte_index))

    def get(self, i):
        # 获取元素i
        elem_index = self.calc_elem_index(i)  # 整除，否则为浮点值
        byte_index = self.calc_bit_index(i)
        if self.array[elem_index] & (1 << byte_index):
            return True
        return False


if __name__ == "__main__":
    # 不重复数组的排序
    MAX = 879
    shuffle_array = [45, 2, 78, 35, 67, 90, 879, 0, 340, 123, 46]
    result = []

    bitmap = BitMap(MAX)
    for num in shuffle_array:
        bitmap.set(num)

    for i in range(MAX + 1):
        if bitmap.get(i):
            result.append(i)

    print('原始数组为:    %s' % shuffle_array)
    print('排序后的数组为: %s' % result)
