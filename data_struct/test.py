#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2019/11/14 13:29
# Author: Hou hailun

# 数组
# 特点: 连续存储空间，查找O(1), 插入删除O(N)
# 可随机访问原因: addr[i] = addr_base + bytes_type * i

# 链表
# 特点：非连续存储空间，查找O(N), 插入删除O(1)


class ListNode:
    # 链表节点类
    def __init__(self, data=None):
        self.data = data
        self.next = None

    def get_next(self):
        return self.next

    def get_date(self):
        return self.data

    def set_next(self, new_next=None):
        self.next = new_next

    def set_data(self, new_data=None):
        self.data = new_data


class LinkList:
    # 链表类
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head

    def add(self, item):
        # 头插法
        new_node = ListNode(item)
        new_node.set_next(self.head)
        self.head = new_node

    def size(self):
        # 链表的节点数
        node_cnt = 0
        tmp_node = self.head
        while tmp_node:
            node_cnt += 1
            tmp_node = tmp_node.get_next()
        return node_cnt

    def search(self, item):
        # 查找值为item的节点
        is_find = False
        tmp_node = self.head
        while tmp_node:
            if item == tmp_node.get_data():
                is_find = True
                break
            tmp_node = tmp_node.get_next()
        return is_find

    def delete(self, ix):
        # 删除位置ix的节点, 要考虑删除头节点，中间结点，末尾节点
        tmp_node = self.head
        pre_node = None
        del_data = 0
        if 0 == ix:  # 删除头节点
            del_data = self.head.get_data()
            self.head = self.head.get_next()
            return del_data
        i = 0
        while tmp_node:
            if i == ix:
                del_data = tmp_node.get_data()
                pre_node.next = tmp_node.get_next()
                break
            if i < ix:
                pre_node = tmp_node
                tmp_node = tmp_node.get_next()
                i += 1
        if i > ix:  # 没有找到ix位置
            del_data = -1
        return del_data


# 链表应用: 两个有序链表的合并、反转列表、判断链表中是否有环，


# 栈，连续内存空间，后进先出，在栈顶插入删除元素
# 常见接口：创建栈，入栈，出栈，栈是否为空，栈内元素个数等
class MyStack:
    # 栈类
    def __init__(self):
        self.stack = []

    def push(self, item):
        # 入栈，即把指定item插入到栈顶
        self.stack.append(item)

    def pop(self):
        if self.stack:
            return self.stack.pop()

    def is_empty(self):
        return self.stack is None

    def size(self):
        return len(self.stack)


# 队列
# 连续内存空间
# 队尾插入数据，对头删除数据，先进先出
# 单端队列，双端队列
# 应用：队列在线程池等有限资源的等待
class MyQueue:
    # 单端队列：对头删除，队尾插入
    # 缺点：tail队尾=n时，需要迁移数据
    def __init__(self):
        self.queue = []

    def enqueue(self, item):
        # 入队列
        self.queue.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def is_empty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)


class cycleQueue:
    # 循环队列：避免迁移数据
    def __init__(self):
        self.arr = []
        self.head = 0
        self.tail = 0
        self.size = 0

    def is_empty(self):
        return self.tail == self.head

    def is_full(self):
        return (self.tail + 1) % len(self.arr) == self.head

    def resize(self, new_capacity):
        # 数据满了，需要扩容
        new_arr = [None] * (new_capacity + 1)
        for i in range(len(self.size)):
            new_arr[i] = self.arr[(i+self.head) % len(self.arr)]
            self

        self.arr = new_arr
        self.head = 0
        self.tail = self.size


class Node:
    # 二叉树的节点类
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    # 二叉树类
    def __init__(self, node=None):
        self.root = node

    def pre_travel(self, node):
        """前序遍历：根-左-右"""
        if not node:
            return

        print(node.data)
        self.pre_travel(node.left)
        self.pre_travel(node.right)

    def mid_travel(self, node):
        """中序遍历：左-根-右"""
        if not node:
            return

        self.mid_travel(node.left)
        print(node.data)
        self.mid_travel(node.right)

    def post_travel(self, node):
        """后序遍历：左-右-根"""
        if node is None:
            return

        self.post_travel(node.left)
        self.post_travel(node.right)
        print(node.data)

    def add(self, item=None):
        """构建完全二叉树"""
        node = Node(item)
        if not self.root:  # 空树，添加到根节点
            self.root = node
            return
        # 不为空，则按照 左右顺序 添加节点,这样构建出来的是一棵有序二叉树，且是完全二叉树
        my_queue = []
        my_queue.append(self.root)
        while True:
            cur_node = my_queue.pop(0)
            if not cur_node.left:  # 左孩子为空
                cur_node.left = node
                return
            elif not cur_node.right:  # 右孩子为空
                cur_node.right = node
                return
            else:
                my_queue.append(cur_node.left)
                my_queue.append(cur_node.right)

    def add_v2(self, data):
        """二叉树的创建：一般二叉树"""
        node = Node(data)
        if self.root is None:
            self.root = node
            return

        # 不为空，则按照 左右顺序 添加节点, 对于为None的节点跳过并占位
        my_queue = []
        my_queue.append(self.root)
        while True:
            cur_node = my_queue.pop(0)
            # 当前节点数据为空，起占位作用
            if cur_node.data is None:
                continue
            if cur_node.left is None:
                cur_node.left = node
                return
            if cur_node.right is None:
                cur_node.right = node
                return
            my_queue.append(cur_node.left)
            my_queue.append(cur_node.right)


