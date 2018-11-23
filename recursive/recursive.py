#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
模块功能：递归
"""


def move_tower(from_pole, to_pole):
    print("move disk from %s to %s" % (from_pole, to_pole))


def hanno_tower(height, from_pole, with_pole, to_pole):
    """
    汉诺塔游戏，伪代码：利用目标杆把n-1个圆盘放到中间杆；把最后一个圆盘放到目标杆；利用起始杆把n-1个圆盘放到目标杆
    """
    if height:
        hanno_tower(height-1, from_pole, to_pole, with_pole)
        move_tower(from_pole, to_pole)
        hanno_tower(height-1, with_pole, from_pole, to_pole)


def
if __name__ == "__main__":

    hanno_tower(5, 'A', 'B', 'C')