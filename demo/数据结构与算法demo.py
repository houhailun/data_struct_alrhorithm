#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2020/8/13 13:54
# Author: Hou hailun


class Node:
    # 链表节点类
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkList:
    # 链表类
    def __init__(self):
        self.head = None  # 头节点

    def add_head(self, data):
        # 插入节点，头插法
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def is_empty(self):
        return self.head == None

    def size(self):
        node = self.head
        count = 0
        while node:
            node = node.next
            count += 1
        return count

    def search(self, key):
        node = self.head
        while node:
            if node.data == key:
                return True
            node = node.next
        return False

    def delete(self, ix):
        node = self.head
        pre_node = None
        if ix == 0:  # 删除头结点指针
            data = self.head.data
            self.head = self.head.next
            return data
        i = 0
        while node:
            if i == ix:
                data = node.data
                pre_node.next = node.next
                return data
            if i < ix:
                pre_node = node
                node = node.next
                i += 1
        if i > ix:
            return -1

    def print_link(self):
        node = self.head
        while node:
            print(node.data, sep=', ')
            node = node.next
#
# obj = LinkList()
# obj.add_head(10)
# obj.add_head(20)
# obj.add_head(30)
# obj.print_link()
# print(obj.search(10))
# print(obj.delete(2))


class TreeNode:
    # 树节点类
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BiTree:
    # 二叉树类
    def __init__(self):
        self.root = None

    def add_total_tree(self, item=None):
        # 构建完全二叉树
        new_node = TreeNode(item)
        if self.root is None:  # 构建根节点
            self.root = new_node
            return
        my_queue = [self.root]
        while True:
            node = my_queue.pop(0)
            if node.left is None:
                node.left = new_node
                return
            if node.right is None:
                node.right = new_node
                return
            my_queue.append(node.left)
            my_queue.append(node.right)

    def add_tree(self, item=None):
        new_node = TreeNode(item)
        if self.root is None:
            self.root = new_node
            return
        my_queue = []
        my_queue.append(self.root)
        while True:
            node = my_queue.pop(0)
            if node.data is None:  # 节点值为空，叶子节点，占位
                continue
            if node.left is None:
                node.left = new_node
                return
            if node.right is None:
                node.right = new_node
                return
            my_queue.append(node.left)
            my_queue.append(node.right)

    def pre_travel(self, node):
        # 前序遍历二叉树: 根-左-右
        if not node:
            return
        print(node.data, end=', ')
        self.pre_travel(node.left)
        self.pre_travel(node.right)

    def in_travel(self, node):
        # 中序遍历二叉树: 左-根-右
        if not node:
            return
        self.in_travel(node.left)
        print(node.data, end=', ')
        self.in_travel(node.right)

    def post_travel(self, node):
        # 后续遍历: 左-右-根
        if not node:
            return
        self.post_travel(node.left)
        self.post_travel(node.right)
        print(node.data, end=', ')

    def bread_travel(self):
        # 层序遍历：利用辅助队列
        my_queue = [self.root]
        while my_queue:
            cur_node = my_queue.pop(0)
            print(cur_node.data, end=', ')
            if cur_node.left:
                my_queue.append(cur_node.left)
            if cur_node.right:
                my_queue.append(cur_node.right)


def bitree_test():
    obj = BiTree()
    # obj.add_total_tree(10)
    # obj.add_total_tree(20)
    # obj.add_total_tree(30)
    # obj.add_total_tree(40)
    # obj.add_total_tree(50)
    # obj.pre_travel(obj.root)
    # print('\n')
    # obj.in_travel(obj.root)
    # print('\n')
    # obj.post_travel(obj.root)
    # print('\n')

    # obj.add_tree(10)
    # obj.add_tree(20)
    # obj.add_tree(30)
    # obj.add_tree()
    # obj.add_tree()
    # obj.add_tree(40)
    # obj.add_tree(50)
    # obj.pre_travel(obj.root)
    # print('\n')
    # obj.in_travel(obj.root)
    # print('\n')
    # obj.post_travel(obj.root)
    # print('\n')
    # obj.bread_travel()


