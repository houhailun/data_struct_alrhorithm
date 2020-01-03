#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2019/12/24 15:35
# Author: Hou hailun

# 回溯算法
# 思想：枚举所有的解，找到满足期望的解；把问题求解的过程分为多个阶段，每个阶段，都会面对一个岔路口，我们先随意选一条路走，
#       当发现这条路走不通的时候（不符合期望的解），就回退到上一个岔路口，另选一种走法继续走

# 应用1：8皇后问题
# 问题描述：8*8的棋盘，放8个棋子，每个棋子所在的行、列、对角线都不能有另一个棋子
# 思路：把问题分为8个阶段，一次把8个棋子放到第1行、第2行，。。。第8行。在放的过程中，不停检查当前的方法是否满足要求。
#       如果满足则跳到下一行继续放棋子，不满足就再换一种方法，继续尝试

class Solution:
    def __init__(self):
        self.result = [None] * 8  # 下标表示行，值表示列

    def cal_8_queens(self, row):
        if row == 8:  # 8个棋子都放好了
            self.print_queens()
            return
        # 对每一行的每一列判断是否可行
        for column in range(8):
            if self.is_ok(row, column):  # 满足要求
                self.result[row] = column  # 第row行的棋子放到column列
                self.cal_8_queens(row+1)  # 考察下一行
        return

    def is_ok(self, row, column):
        # 判断row行column列放置是否合适
        leftup = column - 1
        rightup = column + 1
        for i in range(row-1, -1, -1):    # 逐行网上考察每一行
            if self.result[i] == column:  # 第i行的column列有棋子
                return False
            if leftup >= 0 and self.result[i] == leftup:  # 左上对角线，第i行leftup列有棋子
                return False
            if rightup < 8 and self.result[i] == rightup:  # 右上对角线，第i行rightup列有棋子
                return False

            leftup -= 1
            rightup += 1
        return True