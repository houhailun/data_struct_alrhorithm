#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2019/12/5 18:07
# Author: Hou hailun

# 求一个数的平方根，要求精确到小数点后6位


class Solution:
    def sqrt(self, x):
        low = 0
        mid = x // 2
        high = x
        while low <= high:  # 注意判断条件
            if mid * mid > x:
                high = mid - 1
            elif mid * mid < x:
                low = mid + 1
            else:
                return mid
            mid = (low + high) // 2
        return mid  # 向下取整


obj = Solution()
print(obj.sqrt(10))
