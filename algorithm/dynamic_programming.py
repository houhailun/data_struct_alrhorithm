#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2019/12/27 17:01
# Author: Hou hailun

# 动态规划
# 思想：把问题分解为多个阶段，每个阶段对应一个决策。我们记录每一个阶段可达的状态集合，然后通过当前阶段的状态集合，
#       来推导下一个阶段的状态集合，动态地往前推进。

# 0/1背包


class Solution:
    def __init__(self):
        self.maxW = -1                 # 书包实际装物品的最大重量
        self.weight = [2, 2, 4, 6, 3]  # 物品重要
        self.n = 5                     # 物品个数
        self.w = 9                     # 背包承受的最大重量
        self.mem = [[None] * 10] * 5   # 备忘录

    def f(self, i, cw):
        if cw == self.w or i == self.n:  # cw==w表示装满了，i==self.n表示物品都考察完了
            if cw > self.maxW:
                self.maxW = cw
            return
        if self.mem[i][cw]:  # 重复状态
            return
        self.mem[i][cw] = True  # 记录(i,cw)状态
        self.f(i+1, cw)  # 选择不装第i个物品
        if cw + self.weight[i] <= self.w:  # 选择装第i个物品
            self.f(i+1, cw+self.weight[i])

# 应用一：数塔
# 思路：
#       1、大事化小：把原始问题分为若干子问题，dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + a[i][j]
#       2、小事化了：初始化，dp[1][1] = a[1][1]
def counting_tower(nums):
    if not nums:
        return -1
    length = len(nums)
    dp = [[None] * length] * length

    # 初始化
    dp[0][0] = nums[0][0]
    for i in range(0, length):
        for j in range(0, i):
            dp[i][i] = max(dp[i-1][j-1], dp[i-1][j]) + nums[i][j]


# 应用2：斐波那契
def fibonacci(n):
    # 递归形式
    # if n <= 0:
    #     return 0
    # if n == 1 or n == 2:
    #     return 1
    # return fibonacci(n-1) + fibonacci(n-2)

    # 辗转相加法
    # if n <= 0:
    #     return 0
    # a, b = 0, 1
    # for i in range(2, n+1):
    #     a, b = b, a+b
    # return b

    # 动态规划法：保留中间的数据
    dp = [0] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    print(dp)
    return dp[n]

# print(fibonacci(10))

# 应用3：变态青蛙跳台阶
# 青蛙一次可以跳1级台阶，也可以跳2级台阶，...,它也可以跳到N级台阶，那么N级台阶有多少种方法？
# 状态：f(i)标识一共i级台阶，青蛙跳台阶的方法
# 状态递推：
#   第一步：跳1，2，。。。，n级台阶
#   第二步：跳f(i-1),f(i-2),...f(0)级台阶
#   f(i) = 2*f(i-1)   f(1)=1
def jumpFloor(number):
    if number <= 0:
        return 0

    total = 1
    for i in range(1, number):
        total = 2 * total
    return total

# print(jumpFloor(2))

