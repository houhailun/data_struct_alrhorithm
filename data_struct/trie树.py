#!/usr/bin/env python
# -*- coding:utf-8 -*-
# Time: 2019/12/19 16:35
# Author: Hou hailun

# 用于实现搜索引擎的搜索关键字提示功能
# Trie树，也叫字典树，它是一个树形结构，专门处理字符串匹配的数据结构，用来解决在一组字符串集合中快速查找某个字符串的问题
# Trie树的本质，就是利用字符串之间的公共前缀，将重复的前缀合并在一起。
# 构造过程：每一步，都相当于往trie树中插入一个字符串
# 从根节点到红色节点之间构成一个字符串


class Trie:
    def __init__(self):
        self.root = {}
        self.end = -1

    def insert(self, word):
        # 插入word，时间复杂度为O(N)
        # 从根节点遍历单词,char by char,如果不存在则新增,最后加上一个单词结束标志
        curNode = self.root
        for c in word:
            if not c in curNode:
                curNode[c] = {}
            curNode = curNode[c]
        curNode[self.end] = True  # 结束标志位

    def search(self, word):
        # 搜索word, 时间复杂度为O(K)
        curNode = self.root
        for c in word:
            if not c in curNode:
                return False
            curNode = curNode[c]

        # 没有结束
        if not self.end in curNode:
            return False
        return True

    def startswith(self, prefix):
        # 是否有前缀prefix
        curNode = self.root
        for c in prefix:
            if not c in curNode:
                return False
            curNode = curNode[c]
        return True


if __name__ == "__main__":
    trie = Trie()
    trie.insert('hello')
    trie.insert('hi')
    trie.insert('her')
    trie.insert('see')
    trie.insert('so')

    print(trie.root)
    print(trie.search('her'))
    print(trie.startswith('he'))