# tree = BinaryTree()
# tree.add_v2(1)
# tree.add_v2(2)
# tree.add_v2(None)
# tree.add_v2(4)
# tree.add_v2(5)
# print(' pre '.center(40, '*'))
# tree.pre_travel(tree.root)
# print(' mid '.center(40, '*'))
# tree.mid_travel(tree.root)
# print(' post '.center(40, '*'))
# tree.post_travel(tree.root)


class BSTree:
    # 二叉搜索树：左节点值小于父节点值，右节点值大于父节点值；中序遍历为有序数组
    def __init__(self, node=None):
        self.root = node
        self.size = 0

    def pre_travel(self, node):
        BinaryTree.pre_travel(node)

    def mid_travel(self, node):
        BinaryTree.mid_travel(node)

    def post_travel(self, node):
        BinaryTree.post_travel(node)

    def search(self, node, data):
        """
        查找操作
        思路：从根节点开始如果data小于当前节点的值，则在左子树中查找；否则在右子树中查找
        :param node: 树节点
        :param data: 待查找数据
        :return:
        """
        if node is None:
            return None
        if data == node.data:
            return node
        elif data < node.data:
            return self.search(node.left, data)
        else:
            return self.search(node.right, data)

    def search_loop(self, node, data):
        # 循环版本
        if node is None:
            return None
        while node:
            if data < node.data:
                node = node.left
            elif data > node.data:
                node = node.right
            else:
                return node
        return node


    def insert(self, data):
        """
        二叉树插入操作: 若插入节点的值比根节点值小，则将其插入根节点的左子树；
        若比根节点值大，则插入到根节点右子树
        """

        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_node(data, self.root)

    def insert_node(self, data, bt_node):
        if data < bt_node.data:
            if bt_node.left is None:  # 左子节点为空，则插入左子节点
                bt_node.left = Node(data)
                return
            # 左子节点不为空，则递归左子节点
            self.insert_node(data, bt_node.left)
        elif data > bt_node.data:
            if bt_node.right is None:
                bt_node.right = Node(data)
                return
            self.insert_node(data, bt_node.right)

    def insert_loop(self, key):
        """循环版本"""
        node = Node(key)
        if self.root is None:
            self.root = node
            self.size += 1
        else:
            cur_node = self.root
            while True:
                if key < cur_node.data:
                    if cur_node.left:
                        cur_node = cur_node.left
                    else:
                        cur_node.left = node
                        self.size += 1
                        break
                elif key > cur_node.data:
                    if cur_node.right:
                        cur_node = cur_node.right
                    else:
                        cur_node.right = node
                        self.size += 1
                        break
                else:
                    break

    def find_min(self, root):
        """查找二叉树最小值：最左节点"""
        if root.left:
            return self.find_min(root.left)
        return root

    def find_max(self, root):
        """查找二叉树最大值：最右节点"""
        if root.right:
            return self.find_max(root.right)
        return root

    def delete(self, root, key):
        """
        case1：待删除节点为叶子节点，直接删除
        case2：待删除节点只有左子树或只有右子树，则把其左子树或右子树代替为待删除节点
        case3：待删除节点既有左子树又有右子树，找到该节点右子树中最小值节点，使用该节点代替待删除节点，然后在右子树中删除最小值节点。
        :param root: 根节点
        :param key: 待删除节点的数值
        :return:
        """
        if root is None:
            return None

        # 查找值为key的节点
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            # 叶子节点直接删除
            if root.left is None and root.right is None:
                root = None
            elif root.right is None:  # 只有左子树
                root = root.left
            elif root.left is None:  # 只有右子树
                root = root.right
            else:  # 同时有左子树和右子树
                # 查找右子树中最小值节点，即右子树的最左节点
                tmp_node = self.find_min(root.right)
                root.data = tmp_node.data
                root.right = self.delete(root.right, tmp_node.data)
        return root

    def print_tree(self, root):
        if root is None:
            return None

        self.print_tree(root.left)
        print(root.data, end=', ')
        self.print_tree(root.right)


# tree1 = BSTree()
# for i in [17, 5, 2, 16, 35, 29, 38]:
#     tree1.insert(i)
# tree1.print_tree(tree1.root)

print('\n')
tree2 = BSTree()
for i in [17, 5, 2, 16, 35, 29]:
    tree2.insert_loop(i)
tree2.print_tree(tree2.root)

print('\n')
print(tree2.search_loop(tree2.root, 35).data)

# print('\n')
# print(tree2.find_min(tree2.root).data)
# print(tree2.find_max(tree2.root).data)
#
# print('\n删除节点:\n')
# tree2.delete(tree2.root, 35)
# tree2.print_tree(tree2.root)