#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/nested-list-weight-sum-ii/description/


Given a nested list of integers,
return the sum of all integers in the list weighted by their depth.

Each element is either an integer,
or a list -- whose elements may also be integers or other lists.

Different from the previous question where weight is increasing from
root to leaf, now the weight is defined from bottom up.

i.e., the leaf level integers have weight 1,
and the root level integers have the largest weight.

Example 1:
Given the list [[1,1],2,[1,1]], return 8.
(four 1's at depth 1, one 2 at depth 2)

Example 2:
Given the list [1,[4,[6]]], return 17.
(one 1 at depth 3, one 4 at depth 2, and one 6 at depth 1; 1*3 + 4*2 + 6*1 = 17)
"""

# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
# class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
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


class Solution(object):
    def depthSumInverse(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int

        使用stack.
        stack len 為 level cnt.
        """
        stack = []

        def doDfs(nl):

            c_sum = sum([n.getInteger() for n in nl if n.isInteger()])

            # 用sum因為將一堆list合成一個list
            next_nl = sum([n.getList() for n in nl if not n.isInteger()], [])

            if next_nl:
                doDfs(next_nl)

            stack.append(c_sum)

        doDfs(nestedList)

        total = 0

        while stack:
            total += len(stack) * stack.pop()

        return total

        # ----------- SMART
        # 最外圍的每次都加 也就是 n * level_cnt的概念.
        fin_sum, cur_sum, acc_sum = 0, 0, 0
        cur_list = nestedList
        nxt_list = []

        while cur_list:
            for elt in cur_list:
                if elt.isInteger():
                    cur_sum += elt.getInteger()
                else:
                    l = elt.getList()
                    for n in l:
                        nxt_list += [n]
            fin_sum = fin_sum + cur_sum + acc_sum
            acc_sum = acc_sum + cur_sum  # 給下一層加的目前的值!
            cur_sum = 0

            cur_list = nxt_list
            nxt_list = []

        return fin_sum

    def rewrite(self, nestedList):
        """
        :type nestedList: List[NestedInteger]
        :rtype: int

        使用stack.
        stack len 為 level cnt.
        """
        nn = nestedList

        stack = []



def build():
    return [1, [4, [6]]]


if __name__ == "__main__":
    s = Solution()
    print(s.depthSumInverse(build()))
