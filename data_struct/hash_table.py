#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2019/12/9 18:06
# Author: Hou hailun

# 哈希表，利用数组随机访问特性，可以认为数组的一种拓展
# 查找时间复杂度O(1)  插入/删除时间复杂度O(1)

# 散列函数的基本要求
#   1、散列函数计算得到的值是一个非负整数
#   2、若key1 = key2，则hash(key1) = hash(key2)
#   3、若key1 != key2, 则hash(key1) != hash(key2)
# 实际上第3点很难实现，称之为冲突(key1 != key2, 但是hash(key1) = hash(key2))
# 解决冲突的方法：
#   1、开放定址法
#         1.1 线性探测法
#         1.2 二次探测
#   2、链表法


"""
如何构建一个工业级的哈希表？
思路：何为工业级的哈希表？工业级的哈希表应该具有那些性质？
    1、支持快速的查询、插入、删除操作
    2、内存占用合理，不能浪费过多空间
    3、性能稳定，再极端情况下，哈希表的性能也不会到无法接受到情况
方案：如何设计这样一个散列表呢？
    1、设计一个合适的散列函数
    2、定义装载因子阈值，并且设计动态扩容策略
    3、选择合适的散列冲突解决方法
知识总结：
一、如何设计散列函数？
    1、要尽可能让散列后的值随机且均匀分布，这样会尽可能减小散列冲突，即使冲突后，分配到每个槽内的数据也比较均匀
    2、除此之外，散列函数的设计也不能太复杂，太复杂就会太消耗时间，也会影响到散列表的性能
    3、常见的散列函数设计方法：直接寻址法，平方取中法，折叠法，随机数法等
二、如何根据装载因子动态扩容？
1、如何设置装载因子阈值？
    1.1 可以通过设置装载因子阈值来控制是扩容还是缩容，支持动态扩容的散列表，插入数据的时间复杂度使用均摊分析法
    1.2 装载因子的阈值设置需要权衡时间复杂度和空间复杂度。如何权衡？
        如果内存空间不紧张，对执行效率要求很高，可以降低装载因子的阈值；相反，如果内存空间紧张，对执行效率要求又不高，可以增加装载因子的阈值
2、如何避免低效扩容？分批扩容
    2.1 分批扩容的插入操作：当有新数据要插入时，我们讲数据插入新的散列表，并从老的散列表中拿出一个数据放入新散列表。
        每次插入都是重复上面的过程，这样插入操作就变得很快
    2.2 分批扩容的查询操作: 先查新散列表，再差老散列表
    2.3 通过分批扩容的方式，再任何情况下，插入一个数据的时间复杂度都是O(1)
三、如何选择散列冲突解决方法？
    3.1 常见的2种方法：开放寻址发和链表法
    3.2 大部分情况下，链表法更加普适。而且，我们还可以通过将链表法中的链表改造称其他动态数据结构，比如红黑树，跳表，来避免散列表时间复杂度退化为O(n),
        抵御散列冲突攻击
    3.3 但是，对于小规模数据，装载因子不高的散列表，比较适合用开放寻址法
"""


class HashTable:
    def __init__(self, size):
        """
        哈希表初始化函数
        :param size: 哈希表容量大小
        """
        self.elem = [None] * size
        self.size = size

    def hash(self, item):
        """
        哈希函数(散列函数)
        :param item: 待插入元素
        :return:
        """
        return item % self.size

    def insert(self, item):
        """
        插入item到哈希表
        :param item: 待插入的元素
        :return:
        """
        addr = self.hash(item)
        while self.elem[addr]:  # 开放定址法--线性探测法，解决冲突
            addr = (addr + 1) % self.size

        self.elem[addr] = item

    def search(self, item):
        """
        查找操作
        :param item: 待查找的元素
        :return:
        """
        start = addr = self.hash(item)
        while self.elem[addr] != item or self.elem[addr] == 'deleted':  # 如果当前位置元素被删除，则往后查找
            addr = (addr + 1) % self.size
            # 查找失败条件
            # 1、循环了一圈没找到
            # 2、addr位置没有数据
            if not self.elem[addr] or addr == start:
                return False
        return True

    def delete(self, item):
        """
        删除操作
        :param item: 待删除的操作
        :return:
        """
        addr = self.hash(item)
        if self.elem[addr]:
            self.elem[addr] = 'deleted'



