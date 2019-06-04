#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/maximum-binary-tree/description/


Given an integer array with no duplicates.
A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from
left part subarray divided by the maximum number.

The right subtree is the maximum tree constructed from right
part subarray divided by the maximum number.

Construct the maximum tree by the given array and output the
root node of this tree.

Example 1:
Input: [3,2,1,6,0,5]
Output: return the tree root node representing the following tree:

      6
    /   \
   3     5
    \    /
     2  0
       \
        1
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def construct(r, lt, rt):
            if r is None:
                return r

            root = TreeNode(r)

            lroot = max(lt + [None])
            rroot = max(rt + [None])

            root.left = construct(lroot, lt[:lt.index(lroot)],
                                  lt[lt.index(lroot) + 1:]) if lroot is not \
                None else None

            root.right = construct(rroot, rt[:rt.index(rroot)],
                                   rt[rt.index(rroot) + 1:]) if rroot is not \
                None else None

            return root

        if not nums:
            return None

        root = max(nums)
        lt = nums[:nums.index(root)]
        rt = nums[nums.index(root) + 1:]

        return construct(root, lt, rt)

    def rewrite(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        def build(nums):
            """
            recursive call
            1. extract max
            2. recursive call left, right
            3. return max to upper layer
            """
            if not nums:
                return None
            mx = max(nums)
            idx = nums.index(mx)
            root = TreeNode(mx)
            root.left = build(nums[:idx])
            root.right = build(nums[idx + 1:])

            return root

        return build(nums)


def build():
    return [3, 2, 1, 6, 0, 5]


def prt(root):

    root = [root]

    while root:
        tmp_root = []
        prt = []
        for r in root:
            prt += r.val,
            if r.left:
                tmp_root += r.left,
            if r.right:
                tmp_root += r.right,

        print(prt)
        root = tmp_root


if __name__ == "__main__":
    s = Solution()
    n = s.constructMaximumBinaryTree(build())
    prt(n)
