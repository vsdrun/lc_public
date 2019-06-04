#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/

You need to find the largest value in each row of a binary tree.

Example:
Input:

          1
         / \
        3   2
       / \   \
      5   3   9

Output: [1, 3, 9]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        BFS~
        """

        if not root:
            return []

        queue = [root]
        result = []

        while queue:
            result.append(max([q.val for q in queue if q]))

            tmpq = []

            for q in queue:
                if q.left:
                    tmpq.append(q.left)
                if q.right:
                    tmpq.append(q.right)

            queue = tmpq

        return result


def build():
    """
          1
         / \
        3   2
       / \   \
      5   3   9
    """
    root = TreeNode(1)
    root.left = TreeNode(3)
    root.right = TreeNode(2)
    root.right.right = TreeNode(9)
    root.left.left = TreeNode(5)
    root.left.right = TreeNode(3)
    return root


if __name__ == "__main__":
    s = Solution()
    print(s.largestValues(build()))
