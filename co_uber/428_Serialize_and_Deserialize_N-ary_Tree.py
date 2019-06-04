#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/serialize-and-deserialize-n-ary-tree/

Serialization is the process of converting a data structure or object
into a sequence of bits so that it can be stored in a file or memory buffer,
or transmitted across a network connection link to be reconstructed later in
the same or another computer environment.

Design an algorithm to serialize and deserialize an N-ary tree.
An N-ary tree is a rooted tree in which each node has no more than N children.
There is no restriction on how your serialization/deserialization algorithm
should work.

You just need to ensure that an N-ary tree can be serialized to a string and
this string can be deserialized to the original tree structure.

For example, you may serialize the following 3-ary tree

as [1 [3[5 6] 2 4]].
You do not necessarily need to follow this format,
so please be creative and come up with different approaches yourself.

Note:
N is in the range of [1, 1000]
Do not use class member/global/static variables to store states.
Your serialize and deserialize algorithms should be stateless.
"""

"""
# Definition for a Node.
"""
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children

class Codec:
    def serialize(self, root):
        serial = []

        def preorder(node):
            if not node:
                return

            serial.append(str(node.val))

            for child in node.children:
                preorder(child)

            serial.append("#")      # indicates no more children, continue serialization from parent

        preorder(root)

        return " ".join(serial)

    def deserialize(self, data):
        from collections import deque

        if not data:
            return None

        tokens = deque(data.split())
        root = Node(int(tokens.popleft()), [])

        def helper(node):

            if not tokens:
                return

            while tokens[0] != "#": # add child nodes with subtrees
                value = tokens.popleft()
                child = Node(int(value), [])
                node.children.append(child)
                helper(child)

            tokens.popleft()        # discard the "#"

        helper(root)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))

def build():
    _1 = Node(1, [])
    _2 = Node(2, [])
    _3 = Node(3, [])
    _4 = Node(4, [])
    _5 = Node(5, [])
    _6 = Node(6, [])
    _1.children = [_3, _2, _4]
    _3.children = [_5, _6]
    return _1

def pp(node):
    result = []
    N = [node]

    while N:
        print([n.val for n in N])
        N = [r for n in N if n.children for r in n.children]

if __name__ == "__main__":
    s = Codec()
    print(s.serialize(build()))
    #  pp(s.deserialize(s.serialize(build())))
