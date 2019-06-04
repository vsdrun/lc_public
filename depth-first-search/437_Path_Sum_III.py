#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/path-sum-iii/

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf,
but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range
-1,000,000 to 1,000,000.

Example:
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
"""


# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        # key: accumulate value, value: node value
        from collections import defaultdict as dd
        dmap = dd(list)
        dmap[0] = [None]
        cnt = [0]

        def dfs(node, psum):
            if not node:
                return

            csum = psum + node.val
            needs = csum - sum

            if needs in dmap:
                cnt[0] += len(dmap[needs])

            dmap[csum].append(node.val)

            if node.left:
                dfs(node.left, csum)
            if node.right:
                dfs(node.right, csum)

            dmap[csum].pop()


        dfs(root, 0)

        return cnt[0]



def build():
    """
          10
         /  \
        5   -3
       / \    \
      3   2   11
     / \   \
    3  -2   1
    """
    _10 = TreeNode(10)
    _5 = TreeNode(5)
    _3_1 = TreeNode(3)
    _3_2 = TreeNode(3)
    _3_3 = TreeNode(-3)
    _2_1 = TreeNode(2)
    _2_2 = TreeNode(-2)
    _1 = TreeNode(1)
    _11 = TreeNode(11)

    _10.left = _5
    _10.right = _3_3

    _5.left = _3_1
    _5.right = _2_1

    _3_1.left = _3_2
    _3_1.right= _2_2

    _2_1.right = _1

    _3_3.right = _11

    return _10, 8


# [5,4,8,11,null,13,4,7,2,null,null,5,1], 22

if __name__ == "__main__":
    s = Solution()
    print(s.pathSum(*build()))
