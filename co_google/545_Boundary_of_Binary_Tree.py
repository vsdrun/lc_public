#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/boundary-of-binary-tree/description/


Given a binary tree, return the values of its boundary in
anti-clockwise direction starting from root.
Boundary includes left boundary,
leaves, and right boundary in order without duplicate nodes.


Left boundary is defined as the path from root to the left-most node.
Right boundary is defined as the path from root to the right-most node.
If the root doesn't have left subtree or right subtree,
then the root itself is left boundary or right boundary.

Note this definition only applies to the input binary tree,
and not applies to any subtrees.

The left-most node is defined as a leaf node you could reach when
you always firstly travel to the left subtree if exists.

If not, travel to the right subtree. Repeat until you reach a leaf node.

The right-most node is also defined by the same
way with left and right exchanged.

Example 1

Input:
 1
   \
    2
   / \
  3   4

Ouput:
[1, 3, 4, 2]

Explanation:
The root doesn't have left subtree, so the root itself is left boundary.
The leaves are node 3 and 4.
The right boundary are node 1,2,4.
Note the anti-clockwise direction means you should output reversed
right boundary.

So order them in anti-clockwise without duplicates and we have [1,3,4,2].


Example 2
Input:
    ____1_____
   /          \
  2            3
 / \          /
4   5        6
   / \      / \
  7   8    9  10

Ouput:
[1,2,4,7,8,9,10,6,3]

Explanation:
The left boundary are node 1,2,4.
(4 is the left-most node according to definition)


The leaves are node 4,7,8,9,10.
The right boundary are node 1,3,6,10. (10 is the right-most node).
So order them in anti-clockwise without duplicate nodes we have
[1,2,4,7,8,9,10,6,3].
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def boundaryOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        how about bfs?
        """
        def dfs_leftmost(node):
            print("dfs left: {}".format(node.val))

            if not node or (not node.left and not node.right):
                print("ret dfs left: {}".format(node.val))
                return

            # 先加
            boundary.append(node.val)

            # 注意這個邏輯. 有left則走left 沒有left才走right
            # 有left則不可能走right!
            if node.left:
                dfs_leftmost(node.left)
            else:
                dfs_leftmost(node.right)

        def dfs_leaves(node):
            if not node:
                return

            dfs_leaves(node.left)

            if node != root and not node.left and not node.right:
                boundary.append(node.val)

            dfs_leaves(node.right)

        def dfs_rightmost(node):
            if not node or not node.left and not node.right:
                return

            # 注意這個邏輯. 有right則走right 沒有right才走left
            # 有right則不可能走left!
            if node.right:
                dfs_rightmost(node.right)
            else:
                dfs_rightmost(node.left)

            # 後加 因為為anti-clockwise.
            boundary.append(node.val)

        if not root:
            return []

        boundary = [root.val]

        dfs_leftmost(root.left)

        dfs_leaves(root)

        dfs_rightmost(root.right)

        return boundary


def build():
    """
    ____1_____
   /          \
  2            3
 / \          /
4   5        6
   / \      / \
  7   8    9  10
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.left.left = TreeNode(3)
    root.right = TreeNode(4)
    return root


if __name__ == "__main__":
    s = Solution()
    print(s.boundaryOfBinaryTree(build()))
