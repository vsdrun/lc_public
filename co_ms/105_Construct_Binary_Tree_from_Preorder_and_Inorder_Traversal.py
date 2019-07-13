#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/description/

Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode

        1. 先 preorder 找root
        2. 由 inorder 中藉由root找到左tree, 右tree

        preorder = [3,9,20,15,7]
        inorder = [9,3,15,20,7]
        Return the following binary tree:

            3
           / \
          9  20
            /  \
           15   7
        """
        if not preorder or not inorder:
            return None

        def create(nodes):
            if not nodes:
                return None

            root_val = p.pop()
            root = TreeNode(root_val)

            left = nodes[:nodes.index(root_val)]
            right = nodes[nodes.index(root_val)+1:]

            root.left = create(left)
            root.right= create(right)
            return root


        p = preorder
        i = inorder

        p.reverse() # reverse it thus we could pop data.
        root_val = p.pop()
        root = TreeNode(root_val)

        left = i[: i.index(root_val)]
        right = i[i.index(root_val)+1:]

        root.left = create(left)
        root.right= create(right)

        return root


def build():
    """
    3
   / \
  9  20
    /  \
   15   7
    """
    preorder = [3, 9, 20, 15, 7]
    inorder = [9, 3, 15, 20, 7]
    return preorder, inorder


if __name__ == "__main__":
    s = Solution()
    root = s.buildTree(*build())

    def dfs(node):
        result.append(node.val)

        if node.left:
            dfs(node.left)

        if node.right:
            dfs(node.right)

    result = []
    dfs(root)
    print(result)
