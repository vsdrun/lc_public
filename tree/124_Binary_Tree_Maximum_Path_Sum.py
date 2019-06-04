#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/binary-tree-maximum-path-sum/

Given a non-empty binary tree, find the maximum path sum.

For this problem,
a path is defined as any sequence of nodes from some starting node to any
node in the tree along the parent-child connections.

The path must contain at least one node and does not need
to go through the root.

Example 1:
Input: [1,2,3]

       1
      / \
     2   3
Output: 6


Example 2:
Input: [-10,9,20,null,null,15,7]

   -10
   / \
  9  20
    /  \
   15   7
Output: 42
"""

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        DFS
        左大還是右大 DFS return 最大
        """
        if not root:
            return 0

        gmax = [float("-inf")]

        def dfs(node):
            """
            :ret: return max
            """
            lval = 0
            rval = 0
            lsum = 0

            if node.left:
                lval = dfs(node.left)
            if node.right:
                rval = dfs(node.right)

            # 思考 拉成一直線, 此node為一直線上最後一個值
            # 2 -> -1
            if lval < 0:
                lval = 0
            if rval < 0:
                rval = 0

            gmax[0] = max(gmax[0], node.val + lval + rval)

            return node.val + lval if node.val + lval > node.val + rval else \
                    node.val + rval


        dfs(root)

        return gmax[0]


def build():
    """
       -10
       / \
      9  20
        /  \
       15   7
    Output: 42
    """
    #  _1 = TreeNode(2)
    #  _2 = TreeNode(-1)

    #  _1.left = _2

    #  return _1
    _1 = TreeNode(-10)
    _2 = TreeNode(9)
    _3 = TreeNode(20)
    _4 = TreeNode(15)
    _5 = TreeNode(7)

    _1.left = _2
    _1.right = _3
    _3.left = _4
    _3.right = _5
    return _1


if __name__ == "__main__":
    s = Solution()
    print(s.maxPathSum(build()))
