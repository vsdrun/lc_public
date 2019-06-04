#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/binary-tree-right-side-view/description/


Given a binary tree,
imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.


Example:
Input: [1,2,3,null,5,null,4]
Output: [1, 3, 4]

Explanation:
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        # bfs, take right most value
        if not root:
            return []

        qq = [root]
        result = []

        while qq:
            result.append(qq[-1].val)
            qq = [qv for q in qq for qv in (q.left, q.right) if qv]

        return result


def build():
    """
   1            <---
 /   \
2     3         <---
 \     \
  5     4       <---
  \
   7
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.right = TreeNode(5)
    root.left.right.right = TreeNode(7)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    return root


def pt(node):
    qq = [node]

    while qq:
        print([q.val for q in qq])

        qq = [vq for q in qq if q for vq in (q.left, q.right) if vq]


if __name__ == "__main__":
    s = Solution()
    se = s.rightSideView(build())
    print(se)
