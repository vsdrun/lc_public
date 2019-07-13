#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/


We are given a binary tree (with root node root),
a target node, and an integer value K.

Return a list of the values of all nodes that have a distance K from
the target node.
The answer can be returned in any order.


Example 1:
Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
Output: [7,4,1]
Explanation:
The nodes that are a distance 2 from the target node (with value 5)
have values 7, 4, and 1.

Note that the inputs "root" and "target" are actually TreeNodes.
The descriptions of the inputs above are just serializations of these objects.

Note:
The given tree is non-empty.
Each node in the tree has unique values 0 <= node.val <= 500.
The target node is a node in the tree.
0 <= K <= 1000.
"""


# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        """
        import collections

        conn = collections.defaultdict(list)

        # 建構雙向map
        def connect(parent, child):
            if parent and child:
                conn[parent.val].append(child.val)
                conn[child.val].append(parent.val)
            if child.left: connect(child, child.left)
            if child.right: connect(child, child.right)

        # 開始建構
        connect(None, root)

        bfs = [target.val]
        seen = set(bfs)

        # 有多少distance跑多少次
        for i in xrange(K):
            bfs = [y for x in bfs for y in conn[x] if y not in seen]
            seen |= set(bfs)

        return bfs


def build():
    _3 = TreeNode(3)
    _5 = TreeNode(5)
    _1 = TreeNode(1)
    _6 = TreeNode(6)
    _2 = TreeNode(2)
    _0 = TreeNode(0)
    _8 = TreeNode(8)
    _7 = TreeNode(7)
    _4 = TreeNode(4)

    _3.left = _5
    _3.right = _1
    _5.left = _6
    _5.right = _2
    _2.left = _7
    _2.right = _4
    _1.left = _0
    _1.right = _8

    return _3, TreeNode(5), 2

if __name__ == "__main__":
    s = Solution()
    #  print(s.distanceK(*build()))
    print(s.rewrite(*build()))
