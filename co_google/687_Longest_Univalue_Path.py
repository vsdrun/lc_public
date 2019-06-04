#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/longest-univalue-path/description/


Given a binary tree,
find the length of the longest path where each node in the path
has the same value.

This path may or may not pass through the root.

Note: The length of path between two nodes is represented by the
number of edges between them.

這題目問的是重複值.

Example 1:
Input:

              5
             / \
            4   5
           / \   \
          1   1   5
Output:
2  因為 5,5,5


Example 2:
Input:
              1
             / \
            4   5
           / \   \
          4   4   5
Output:
2  因為 4,4,4
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
              5
             / \
            4   5
           / \   \
          1   1   5
        """

        mx = [0]

        def dfs(root):
            """
            :ret: node, cnt
            """
            # 因為有可能一開始的tree為None.
            if not root:
                return

            lcnt = rcnt = 0

            if root.left:
                ret_lcnt = dfs(root.left)

                if root.left.val == root.val:
                    lcnt = ret_lcnt + 1

            if root.right:
                ret_rcnt = dfs(root.right)

                if root.right.val == root.val:
                    rcnt = ret_rcnt + 1

            mx[0] = max(mx[0], lcnt + rcnt)

            return lcnt if lcnt > rcnt else rcnt

        dfs(root)

        return mx[0]


def build():
    """
              5
             / \
            4   5
           / \   \
          1   1   5
         /
        1
         \
          1
        /
       1
        \
         1
    """
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.left.right = TreeNode(1)
    root.left.left = TreeNode(1)
    root.left.left.left = TreeNode(1)
    root.left.left.left.right = TreeNode(1)
    root.left.left.left.right.left = TreeNode(1)
    root.left.left.left.right.left.right = TreeNode(1)
    root.right = TreeNode(5)
    root.right.right = TreeNode(5)
    root.right.right.left = TreeNode(5)
    return root


if __name__ == "__main__":
    s = Solution()
    result = s.longestUnivaluePath(build())
    print(result)
