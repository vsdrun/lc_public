#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/symmetric-tree/description/


Given a binary tree,
check whether it is a mirror of itself (ie, symmetric around its center).


For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3


But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        BFS, 先把root放到list內~
            1
           / \
          2   2
         / \ / \
        3  x 4  3
        """

        if not root:
            return True

        r = [root]

        while r:
            for i in range(len(r) / 2):
                if r[i] and r[~i] and r[i].val == r[~i].val:
                    continue
                if r[i] is r[~i]:
                    continue
                return False

            r = [n for node in r if node for n in (node.left, node.right)]

        return True

def build():
    """
        1
       / \
      2   2
     / \ / \
    3  X 4  3
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)

    root.right.right = TreeNode(3)
    root.right.left = TreeNode(4)

    root.left.left = TreeNode(3)
    root.left.right = TreeNode(None)
    return root


if __name__ == "__main__":
    s = Solution()
    print(s.isSymmetric(build()))
