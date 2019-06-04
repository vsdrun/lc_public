#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/description/


Given inorder and postorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

For example, given

inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]
Return the following binary tree:

    3
   / \
  9  20
    /  \
   15   7

postorder 的最後一個值 為 root.  倒數第二個一路下去
為最右邊的node的root...

有了root則從inorder中分隔左右兩邊.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
            3
           / \
          9  20
            /  \
           15   7
        inorder = [9,3,15,20,7]
        postorder = [9,15,7,20,3]

        in   [2, 1]
        post [2, 1]
        """

        def build_t(ino, posto):
            # 找 root

            root = posto.pop()
            root_node = TreeNode(root)

            leftino = ino[: ino.index(root)]
            rightino = ino[ino.index(root) + 1:]

            root_node.right = build_t(rightino, posto) if rightino else None
            root_node.left = build_t(leftino, posto) if leftino else None

            return root_node

        return build_t(inorder, postorder) if inorder and postorder else None


def build():
    """
    3
   / \
  9  20
    /  \
   15   7
    """
    return [9, 3, 15, 20, 7], [9, 15, 7, 20, 3]
    return [2, 1], [2, 1]
    return [], []


if __name__ == "__main__":
    def run(r):
        if r:
            ll = [r]

            result = []

            while ll:
                r = ll.pop(0)
                result.append(r.val)

                if r.left:
                    ll.append(r.left)
                if r.right:
                    ll.append(r.right)

            print(result)

    s = Solution()
    r = s.buildTree(*build())
    run(r)
