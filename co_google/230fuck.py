#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/kth-smallest-element-in-a-bst/


Given a binary search tree,
write a function kthSmallest to find the kth smallest element in it.

Note:
You may assume k is always valid, 1 ≤ k ≤ BST's total elements.

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
        if root:
            print("root.val :{}".format(root.val))
        else:
            print("None")

        if root is not None:
            for val in self.inorder(root.left):
                print("val: {}".format(val))
                yield val

            yield root.val

            for val in self.inorder(root.right):
                yield val


def build_input():
    """
    Wrong input...
    """
    root = TreeNode(None)
    root.left = TreeNode(1)
    root.right = TreeNode(2)
    return root


if __name__ == "__main__":
    r = build_input()

    s = Solution()
    result = s.kthSmallest(r, 2)

    print(result)