# 应用三：矩阵覆盖
# 状态递推：
#   第一步：竖着放一个 f(i-1) 或者 横着放一个f(i-2)
#   f(i) = f(i-1) + f(i-2)
def rectCover(number):
    if number <= 0:
        return 0
    if number == 1:
        return 1
    if number == 2:
        return 2

    dp = [0] * (number+1)
    dp[0], dp[1], dp[2] = 0, 1, 2
    for i in range(3, number+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[number]

# 应用4：最大连续数列和
def maxSeqSub(nums):
    if nums is None:
        return

    # cur_sum = max_sum = 0
    # for num in nums:
    #     if cur_sum < 0:
    #         cur_sum = num
    #     else:
    #         cur_sum = cur_sum + num
    #     if cur_sum > max_sum:
    #         max_sum = cur_sum
    # return max_sum

    # 动态规划


# print(maxSeqSub([6, -3, 7, -15, 1, 22]))

#  应用5：triangle，找最小路径和
# [
# [2],
# [3,4],
# [6,5,7],
# [4,1,8,3]
# ]
# 分析：f(i,j) 表示从(0,0)到(i,j)的最小路径和
#   状态转移方程: f(i,j) = min(f(i-1, j-1), f(i-1,j)) + a[i][j]
#   最左边：j=0，则f(i,j) = f(i-1,j) + a[i][j]
#   最右边，j == i，则f(i,j) = f(i-1,j-1) + a[i][j]
#   初始化: f(0,0) = a[i][j]
#   返回结果：f(n-1,0) f(n-1,1),...,f(n-1,i)
def mininumTotal(nums, n):
    if nums is None:
        return 0
    min_sum = [[0] * n] * n
    min_sum[0][0] = nums[0][0]  # 初始化

    # 地推
    for i in range(n):
        for j in range(i+1):
            if j == 0:  # 左边界
                min_sum[i][j] = min_sum[i-1][j] + nums[i][j]
            elif j == i:  # 右边界
                min_sum[i][j] = min_sum[i-1][j-1] + nums[i][j]
            else:
                min_sum[i][j] = min(min_sum[i - 1][j - 1], min_sum[i - 1][j])
                min_sum[i][j] = min_sum[i][j] + nums[i][j]

    # 最小路径
    print(min_sum)
    result = min_sum[n-1][0]
    for i in range(n):
        result = min(result, min_sum[n-1][i])
    return result


# print(mininumTotal([[2], [3, 4], [6,5,7], [4,1,1,3]], 4))

# 应用6：棋盘从左上角走到右下角的最小路径，只能往下或往右走
# 状态转移方程: f(i)(j) = min(f(i-1,j), f(i,j-1)) + num[i][j]
# 第一行和第一列特殊，需要单独初始化
def minDist(nums, m, n):
    if nums is None:
        return 0
    if m <= 0 or n <= 0:
        return 0

    dp = [[0] * n] * m        # m*n
    dp[0][0] = nums[0][0]     # 初始化
    for i in range(1, m):     # 初始化第一列
        dp[i][0] = dp[i-1][0] + nums[i][0]
    for i in range(1, n):     # 初始化第一行
        dp[0][i] = dp[0][i-1] + nums[0][i]

    # 动态规划递推
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + nums[i][j]
    print(dp)
    return dp[m-1][n-1]


nums = [[1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 2, 3, 1],
        [8, 5, 7, 2]]

# print(minDist(nums, 4, 4))


# 应用7：使用编辑距离来量化两个字符串的相似度
# 编辑距离：将一个字符串转化为另一个字符串，需要的最少编辑操作次数。编辑距离越大，说明两个字符串的相似程度越小
#   编辑距离有多种计算方式：莱温斯坦距离(允许增加、删除、替换字符)，最长公共字串长度(允许增加、删除字符)
#   莱温斯坦距离：表示2个字符串差异的大小
#   最长公共字串长度：表示2个字符串相似程度的大小

# 回溯法
import sys
class Solution:
    def __init__(self):
        self.a = 'mitcmu'
        self.b = 'mtacnu'
        self.m = 6
        self.n = 6
        self.min_dist = sys.maxsize

    def lwstBT(self, i, j, edist):
        # 有1个字符串已经遍历完
        if i == self.n or j == self.m:
            if i < self.n:  # i指向的字符串还有(n-i)个编辑距离
                edist += (self.n-i)
            if j < self.m:
                edist += (self.m-j)
            if edist < self.min_dist:
                self.min_dist = edist
            return
        # 2个字符匹配
        if self.a[i] == self.b[j]:
            self.lwstBT(i+1, j+1, edist)
        else:
            self.lwstBT(i + 1, j, edist+1)  # 删除a[i]或者b[j]前添加一个字符
            self.lwstBT(i, j + 1, edist+1)  # 删除b[j[或者a[i]前添加一个字符
            self.lwstBT(i + 1, j + 1, edist+1)  # 将a[i]和b[j]替换为相同字符

    def lwst_dp(self):
        # 动态规划法
        # 状态转移方程：
        pass

obj = Solution()
obj.lwstBT(0, 0, 0)
print(obj.min_dist)