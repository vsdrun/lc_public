#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/count-complete-tree-nodes/

Given a complete binary tree, count the number of nodes.

Note:
Definition of a complete binary tree from Wikipedia:

每一層填滿 再往下一層去.
所以說 若有下一層 代表此層已經填滿.

In a complete binary tree every level, except possibly the last,
is completely filled, and all nodes in the last level are as far left as possible.
It can have between 1 and 2^h nodes inclusive at the last level h.


Example:
Input:
    1
   / \
  2   3
 / \  /
4  5 6
Output: 6

https://leetcode.com/problems/count-complete-tree-nodes/discuss/62088/My-python-solution-in-O(lgn-*-lgn)-time
"""


# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        Comparing the depth between left sub tree and right sub tree,

        If it is equal, it means the left sub tree is a perfect binary tree,
            not only a full binary tree.

        If it is not , it means the right sub tree is a perfect binary tree.
            1
           / \
          2   3
         / \  /\
        4  5 6  7
       / \ /\/\ /\
      8  9,10,11,12,13,14,15

        """

        def depth(node):
            if not node:
                return 0
            return 1 + depth(node.left)

        def run(node):
            if not node:
                return 0

            left = depth(node.left)
            print("left: {}".format(left))
            right = depth(node.right)
            print("r: {}".format(right))
            print("---")


            if left == right:
                cur = pow(2, left)
                nxt = run(node.right)
                return cur + nxt
            else:  # only left > right
                cur = pow(2, right)
                #  print("cur: {}".format(cur))
                nxt = run(node.left)
                return cur + nxt

        return run(root)


def build():
    """
            1
           / \
          2   3
         / \  /\
        4  5 6  7
       /
      8

      思考變形的圖案...
    """
    _1 = TreeNode(1)
    _2 = TreeNode(2)
    _3 = TreeNode(3)
    _4 = TreeNode(4)
    _5 = TreeNode(5)
    _6 = TreeNode(6)
    _7 = TreeNode(7)
    _8 = TreeNode(8)

    _1.left = _2
    _1.right = _3

    _2.left = _4
    _2.right = _5

    _3.left = _6
    _3.right = _7

    _4.left = _8

    return _1



def pp(nodes):
    result = []

    while nodes:
        result.append(nodes.val)
        nodes = nodes.next

    print(result)


if __name__ == "__main__":
    s = Solution()
    print(s.countNodes(build()))
