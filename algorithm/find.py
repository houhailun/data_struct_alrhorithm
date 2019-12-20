#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
模块功能：实现python的查找算法，包括：顺序查找、二分查找、插值差值、斐波那契查找、树表查找、哈希查找
"""


class Search(object):
    """查找算法类"""
    def __init__(self):
        self.data = [10, -3, 34, 56, 97, 100]

    def sequent_search(self, key):
        """
        顺序查找：顾名思义就是从序列开始逐个查找
        时间复杂度：O(N)
        :return:
        """
        flag = False
        for val in self.data:
            if val == key:
                flag = True
                break
        return flag, key

    def binary_search(self, key):
        """
        二分查找：前提条件为序列是有序的或者基本有序
        思想：中间元素等于key，则ok；中间元素大于key，则在左子序列查找；否则在右子序列查找
        时间复杂度:O(logN)

        注意点：
            1、循环终止条件 start <= end
                分析为什么是<=而不是<
                假设a={1,2,3};要查找的num=3;
                第一步，low=0,high=2,mid=1;a[mid]<3,所以low=mid+1=2;
                如果循环跳出条件是low<high,此时就跳出循环了，得出结果 -1，所以需要<=
            2、mid的取值
                mid = (start+end)/2, 当start，end很大时可能造成溢出，可以改为low+(high-low)//2, 进一步可写为low+(high-low)>>1
            3、start,end的更新

        局限性：
            1、二分查找依赖顺序表结构，简单来说就是数组。链表不能用二分，因为二分是根据下标随机访问元素的
            2、二分查找针对的是有序数据，所以二分使用于插入、删除操作不频繁，一次排序多次查找的场景
            3、数据量太小不适合二分查找
                例外：数据之间的比较非常耗时，不管数据量大小，推荐使用二分查找，为了减小比较次数
            4、数据量太大也不适合二分查找
                二分查找的底层依赖数组这种数据结构，数组为了支持随机访问，要求内存空间连续，对内存要求较苛刻。
        :param key:
        :return:
        """
        array = self.data.copy()
        array.sort()
        start = 0
        end = len(array) - 1
        flag = False
        while start <= end:
            mid = (start + end) // 2
            if array[mid] == key:
                flag = True
                break
            elif array[mid] < key:  # 右子序列
                start = mid + 1
            else:                   # 左子序列
                end = mid - 1

        return flag, key

    def insert_search(self, key):
        """
        差值查找：前提条件：序列有序，mid =low+(high-low)*(key-a[low])/(a[high]-a[low])
        对于表长较大，而关键字分布又比较均匀的查找表来说，插值查找算法的平均性能比折半查找要好得多
        """
        array = self.data.copy()
        array.sort()
        start = 0
        end = len(array) - 1
        flag = False
        while start < end:
            mid = start + (end - start) * (key - array[start]) // (array[end] - array[start])
            if array[mid] == key:
                flag = True
                break
            elif array[mid] < key:  # 右子序列
                start = mid + 1
            else:  # 左子序列
                end = mid - 1

        return flag, key

    def Fibnacio_search(self, key):
        """
        斐波那契查找：主要是利用斐波那契性质a[i] = a[i-1]+a[i-2]
        :param key:
        :return:
        """
        pass


class BSTNode:
    """
    二叉搜索树节点类
    """
    def __init__(self, data, left=None, right=None):
        """
        初始化节点
        :param data: 数据
        :param left: 左节点指针
        :param right: 右节点指针
        """
        self.data = data
        self.left = left
        self.right = right


class BinarySortTree:
    """二叉搜索树类"""
    def __init__(self):
        self._root = None

    def is_empty(self):
        return self._root is None

    def search(self, key):
        """
        关键字建索
        :param key:
        :return: 查找节点或None
        """
        bt = self._root
        while bt:
            entry = bt.data
            if entry > key:
                bt = bt.left
            elif entry < key:
                bt = bt.right
            else:
                return bt
        return None

    def insert(self, key):
        """
        插入操作
        :param key: 关键码
        :return: 布尔值
        """
        bt = self._root
        if not bt:  # 根节点
            self._root = BSTNode(key)
            return
        while True:
            entry = bt.data
            if key < entry:  # 左节点
                if bt.left is None:
                    bt.left = BSTNode(key)
                    return
                bt = bt.left
            elif key > entry:  # 右节点
                if bt.right is None:
                    bt.right = BSTNode(key)
                    return
                bt = bt.right
            else:
                bt.data = key
                return

    def delete(self, key):
        """
        删除操作
        :param key: 关键码
        :return: 布尔值
        """
        p, q = None, self._root  # 维持p为q的父节点，用于链接操作
        if not q:
            print("空树!")

        # 在树中查找key
        while q and q.data != key:
            p = q
            if key < q.data:
                q = q.left
            else:
                q = q.right
            if not q:  # 当树中没有关键码key时，结束退出
                return

        # 这里已经找到了要删除的节点，用q引用，p是q的父节点或者None（q是根节点）
        pass

    def iter(self, node):
        """中序遍历可得到有序序列:左、根、右"""
        stack = []
        if node:
            self.iter(node.left)
            stack.append(node.data)
            self.iter(node.right)
        return stack


class HashTable:
    """
    哈希表就是一种以键-值(key-indexed) 存储数据的结构，只要输入待查找的值即key，即可查找到其对应的值
    算法思想
        哈希的思路很简单，如果所有的键都是整数，那么就可以使用一个简单的无序数组来实现：将键作为索引，值即为其对应的值，这样就可以快速访问任意键的值。
        这是对于简单的键的情况，我们将其扩展到可以处理更加复杂的类型的键
    算法流程
