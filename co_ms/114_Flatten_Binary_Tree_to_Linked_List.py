#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/

Given a binary tree, flatten it to a linked list in-place.

For example, given the following tree:

    1
   / \
  2   5
 / \   \
3   4   6
The flattened tree should look like:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def flatten(self, root):
        def dfs(node):
            if not node:
                return

            # return last node
            oright = node.right
            leftEnd = None
            rightEnd = None

            if node.left:
                node.right = node.left
                leftEnd = dfs(node.left)
                node.left = None

            if oright:
                rightEnd = dfs(oright)

            if leftEnd:
                leftEnd.right = oright

            return rightEnd if rightEnd else leftEnd if leftEnd else node

        dfs(root)


def build():
    """
        1
       / \
      2   5
     / \   \
    3   4   6

        1
       /
      2
     /
    3
    """
    _1= TreeNode(1)
    _2= TreeNode(2)
    _3= TreeNode(3)
    _1.left = _2
    _2.left= _3
    return _1


    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(4)
    root.right = TreeNode(5)
    root.right.right = TreeNode(6)
    return root


def pr(t):
    while t:
        print(t.val)
        if t.right:
            t = t.right
        else:
            break

def debug(t):
    r = [t]

    while r:
        print([n.val for n in r])
        r = [N for n in r for N in (n.left, n.right) if N]


if __name__ == "__main__":
    s = Solution()
    t = build()
    s.flatten(t)
    pr(t)
