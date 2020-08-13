#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/6/15 11:10
# Author: Hou hailun

# 使用邻接矩阵实现图


class Graph:
    def __init__(self, num_vertex):
        self.num_vertex = num_vertex
        self.num_edge = None
        self.vertex = [None] * self.num_vertex
        self.edges = [[None] * self.num_vertex] * self.num_vertex

    def create_graph(self):
        # 构件图，实际上就是在添加顶点，添加边