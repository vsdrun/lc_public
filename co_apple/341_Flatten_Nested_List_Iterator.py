#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/flatten-nested-list-iterator/description/

Given a nested list of integers, implement an iterator to flatten it.

Each element is either an integer,
or a list -- whose elements may also be integers or other lists.

Example 1:
Given the list [[1,1],2,[1,1]],
By calling next repeatedly until hasNext returns false,
the order of elements returned by next should be: [1,1,2,1,1].


Example 2:
Given the list [1,[4,[6]]],
By calling next repeatedly until hasNext returns false, the order of elements
returned by next should be: [1,4,6].

注意!
這是有多層list in list, 不單只有一層.

由後往前塞入 list 為底的 stack.
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """


class NestedIterator(object):

    def __init__(self, nestedList):
        """
        Initialize your data structure here.
        :type nestedList: List[NestedInteger]
        """
        """
        想法, 將list內容訪入stack 然後一個個pop出來.
        遇到list, 直接放入stack, 待pop()時發現為list再解開放入stack
        """
        self.stack = [e for e in nestedList[::-1]]
        print(self.stack)

    def next(self):
        """
        :rtype: int
        """
        val = self.stack.pop()
        return val.getInteger()

    def hasNext(self):
        """
        :rtype: bool
        """
        if len(self.stack) > 0:
            if not self.stack[-1].isInteger():
                while len(self.stack) > 0 and not self.stack[-1].isInteger():
                    val = self.stack.pop()
                    val = val.getList()
                    self.stack += [e for e in val[::-1]]
            if not self.stack:
                return False

            return True
        else:
            return False


# Your NestedIterator object will be instantiated and called as such:
# i, v = NestedIterator(nestedList), []
# while i.hasNext(): v.append(i.next())

def build():
    return [[1, [3, 2, [1, 2]]], 2, [1, 1]]
    return [[1, 1], 2, [1, 1]]
    return [9, [1, [3, 2, [1, 2]]], 2, [1, 1]]
    return [[[8], 4]]


if __name__ == "__main__":
    s = NestedIterator(build())
    v = []

    while s.hasNext():
        v.append(s.next())

    print(v)
