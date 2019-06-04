#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/add-and-search-word-data-structure-design/description/

Design a data structure that supports the following two operations:
void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string
containing only letters a-z or .
A . means it can represent any one letter.

For example:

addWord("bad")
addWord("dad")
addWord("mad")
search("pad") -> false
search("bad") -> true
search(".ad") -> true
search("b..") -> true

Note:
You may assume that all words are consist of lowercase letters a-z.

當遇到.時，node dict裡的values 全上.
題目要找的是whole word, 不是substring.
故底為None是必要的條件。

Use trie.
"""


class WordDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        root = self.root

        for c in word:
            # set key: c, value: dict and return value.
            # iff key c doesn't exist at dict.
            root = root.setdefault(c, dict())

        # 重要! 每個Trie都要注意! 將None作為底加入Key/Value
        root[None] = None

    def search(self, word):
        """
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        # init the list of dict, as we'll interate through it.
        nodes = [self.root]

        for char in word:
            # filter: function 為None 時(item for item in iterable if item)
            # https://docs.python.org/3/library/functions.html#filter
            # If function is None, the identity function is assumed,
            # that is, all elements of iterable that are false are removed.
            nodes = [subnode
                     for node in nodes
                     for subnode in ([node[char]]  # list of dict
                                     if char in node else
                                     filter(None, (node.values()))
                                     if char == "." else [])
                     ]

        for n in nodes:
            if None in n:
                return True
        return False

        # --------------------------------------
        # 第二解法:
        nodes = [self.root]

        for char in word:
            nodes = [kid for node in nodes for kid in
                     ([node[char]] if char in node else
                      filter(None, node.values()) if char == '.' else [])]

        return any(None in node for node in nodes)

class WordDictionaryRewrite(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = {}

    def addWord(self, word):
        """
        Adds a word into the data structure.
        :type word: str
        :rtype: void
        """
        root = self.root

        for c in word:
            print(c)
            r = root.setdefault(c, {})
            root = r

        root[None] = None


    def search(self, word):
        """
        Returns if the word is in the data structure.
        A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool

        Use BFS!!!
        """

        root = [self.root]  # list of dict key entry

        for c in word:
            root = [m for r in root for m in (
                [r[c]] if c in r else
                filter(None, r.values()) if c == "." else []
                )] # as generator


        return any(None in node for node in root)

        nodes = [self.root]

        for char in word:
            nodes = [kid for node in nodes for kid in
                     ([node[char]] if char in node else
                      filter(None, node.values()) if char == '.' else [])]

        return any(None in node for node in nodes)


"""
Your WordDictionary object will be instantiated and called as such:
obj = WordDictionary()
obj.addWord(word)
param_2 = obj.search(word)
"""

if __name__ == "__main__":
    s = WordDictionary()
    s.addWord("ru")
    print(s.search("r.."))

    print("----------\n\n")

    s = WordDictionaryRewrite()
    s.addWord("ru")
    print(s.search("r.."))