class BSTree:
    # 二叉搜索树类: 根节点值大于左子树值，小于右子树值
    def __init__(self):
        self.root = None

    def insert(self, value):
        if self.root is None:
            self.root = TreeNode(value)
        else:
            self.insert_node(value, self.root)

    def insert_node(self, value, root):
        # 递归版本
        if value < root.data:  # 插入左子树
            if root.left is None:
                root.left = TreeNode(value)
                return
            self.insert_node(value, root.left)
        elif value > root.data:
            if root.right is None:
                root.right = TreeNode(value)
                return
            self.insert_node(value, root.right)

    def insert_loop(self, value):
        node = TreeNode(value)
        if self.root is None:
            self.root = node
            return
        cur_node = self.root
        while True:
            if value < cur_node.data:
                if cur_node.left:
                    cur_node = cur_node.left
                else:
                    cur_node.left = node
                    break
            elif value > cur_node.data:
                if cur_node.right:
                    cur_node = cur_node.right
                else:
                    cur_node.right = node
                    break
            else:
                break

    def find_min(self, root):
        # 最小值即最左子节点
        if root.left:
            return self.find_min(root.left)
        return root.data

    def find_min_loop(self):
        root = self.root
        while root.left:
            root = root.left
        return root.data

    def pre_travel(self, node):
        if not node:
            return
        print(node.data, end=', ')
        self.pre_travel(node.left)
        self.pre_travel(node.right)

    def in_travel(self, node):
        if not node:
            return
        self.in_travel(node.left)
        print(node.data, end=', ')
        self.in_travel(node.right)

    def post_traval(self, node):
        if not node:
            return
        self.post_traval(node.left)
        self.post_traval(node.right)
        print(node.data, end=', ')

    def delete(self, root, key):
        # 在root树上删除值为key的节点
        # case1：待删除节点为叶子节点，直接删除
        # case2：待删除节点只有左子树或右子树，则使用左子树或右子树替换
        # case3：待删除节点既有左子树又有右子树
        #   1、该节点右子树中最小值节点，使用该节点代替待删除节点，然后在右子树中删除最小值节点。
        #   2、该节点左子树最大值节点，使用该节点代替待删除节点，然后在左子树中删除最大值节点
        pass
#
# obj = BSTree()
# obj.insert_loop(20)
# obj.insert_loop(10)
# obj.insert_loop(30)
# obj.insert_loop(5)
# obj.insert_loop(25)
# obj.insert_loop(40)
# print(obj.find_min(obj.root))
# print(obj.find_min_loop())
# obj.pre_travel(obj.root)
# print('\n')
# obj.in_travel(obj.root)
# print('\n')
# obj.post_traval(obj.root)

# 20210310 数据结构复习
# 数据结构之栈
# 栈特点：先进后出 后进先出
class MyStack:
    def __init__(self):
        self.stack = []

    def push(self, item):
        # 入栈：直接压入栈
        self.stack.append(item)

    def pop(self):
        # 出栈：栈顶弹出
        if not self.is_empty():
            return self.stack.pop()
        return None

    def is_empty(self):
        return len(self.stack) == 0

    def top(self):
        # 获取栈顶元素
        if not self.is_empty():
            return self.stack[-1]
        return None

    def print_stack(self):
        print(self.stack)


def stack_test():
    my_stack = MyStack()
    print(my_stack.pop())
    my_stack.push(10)
    print(my_stack.top())
    my_stack.push(20)
    my_stack.push(30)
    my_stack.push(40)
    my_stack.print_stack()
    my_stack.pop()
    my_stack.print_stack()

# 栈的应用 -- 括号检查，用于检查括号是否匹配
# NOTE: 暂时认为symbol_str里全部都是括号，不存在其他字符
def match_parentheses(s):
    ls = []
    parentheses = "()[]{}"
    for i in range(len(s)):
        si = s[i]
        # 跳过非括号的字符
        if si not in parentheses:
            continue
        # 左括号入栈
        if si == '(' or si == '[' or si == '{':
            ls.append(si)
            continue
        # 没有左括号必然不匹配
        if len(ls) == 0:
            return False
        # 出栈，比较是否匹配
        p = ls.pop()
        if (p == '(' and si == ')') or (p == '[' and si == ']') or (p == '{' and si == '}'):
            continue
        else:
            return False

    # 遍历s完成后，如果栈ls种还有元素，则必然不匹配
    if len(ls) > 0:
        return False
    return True

