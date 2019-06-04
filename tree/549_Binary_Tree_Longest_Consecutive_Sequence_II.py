#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/binary-tree-longest-consecutive-sequence-ii/description/


Given a binary tree,
you need to find the length of Longest Consecutive Path in Binary Tree.

Especially, this path can be either increasing or decreasing.

For example, [1,2,3,4] and [4,3,2,1] are both considered valid,
but the path [1,2,4,3] is not valid.

On the other hand,
the path can be in the child-Parent-child order,
where not necessarily be parent-child order.


Example 1:
Input:
        1
       / \
      2   3

Output: 2
Explanation: The longest consecutive path is [1, 2] or [2, 1].
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def longestConsecutive(self, root):
        """
        :type root: TreeNode
        :rtype: int
        dfs
        兩種解法??
        1. convert成 linked list 解? 不可能~~ 有多重路徑.
        2. 直接上.
        """

        def dfs(node, prev):
            """
            input
            output left: increase, right: decrease
            """

            if not node:
                return

            linc = ldec = rinc = rdec = 0

            if node.left:
                linc, ldec = dfs(node.left, node)

            if node.right:
                rinc, rdec = dfs(node.right, node)

            gmx[0] = max(gmx[0], linc + rdec + 1, ldec + rinc + 1)

            if node is not prev:
                if node.val == prev.val - 1:
                    # increase inorder.
                    mx_inc = max(linc + 1, rinc + 1)

                    return mx_inc, 0

                elif node.val == prev.val + 1:
                    mx_dec = max(ldec + 1, rdec + 1)

                    return 0, mx_dec
                else:
                    return 0, 0

        gmx = [0]
        dfs(root, root)

        return gmx[0]

    def lc_answer(self, root):
        def dfs(node, parent):
            if not node:
                return 0, 0

            li, ld = dfs(node.left, node)
            ri, rd = dfs(node.right, node)
            l[0] = max(l[0], li + rd + 1, ld + ri + 1)

            if node.val == parent.val + 1:
                return max(li, ri) + 1, 0

            if node.val == parent.val - 1:
                return 0, max(ld, rd) + 1
            return 0, 0

        l = [0]
        dfs(root, root)

        return l[0]


def build():
    """
    3
   / \
  2  4
    /  \
   5    7
    """
    root = TreeNode(3)
    root.left = TreeNode(2)
    root.right = TreeNode(4)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(5)
    return root


if __name__ == "__main__":
    s = Solution()
    print(s.longestConsecutive(build()))
