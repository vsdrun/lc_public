#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/path-sum-ii/description/

Given a binary tree and a sum,
find all root-to-leaf paths where each path's sum equals the given sum.

For example:
Given the below binary tree and sum = 22,
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
return
[
   [5,4,11,2],
   [5,8,4,5]
]
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def pathSum(self, root, su):
        """
        :type root: TreeNode
        :type su: int
        :rtype: List[List[int]]

        DFS:
        Use stack to save path.

        用 sum - current value 直到 根node等於剩下的sum 則為答案
        這樣比較快 不用每次sum[stack]
        """
        if not root:
            return []

        def dfs(node):
            stack.append(node)

            if not node.left and not node.right:
                vals = [i.val for i in stack]

                if sum(vals) == su:
                    result.append(vals)

            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)

            stack.pop()

        stack = []
        result = []

        dfs(root)

        return result

    def rewrite(self, root, sum):
        """
        :type root: TreeNode
        :type su: int
        :rtype: List[List[int]]
        use minus!
        """
        # 存path.
        stack = []
        # 存結果.
        result = []

        def dfs(node, s):
            if not node:
                return False

            stack.append(node.val)

            if not node.left and not node.right and s - node.val == 0:
                result.append(stack[:])
                stack.pop()
                return True

            dfs(node.left, s - node.val)
            dfs(node.right, s - node.val)
            stack.pop()
            return False

        dfs(root, sum)
        return result


def build():
    """
              5
             / \
            4   8
           /   / \
          11  13  4
         /  \    / \
        7    2  5   1
    """
    root = TreeNode(5)
    root.left = TreeNode(4)
    root.right = TreeNode(8)
    root.right.right = TreeNode(4)
    root.right.right.right = TreeNode(1)
    root.right.right.left = TreeNode(5)
    root.right.left = TreeNode(13)
    root.left.left = TreeNode(11)
    root.left.left.left = TreeNode(7)
    root.left.left.right = TreeNode(2)
    return root, 22


if __name__ == "__main__":
    s = Solution()
    print(s.pathSum(*build()))
    print(s.rewrite(*build()))
