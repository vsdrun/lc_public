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
        2. 由inorder中藉由root找到左tree, 右tree
        """
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        ridx = inorder.index(root.val)

        left_in = inorder[:ridx]
        right_in = inorder[ridx + 1:]

        left_pre = preorder[1: 1 + len(left_in)]
        right_pre = preorder[1 + len(left_in):]

        root.left = self.buildTree(left_pre, left_in)
        root.right = self.buildTree(right_pre, right_in)

        return root

        # -----fast?

        def construct(preorder, inorder, i, j):
            if i < j:
                val = preorder.pop()
                index = self.map[val]
                root = TreeNode(val)
                root.left = construct(preorder, inorder, i, index)
                root.right = construct(preorder, inorder, index + 1, j)
                return root

        preorder.reverse()
        self.map = {}

        for i, val in enumerate(inorder):
            self.map[val] = i

        return construct(preorder, inorder, 0, len(inorder))

    def rewrite(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode

        1. 先 preorder 找root
        2. 由inorder中藉由root找到左tree, 右tree

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

        def build(preo, ino):
            if not ino:
                return None

            root = preo.pop()
            left = ino[:ino.index(root)]
            right = ino[ino.index(root)+1:]

            rootTN = TreeNode(root)
            rootTN.left = build(preo, left)
            rootTN.right = build(preo, right)

            return rootTN

        preorder.reverse()
        # get root
        root = preorder.pop()
        left = inorder[:inorder.index(root)]
        right = inorder[inorder.index(root)+1:]

        rootTN = TreeNode(root)
        rootTN.left = build(preorder, left)
        rootTN.right = build(preorder, right)
        return rootTN

    def rewrite2(self, preorder, inorder):
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

        def create(nodes, p):
            if not nodes:
                return None

            root_val = p.pop()
            root = TreeNode(root_val)

            left = nodes[:nodes.index(root_val)]
            right = nodes[nodes.index(root_val)+1:]

            root.left = create(left, p)
            root.right= create(right, p)
            return root



        p = preorder
        i = inorder

        p.reverse() # reverse it thus we could pop data.
        root_val = p.pop()
        root = TreeNode(root_val)

        left = i[: i.index(root_val)]
        right = i[i.index(root_val)+1:]

        root.left = create(left, p)
        root.right= create(right, p)

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
    root_1 = s.buildTree(*build())
    root_2 = s.rewrite(*build())
    root_3 = s.rewrite2(*build())

    def dfs(node, result):
        result.append(node.val)

        if node.left:
            dfs(node.left, result)

        if node.right:
            dfs(node.right, result)

    result = []
    dfs(root_1, result)
    print(result)

    result = []
    dfs(root_2, result)
    print(result)

    result = []
    dfs(root_3, result)
    print(result)
