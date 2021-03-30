#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/8/13 15:06
# Author: Hou hailun

"""
BFS算法接替套路框架 (DFS算法实际上就是回溯算法)

核心思想: 把问题抽象成图，从一个点开始，向四周扩散，一般来说，用队列辅助，每次把一个点周围的所有节点加入队列中
BFS和DFS的区别: BFS找到的路径一定是最短的，但代价就是空间复杂度大

框架
def bfs(start, target):
    # 计算从起点start到终点target的最近距离
    q = []           # 核心数据结构，队列
    visited = []     # 避免走回头路
    q.append(start)  # 将起点加入队列
    visited.append(start)
    step = 0         # 记录扩散步数
    while q:
        sz = len(q)
        for i in range(sz):
            cur = q.pop()
            # 这里判断是否到达终点
            if cur == target:
                return step
            # 划重点: 将cur的相邻节点加入队列
            for x in cur.adj():  # cur.adj() 泛指cur的相邻节点
                q.append(x)
                visited.append(x)
        # 划重点: 更新步数
        step += 1
"""

# 应用1：层次遍历二叉树
# 应用2：二叉树的最小高度
# 思路: 起点是根节点, 重点是最靠近根节点的叶子节点
def minDepth(root):
    if not root:
        return 0
    q = [root]
    depth = 1
    while q:
        sz = len(q)
        # 将当前队列中的所有节点向四周扩散
        for i in range(0, sz):
            cur = q.pop()
            # 判断是否是终点:到达叶子节点
            if cur.left is None and cur.right is None:
                return depth
            if cur.left:
                q.append(cur.left)
            if cur.right:
                q.append(cur.right)
        depth += 1
    return depth

# 应用3：leetcode752 解开密码锁的最少次数
def plusOne(s, j):
    # 将s[j]向上拨动1次
    ch = list(s)
    if ch[j] == '9':
        ch[j] = '0'
    else:
        ch[j] = str(int(ch[j]) + 1)
    return ''.join(ch)

def minusOne(s, j):
    # 将s[j]向下拨动1次
    ch = list(s)
    if ch[j] == '0':
        ch[j] = '9'
    else:
        ch[j] = str(int(ch[j]) - 1)
    return ''.join(ch)

def openLock(deadends, target):
    visied = []              # 记录已经穷举过的密码，防止走回头路
    q = ["0000"]
    step = 0                 # 从起点开始广度优先搜索
    while q:
        sz = len(q)
        # 将当前队列终所有节点向周围扩散
        for i in range(sz):
            cur = q.pop()

            """ 判断是否到达终点 """
            if cur in deadends:
                continue
            if cur == target:
                return step

            """ 将每一个节点的未遍历的相邻节点加到队列 """
            for j in range(4):
                up = plusOne(cur, j)
                down = minusOne(cur, j)
                if up not in visied:
                    q.append(up)
                    visied.append(up)
                if down not in visied:
                    q.append(down)
                    visied.append(down)
        """ 这里增加步数 """
        step += 1
    # 穷举完都没有找到目标密码
    return -1
print(openLock(["8888"], "4209"))