# print(match_parentheses('9{}a[()]10'))

# 数据结构之队列
# 队列特点：先进先出，对头出，队尾进
class MyQueue:
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        # 入队列: 直接队尾压入
        self.queue.append(item)

    def dequeue(self, item):
        # 出队：对头弹出
        if not self.is_empty():
            return self.queue.pop(0)

    def is_empty(self):
        return len(self.queue) == 0

# 数据结构之链表
# 链表特点：非连续地址空间，通过next指针指向下一个元素，查找O(n),删除O(1)
class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyList:
    def __init__(self):
        self.head = None  # 初始化头节点为空

    def is_empty(self):
        return self.head is None

    def add(self, item):
        # 头插法：每次在链表开头插入节点
        new_node = ListNode(item)
        new_node.next = self.head
        self.head = new_node

    def size(self):
        # 链表结点个数
        cnt = 0
        node = self.head
        while node:
            node = node.next
            cnt += 1
        return cnt

    def search(self, item):
        # 在链表中查找值为item的节点
        node = self.head
        while node:
            if node.val == item:
                return True
            node = node.next
        return False

    def remove(self, ix):
        # 删除位置ix的节点, 注意并不是物理删除，而是指针跳过
        del_data = 0
        cur_node = self.head
        pre_node = None
        if ix == 0:  # 待删除头节点
            del_data = self.head.val
            self.head = self.head.next
            return del_data
        i = 0
        while cur_node:
            if i == ix:  # 找到节点
                del_data = cur_node.val
                pre_node.next = cur_node.next
                break
            elif i < ix:  # 遍历
                pre_node = cur_node
                cur_node = cur_node.next
                i += 1
        if i < ix or i > ix:
            return -1
        return del_data

# 数据结构之二叉树
# 二叉树（Binary Tree）是n （n>=0）个节点的有限集合，该集合可以为空集（称为空二叉树），或者由一个根节点和两个互不相交的，分别称为根节点的左子树和右子树的二叉树组成
# 特点：
#   1、每个节点最多有2个子树
#   2、左右子树有顺序，次序不能任意颠倒
#   3、即使树种某节点只有一颗子树，也要区分是左子树还是右子树
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None  # 初始根节点为空

    def pre_order(self, node):
        # 前序遍历：根-左-右
        if not node:
            return
        print(node.val)
        self.pre_order(node.left)
        self.pre_order(node.right)

    def mid_order(self, node):
        # 中序遍历：左-根-右
        if not node:
            return
        self.mid_order(node.left)
        print(node.val)
        self.mid_order(node.right)

    def post_order(self, node):
        # 后续遍历：左-右-根
        if not node:
            return
        self.post_order(node.left)
        self.post_order(node.right)
        print(node.val)

    def bread_travel(self, node):
        # 层次遍历：从上往下，一层一层遍历,同一层从左到右打印
        # 实际上是广度遍历，需要辅助对列
        if not node:
            return
        queue = [node]
        while queue:
            node = queue.pop(0)
            print(node.val)
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)

    def add_complete_binary_tree(self, item):
        # 构建树，完全二叉树
        node = TreeNode(item)
        if not self.root:  # 空树，添加到根节点
            self.root = node
            return
        # 当前树不为空，则按照 左右顺序 添加节点,这样构建出来的是一棵有序二叉树，且是完全二叉树
        queue = [self.root]
        while True:
            cur_node = queue.pop(0)
            if cur_node.left is None:  # 左子树为空，则添加到左子树
                cur_node.left = node
                return
            if cur_node.right is None:
                cur_node.right = node
                return
            # 左右子树都不为空，则继续往下
            queue.append(cur_node.left)
            queue.append(cur_node.right)

    def add_binary_tree(self, item):
        # 构建树，二叉树，非完全二叉树
        node = TreeNode(item)
        if not self.root and self.root.data is None:
            self.root = node
            return
        queue = [self.root]
        while True:
            cur_node = queue.pop(0)
            if cur_node.data is None:  # 占位作用
                continue
            if not cur_node.left:
                cur_node.left = node
                return
            if not cur_node.right:
                cur_node.right = node
                return
            queue.append(cur_node.left)
            queue.append(cur_node.right)

    def pre_travel_stack(self, node):
        # 前序遍历 使用辅助栈实现
        if not node:
            return
        stack = [node]
        while stack:
            s = stack.pop()  # 弹出栈顶元素
            if s:
                print(s.val)
                # 由于栈的先入后出特性，这里先加right孩子
                stack.append(s.right)
                stack.append(s.left)


