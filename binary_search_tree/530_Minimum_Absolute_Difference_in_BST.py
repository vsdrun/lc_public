#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/minimum-absolute-difference-in-bst/description/


Given a binary search tree with non-negative values,
find the minimum absolute difference between values of any two nodes.


Example:
Input:

   1
    \
     3
    /
   2

Output:
1

Explanation:
The minimum absolute difference is 1,
which is the difference between 2 and 1 (or between 2 and 3).
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def getMinimumDifference(self, root):
        """
        :type root: TreeNode
        :rtype: int
       1
        \
         3
        /
       2

       1 2 3 4 20 算彼此之差最小.
        """
        anchor = [100000000]
        mmin = [100000000]

        def dfs(root):
            """
            inorder traverse.
            :ret: min, max
            """

            if not root:
                return

            lmin = lmax = rmin = rmax = None

            if root.left:
                lmin, lmax = dfs(root.left)
                mmin[0] = min(mmin[0], root.val - lmax.val)

            if root.right:
                rmin, rmax = dfs(root.right)
                mmin[0] = min(mmin[0], rmin.val - root.val)

            if not lmin:
                lmin = root

            if not rmax:
                rmax = root

            return lmin, rmax

        dfs(root)
        return mmin[0] if mmin[0] != anchor[0] else 0


def build():
    """
   1
    \
     3
    /
   2
    """
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    return root


if __name__ == "__main__":
    s = Solution()
    result = s.getMinimumDifference(build())
    print(result)
