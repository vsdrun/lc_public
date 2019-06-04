#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/implement-trie-prefix-tree/description/

Implement a trie with insert, search, and startsWith methods.

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""

import collections as cc


class Trie(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = cc.defaultdict(dict)

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """

        root = self.root

        for c in word:
            if c not in root:
                root[c] = dict()
            root = root[c]

        root[None] = None

    def search(self, word, prefix=False):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self.root

        for c in word:
            if c in root:
                root = root[c]
            else:
                return False

        if not prefix and None in root:
            return True
        elif prefix:
            return True
        else:
            return False

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        return self.search(prefix, True)


class Trie_rewrite(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._dict = dict()

    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """

        root = self._dict

        for w in word:
            if w not in root:
                root[w] = dict()
                root = root[w]
            else:
                root = root[w]

        root[None] = None

    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        root = self._dict

        for w in word:
            if w not in root:
                return False
            root = root[w]

        if None not in root:
            return False
        return True

    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """

        root = self._dict

        for w in prefix:
            if w not in root:
                return False
            root = root[w]

        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

def build():
    return "Hello", "world"
    return "a"


if __name__ == "__main__":
    #  s = Trie()

    #  for v in build():
        #  s.insert(v)

    #  print(s.search("a"))
    #  print(s.startsWith("a"))

    s = Trie_rewrite()

    for v in build():
        s.insert(v)

    print(s.search("world"))
    print(s.startsWith("Hel"))
