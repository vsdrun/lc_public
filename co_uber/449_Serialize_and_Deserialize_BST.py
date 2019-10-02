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
        或者, preorder serialize without '#'
        """
        result = []

        def dfs(node):
            if not node:
                return

            result.append(str(node.val))
            if node.left:
                dfs(node.left)
            if node.right:
                dfs(node.right)

        dfs(root)
        return " ".join(result)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str, preordered.
        :rtype: TreeNode
             5
            / \
           2   6
          / \
         1   3
        [5,2,1,3,6]
        """
        if not data:
            return

        # inverse, because we are using list.pop()
        data = map(int, data.split()[::-1])

        def dfs(left, right):
            tval = data.pop()
            tnode = TreeNode(tval)

            if data and left < data[-1] < tval:
                tnode.left = dfs(left, tval)

            if data and right > data[-1] > tval:
                tnode.right = dfs(tval, right)

            return tnode

        return dfs(float("-inf"), float("inf"))

def build():
    """
      5
     / \
    2   7
    """
    #  root = TreeNode(5)
    #  root.left = TreeNode(2)
    #  root.right = TreeNode(7)
    #  return root

    """
             5
            / \
           2   6
          / \
         1   3
        [5,2,1,3,6]
    """
    _5 = TreeNode(5)
    _2 = TreeNode(2)
    _6 = TreeNode(6)
    _1 = TreeNode(1)
    _3 = TreeNode(3)
    _5.left = _2
    _5.right = _6
    _2.left = _1
    _2.right = _3
    return _5


def pt(node):
    qq = [node]

    while qq:
        print([q.val for q in qq])

        qq = [vq for q in qq if q for vq in (q.left, q.right) if vq]


if __name__ == "__main__":
    s = Codec()
    se = s.serialize(build())
    print("serialized: {}".format(se))
    de = s.deserialize(se)
    pt(de)
