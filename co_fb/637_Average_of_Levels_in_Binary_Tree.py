#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/average-of-levels-in-binary-tree/description/

Given a non-empty binary tree,
return the average value of the nodes on each level in the form of an array.

Example 1:
Input:
    3
   / \
  9  20
    /  \
   15   7
Output: [3, 14.5, 11]

Explanation:
The average value of nodes on level 0 is 3,
on level 1 is 14.5, and on level 2 is 11. Hence return [3, 14.5, 11].
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        root = [root]
        result = []

        while root:

            result.append(sum([r.val for r in root]) / float(len(root)))

            root = [node for r in root for node in (r.left, r.right) if node]


        return result

def build():
    """
    3
   / \
  9  20
 /  /  \
8  15   7
    """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.left.left = TreeNode(8)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)
    return root


if __name__ == "__main__":
    s = Solution()
    print(s.averageOfLevels(build()))
