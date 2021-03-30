#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/8/14 11:19
# Author: Hou hailun

# 表现形式: 求最值
# 核心问题：穷举，当然是有策略的穷举，备忘录，DP Table
# 三要素：
#   1. 重叠子问题:
#   2. 最优子结构：子问题间独立，通过子问题的最优价计算原问题的最优解
#   3. 状态转移方程:
#       辅助思考状态转移方程: 明确状态 -> 定义dp数组/函数的含义 -> 明确选择 -> 明确 base case

# 应用1：斐波那契数列
def fib(n):
    # dp[i]表示第i个数, dp[i] = dp[i-1][i-2]
    dp = [None] * (n+1)
    dp[0] = 0
    dp[1] = 1
    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]
    return dp[n]

def fib_2(n):
    # 由于本题只和dp[i-1],dp[i-2]两个数有关,因此省去使用dp数组
    a, b = 0, 1
    for i in range(2, n+1):
        a, b = b, a+b
    return b

# print(fib(7))
# print(fib_2(7))

# 应用2: 凑零钱
# dp[n]为目标金额为n时至少需要dp[n]个硬币
# dp[n] = min(dp[n-coin]+1 | coin in coins), n > 0
# dp[n]=0, n=0, dp[n]=-1, n<0
def coinChange(coins, amount):
    dp = [amount+1] * (amount + 1)  # 初值默认为最大枚硬币数
    dp[0] = 0
    for i in range(1, len(dp)):
        for coin in coins:  # 内层循环 求所有子问题+1的最小值,实际上就是对每种硬币找最小
            if i - coin < 0:  # 子问题无解跳过,实际上就是当前总金额 小于 硬币面值时无法凑零钱
                continue
            dp[i] = min(dp[i], dp[i-coin]+1)
    return dp[amount] if dp[amount] != amount + 1 else -1

# print(coinChange([1, 2, 5], 23))


# 应用3:最长递增子序列LIS
# 输入: [10,9,2,5,3,7,101,18]
# 输出: 4
# 解释: 最长的上升子序列是[2,3,7,101], 子序列不一定连续
# 思路: dp[i]表示以nums[i]结尾的最长递增子序列的长度
#      dp[i]依赖于前面0~i的元素
def longestIncreseSubSeq(nums):
    res = 0
    if not nums:
        return res
    dp = [1] * len(nums)
    for i in range(1, len(nums)):
        for j in range(i):  # 内层循环: 判断nums[i]是否大于i前面的元素
            if nums[i] > nums[j]:  # nums[i]大于nums[j]表示以dp[i]等于dp[j]+1,构成长度加1的递增子序列
                dp[i] = max(dp[i], dp[j]+1)
    print(dp)
    return max(dp)  # 必须返回dp数组中的最大

# print(longestIncreseSubSeq([10,9,2,15,20,7,1]))


# 应用4: 高楼扔鸡蛋
# 你面前有一栋从 1 到 N 共 N 层的楼，然后给你 K 个鸡蛋（K 至少为 1）。现在确定这栋楼存在楼层 0 <= F <= N，在这层楼将鸡蛋扔下去，
# 鸡蛋恰好没摔碎（高于 F 的楼层都会碎，低于 F 的楼层都不会碎）。现在问你，最坏情况下，你至少要扔几次鸡蛋，才能确定这个楼层 F 呢？
# 思路:
#   状态: 当前的鸡蛋数K, 需要测试的楼层数 N. 随着测试的进行，鸡蛋个数可能减少，楼层的搜索范围会减小，这就是状态的变化。
#   选择: 选择去哪层楼扔鸡蛋
#   选择再第i层扔鸡蛋后,出现两种结果:
#       1. 鸡蛋碎了,那么鸡蛋个数K-1, 搜索层数变为1~i-1
#       2. 鸡蛋没碎,那么鸡蛋个数K不变,搜索层数变为i+1~N
def supperEggDrop(K, N):
    memo = {}

    def dp(K, N):
        """
        返回这个状态下的最优结果
        :param K: 当前状态为K个鸡蛋
        :param N: 面对N层楼
        :return: 最优结果
        """
        if K == 1:  # 只有1个鸡蛋,只能线性扫描所有楼层
            return N
        if N == 0:
            return 0
        if (K, N) in memo:  # 避免重复计算
            return memo[(K, N)]

        res = float('inf')
        # 穷举所有的可能
        for i in range(1, N+1):
            res = min(res,
                      max(dp(K-1, i-1), dp(K, N-i)) + 1)

        memo[(K, N)] = res
        return res
    return dp(K, N)

# print(supperEggDrop(5, 10))


"""
动态规划之子序列问题解题模板
子序列可以不连续,故较子数组,子串更为复杂
一.dp数组的两种思路
1. 一维的dp数组
    n = len(array)
    np = [None] * n
    for i in range(1, n):
        for j in range(i):
            dp[i] = 最值(dp[i], dp[j] + ...)
            
2. 二维的dp数组
    n = len(arr)
    dp = [[None] * n for i in range(n)]
    for i in range(n):
        for j in range(n):
            if arr[i] == arr[j]:
                dp[i][j] = dp[i][j] + ...
            else:
                dp[i][j] = 最值(...)
    涉及到两个字符串/数组的子序列
"""

import pprint
# 应用5: 最长回文子序列
# 给定一个字符串 s，找到 s 中最长的回文子串
# 思路: 因为回文子序列涉及到头尾两个指针,因此需要二维的dp数组
#   定义dp[i][j]为在子串s[i,...j]中,最长回文子序列为dp[i][j]
#   状态转移方程: dp[i][j] = dp[i+1][j-1] +2 if s[i]==s[j]
def longestPalindromeSubseq(s):
    n = len(s)
    dp = [[0] * n for i in range(n)]
    # 初始化: 单个字符是回文
    for i in range(n):
        dp[i][i] = 1

    # 从下往上遍历
    for i in range(n-1, -1, -1):
        for j in range(i+1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1] + 2
            else:
                dp[i][j] = max(dp[i+1][j], dp[i][j-1])
    pprint.pprint(dp)
    # 返回整个字符串s中的最长回文串长度
    return dp[0][n-1]

print(longestPalindromeSubseq("abcddcba"))