　　  1）用给定的哈希函数构造哈希表；
　　  2）根据选择的冲突处理方法解决地址冲突；常见的解决冲突的方法：拉链法和线性探测法。
　　  3）在哈希表的基础上执行哈希查找。
    哈希函数：一种映射关系，根据key通过一定的函数关系，计算出该元素存储位置的函数；
    常用的哈希函数有：
        直接定址法：即取关键字或关键字的线性函数计算地址，表示为：Hash(key)=key或Hash(key)=a*key+b
        除留余数法：取关键字被某个不大于哈希表长度m的数p求余，表示为：hash(key)=key % p, p<=m
        数字分析法、平方取中法、折叠法、随机数法等
    复杂度分析: 单纯论查找复杂度：对于无冲突的Hash表而言，查找复杂度为O(1)（注意，在查找之前我们需要构建相应的Hash表）
    """
    def __init__(self, size):
        self.elem = [None] * size  # 哈希表
        self.count = size          # 最大表长

    def hash(self, key):
        return key % self.count  # 散列函数采用除留余数法

    def insert_hash(self, key):
        """插入关键字到和哈希表"""
        address = self.hash(key)
        while self.elem[address]:  # 当前位置有数据，发生冲突
            address = (address+1) % self.count  # 线性探测下一位置是否可用
        self.elem[address] = key

    def search_hash(self, key):
        """查找关键字"""
        star = address = self.hash(key)
        while self.elem[address] != key:
            address = (address+1) % self.count
            if not self.elem[address] or address == star:  # 说明没找到或者循环到了开始的位置
                return False
            return True


class BinarySearchConvert:
    # 二叉查找的变形问题
    def __init__(self):
        self.array = [1, 2, 2, 3, 3, 4, 5, 6, 7, 8]

    def find_first_key(self, num):
        # 在可能有重复元素的数组中，查找第一个等于key的元素
        data = self.array.copy()
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] < num:
                low = mid + 1
            elif data[mid] > num:
                high = mid - 1
            elif mid == 0 or data[mid-1] != num:  # mid=0或者前一个元素不等于num，表示找到了第一个
                return mid
            else:                                 # 相等但不是第一个，则在左半区间查
                high = mid - 1
        return -1

    def find_last_key(self, num):
        # 在可能有重复元素的数组中，查找最后一个等于key的元素
        data = self.array.copy()
        low = 0
        high = len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] > num:
                high = mid - 1
            elif data[mid] < num:
                low = mid + 1
            elif mid == len(data)-1 or data[mid+1] != num:  # mid==len(data),或者下一个元素不等于num，表示已经找到最后一个
                return mid
            else:
                low = mid + 1
        return -1

    def find_firse_large_equal_key(self, num):
        # 在可能有重复元素的数组中，查找第一个大于等于 num 的元素
        data = self.array.copy()
        low, high = 0, len(data)-1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] >= num:                   # mid下标值大于等于num
                if mid == 0 or data[mid-1] < num:  # mid==0 或者 前一个元素小于num，则当前元素满足
                    return mid
                else:                              # 不是第一个往必然在左半区间内
                    high = mid - 1
            else:
                low = mid + 1
        return -1

    def find_last_less_equal_key(self, num):
        # 在可能有重复元素的数组中，查找最后一个小于key的元素
        data = self.array.copy()
        low, high = 0, len(data) - 1
        while low <= high:
            mid = (low + high) // 2
            if data[mid] <= num:                             # mid下标值小于等于num
                if mid == len(data)-1 or data[mid+1] > num:  # mid是最后一个元素 或者 下一个元素大于num，则当前元素满足
                    return mid
                else:                                        # 不是最后一个，则必然在右半区间
                    low = mid + 1
            else:
                high = mid - 1
        return -1


if __name__ == "__main__":
    # search = Search()
    # print(search.sequent_search(34))
    # print(search.binary_search(34))
    # print(search.insert_search(34))

    obj = BinarySearchConvert()
    print(obj.find_first_key(3))
    print(obj.find_last_key(3))
    print(obj.find_firse_large_equal_key(3))
    print(obj.find_last_less_equal_key(3))