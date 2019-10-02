#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/subtree-of-another-tree/description/

Given two non-empty binary trees s and t,
check whether tree t has exactly the same structure and node
values with a subtree of s.

A subtree of s is a tree consists of a node in s and all of this
node's descendants.

The tree s could also be considered as a subtree of itself.

Example 1:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
Given tree t:
   4
  / \
 1   2
Return true,
because t has the same structure and node values with a subtree of s.


Example 2:
Given tree s:

     3
    / \
   4   5
  / \
 1   2
    /
   0
Given tree t:
   4
  / \
 1   2
Return false.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool

        make it better:
        t only belongs to s while s's some node has the depth as t's
        only compare s's some node to t.

        or 編碼... 比對編碼 with string comparason.
        """
        bfs_list = [s]

        def dfs(ss, tt):
            if ss == tt:
                return True

            if ss.val == tt.val:
                if not bool(ss.left) ^ bool(tt.left) and \
                        not bool(ss.right) ^ bool(tt.right):
                    if dfs(ss.left, tt.left) and dfs(ss.right, tt.right):
                        return True
            return False

        while bfs_list:
            s = bfs_list.pop(0)

            if s.val == t.val:
                if dfs(s, t):
                    return True

            if s.left:
                bfs_list.append(s.left)
            if s.right:
                bfs_list.append(s.right)

        return False


def build():
    """
    3
   / \
  9  20
 /  /  \
8  15   7
        \
        11

    """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.left.left = TreeNode(8)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    #  root.right.right.right = TreeNode(11)
    root.right.left = TreeNode(15)

    sub = TreeNode(20)
    sub.left = TreeNode(15)
    sub.right = TreeNode(7)
    return root, sub


if __name__ == "__main__":
    s = Solution()
    print(s.isSubtree(*build()))
