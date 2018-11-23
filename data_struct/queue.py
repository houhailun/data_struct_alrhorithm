#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
模块功能：实现队列类:尾部插入，头部删除
"""


class MyQueue(object):
    """ 队列类 """
    def __init__(self):
        self.queue = []

    def enqueue(self, val):
        self.queue.append(val)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0)

    def is_empty(self):
        return self.queue == []

    def size(self):
        return len(self.queue)


class MyDeque(object):
    """ 双端队列：既可以在头部插入删除又可以在尾部插入删除 """
    def __init__(self):
        self.deque = []

    def is_empty(self):
        return self.deque == []

    def add_front(self, val):
        self.deque.insert(0, val)

    def add_tail(self, val):
        self.deque.append(val)

    def del_front(self):
        if not self.is_empty():
            self.deque.pop(0)

    def del_tail(self):
        if not self.is_empty():
            self.deque.pop()

    def size(self):
        return len(self.deque)


def queue_test():
    my_queue = MyQueue()
    my_queue.enqueue(10)
    my_queue.enqueue('dog')
    print(my_queue.queue)

    my_queue.dequeue()
    print(my_queue.queue)

    print(my_queue.size())


def deque_test():
    my_deque = MyDeque()
    my_deque.add_front(10)
    my_deque.add_tail('dog')
    my_deque.add_front('cat')
    print(my_deque.deque)

    my_deque.del_front()
    print(my_deque.deque)


if __name__ == "__main__":
    # queue_test()

    deque_test()
