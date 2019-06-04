#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/serialize-and-deserialize-bst/description/


Serialization is the process of converting a data structure or object into a
sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later
in the same or another computer environment.

Design an algorithm to serialize and deserialize a binary search tree.
There is no restriction on how your serialization/deserialization algorithm
should work.

You just need to ensure that a binary search tree can be
serialized to a string and this string can be deserialized to
the original tree structure.

The encoded string should be as compact as possible.

Idea:
Hey, this is a BST tree, i.e inorder traverse is in it's DNA!
We just need to encoded with a preorder and when pass to
decode, we can sort the preorder and get the inorder!
And with preorder and inorder, we can reconstruct the tree!!!
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        請用297解決 謝謝.
        """
        # let's encode with preorder.
        result = []

        def encode(node):
            if not node:
                return

            result.append(str(node.val) + ' ')
            encode(node.left)
            encode(node.right)

        encode(root)
        return "".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str, preordered.
        :rtype: TreeNode
        """
        if not data:
            return

        # sorted str
        inorder = sorted(int(c) for c in data.split())
        preorder = [int(c) for c in data.split()]  # 找 root

        def build(root, inorder):
            """
            Create root node and return root node.
            """
            rtn = TreeNode(root)

            left_inorder = inorder[: inorder.index(root)]
            left_tree = right_tree = None

            if left_inorder:
                next_root = preorder.pop(0)
                left_tree = build(next_root, left_inorder)

            right_inorder = inorder[inorder.index(root) + 1:]

            if right_inorder:
                next_root = preorder.pop(0)
                right_tree = build(next_root, right_inorder)

            rtn.left = left_tree
            rtn.right = right_tree
            return rtn

        root = preorder.pop(0)
        rtn = build(root, inorder)

        return rtn


def build():
    """
      5
     / \
    2   7
    """
    root = TreeNode(5)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    return root


def pt(node):
    qq = [node]

    while qq:
        print([q.val for q in qq])

        qq = [vq for q in qq if q for vq in (q.left, q.right) if vq]


if __name__ == "__main__":
    s = Codec()
    se = s.serialize(build())
    print(se)
    de = s.deserialize(se)
    pt(de)
