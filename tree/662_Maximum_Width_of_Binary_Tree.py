#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/maximum-width-of-binary-tree/description/



Given a binary tree,
write a function to get the maximum width of the given tree.
The width of a tree is the maximum width among all levels.
The binary tree has the same structure as a full binary tree,
but some nodes are null.

The width of one level is defined as the length between the end-nodes
(the leftmost and right most non-null nodes in the level,
where the null nodes between the end-nodes are also
counted into the length calculation.


Example 1:
Input:

           1
         /   \
        3     2
       / \     \
      5   3     9


Output: 4
Explanation:
The maximum width existing in the third level with the length 4 (5,3,null,9).


Example 2:
Input:

          1
         /
        3
       / \
      5   3

Output: 2
Explanation: The maximum width existing in the third level with the length 2 (5,3).


Example 3:
Input:

          1
         / \
        3   2
       /
      5

Output: 2
Explanation: The maximum width existing in the second level with the length 2 (3,2).


Example 4:
Input:

          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
Output: 8
Explanation:The maximum width existing in the fourth level with the length 8
(6,null,null,null,null,null,null,7).

"""


# Defini# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int

        判斷:
        頭, 尾 然後算level
        """
        if not root:
            return 0

        rq = [(0, root)]
        w_cnt = 0

        while rq:
            tmp_rq = []

            w_cnt = max(w_cnt, (rq[-1][0] - rq[0][0]) + 1)

            # be consistent!!!
            # adding sequence!
            # idea: 下一個layer的index為此layer * 2 (+1 if right)
            for idx, r in rq:
                if r.left:
                    tmp_rq.append((idx * 2, r.left))
                if r.right:
                    tmp_rq.append((idx * 2 + 1, r.right))

            rq = tmp_rq

        return w_cnt


def build():
    """
          1
         / \
        3   2
       /     \
      5       9
     /         \
    6           7
    """

    root = TreeNode(1)
    root.right = TreeNode(2)
    root.right.right = TreeNode(9)
    root.right.right.right = TreeNode(7)
    root.left = TreeNode(3)
    root.left.left = TreeNode(5)
    root.left.left.left = TreeNode(6)
    return root


if __name__ == "__main__":
    s = Solution()
    print(s.widthOfBinaryTree(build()))
