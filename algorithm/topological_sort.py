#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/1/2 10:56
# Author: Hou hailun

# 拓扑排序算法
# 定义：将一个有向无环图(Directed Acyclic Graph简称DAG)进行排序进而得到一个有序的线性序列；在拓扑排序中，如果存在一条从顶点A到顶点B的路径，那么在排序结果中B出现在A的后面
# 应用场景：源文件编译顺序

from collections import defaultdict


class Graph:
    def __init__(self, vertices):
        self.graph = defaultdict(list)
        self.V = vertices

    def add_edge(self, u, v):
        self.graph[u].append(v)

    def topsort_kahn(self):
        # kahn算法实现拓扑排序
        # 思想：利用贪心算法，先找到入度为0的顶点，将其输出到拓扑排序的结果序列中，并把这个顶点从图中删除，
        #       也就是把这个顶点的可达顶点的入度都减1；循环执行，直到所有的顶点都被输出
        in_degrees = dict((i, 0) for i in range(self.V))

        # 统计顶点入度
        for u in self.graph:
            for v in self.graph[u]:
                in_degrees[v] += 1

        # 筛选入读为0的订单
        Q = [u for u in in_degrees if in_degrees[u] == 0]
        seq = []
        while Q:
            u = Q.pop()
            seq.append(u)  # 从入度为0的中选择1个顶点，入队列，并删除该顶点，移除该顶点的所有指向
            if u in self.graph:  # 由于图中不会列出所有顶点，这里必须要检查u是否位于图中
                for v in self.graph[u]:  # 检查顶点u可达的其他顶点
                    in_degrees[v] -= 1   # 顶点u指向的顶点的入度减1
                    if in_degrees[v] == 0:  # 再次筛选入度为0的顶点
                        Q.append(v)
        if len(seq) == self.V:  # 如果循环结束后存在非0入度的顶点说明图中有环，不存在拓扑排序
            return seq
        return -1

    def topsort_dfs(self):
        # DFS实现拓扑排序
        visited = [False] * self.V
        stack = []

        for i in range(self.V):
            if not visited[i]:
                self.topsort_dfs_util(i, visited, stack)
        return stack

    def topsort_dfs_util(self, v, visited, stack):
        visited[v] = True

        for i in self.graph[v]:
            if not visited[i]:
                self.topsort_dfs_util(i, visited, stack)
        stack.insert(0, v)


g = Graph(6)
g.add_edge(5, 2)
g.add_edge(5, 1)
g.add_edge(4, 0)
g.add_edge(4, 1)
g.add_edge(2, 3)
g.add_edge(3, 1)
print(g.graph)

print(' 拓扑排序结果: ')
print(g.topsort_kahn())
print(g.topsort_dfs())
