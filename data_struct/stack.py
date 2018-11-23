#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
模块功能：1、实现栈类
         2、栈的应用：括号匹配问题；符号匹配问题；十进制转换二进制；前缀表达式和后缀表达式等
"""


class MyStack(object):
    """ 栈类 """
    def __init__(self):
        self.stack = []

    def push(self, value):
        self.stack.append(value)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()

    def top(self):
        if not self.is_empty():
            return self.stack[len(self.stack)-1]
        else:
            return None

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        return False

    def print_stack(self):
        if not self.stack:
            print('stack is empty')
        else:
            for i in range(len(self.stack)):
                print(self.stack[i])


def stack_test():
    """ 测试栈 """
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


def par_checker(symbol_str):
    """
    栈的应用：括号检查，用于检查括号是否匹配
    NOTE: 暂时认为symbol_str里全部都是括号，不存在其他字符
    :param symbol_str: 括号字符串
    :return: True or False
    """
    if not symbol_str:
        return False
    index = 0
    flag = True
    my_stack = MyStack()
    while flag and index < len(symbol_str):
        symbol = symbol_str[index]
        if symbol == '(':
            my_stack.push(symbol)
        else:
            if my_stack.is_empty():
                flag = False
            else:
                my_stack.pop()
        index += 1
    if flag and my_stack.is_empty():
        return True
    else:
        return False


def par_checker_test():
    symbol_str1 = "((()))"
    symbol_str2 = "(()()())"
    symbol_str3 = "(()()()"
    symbol_str4 = "(()()))"
    symbol_str5 = "()()()"
    symbol_str6 = "()aaa()()"
    print(par_checker(symbol_str1))  # True
    print(par_checker(symbol_str2))  # True
    print(par_checker(symbol_str3))  # False
    print(par_checker(symbol_str4))  # False
    print(par_checker(symbol_str5))  # True
    print(par_checker(symbol_str6))  # True


if __name__ == "__main__":
    # stack_test()

    # par_checker_test()

