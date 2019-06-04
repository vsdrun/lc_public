#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/equal-tree-partition/description/

Given a binary tree with n nodes, your task is to check
if it's possible to partition the tree to two trees
which have the equal sum of values after removing exactly one
edge on the original tree.

Example 1:
Input:
    5
   / \
  10 10
    /  \
   2   3

Output: True
Explanation:
    5
   /
  10

Sum: 15

   10
  /  \
 2    3

Sum: 15


Example 2:
Input:
    1
   / \
  2  10
    /  \
   2   20

Output: False
Explanation: You can't split the tree into two trees with
equal sum after removing exactly one edge on the tree.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def checkEqualTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool

        也就是 total sum須為偶數 可以分割.

        累加的概念. 如果sub tree sum 有 total_sum/2 則可以分割.

        然要注意! 確定是否真的可以分割!
        簡單 將 sum 為 half 的 node 存起來
        看看其是否真的為其他node的left or right
        https://leetcode.com/problems/equal-tree-partition/discuss/128816/Let's-axe-the-tree-O(N)-java-solution
        """
        sum_set = set()

        gotit = [None]  # save node that has it's accumulation equals to half
        # total

        def sumup(node, half=None):
            sm = 0

            if not node:
                return sm

            sm = node.val + sumup(node.left, half) + sumup(node.right, half)

            if half is not None:
                if sm == half and gotit[0] is None:  # 存子不存父
                    # true split
                    gotit[0] = node

            sum_set.add(sm)

            return sm

        total = sumup(root)

        if total % 2:
            return False

        half = (total / 2)

        sumup(root, half)

        root_q = [root]

        while root_q:
            tmp_q = []

            for r in root_q:
                if gotit[0] is not None and r.left == gotit[0]:
                    return True

                if gotit[0] is not None and r.right == gotit[0]:
                    return True

                tmp_q += [q for q in (r.left, r.right) if q]

            root_q = tmp_q

        return False


def build():
    """
    5
   / \
  10 10
    /  \
   2   3
    """

    root = TreeNode(0)
    root.right = TreeNode(0)
    return root
    root = TreeNode(0)
    root.left = TreeNode(-1)
    root.right = TreeNode(1)
    return root
    root = TreeNode(5)
    root.left = TreeNode(10)
    root.right = TreeNode(10)
    root.right.right = TreeNode(3)
    root.right.left = TreeNode(2)
    return root
    root = TreeNode(2)
    root.right = TreeNode(3)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(5)
    root.right.right.right.right = TreeNode(6)
    return root


if __name__ == "__main__":
    s = Solution()
    print(s.checkEqualTree(build()))
