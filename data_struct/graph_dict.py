#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/1/2 16:02
# Author: Hou hailun

# 图
# C/C++中用邻接矩阵或邻接表来实现
# python中用字典来实现邻接表，用多重列表来实现邻接矩阵
import sys
from collections import defaultdict


class Graph:
    def __init__(self, num_vertex=0):
        self.graph = defaultdict(list)
        self.num_vertex = num_vertex

    def add_edge(self, u, v):
        """
        增加有向边: u —> v
        :param u:
        :param v:
        :return:
        """
        self.graph[u].append(v)

    def search_bfs(self, start):
        """
        广度优先搜索，层次遍历
        核心思想：解决图的BFS问题就是利用队列的先进先出的思想来解决问题。因为我们需要利用queue来保证树的第几层或者说是图中我们遍历走了几步的顺序。
            BFS和树的层序遍历非常类似，树和图的遍历，主要区别是树有根节点，所以指定了，而图需要我们自身指定开始遍历的节点，起始节点的不同会导致遍历节点的不同
        :param start: 起始遍历顶点
        :return:
        """
        queue = list()
        queue.append(start)
        visited = set()
        visited.add(start)

        while len(queue) > 0:
            vertex = queue.pop(0)  # 弹出第一个顶点
            nodes = self.graph[vertex]  # 顶点vertex相邻的顶点
            for w in nodes:
                if w not in visited:  # 临界点 && 没有访问
                    queue.append(w)   # 将没有遍历过的顶点入队
                    visited.add(w)    # 标记为已遍历
            print(' 当前出队的是: ', vertex)

    def search_dfs(self, start):
        """
        深度优先搜索
        回溯法(会回看前面的节点)，一直往前走，走不下去往回跳
        使用stack来进行深度的顺序，把栈顶元素去除，在把临接点放入
        注意：和BFS的区别仅仅在于使用栈
        :param start: 起始遍历顶点
        :return:
        """
        stack = list()
        stack.append(start)
        visited = set()
        visited.add(start)

        while len(stack) > 0:
            vertex = stack.pop()  # 弹出最后一个顶点
            nodes = self.graph[vertex]  # vetex的所有邻接顶点
            for w in nodes:
                if w not in visited:  # 邻接顶点 && 没有被访问过
                    stack.append(w)
                    visited.add(w)
            print('当前出栈的是:', vertex)

    def dijkstra_adjacency_matrix(self):
        """
        使用 Dijkstra 算法计算指定点 v0 到图 G 中任意点的最短路径的距离
        思想：
            1）找出距离当前节点（即起点S）最近的节点，也即权重最小的边，前往该节点（即B）；
            2）对于该节点（B）的邻居，较之已有的路径，检查是否有前往他们更短路径，如果有，就更新其开销（譬如SA=6,但是经过B点再到A的开销为5，小于6，更新）；
            3）更新完所有邻居节点的开销后，又回到第（1）步，即选择距离当前节点最近的节点（已前往过的节点跳过），前往该节点并更新邻居的开销；循环这个过程，直到每个节点都走过；
            4）计算最终路径。
        """
        inf = float('inf')
        edges = [[0, 1, 12, inf, inf, inf],
                 [inf, 0, 9, 3, inf, inf],
                 [inf, inf, 0, inf, 5, inf],
                 [inf, inf, 4, 0, 13, 15],
                 [inf, inf, inf, inf, 0, 4],
                 [inf, inf, inf, inf, inf, 0]]
        dis = {2: 1, 3: 12, 4: inf, 5: inf, 6: inf}
        visited = []

        min_dis = None        # 记录离起始点最小距离
        min_dis_point = None  # 记录离起始点最小距离的顶点

        for i in range(len(dis)):
            sort_dist = sorted(dis.items(), key=lambda x: x[1])  # 根据权值排序
            # 找到dis中距离起点距离最小的点
            for point, did in sort_dist:
                if point not in visited:
                    min_dis_point = point
                    min_dis = did
                    visited.append(point)
                    break
            for j in range(len(edges)):
                # 权重小于inf的为相邻点
                if edges[min_dis_point-1][j] != inf:
                    update = min_dis + edges[min_dis_point-1][j]
                    # 若经过min_dis_point到达j的距离比起点直达j的距离小，则更新
                    if dis[j+1] > update:
                        dis[j+1] = update
        return dis
        # 由于python中列表的索引是从0开始的，而我们的点是1-6，因此min_dis_point在邻接矩阵中的位置需要减一，
        # 这里容易犯错，若是将点改为从0开始无论是写还是可读性都会好很多

    def dijkstra_adjacency_table(self):
        """
        邻接表的 dijkstra 实现
        :return:
        """
        # 由于python没有指针，用嵌套字典来实现邻接表
        inf = float('inf')
        adj = {1: {2: 1, 3: 12}, 2: {4: 3, 3: 9}, 3: {5: 5}, 4: {3: 4, 5: 13, 6: 15}, 5: {6: 4}}
        dis = {2: 1, 3: 12, 4: inf, 5: inf, 6: inf}
        parents_node = {2: 1}
        visited = []

        min_dis = None
        min_dis_point = None
        for i in range(len(dis)):
            sort_dis = sorted(dis.items(), key=lambda x: x[1])
            # 找到dis中距离起始点距离最小的点
            for point, did in sort_dis:
                if point not in visited:
                    min_dis_point = point
                    min_dis = did
                    visited.append(point)
                    break
            try:
                # 更新相邻点的开销
                for n in adj[min_dis_point].keys():
                    update = min_dis + adj[min_dis_point][n]
                    if dis[n] > update:
                        dis[n] = update
                        parents_node[n] = min_dis_point
            except:  # 最后一个点6有进没出，因为没有临界点会报错
                pass

        print(dis)
        print(parents_node)
        travel = ''
        for node, parents in parents_node.items():
            travel += str(parents) + '->' + str(node) + '->'
        return travel


if __name__ == "__main__":
    g = Graph(6)
    g.add_edge('A', 'B')
    g.add_edge('A', 'C')
    g.add_edge('B', 'A')
    g.add_edge('B', 'C')
    g.add_edge('B', 'D')
    g.add_edge('C', 'A')
    g.add_edge('C', 'B')
    g.add_edge('C', 'D')
    g.add_edge('C', 'E')
    g.add_edge('D', 'B')
    g.add_edge('D', 'C')
    g.add_edge('D', 'E')
    g.add_edge('D', 'F')
    g.add_edge('E', 'C')
    g.add_edge('E', 'D')
    g.add_edge('F', 'D')

    print(g.graph)

    print(' BFS '.center(40, '*'))
    print(g.search_bfs('A'))

    print(' DFS '.center(40, '*'))
    print(g.search_dfs('A'))

    print(' Dijkstra_邻接矩阵'.center(40, '*'))
    print(g.dijkstra_adjacency_matrix())

    print(' Dijkstra_邻接表'.center(40, '*'))
    print(g.dijkstra_adjacency_table())