class BinarySearchTree:
    # 二叉搜索树类：左节点值 < 根节点值 < 右节点值
    def __init__(self):
        self.root = None
        self.size = 0  # 树中结点个数

    def insert(self, item):
        # 插入节点
        if not self.root:
            self.root = TreeNode(item)
            return
        self.insert_node(item, self.root)

    def insert_node(self, val, bt_node):
        if val < bt_node.val:  # 在左子树插入节点
            if bt_node.left is None:
                bt_node.left = TreeNode(val)
                return
            self.insert_node(val, bt_node.left)
        elif val > bt_node.val:  # 在右子树插入
            if bt_node.right is None:
                bt_node.right = TreeNode(val)
                return
            self.insert_node(val, bt_node.right)

    def insert_node_loop(self, val):
        # 插入节点 循环版本
        if self.root is None:
            self.root = TreeNode(val)
            return
        cur_node = self.root
        while True:
            if val < cur_node.val:
                if cur_node.left is None:
                    cur_node.left = TreeNode(val)
                    return
                cur_node = cur_node.left
            if val > cur_node.val:
                if cur_node.right is None:
                    cur_node.right = TreeNode(val)
                    return
                cur_node = cur_node.right
            if val == cur_node.val:
                break

    def find_min(self, node):
        # 最小值：最左节点
        if node.left:
            return self.find_min(node.left)
        return node

    def find_max(self, node):
        if node.right:
            return self.find_max(node.right)
        return node

    def delete(self, root, key):
        # 在二叉树中删除值为key的节点
        if not root:
            return
        # 先在树中查找值为key的节点
        if key < root.val:
            root = root.left
        elif key > root.val:
            root = root.right
        else:
            if root.left is None and root.right is None:  # 待删除的是叶子节点
                root = None
            elif root.left is None:  # 左子树为空，只有右子树，把右子树替换为当前节点
                root = root.right
            elif root.right is None:  # 右子树为空，只有左子树，把左子树替换为当前节点
                root = root.left
            elif root.left and root.right:  # 左右子树都不空
                tmp_node = self.find_min(root.right)  # 找到右子树中最小值节点
                root.data = tmp_node.data  # 替换待删除节点值
                root.right = self.delete(root.right, tmp_node.data)  # 删除右子树中最小值节点

        return root

# 数据结构之哈希表
# 哈希表: 通过哈希函数，把key映射到指定ix上，能在O(1)时间内查找，插入，删除
# 哈希函数: ix = hash(key)
# 冲突: key1 != key2, hash(key1) == hash(key2)
# 解决冲突方法：开放定址法，拉链法

from collections import defaultdict
# 数据结构之图
# 使用字典来构建图的邻接表实现
class Graph:
    def __init__(self, num_vertex):
        self.graph = defaultdict(list)  # 图邻接字典
        self.num_vertex = num_vertex    # 定点数

    def add_edge(self, u, v):
        # 增加有向边， u->v
        self.graph[u].append(v)

    def search_bfs(self, start):
        # 广度优先遍历，指定起始遍历位置start
        # 思想：类似于树的层次遍历，start为第一层，start顶点的连接点为第2层，然后依次从连接点开始找后续顶点
        queue = [start]
        visited = set()
        visited.add(start)
        while queue:
            vertex = queue.pop(0)
            nodes = self.graph[vertex]
            for node in nodes:
                if node not in visited:  # 临界点 & 没有被访问过
                    queue.append(node)   # 添加到队列中
                    visited.add(node)    # 标记为以访问
            print(' 当前出队的是: ', vertex)

    def search_dfs(self, start):
        # 深度优先遍历
        # 思想：
        #   1、首先以一个未被访问过的顶点作为起始顶点，沿当前顶点的边走到未访问过的顶点；
        #   2、当没有未访问过的顶点时，则回到上一个顶点，继续试探别的顶点，直至所有的顶点都被访问过。