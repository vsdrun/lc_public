#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/construct-binary-tree-from-string/description/


You need to construct a binary tree from a string
consisting of parenthesis and integers.

The whole input represents a binary tree.

It contains an integer followed by zero, one or two pairs of parenthesis.

The integer represents the root's value and a pair of parenthesis contains
a child binary tree with the same structure.

You always start to construct the left child node of the parent
first if it exists.

Example:
Input: "4(2(3)(1))(6(5))"
Output: return the tree root node representing the following tree:

       4
     /   \
    2     6
   / \   /
  3   1 5
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def str2tree(self, s):
        """
        :type s: str
        :rtype: TreeNode
        """
        if not s:
            return

        p_stack = []  # if len == 0 node complete.
        idx = 0
        tmp_num = ""

        while idx < len(s):
            if s[idx] == '(':
                if tmp_num:
                    root = TreeNode(int(tmp_num))
                    tmp_num = ""
                    p_stack += root,
            elif s[idx] == ')':
                if tmp_num:
                    child = TreeNode(int(tmp_num))
                    tmp_num = ""
                    root = p_stack[-1]
                    if not root.left:
                        root.left = child
                    elif not root.right:
                        root.right = child
                else:
                    child = p_stack.pop()
                    root = p_stack[-1]
                    if not root.left:
                        root.left = child
                    elif not root.right:
                        root.right = child

            else:
                tmp_num += s[idx]

            idx += 1

        if tmp_num:
            root = TreeNode(int(tmp_num))
            p_stack += root,

        return p_stack[0]


def build():
    return "4(2(3)(1))(6(5))"
    return "51(232)(434)"
    return "4"
    return "-4(2(3)(1))(6(5)(7))"


def pt(node):
    q = [node]

    while q:
        tmp_q = []

        print([v.val for v in q])

        for v in q:
            if v.left:
                tmp_q += v.left,
            if v.right:
                tmp_q += v.right,

        q = tmp_q


if __name__ == "__main__":
    s = Solution()
    result = s.str2tree(build())
    pt(result)
