#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/8/13 16:45
# Author: Hou hailun

"""
二分法
    目的: 在给定的有序数组中查找target
    前提: 数组必须有序
    框架:
        def binarySearch(nums, target):
            start, end = 0, len(nums)-1
            while start <= end:
                mid = start + (end - start) >> 1  # 好处: 可以避免2个大整数相加后溢出；右移可以加快执行速度
                if nums[mid] < target:    # 在右半子数组查找
                    start = mid + 1
                elif nums[mid] > target:  # 在左半数组查找
                    end = mid - 1
                else:                     # 找到
                    return mid
            return -1
    小技巧: 不要出现else, 而是把所有情况用elif写清楚，这样能清楚低展示所有细节
    二分的变形:
        1、target有多个，要求找到左侧边界，右侧边界，target的个数
"""