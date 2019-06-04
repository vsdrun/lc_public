#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/

Given a binary search tree,
write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

Example 1:

Input: root = [3,1,4,null,2], k = 1
   3
  / \
 1   4
  \
   2
Output: 1

Example 2:
Input: root = [5,3,6,2,4,null,null,1], k = 3
       5
      / \
     3   6
    / \
   2   4
  /
 1
Output: 3


Follow up:
What if the BST is modified (insert / delete operations) often and you need to
find the kth smallest frequently? How would you optimize the kthSmallest
routine?
"""

# Definition for a binary tree node.


class TreeNode(object):

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):

    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        for val in self.inorder(root):
            if k == 1:
                return val
            else:
                k -= 1

    def inorder(self, root):
        if root is not None:
            for val in self.inorder(root.left):
                yield val

            yield root.val

            for val in self.inorder(root.right):
                yield val

def build():
    """
       5
      / \
     3   6
    / \
   2   4
  /
 1
    """
    _1 = TreeNode(1)
    _2 = TreeNode(2)
    _3 = TreeNode(3)
    _4 = TreeNode(4)
    _5 = TreeNode(5)
    _6 = TreeNode(6)

    _5.left = _3
    _5.right = _6
    _3.left = _2
    _3.right = _4
    _2.left = _1
    return _5

if __name__ == "__main__":
    s = Solution()
    print(s.kthSmallest(build(), 2))
