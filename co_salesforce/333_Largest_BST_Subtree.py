#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/largest-bst-subtree/description/


Given a binary tree,
find the largest subtree which is a Binary Search Tree (BST),
where largest means subtree with largest number of nodes in it.

!!也就是找bst subtree 有最多的node.

Note:
重要!
A subtree must include all of its descendants.

Here's an example:
    10
    / \
   5  15
  / \   \
 1   8   7

The Largest BST Subtree in this case is the highlighted one.
The return value is the subtree's size, which is 3.

   5
  / \
 1   8

Follow up:
Can you figure out ways to solve it with O(n) time complexity?
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def largestBSTSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: int
            10
            / \
           5  15
          / \   \
         1   8   7
        """
        mmax = [0]

        def dfs(node):
            """
            :ret: min, max, cnt:-1 if no bst
            """
            if not node:
                return -1, -1, 0

            #  print("---")
            #  print("node: {}".format(node.val))

            lmin = lmax = rmin = rmax = 0
            currentCnt = lcnt = rcnt = 0

            lmin, lmax, lcnt = dfs(node.left)
            rmin, rmax, rcnt = dfs(node.right)
            olmax = lmax
            ormin = rmin

            # 準備return 的值
            if lmax == -1:
                lmax = node.val
            if rmin == -1:
                rmin = node.val

            if lmin == -1:
                lmin= node.val
            if rmax == -1:
                rmax= node.val

            # leaf node
            if lcnt == 0 and rcnt == 0:
                #  print("leaf: {}".format(node.val))
                currentCnt += 1
                mmax[0] = max(mmax[0], currentCnt)
                return lmax, rmin, currentCnt

            # 此node以下不能作為bst
            if lcnt == -1 or rcnt == -1:
                #  print("no can do: {}".format(node.val))
                return -1, -1, -1

            if (olmax if olmax != -1 else float("-inf")) < node.val < \
                (ormin if ormin != -1 else float("inf")):

                #  print("olmax: {} ormin: {} node: {}".format(olmax, ormin, node.val))
                currentCnt = 1 + lcnt + rcnt
                mmax[0] = max(mmax[0], currentCnt)
                #  print("lcnt: {} rcnt: {} currentCnt: {}".format(lcnt, rcnt, currentCnt))
                return lmin, rmax, currentCnt
            else:
                return -1, -1, -1

        dfs(root)
        return mmax[0]

    def rewrite(self, root):
        """
        :type root: TreeNode
        :rtype: int
            10
            / \
           5  15
          / \   \
         1   8   7

         Best solution
        """

        def dfs(root):
            """
            :ret: Size of BST, number of bst nodes (0 if not bst), min, max
            """
            if not root:
                return 0, 0, float('inf'), float('-inf')

            N1, n1, min1, max1 = dfs(root.left)
            N2, n2, min2, max2 = dfs(root.right)
            # 注意 float("-inf") trick... 因為可能不是bst!
            n = n1 + 1 + n2 if max1 < root.val < min2 else float("-inf")

            return max(N1, N2, n), n, min(min1, root.val), max(max2, root.val)

        return dfs(root)[0]

def build():
    """
    10
    / \
   5  15
  / \   \
 1   8   7


    3
  /   \
 2     4
     /
    1
    """
    root = TreeNode(4)
    root.left = TreeNode(1)
    root.right = TreeNode(6)
    root.right.left = TreeNode(5)
    root.right.left.left = TreeNode(2)
    return root

    root = TreeNode(10)
    root.left = TreeNode(5)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(8)
    root.right = TreeNode(15)
    root.right.right = TreeNode(7)
    return root


def prt(root):
    r = [root]

    while r:
        print(n.val for n in r)

        r = [v for n in r for v in (n.left, n.right) if v]


if __name__ == "__main__":
    s = Solution()
    print(s.largestBSTSubtree(build()))
    print(s.rewrite(build()))
