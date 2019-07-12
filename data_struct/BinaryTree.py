#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
@Time    : 2019/6/28 13:08
@Author  : Hou hailun
@File    : BinaryTree.py
"""
print(__doc__)


class TNode(object):
    """二叉树节点类"""
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


class BTree(object):
    """二叉树类"""
    def __init__(self, node=None):
        self.root = node

    def add(self, item=None):
        """构建完全二叉树"""
        node = TNode(item)
        if not self.root:  # 空树，添加到根节点
            self.root = node
            return
        # 不为空，则按照 左右顺序 添加节点,这样构建出来的是一棵有序二叉树，且是完全二叉树
        my_queue = []
        my_queue.append(self.root)
        while True:
            cur_node = my_queue.pop(0)
            if not cur_node.left:
                cur_node.left = node
                return
            elif not cur_node.right:
                cur_node.right = node
                return
            else:
                my_queue.append(cur_node.left)
                my_queue.append(cur_node.right)

    def add_v2(self, item=None):
        """构建一般二叉树"""
        node = TNode(item)
        if not self.root and self.root.data is None:
            self.root = node
            return
        my_queue = []
        my_queue.append(self.root)
        while True:
            cur_node = my_queue.pop(0)
            # 如果当前节点为空节点则跳过它，起到占位的作用
            if cur_node.data is None:
                continue
            if not cur_node.left:
                cur_node.left = node
                return
            elif not cur_node.right:
                cur_node.right = node
                return
            else:
                my_queue.append(cur_node.left)
                my_queue.append(cur_node.right)

    def pre_travel(self, node):
        """前序遍历: 根-左-右"""
        if not node:  # 空树
            return

        print(node.data, end=', ')
        self.pre_travel(node.left)
        self.pre_travel(node.right)

    def mid_travel(self, node):
        """中序遍历: 左-根-右"""
        if not node:
            return

        self.mid_travel(node.left)
        print(node.data, end=', ')
        self.mid_travel(node.right)

    def post_travel(self, node):
        """后序遍历: 左-右-根"""
        if not node:
            return

        self.post_travel(node.left)
        self.post_travel(node.right)
        print(node.data, end=', ')

    def bread_travel(self):
        """层次遍历，广度遍历"""
        if self.root is None:
            return
        my_queue = [self.root]
        while my_queue:
            cur_node = my_queue.pop(0)
            print(cur_node.data, end=', ')
            if cur_node.left is not None:
                my_queue.append(cur_node.left)
            if cur_node.right is not None:
                my_queue.append(cur_node.right)

    def pre_travel_stack(self, root):
        """利用堆栈实现树的先序遍历"""
        if not root:
            return
        my_stack = []
        node = root
        while node or my_stack:
            while node:   # 从根节点开始，一直找它的左子树
                print(node.data, end=', ')
                my_stack.append(node)
                node = node.left
            node = my_stack.pop()  # while结束表示当前节点node为空，即前一个节点没有左子树了
            node = node.right      # 开始查看它的右子树

    def mid_travel_stack(self, root):
        """利用堆栈实现中序遍历"""
        if not root:
            return
        my_quene = []
        node = root
        while node or my_quene:
            while node:
                my_quene.append(node)
                node = node.left
            node = my_quene.pop()
            print(node.data, end=', ')
            node = node.right

    def post_travel_stack(self, root):
        """利用堆栈实现后序遍历"""
        if not root:
            return
        my_stack1 = []
        my_stack2 = []
        node = root
        my_stack1.append(node)
        while my_stack1:  # 这个while循环的功能是找出后序遍历的逆序，存在myStack2里面
            node = my_stack1.pop()
            if node.left:
                my_stack1.append(node.left)
            if node.right:
                my_stack1.append(node.right)
            my_stack2.append(node)
        while my_stack2:  # 将myStack2中的元素出栈，即为后序遍历次序
            print(my_stack2.pop().data, end=', ')


class BSTree(object):
    """
    二叉搜索树类：左节点值小于根节点值，右节点值大于根节点值
    """
    def __init__(self, node=None):
        self.root = node
        self.size = 0

    def insert(self, val):
        """
        二叉树插入操作: 若插入节点的值比根节点值小，则将其插入根节点的左子树；
        若比根节点值大，则插入到根节点右子树
        """
        if self.root is None:
            self.root = TNode(val)
        else:
            self.insert_node(val, self.root)

    def insert_node(self, val, bt_node):
        if val < bt_node.data:
            if bt_node.left is None:
                bt_node.left = TNode(val)
                return
            self.insert_node(val, bt_node.left)
        elif val > bt_node.data:
            if bt_node.right is None:
                bt_node.right = TNode(val)
                return
            self.insert_node(val, bt_node.right)

    def insert_loop(self, key):
        """循环版本"""
        node = TNode(key)
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
        """查询最小值: 最左节点"""
        if root.left:
            return self.find_min(root.left)
        return root

    def find_max(self, root):
        """查询最大值: 最右子节点"""
        if root.right:
            return self.find_max(root.right)
        return root

    def delete(self, root, key):
        """
        case1：待删除节点为叶子节点，直接删除
        case2：待删除节点只有左子树或只有右子树，则把其左子树或右子树代替为待删除节点
        case3：待删除节点既有左子树又有右子树，找到该节点右子树中最小值节点，使用该节点代替待删除节点，然后在右子树中删除最小值节点。
        :param key:
        :return:
        """
        if root is None:
            return
        if key < root.data:
            root.left = self.delete(root.left, key)
        elif key > root.data:
            root.right = self.delete(root.right, key)
        else:
            # 叶子节点，直接删除
            if root.left is None and root.right is None:
                root = None
            # 只有左子树或右子树
            elif root.left is None:
                root = root.left
            elif root.right is None:
                root = root.right
            # 既有左子树又有右子树
            elif root.left and root.right:
                tmp_node = self.find_min(root.right)  # 找到右子树中最小值节点
                root.val = tmp_node.data               # 替换待删除节点值
                root.right = self.delete(root.right, tmp_node.data)  # 删除右子树中最小值节点
        return root

    def print_tree(self, node):
        if node is None:
            return
        print(node.data, end=', ')
        self.print_tree(node.left)
        self.print_tree(node.right)


def BTree_test():
    tree = BTree()
    tree.add(0)
    tree.add(1)
    tree.add(2)
    tree.add(3)
    tree.add(4)
    tree.add(5)
    tree.add(6)
    tree.add(7)
    tree.add(8)
    tree.add(9)

    print('前序遍历:\n')
    tree.pre_travel(tree.root)
    print('\n')
    tree.pre_travel_stack(tree.root)
    print('\n')
    print('中序遍历:\n')
    tree.mid_travel(tree.root)
    print('\n')
    tree.mid_travel_stack(tree.root)
    print('\n')
    print('后续遍历:\n')
    tree.post_travel(tree.root)
    print('\n')
    tree.post_travel_stack(tree.root)
    print('\n')
    print('层次遍历:\n')
    tree.bread_travel()


def BSTree_test():
    tree1 = BSTree()
    for i in [17, 5, 2, 16, 35, 29, 38]:
        tree1.insert_loop(i)
    tree1.print_tree(tree1.root)

    print('\n')
    tree2 = BSTree()
    for i in [17, 5, 2, 16, 35, 29, 38]:
        tree2.insert(i)
    tree2.print_tree(tree2.root)

    print('删除节点:\n')

if __name__ == "__main__":
    # BTree_test()

    BSTree_test()