#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/second-minimum-node-in-a-binary-tree/description/

題目解釋的不清楚.
即使沒有two subnode 也會被放入比較的set中.

Given a non-empty special binary tree consisting of nodes with the
non-negative value,
where each node in this tree has exactly

*two or
*zero sub-node.

If the node has two sub-nodes,
then this node's value is the smaller value among its two sub-nodes.

Given such a binary tree,
you need to output the second minimum value in the set made of all
the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.

Example 1:
Input:
    2
   / \
  2   5
     / \
    5   7

Output: 5
Explanation: The smallest value is 2, the second smallest value is 5.


Example 2:
Input:
    5
   / \
  5   6

Output: 6
"""

# Definition for a binary tree node.


class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findSecondMinimumValue(self, root):
        """
        :type root: TreeNode
        :rtype: int
        最小封頂的概念.

        DFS
        """
        res = [float('inf')]

        def traverse(node):
            if not node:
                return

            if root.val < node.val < res[0]:
                res[0] = node.val

            # 不行! 因為... 即使與此node相同 下面會有第二小的
            #  if node.left and node.left.val != node.val:
            traverse(node.left)
            #  if node.right and node..val != node.val:
            traverse(node.right)

        traverse(root)
        return -1 if res[0] == float('inf') else res[0]

    def rewrite(self, root):
        """
        :type root: TreeNode
        :rtype: int
        最小封頂的概念.
        提早bail out, 但是如果沒有 > gval, 每個node仍要traverse.
        DFS, BEST Solution always from SHC.
        """
        if not root:
            return -1

        gval = root.val

        def dfs(node):
            if not node:
                return -1

            if node.val > gval:
                return node.val

            lval = dfs(node.left)
            rval = dfs(node.right)

            if lval != -1 and rval != -1:
                return min(rval, lval)

            if lval != -1:
                return lval
            if rval != -1:
                return rval

            return -1

        return dfs(root)

def build():
    """
    2
   / \
  2   2

    2
   / \
  2   5
     / \
    5   7

    [5,5,6]
    """
    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(5)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(5)
    return root

    root = TreeNode(5)
    root.left = TreeNode(5)
    root.right = TreeNode(6)
    return root

    root = TreeNode(2)
    root.left = TreeNode(2)
    root.right = TreeNode(2)
    return root


if __name__ == "__main__":
    s = Solution()
    print(s.findSecondMinimumValue(build()))
    print(s.rewrite(build()))
