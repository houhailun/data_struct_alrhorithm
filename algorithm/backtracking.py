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


"""
解决一个回溯问题，实际上就是一个决策树的遍历过程，只需要思路3个问题：
    1、路径: 也就是已经做出的选择
    2、选择列表：也就是你当前可以做的选择
    3、结束条件：也就是达到决策树底层，无法再做选择的条件

任何算法的核心都是穷举，回溯算法就是一个暴力穷举法
回溯的框架：
result = []
def backtrack(路径，选择列表):
    if 满足结束条件:
        result.add(路径)
        return
    for 选择 in 选择列表:
        做选择
        backtrack(路径，选择列表)   # 这里要在选择列表中把前面的选择剔除，路径中要加上刚才的选择
        撤销选择
"""


# 全排列问题
def permute(nums):
    result = []

    def backtrack(nums, tmp):
        # nums: 选择列表, tmp: 路径
        # 结束条件，nums中的元素遍历完
        if not nums:
            result.append(tmp)
            return
        for i in range(len(nums)):
            # 做选择tmp+nms[i]
            # 选择列表剔除当前选择num[i]
            # 这里自动撤销选择，因为函数参数回调时会自动回复之前的数据
            backtrack(nums[:i] + nums[i+1:], tmp+[nums[i]])
    backtrack(nums, [])
    return result
# print(permute([1,2,3]))


# 8皇后问题
import copy
import pprint
def solveNQueens(n):
    result = []
    board = [['.'] * n for i in range(n)]  # 记录皇后位置

    def backtrack(board, row):
        # board中小于row的那些行都已经放好
        # 选择列表: 第row行的所有列都是放置皇后的选择
        # 结束条件: row超过board的最后一行
        if row == len(board):
            tmp = copy.deepcopy(board)
            result.append(tmp)
            return
        for col in range(len(board)):               # 遍历选择列列表
            if not isValid(board, row, col):  # 检查是否row行col列是否有效
                continue
            board[row][col] = 'Q'      # 做选择
            backtrack(board, row+1)    # 进行下一行决策
            board[row][col] = '.'      # 撤销选择

    def isValid(board, row, col):
        # 是否可以再board[row][col]放置皇后
        n = len(board)
        for i in range(n):  # 检查列是否有冲突
            if board[i][col] == 'Q':
                return False
        # 检查右上方是否有冲突
        for i, j in zip(range(row-1, -1, -1), range(col+1, n)):
            if board[i][j] == 'Q':
                return False

        # 检查左上方是否有皇后冲突
        for i, j in zip(range(row-1, -1, -1), range(col-1, -1, -1)):
            if board[i][j] == 'Q':
                return False
        return True

    backtrack(board, 0)
    return result

pprint.pprint(solveNQueens(4))