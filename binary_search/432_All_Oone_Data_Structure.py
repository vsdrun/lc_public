#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/all-oone-data-structure/

Implement a data structure supporting the following operations:

Inc(Key) - Inserts a new key with value 1. Or increments an existing key by 1. Key is guaranteed to be a non-empty string.

Dec(Key) - If Key's value is 1, remove it from the data structure.
Otherwise decrements an existing key by 1. If the key does not exist, this function does nothing. Key is guaranteed to be a non-empty string.

GetMaxKey() - Returns one of the keys with maximal value. If no element exists, return an empty string "".

GetMinKey() - Returns one of the keys with minimal value. If no element exists, return an empty string "".

Challenge: Perform all these in O(1) time complexity.
"""

# 可以用Counter :-p
# 其實就是要妳實做Counter
# 使用bisect with sorted array

import bisect as bi

class AllOne(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dmap = dict()
        self.sarry = []

    def inc(self, key):
        """
        Inserts a new key <Key> with value 1. Or increments an existing key by 1.
        :type key: str
        :rtype: None
        """

        if key in self.dmap:
            didx = bi.bisect_right(self.sarry, (self.dmap[key], key)) - 1
            self.sarry = self.sarry[:didx] + self.sarry[didx+1:]
            self.dmap[key] += 1
        else:
            self.dmap[key] = 1

        bi.insort(self.sarry, (self.dmap[key], key))

    def dec(self, key):
        """
        Decrements an existing key by 1. If Key's value is 1, remove it from the data structure.
        :type key: str
        :rtype: None
        """
        if key in self.dmap:
            didx = bi.bisect_right(self.sarry, (self.dmap[key], key)) - 1
            self.sarry = self.sarry[:didx] + self.sarry[didx+1:]
            self.dmap[key] -= 1
        else:
            return

        if self.dmap[key] == 0:
            self.dmap.pop(key)
            return

        bi.insort(self.sarry, (self.dmap[key], key))

    def getMaxKey(self):
        """
        Returns one of the keys with maximal value.
        :rtype: str
        """
        return self.sarry[-1][1] if self.sarry else ""

    def getMinKey(self):
        """
        Returns one of the keys with Minimal value.
        :rtype: str
        """
        return self.sarry[0][1] if self.sarry else ""


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

def build():
    return


if __name__ == "__main__":
    """
["AllOne","inc","inc","inc","dec","inc","inc","getMaxKey","dec","dec","dec","getMaxKey"]
[[],["hello"],["world"],["hello"],["world"],["hello"],["leet"],[],["hello"],["hello"],["hello"],[]]

[null,null,null,null,null,null,null,"hello",null,null,null,"leet"]
    """
    s = AllOne()
    s.inc("hello")
    s.inc("world")
    s.inc("hello")
    s.dec("world")
    s.inc("hello")
    s.inc("leet")
    print(s.getMaxKey())
    s.dec("hello")
    s.dec("hello")
    s.dec("hello")
    print(s.getMaxKey())
