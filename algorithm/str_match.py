#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2019/12/18 16:31
# Author: Hou hailun
# 字符串匹配


class StrMatch:
    # 字符串匹配算法
    def bf(self, s, p, pos=0):
        """
        bf算法，也叫暴力匹配算法，朴素匹配算法
        思想：在主串中，检查起始位置分别是0，1，2，...，n-m长度为m的n-m+1个子串，看有没有和模式串匹配的
        在好的情况下时间复杂度为O(n+m)，在最求的情况下时间复杂度为O((n-m+1)*m)
        :param s: 主串
        :param p: 匹配串，也叫模式串
        :param pos: 从pos位置开始匹配
        :return:
        """
        i = pos
        j = 0
        # 循环终止条件：2个串有1个完全匹配为止
        while i < len(s) and j < len(p):
            if s[i] == p[j]:  # 两字母相等，判断下一位
                i += 1
                j += 1
            else:
                i = i - j + 1  # i退回到上次匹配首尾的下一位
                j = 0          # j退回到模式串首位

        # 判断匹配完成条件：匹配串下标j等于匹配串长度
        if j == len(p):
            return i - len(p)  # 匹配成功，返回匹配串在主串中的索引下标
        return -1

    def rk(self, s, p, pos=0):
        """
        Rabin-Karp算法
        :param s:
        :param p:
        :param pos:
        :return:
        """
        pass

    def bm(self, s, p, pos=0):
        """
        bm算法, 包括：坏字符规则，好后缀规则
        坏字符规则：按照模式串下标从大到小的顺序，倒着匹配。当某个字符没法匹配的时候，称这个没有匹配的字符叫做坏字符(主串中的字符)
            匹配串移动规则：坏字符对于的模式串中字符下标记为Si，如果坏字符在模式串中存在，把坏字符在模式串中的下标记为Xi，如果不存在Xi为-1
                ，则模式串往后移动的位数为Si-Xi
            注意：最好情况下时间复杂度为O(n/m)；有可能Si-Xi是负数
        好后缀规则：
        :param s:
        :param p:
        :param pos:
        :return:
        """
        size = 256

        # 散列表：字符的ascii码作为散列表的下标，字符在模式串中的位置作为散列表的值
        bc = [-1] * size
        for ix in range(len(p)):
            ascii_val = ord(p[ix])
            bc[ascii_val] = ix

        i = 0  # i表示主串与模式串对齐的第一个字符
        while i <= len(s) - len(p):
            # 模式串从后往前匹配
            j = len(p) - 1
            while j >= 0:
                if s[i+j] != p[j]:  # 坏字符对应模式串中的下标为j
                    break
                j -= 1
            if j < 0:  # 匹配成功，返回主串与模式串第一个匹配的字符的位置
                return i
            # 等同于将模式串往后移动 j-bc[ord(s[i+j])]
            i = i + (j - bc[ord(s[i+j])])
        return -1

    def kmp(self, s, p):
        """
        KMP算法: 主串不变位置，只移动模式串
        和朴素匹配法的差异为当匹配失效的时候只移动j
        :param s:
        :param p:
        :return:
        """
        i = j = 0
        next = self.getNexts(p)
        print(next)

        while i < len(s) and j < len(p):
            if j == -1 or s[i] == p[j]:  # j=-1 或者 当前字符匹配成功
                i += 1
                j += 1
            else:  # 如果j != -1，且当前字符匹配失败（即S[i] != P[j]），则令 i 不变，j = next[j],next[j]即为j所对应的next值
                j = next[j]
        if j == len(p):
            return i - j
        return -1

    def getNexts(self, p):
        # KMP的next数组函数
        next = [None] * len(p)
        next[0] = -1
        k = -1
        j = 0
        while j < len(p)-1:
            # p[k]表示前缀, p[j]表示后缀
            if k == -1 or p[k] == p[j]:
                k += 1
                j += 1
                next[j] = k
            else:
                k = next[k]
        return next


if __name__ == "__main__":
    obj = StrMatch()
    print(obj.bf('goodgoogle', 'google'))
    print(obj.bm('goodgoogle', 'google'))
    print(obj.kmp('goodgoogle', 'google'))
