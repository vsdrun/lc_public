#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/same-tree/description/

Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are
structurally identical and the nodes have the same value.


Example 1:
Input:     1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:
Input:     1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:
Input:     1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and \
                self.isSameTree(p.left, q.left) and \
                self.isSameTree(p.right, q.right)

        return p is q

    def rewrite(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        # 不要用encode/decode 慢..
        # 直接一個node一個node 比對.

        def isSame(r1, r2):
            """
            ret: True, same, False, not same.
            """
            if r1 and r2:
                if r1.val != r2.val:
                    return False

                return isSame(r1.left, r2.left) and isSame(r1.right, r2.right)

            return False if r1 != r2 else True

        return isSame(p, q)


def build():
    """
        1
       / \
      2   2
     / \ / \
    3  4 4  3
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    root.right.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)

    root2 = TreeNode(1)
    root2.left = TreeNode(2)
    root2.right = TreeNode(2)
    root2.right.right = TreeNode(3)
    root2.right.left = TreeNode(2)
    root2.left.left = TreeNode(3)
    root2.left.right = TreeNode(4)
    return root, root2


if __name__ == "__main__":
    s = Solution()
    print(s.isSameTree(*build()))
    print(s.rewrite(*build()))
