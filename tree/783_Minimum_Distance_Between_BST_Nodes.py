#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/minimum-distance-between-bst-nodes/description/

Given a Binary Search Tree (BST) with the root node root,
return the minimum difference between the values of any two different
nodes in the tree.

Example :

Input: root = [4,2,6,1,3,null,null]
Output: 1
Explanation:
Note that root is a TreeNode object, not an array.

The given tree [4,2,6,1,3,null,null] is represented by the following diagram:

          4
        /   \
      2      6
     / \
    1   3

while the minimum difference in this tree is 1,
it occurs between node 1 and node 2, also between node 3 and node 2.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDiffInBST(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        # dfs traverse

        diff = [float("inf")]

        def dfs(root):
            """
            :ret: min, max
            """

            if not root:
                return
            lsmall = llarge = rsmall = rlarge = None

            if root.left:
                lsmall, llarge = dfs(root.left)
                diff[0] = min(diff[0], root.val - llarge.val)

            if root.right:
                rsmall, rlarge = dfs(root.right)
                diff[0] = min(diff[0], rsmall.val - root.val)

            if not lsmall:
                lsmall = root
            if not rlarge:
                rlarge = root

            return lsmall, rlarge

        dfs(root)

        return diff[0]

    def rewrite(self, root):
        """
        :type root: TreeNode
        :rtype: int

        using yield, inorder to trigger it, use for loop
        """

        def dfs(node):
            """
            yield!
            """
            if not node:
                return

            for v in dfs(node.left):
                yield v

            yield node

            for v in dfs(node.right):
                yield v

        previous = None
        mmin = float("inf")

        for n in dfs(root):
            if previous:
                mmin = min(mmin, n.val - previous.val)
            previous = n

        return mmin


def build():
    """
          4
        /   \
      2      6
     / \
    1   3
    """

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.right = TreeNode(3)
    root.left.left = TreeNode(1)
    root.right = TreeNode(6)
    return root


if __name__ == "__main__":
    s = Solution()
    result = s.minDiffInBST(build())
    print(result)
    result = s.rewrite(build())
    print(result)
