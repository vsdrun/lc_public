#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/serialize-and-deserialize-binary-tree/description/


Serialization is the process of converting a data structure or
object into a sequence of bits so that it can be stored
in a file or memory buffer,
or transmitted across a network connection link to be
reconstructed later in the same or another computer environment.


Design an algorithm to serialize and deserialize a binary tree.


There is no restriction on how your serialization/deserialization
algorithm should work. You just need to ensure that a binary tree
can be serialized to a string and this string can be deserialized
to the original tree structure.

For example, you may serialize the following tree
    1
   / \
  2   3
     / \
    4   5

as "[1,2,3,null,null,4,5]", just the same as how LeetCode OJ serializes a
binary tree.  (一層一層由左至右)

You do not necessarily need to follow this format,
so please be creative and come up with different approaches yourself.


Note: Do not use class member/global/static variables to store states. Your
serialize and deserialize algorithms should be stateless.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        # preorder serializing.
        # By the end needs to have an anchor #.
        def doit(node):
            if node:
                vals.append(str(node.val))
                doit(node.left)
                doit(node.right)
            else:
                vals.append('#')  # 重要!

        vals = []
        doit(root)

        return ' '.join(vals)

    def deserialize(self, data):
        def doit():
            # same way to deserializing.
            val = next(vals)

            if val == '#':
                return None

            node = TreeNode(int(val))
            node.left = doit()
            node.right = doit()

            return node

        vals = iter(data.split())
        return doit()


"""
# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
"""


def build():
    """
        1
       / \
      2   3
     /   / \
    7   4   5

    1 2 7 # # # 3 4 # # 5 # #
    """
    r = TreeNode(1)
    r.left = TreeNode(2)
    r.left.left = TreeNode(7)

    r.right = TreeNode(3)
    r.right.left = TreeNode(4)
    r.right.right = TreeNode(5)

    return r


if __name__ == "__main__":
    c = Codec()

    s = c.serialize(build())
    print(s)

    s = c.deserialize(s)

    s = c.serialize(s)
    print(s)
