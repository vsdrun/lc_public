#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/find-duplicate-subtrees/description/


Given a binary tree, return all duplicate subtrees.
For each kind of duplicate subtrees,
you only need to return the root node of any one of them.

Two trees are duplicate if they have the same structure with same node values.

Example 1:
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4

The following are two duplicate subtrees:
      2
     /
    4

and
    4

Therefore, you need to return above trees' root in the form of a list.

注意!!
inorder 才能構成獨一無二的  signature 嗎?
錯! 只要 root node 也 encode 即可, preorder 也行!
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findDuplicateSubtrees(self, root):
        """
        :type root: TreeNode
        :rtype: List[TreeNode]
        Look for signature!
        """

        from collections import defaultdict as dd
        resultDict= dd(None)
        keySet = set()

        def encode(root):
            if not root:
                return "#"

            code = []
            code.append(str(root.val))

            code.append(encode(root.left))
            code.append(encode(root.right))

            enc = "".join(code)
            if enc in keySet:
                resultDict[enc] = root

            keySet.add(enc)

            return enc


        encode(root)
        return resultDict.values()


def build():
    """
        1
       / \
      2   3
     /   / \
    4   2   4
       /
      4
    """
    #  root = TreeNode(1)
    #  root.right = TreeNode(3)
    #  root.left = TreeNode(1)
    #  root.left.right = TreeNode(3)
    #  return root

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.left = TreeNode(2)
    root.right.left.left = TreeNode(4)
    return root

def pp(node):
    if not node:
        return
    print(node.val)
    pp(node.left)
    pp(node.right)


if __name__ == "__main__":
    s = Solution()
    [pp(l) for l in s.findDuplicateSubtrees(build())]
