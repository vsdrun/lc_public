#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/binary-tree-longest-consecutive-sequence/

Given a binary tree, find the length of the longest consecutive sequence path.

The path refers to any sequence of nodes from some starting node
to any node in the tree along the parent-child connections.
The longest consecutive path need to be from parent to child
(cannot be the reverse).

For example,

1
\
 3
/ \
2   4
    \
     5

Longest consecutive sequence path is 3-4-5, so return 3.

   2
    \
     3
    /
   2
  /
 1

Longest consecutive sequence path is 2-3,not3-2-1, so return 2.
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
        """
        if not root:
            return 0

        ret = 0
        stack = [(root, 1)]

        while stack:
            node, cnt = stack.pop()
            if node.left:
                stack.append(
                    (node.left,
                        cnt + 1 if node.left.val == node.val + 1 else 1))
            if node.right:
                stack.append(
                    (node.right,
                        cnt + 1 if node.right.val == node.val + 1 else 1))

            ret = max(ret, cnt)

        return ret

    def rewrite(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        def dfs(node):
            """
            input:  current
            output: current path cnt
            """

            if not node:
                return 0

            cnt = 1
            rcnt = lcnt = 0

            if node.left:
                lcnt = dfs(node.left)
                if node.val + 1 != node.left.val:
                    lcnt = 0

            if node.right:
                rcnt = dfs(node.right)
                if node.val + 1 != node.right.val:
                    rcnt = 0

            gmx[0] = max(gmx[0], cnt + lcnt, cnt + rcnt)

            return max(cnt + lcnt, cnt + rcnt)

        gmx = [0]
        dfs(root)

        return gmx[0]


def build():
    """
        2
         \
          3
        /
       2
      /
     1

       1
        \
         3
        /
       2   4
      /
     1       5
    """

    root = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.left.left = TreeNode(1)
    return root

    root = TreeNode(1)
    root.right = TreeNode(3)
    root.right.left = TreeNode(2)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    return root

    root = TreeNode(1)
    return root


if __name__ == "__main__":
    s = Solution()
    result = s.longestConsecutive(build())
    print(result)
    result = s.rewrite(build())
    print(result)
