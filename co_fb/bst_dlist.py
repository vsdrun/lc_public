#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/roman-to-integer/description/

Given a roman numeral, convert it to an integer.

Input is guaranteed to be within the range from 1 to 3999.

Symbol	I	V	X	L	C	D	M
Value	1	5	10	50	100	500	1,000

https://en.wikipedia.org/wiki/Roman_numerals
"""


class Node(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution(object):
    def bst_llst(self, root):

        def dfs(root):
            """
            :param root: Node
            :ret: (min, max)
                    9

                 6        14

              3    8|  12
                 /
                7

            """

            if not root:
                return

            lmin = lmax = rmin = rmax = None

            if root.left:
                lmin, lmax = dfs(root.left)
                lmax.right = root
                root.left = lmax

            if root.right:
                rmin, rmax = dfs(root.right)
                root.right = rmin
                rmin.left = root

            if not lmin:
                lmin = root
            if not rmax:
                rmax = root

            return lmin, rmax

        mmin, mmax = dfs(root)

        mmin.left = mmax
        mmax.right = mmin
        return mmin

    def bst_llst_old(self, root):
        def dfs(root, small_node):
            if not root:
                return

            small_node[0] = root if root.val < small_node[0].val else \
                small_node[0]

            if root.left:
                r = dfs(root.left, small_node)
                r.right = root
                root.left = r

            if root.right:
                r = dfs(root.right, small_node)
                r.left = root
                return r
            return root

        small_node = [Node(100000000)]
        large_node = dfs(root, small_node)
        large_node.right = small_node[0]
        small_node[0].left = large_node
        return small_node[0]


def build():
    """
        9

     6        14

  3    8|  12

    7

    """

    root = Node(9)
    root.left = Node(6)
    root.left.left = Node(3)
    root.left.right = Node(8)
    root.left.right.left = Node(7)
    root.right = Node(14)
    root.right.left = Node(12)
    return root


if __name__ == "__main__":

    s = Solution()
    result = s.bst_llst(build())
    val = result.val

    print(val)
    result = result.right

    while result and result.val > val:
        print(result.val)
        result = result.right

    result = result.left

    while result and result.val > val:
        print(result.val)
        result = result.left
