#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/8/14 15:00
# Author: Hou hailun

# 贪心是动态规划的特殊情况
# 贪心总使做出在当前看来最优的选择,最后得到总体最优

# 应用1: 区间调度
# 给你很多形如 [start, end] 的闭区间，请你设计一个算法，算出这些区间中最多有几个互不相交的区间。
def intervalSchedule(intvs):
    if not intvs:
        return 0
    # 贪心策略: 选择最早结束的子区间作为第一个,然后把这个子区间相交的区间删除,在剩余的区间中选择最早结束的区间,...
    intvs_sorted = sorted(intvs, key=lambda x: x[1])

    count = 1
    x_end = intvs_sorted[0][1]  # 第一个区间
    for interval in intvs_sorted:
        start = interval[0]
        if start >= x_end:  # 另一个区间的start大于等于选中的区间end,表示不相交
            count += 1
            x_end = interval[1]
    return count

# print(intervalSchedule([[2, 4], [1,3], [3,6]]))

# 应用2: 无重叠区间
# 题目: 给定一个区间的集合,找到需要移除区间的最小数量,使得剩余区间互不相交
# 思考: 上一题中已经计算了有最多几个不相交的区间, 因此本题 = n - intervalSchedule()
def eraseOverlapIntervals(intervals):
    n = len(intervals)
    return n - intervalSchedule(intervals)
# print(eraseOverlapIntervals([[2, 4], [1,3], [3,6]]))

# 应用3: 用最少的箭头射爆气球
# 本体要求至少需要多少只箭头,实际上就等于最多有多少个不相交的区间
# 这里的相交判断 start > x_end
def findMinArrowShots(intvs):
    if not intvs:
        return 0
    # 贪心策略: 选择最早结束的子区间作为第一个,然后把这个子区间相交的区间删除,在剩余的区间中选择最早结束的区间,...
    intvs_sorted = sorted(intvs, key=lambda x: x[1])

    count = 1
    x_end = intvs_sorted[0][1]  # 第一个区间
    for interval in intvs_sorted:
        start = interval[0]
        if start > x_end:  # 另一个区间的start大于选中的区间end,表示不相交
            count += 1
            x_end = interval[1]
    return count
