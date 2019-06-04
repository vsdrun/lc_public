#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/description/

Given an array where elements are sorted in ascending order,
convert it to a height balanced BST.

For this problem,
a height-balanced binary tree is defined as a binary tree in
which the depth of the two subtrees of every node never differ by more than 1.

Example:
Given the sorted array: [-10,-3,0,5,9],
One possible answer is: [0,-3,9,-10,null,5],
which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return

        def build(root_val, left_ary, right_ary):
            root = TreeNode(root_val)

            root.left = build(left_ary[len(left_ary) / 2],
                              left_ary[:len(left_ary) / 2],
                              left_ary[len(left_ary) / 2 + 1:]) if left_ary else \
                None

            root.right = build(right_ary[len(right_ary) / 2],
                               right_ary[:len(right_ary) / 2],
                               right_ary[len(right_ary) / 2 + 1:]) if right_ary else \
                None
            return root

        return build(nums[len(nums) / 2],
                     nums[:len(nums) / 2],
                     nums[len(nums) / 2 + 1:])


def build():
    return [-10, -3, 0, 5, 9]


def pp(node):
    nodes = [node]

    while nodes:
        print([n.val for n in nodes])

        nodes = [i for n in nodes for i in (n.left, n.right) if i]


if __name__ == "__main__":
    s = Solution()
    r = s.sortedArrayToBST(build())
    pp(r)
