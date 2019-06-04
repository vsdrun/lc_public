#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/most-frequent-subtree-sum/description/


Given the root of a tree, you are asked to find the most frequent subtree sum.
The subtree sum of a node is defined as the sum of all the node values
formed by the subtree rooted at that node (including the node itself).

So what is the most frequent subtree sum value?

If there is a tie,
return all the values with the highest frequency in any order.

Examples 1
Input:
  5
 /  \
2   -3
return [2, -3, 4], since all the values happen only once, return all of them in any order.



Examples 2
Input:

  5
 /  \
2   -5
return [2], since 2 happens twice, however -5 only occur once.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        from collections import Counter as cc

        sum_set = []

        def get_sum(node):
            if not node:
                return 0

            lr_sum = 0

            if node.left:
                lr_sum += get_sum(node.left)

            if node.right:
                lr_sum += get_sum(node.right)

            sum_set.append(node.val + lr_sum)

            return node.val + lr_sum

        get_sum(root)
        cs = cc(sum_set)

        if len(set(cs.values())) == 1:
            return cs.keys()
        else:
            key = max(set(cs.itervalues()))
            return [k for k, v in cs.iteritems() if v == key]


def build():
    """
      5
     /  \
    2   -5
    """
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(-5)
    return root


if __name__ == "__main__":
    s = Solution()
    print(s.findFrequentTreeSum(build()))
