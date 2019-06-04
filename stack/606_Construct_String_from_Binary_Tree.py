#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/construct-string-from-binary-tree/

You need to construct a string consists of parenthesis and integers from a
binary tree with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()".
And you need to omit all the empty parenthesis pairs that don't affect the
one-to-one mapping relationship between the string and the original
binary tree.


Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /
  4

Output: "1(2(4))(3)"

Explanation: Originallay it needs to be "1(2(4)())(3()())",
but you need to omit all the unnecessary empty parenthesis pairs.
And it will be "1(2(4))(3)".

Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \
      4

Output: "1(2()(4))(3)"

Explanation: Almost the same as the first example,
except we can't omit the first parenthesis pair to break the one-to-one
mapping relationship between the input and the output.
"""

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution(object):
    def tree2str(self, t):
        """
        :type t: TreeNode
        :rtype: str
        """
        if not t:
            return ""

        result = []

        def dfs(node):
            if not node:
                return

            result.append(str(node.val))

            if not node.left and not node.right:
                return

            result.append("(")
            dfs(node.left)
            result.append(")")

            if node.right:
                result.append("(")
                dfs(node.right)
                result.append(")")

        dfs(t)
        return "".join(result)


def build():
    """
       1
     /   \
    2     3
     \
      4
Output: "1(2()(4))(3)"
    """
    _1 = TreeNode(1)
    _2 = TreeNode(2)
    _3 = TreeNode(3)
    _4 = TreeNode(4)
    _1.left = _2
    _1.right = _3
    _2.right = _4

    return _1

if __name__ == "__main__":
    s = Solution()
    print(s.tree2str(build()))
