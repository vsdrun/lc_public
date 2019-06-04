#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/delete-node-in-a-bst/description/

Given a root node reference of a BST and a key,
delete the node with the given key in the BST.
Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

Search for a node to remove.
If the node is found, delete the node.
Note: Time complexity should be O(height of tree).


Example:
root = [5,3,6,2,4,null,7]
key = 3

    5
   / \
  3   6
 / \   \
2   4   7

Given key to delete is 3. So we find the node with value 3 and delete it.

One valid answer is [5,4,6,2,null,null,7], shown in the following BST.

    5
   / \
  4   6
 /     \
2       7

Another valid answer is [5,2,6,null,4,null,7].

    5
   / \
  2   6
   \   \
    4   7

把左邊最大放到被刪除的node便是。
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def deleteNode(self, root, key):
        """
        :type root: TreeNode
        :type key: int
        :rtype: TreeNode
        """
        def dfs(node):
            if node.right:
                return dfs(node.right)
            return node

        def find(node):
            next = None

            if not node:
                return
            elif node.val < key:
                next = find(node.right)
                node.right = next
                return node
            elif node.val > key:
                next = find(node.left)
                node.left = next
                return node
            else:
                retNode = None

                if node.left:
                    retNode = node.left
                    rightMost = dfs(node.left)
                    rightMost.right = node.right
                else:
                    retNode = node.right

                return retNode

        return find(root)

def build():
    """
    3
   / \
  9  20
    /  \
   15   7
    """
    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)
    return root, 20

def pp(node):
    root = [node]

    while root:
        print([n.val for n in root])
        root = [child for n in root for child in (n.left, n.right) if child]


if __name__ == "__main__":
    s = Solution()
    pp(s.deleteNode(*build()))
    print("----")
    pp(s.rewrite(*build()))
