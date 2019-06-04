#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/binary-tree-vertical-order-traversal/description/

Given a binary tree, return the vertical order traversal of its nodes' values.
(ie, from top to bottom, column by column).

If two nodes are in the same row and column,
the order should be from left to right.


Examples:

Given binary tree [3,9,20,null,null,15,7],

   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7



return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]


Given binary tree [3,9,8,4,0,1,7],
     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7

return its vertical order traversal as:
[
  [4],
  [9],
  [3,0,1],
  [8],
  [7]
]


Given binary tree [3,9,8,4,0,1,7,null,null,null,2,5]
(0's right child is 2 and 1's left child is 5),

     3
    /\
   /  \
   9   8
  /\  /\
 /  \/  \
 4  01   7
    /\
   /  \
   5   2

return its vertical order traversal as:
[
  [4],
  [9,5],
  [3,0,1],
  [8,2],
  [7]
]
"""

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def verticalOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        用這個~
        smarter..
        利用stack來區分前後...
        就是 BFS!!!
        """
        if not root:
            return []

        from collections import defaultdict as dd

        dmap = dd(list)

        root = [(root, 0)]
        mmin = float("inf")
        mmax = float("-inf")

        while root:
            tmp = []

            for r in root:
                node, cnt = r[0], r[1]
                mmin = min(mmin, cnt)
                mmax = max(mmax, cnt)

                dmap[cnt].append(node.val)

                if node.left:
                    tmp.append((node.left, cnt - 1))
                if node.right:
                    tmp.append((node.right, cnt + 1))

            root = tmp

        return [dmap[i] for i in range(mmin, mmax + 1)]


def build():
    """
   3
  /\
 /  \
 9  20
    /\
   /  \
  15   7

return its vertical order traversal as:
[
  [9],
  [3,15],
  [20],
  [7]
]
    """
    _3 = TreeNode(3)
    _9 = TreeNode(9)
    _20 = TreeNode(20)
    _15 = TreeNode(15)
    _7 = TreeNode(7)
    _3.left = _9
    _3.right = _20
    _20.left = _15
    _20.right = _7
    return _3


if __name__ == "__main__":
    s = Solution()
    print(s.verticalOrder(build()))
