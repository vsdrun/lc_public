#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/find-leaves-of-binary-tree/description/

Given a binary tree,
collect a tree's nodes as if you were doing this:
Collect and remove all leaves, repeat until the tree is empty.

Example:
Given binary tree
          1
         / \
        2   3
       / \
      4   5
Returns [4, 5, 3], [2], [1].

Explanation:
1. Removing the leaves [4, 5, 3] would result in this tree:

          1
         /
        2
2. Now removing the leaf [2] would result in this tree:

          1
3. Now removing the leaf [1] would result in the empty tree:

          []
Returns [4, 5, 3], [2], [1].

"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        DFS collect~
        """

        collect = []

        def dfs(node, tc):

            if not node.left and not node.right:
                tc.append(node.val)
                return True

            if node.left:
                if dfs(node.left, tc):
                    node.left = None

            if node.right:
                if dfs(node.right, tc):
                    node.right = None

        while root:
            this_collect = []

            if dfs(root, this_collect):
                root = None

            collect.append(this_collect)

        return collect

        # ---better---

        def DFS(root):
            if not root:
                return 0

            left = DFS(root.left)
            right = DFS(root.right)
            level = max(left, right) + 1

            if len(res) >= level:
                res[level - 1].append(root.val)
            else:
                res.append([root.val])

            return level

        res = []
        DFS(root)

        return res

    def rewrite(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]

        DFS collect~
        """
        if not root:
            return []

        # 0 為最底, stack of list
        stack = []

        def dfs(node):
            """
            :ret: level
            """
            if not node:
                return 0

            currentLevel = 1 + max(dfs(node.left), dfs(node.right))
            levels = len(stack)

            if currentLevel > levels:
                stack.append([])

            # stack 裡第幾層.
            stack[currentLevel - 1].append(node.val)

            return currentLevel

        dfs(root)
        return stack


def build():
    """
          1
         / \
        2   3
       / \
      4   5
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root


if __name__ == "__main__":
    s = Solution()
    print(s.findLeaves(build()))
    print(s.rewrite(build()))
