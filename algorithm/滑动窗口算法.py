#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/8/13 17:01
# Author: Hou hailun

# 滑动窗口技巧
#  基本逻辑
"""
def slidWindow(nums):
    window = list()
    left, right = 0, 0
    while right < len(nums):
        window.append(nums[right])
        right += 1

        while window need shrink:  # 窗口需要滑动，缩放等
            # 缩小窗口
            window.pop(nums[left])
            left += 1
"""

# 应用1：最小覆盖子串
# 给定字符串S和T，请在S中找到: 包含T所有字母的最小子串
# 输入: S = "AD0BEC0DEBANC", T = "ABC"
# 输出: "BANC"
# 思路: 在s中找到包含t中的全部字母的一个子串，顺序无所谓，这个子串要求最短子串
def findSubStr(s, t):
    if not s or not t:
        return ""

    # 暴力破解，穷举法
    # O(N*N)
    # for i in range(len(s)):
    #     for j in range(i+1, len(s)):
    #         # 若s[i:j]中包含t的所有字母，则更新答案
    #         pass

    def checkIsMatch(s, t):
        # t是否是s的子集
        return set(t).issubset(set(s))

    # 方法2: 利用滑动窗口实现
    # step1：初始化left = right = 0，把索引区间[left, right]作为滑动窗口
    # step2：不断增加right，扩大窗口[left, right], 直到窗口中的字符串满足要求: 包含了T中的所有字符
    # step3：不断增加left，缩小窗口[left,  right], 直到窗口中的字符串不满足要求: 不包含T中的所有字符
    # step4：更新最短子串
    shortestSubStr = s
    left = right = 0
    s_len, t_len = len(s), len(t)
    if s_len < t_len:
        return ""
    while right < s_len:
        for right in range(right, s_len):
            if checkIsMatch(s[left: right+1], t):  # right必须+1,因为s[left:right]的范围是从left，left+1,...,right-1的
                break

        if right == s_len-1 and not checkIsMatch(s[left: right+1], t):
            return ""

        for left in range(left, right):
            if not checkIsMatch(s[left: right+1], t):
                break

        # 更新最短子串，根据长度来比较
        shortestSubStr = min(shortestSubStr, s[left-1: right+1], key=len)
        right += 1  # 移动窗口，left已经+1，这里就不用再显示+1
    return shortestSubStr

# print(findSubStr("a", "b"))

from collections import defaultdict
# 使用框架
def minWindow(s, t):
    start = 0
    min_len = float('inf')
    left = right = 0
    match = 0     # 记录window中已经有多少字符符合要求了
    window, needs = defaultdict(int), defaultdict(int)
    for ch in t:  # needs保存t中字符及次数
        needs[ch] += 1

    while right < len(s):  # 终止条件
        # 更新窗口内容，right不断后移
        c1 = s[right]
        if c1 in needs:
            window[c1] += 1
            if window[c1] == needs[c1]:
                match += 1
        right += 1

        # 若符合要求，移动left缩小窗口
        while match == len(needs):
            # 更新最小子串的位置和长度
            if right - left < min_len:
                start = left
                min_len = right - start
            # 缩小窗口
            c2 = s[left]
            if needs.get(c2, 0):
                window[c2] -= 1
                if window[c2] < needs[c2]:  # 字符c2的次数不在符合要求
                    match -= 1
            left += 1
    if min_len == float('inf'):
        return ""
    else:
        return s[start: start+min_len]

# print(minWindow("aa", "b"))

# 应用2：找出字符串中所有字母异位词
# 异位词: 字符串的字母相同，但排列不同
def findAnagrams(s, t):
    # 和上一题类似
    res = []
    left = right = 0
    needs = defaultdict(int)
    window = defaultdict(int)
    match = 0
    for ch in t:
        needs[ch] += 1

    while right < len(s):
        c1 = s[right]
        if c1 in needs:
            window[c1] += 1
            if window[c1] == needs[c1]:
                match += 1
        right += 1

        while match == len(needs):
            if right - left == len(t) and s[left: right] != t:  # 剔除相同字符串
                res.append(left)
            c2 = s[left]
            if needs.get(c2, 0) > 0:
                window[c2] -= 1
                if window[c2] < needs[c2]:
                    match -= 1
            left += 1
    return res

def findAnagrams_2(s, t):
    # 思路: 本体窗口大小固定为3，依次从前往后滑动窗口，判断窗户内字符串和p串是否是异位词
    #   判断异位词: window[i:i+3]!=p 但是 set(window[i:i+3])==set(p)
    #   或者: 使用字典来表示每个字符的次数，次数相等，但是字符串不相等
    gap = len(t)
    res = []
    for i in range(0, len(s)-gap+1):
        sub = s[i: i+gap]
        if checkIsAnagrams(sub, t):
            res.append(i)
    return res

def checkIsAnagrams(s, t):
    if set(s) == set(t) and s != t:
        return True
    return False

# print(findAnagrams("cbaebabacd", "abc"))
# print(findAnagrams_2("cbaebabacd", "abc"))

# 应用3：无重复字符的最长子串
def lengthOfLongestSubstring(s):
    res = ''
    max_len = float('-inf')
    for ch in s:
        if ch not in res:
            res += ch
            max_len = max(max_len, len(res))
        else:
            res += ch
            res = res[res.index(ch)+1:]
    return max_len

def lengthOfLongestSubstring_window(s):
    # 滑动窗口方法
    # 使用window作为计数器记录窗口中的字符出现次数，然后先向右移动 right，当 window 中出现重复字符时，开始移动 left 缩小窗口，如此往复
    left = right = 0
    window = defaultdict(int)
    max_len = 0
    while right < len(s):
        c1 = s[right]
        window[c1] += 1
        right += 1

        # window中出现重复子串，移动left缩小窗口
        while window[c1] > 1:
            c2 = s[left]
            window[c2] -= 1
            left += 1
        max_len = max(max_len, right-left)
    return max_len

print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring_window("pwwkew"))


# 滑动窗口的抽象思想
"""
left = right = 0
while right < len(s):
    window[s[right]] += 1
    right += 1

    while valid:
        window[s[left]] -= 1
        left += 1
"""