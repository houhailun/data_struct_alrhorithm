#!/usr/bin/env python
# -*- coding:utf-8 -*-
import Queue

#
# 模块功能：图结构
# 定义：图是由顶点的有穷非空集合和顶点之间边的集合组成，表示为G(V,E)
# 图的存储结构
#     一、邻接矩阵
#         1、定义：邻接矩阵是指用二阶矩阵来表示图，矩阵的下标表示顶点，矩阵的元素信息表示边
#             A[i][j] = 1 <- 顶点i与j之间存在边；A[i][j]=0 <- 顶点i与j之间没有边
#         2、通常采用两个数组来实现邻接矩阵：一个一维数组用来保存顶点信息，一个二维数组来用保存边的信息
#         3、缺点：耗费空间
#             3.1 无向图是关于对角线对称的，因此只需要利用一半空间就够了
#             3.2 对于稀树图，顶点很多，边很少。使用邻接矩阵存储浪费大量空间
#         5、优点：存储方式简单、直接；基于数组可以方便高效的获取两顶点的关系；
#                 方便计算，因为用邻接矩阵的方式存储图，可以讲图的运算转换为矩阵之间的运算
#         6、适用于稠密图
#     二、邻接表
#         1、定义：一种链式存储方法，是改进后的”邻接矩阵”，它的缺点是不方便判断两个顶点之间是否有边，但是相对邻接矩阵来说更省空间
#         2、在邻接列表实现中，每一个顶点会存储一个从它这里开始的边的列表
#         3、适用于稀树图
#         4、缺点：不方便查找
#     三、两种存储方式对比
#     操作	        邻接列表    	邻接矩阵
#     存储空间	    O(V + E)	O(V^2)
#     添加顶点	    O(1)	    O(V^2)
#     添加边	    O(1)	    O(1)
#     检查相邻性	O(V)	    O(1)
#     四：应用场景：社交关系、知识图谱
#     五、拓展
#         对于微信来说的好友关系是无向图
#         对于微博来说的好友关系是有向图，因为有A关注B，B没有关注A
#         社交网络是稀疏图，采用邻接表来存储
#         5.1 查找用户A关注了哪些用户：在邻接表中查找用户A开头的链表
#         5.2 查找哪些用户关注了用户A
#             case1：遍历邻接表，在每个链表中查找是否有用户A，较困难
#             case2：构建逆邻接表，存储的是用户的被关注关系，每个顶点的链表中存储的是指向这个顶点的顶点，这样可以直接查找用户A顶点
#         5.3 由于邻接表不方便查找，可以把邻接表中的链表改为动态数据结构：红黑树、跳表、哈希表等


class Vertex:
    # 顶点类, 邻接表实现
    def __init__(self, key):
        """
        顶点构造函数，用于初始化id
        :param key:
        """
        self.id = key          # 顶点id
        self.connectedTo = {}  # 跟踪顶点连接的顶点和边的权重

    def addNeighbor(self, nbr, weight=0):
        """
        构建连接
        :param nbr: 连接到的顶点
        :param weight: 边权重
        :return:
        """
        self.connectedTo[nbr] = weight

    def getConnections(self):
        # 返回该顶点的连接表中的所有顶点
        return self.connectedTo.keys()

    def getId(self):
        return self.id

    def getWeight(self, nbr):
        """
        从该顶点到nbr顶点的边的权重
        :param nbr:
        :return:
        """
        return self.connectedTo[nbr]

    def __str__(self):  # 当使用print输出对象的时候，只要自己定义了__str__(self)方法，那么就会打印从在这个方法中return的数据
        return str(self.id) + ' connectedTo: ' + str([x.id for x in self.connectedTo])


class Graph:
    # 图类，保存顶点的主列表
    def __init__(self):
        self.verList = {}     # 用于把顶点名称映射到顶点对象
        self.numVertices = 0  # 顶点个数

    def addVertex(self, key):
        """
        增加顶点
        :param key:
        :return:
        """
        self.numVertices += 1
        newVertex = Vertex(key)
        self.verList[key] = newVertex
        return newVertex

    def getVertex(self, n):
        """
        获取id为n的顶点
        :param n:
        :return:
        """
        if n in self.verList:
            return self.verList[n]
        return None

    def __contains__(self, n):
        return n in self.verList

    def addEdge(self, f, t, cost=0):
        """
        在顶点f，t间增加边
        :param f:
        :param t:
        :param cost:
        :return:
        """
        if f not in self.verList:
            _ = self.addVertex(f)
        if t not in self.verList:
            _ = self.addVertex(t)
        self.verList[f].addNeighbor(self.verList[t], cost)

    def getVertices(self):
        return self.verList.keys()

    def __iter__(self):  # 便于遍历图中所有的顶点对象
        return iter(self.verList.values())

    # 搜索算法：
    #   暴力法：广度优先遍历、深度优先遍历
    #   启发式: A*, IDA*
    def bfs(self, s, e):
        """
        广度优先搜索，找到一条从s到e的路径，也就是最短路径
        :param s: 起始顶点
        :param e: 终止顶点
        :return:
        """
        if s == e:
            return None

        visited = []


#  应用1：字梯的问题（把一个单词转换为另一个长度相同的单词，每次只允许改变其中一个字母）
def buildGraph(wordFile):
    """
    构建字梯图
    思路：把所有长度相同，只有一个字母不同的单词放到同一个桶中，对桶中的单词创建边
    :param wordFile:
    :return:
    """
    d = {}
    g = Graph()
    wfile = open(wordFile, 'r')
    for line in wfile:
        word = line[:-1]
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i+1:]  # 把每一位作为一个通配符，认为是一个桶
            if bucket in d:  # 把每个桶放到字典中
                d[bucket].append(word)
            else:
                d[bucket] = [word]

    # 对相同的桶增加顶点和边
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    g.addEdge(word1, word2)
    return g


if __name__ == "__main__":
    g = Graph()
    for i in range(6):  # 创建编号为0到5的6个顶点
        g.addVertex(i)
    print(g.verList)
    g.addEdge(0, 1, 5)
    g.addEdge(0, 5, 2)
    g.addEdge(1, 2, 4)
    g.addEdge(2, 3, 9)
    g.addEdge(3, 4, 7)
    g.addEdge(3, 5, 3)
    g.addEdge(4, 0, 1)
    g.addEdge(5, 4, 8)
    g.addEdge(5, 2, 1)
    for v in g:  # 调用__iter__()方法
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))

    g = buildGraph('wordFile')
    print(g)
    for v in g:  # 调用__iter__()方法
        print(v)
        for w in v.getConnections():
            print("( %s , %s )" % (v.getId(), w.getId()))
