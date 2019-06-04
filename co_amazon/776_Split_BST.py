#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/split-bst/description/


Given a Binary Search Tree (BST) with root node root,
and a target value V,


split the tree into two subtrees where one subtree has nodes that are
all ***(smaller or equal) to the target value,
while the other subtree has all nodes that are ***(greater) than the target value.
It's not necessarily the case that the tree contains a node with value V.


Additionally, most of the structure of the original tree should remain.
Formally, for any child C with parent P in the original tree,
if they are both in the same subtree after the split,
then node C should still have the parent P.

You should output the root TreeNode of
both subtrees after splitting, in any order.


Example 1:
Input: root = [4,2,6,1,3,5,7], V = 2
Output: [[2,1],[4,3,6,null,null,5,7]]

Explanation:
Note that root, output[0], and output[1] are TreeNode objects, not arrays.

The given tree [4,2,6,1,3,5,7] is represented by the following diagram:

          4
        /   \
      2      6
     / \    / \
    1   3  5   7

while the diagrams for the outputs are:

          4
        /   \
      3      6      and    2
            / \           /
           5   7         1
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def splitBST(self, root, V):
        """
        :type root: TreeNode
        :type V: int
        :rtype: List[TreeNode]
        """

        def get_me_l_s(node):
            """
                  4
                /   \
              2      6
             / \    / \
            1   3  5   7
            find the closest node and split it.
            :ret: small tree, large tree
            """

            if not node:
                return None, None

            if node.val > V:
                l_root = node
                st, lt = get_me_l_s(node.left)
                l_root.left = lt
                return st, l_root
            else:  # <= V
                s_root = node
                st, lt = get_me_l_s(node.right)
                s_root.right = st
                return s_root, lt

        return get_me_l_s(root)


def build():
    """
          4
        /   \
      2      6
     / \    / \
    1   3  5   7
    """
    root = TreeNode(4)
    root.left = TreeNode(2)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right = TreeNode(6)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(5)
    return root, 2


if __name__ == "__main__":
    s = Solution()
    result = s.splitBST(*build())
    print(result)
