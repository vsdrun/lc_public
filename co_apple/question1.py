#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
1) given a binary tree, each tree node has an integer value
2) we define a path as a series of node that starts from root node, ends at a leaf node
3) add the numbers up along the path
4) return the sum of the longest path
 e.g. you have a tree looks like this:
                 1
             /      \
            2        3
             \      /   \
              5    6     7
             /
            1
 there are 3 paths in this tree: (1,2,5,1), (1,3,6), (1,3,7)
 add them up, you will get 3 sums: 9(1+2+5+1), 10(1+3+6), 11(1+3+7)
 then the function should return 9, which is the longest path with lengh of 4
5) if there are multiple paths that have the same longest length, please return the largest sum among those sums
"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def maxSum(self, root):
        """
        using bfs due to we have multiple values at last layer,
        pick the maximum one.
        """

        nodes = [root]
        prev = None

        while nodes:
            tmp = []
            prev = nodes

            for n in nodes:
                if n.left:
                    n.left.val += n.val
                    tmp.append(n.left)
                if n.right:
                    n.right.val += n.val
                    tmp.append(n.right)

            nodes = tmp

        return max(n.val for n in prev)


def build():
    """
                 1
             /      \
            2        3
             \      /   \
              5    6     107
             /    /
            1    42
    """
    _1_1 = Node(1)
    _1_2 = Node(1)
    _2 = Node(2)
    _3 = Node(3)
    _5 = Node(5)
    _6 = Node(6)
    _107 = Node(107)
    _42 = Node(42)

    _1_1.left = _2
    _1_1.right = _3
    _2.right = _5
    _5.left = _1_2
    _3.left = _6
    _3.right = _107
    _6.left = _42
    return _1_1


if __name__ == "__main__":
    s = Solution()
    print(s.maxSum(build()))
