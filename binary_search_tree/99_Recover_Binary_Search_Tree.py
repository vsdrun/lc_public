#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/recover-binary-search-tree/

Two elements of a binary search tree (BST) are swapped by mistake.

Recover the tree without changing its structure.

Example 1:
Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2


Example 2:
Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3
Follow up:

A solution using O(n) space is pretty straight forward.
Could you devise a constant space solution?
"""

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
          3
         / \
        1   4
           /
          2

        -> 1, 3, 2, 4 -> 1, 2, 3, 4


          2
         / \
        1   4
           /
          3

          1
         /
        3
         \
          2

        -> 3, 2, 1 -> 1, 2, 3

          3
         /
        1
         \
          2
        """
        tmp = [None, None, None]  # prev, first, second

        def inorder(node):
            if not node:
                return

            inorder(node.left)

            if tmp[0] and tmp[0].val > node.val:
                # 重要! 只設定一次
                if tmp[1] is None:
                    tmp[1] = tmp[0]
                tmp[2] = node

            tmp[0] = node

            inorder(node.right)

        inorder(root)

        tmp[1].val, tmp[2].val = tmp[2].val, tmp[1].val



def build():
    """
      1
     /
    3
     \
      2

      3
     /
    1
     \
      2

      2
     /
    3
     \
      1
      [1,3,null,null,2]
      [3,1,null,null,2]
      [2,3,null,null,1]
    """
    _3 = TreeNode(3)
    _1 = TreeNode(1)
    _4 = TreeNode(4)
    _2 = TreeNode(2)
    _3.left = _1
    _3.right = _4
    _4.left = _2
    return _3

def pp(node):
    tmp = []
    nodes = [node]

    print("start pp")

    while nodes:
        next = []
        local = []

        for n in nodes:
            local.append(n.val)
            if n:
                if n.left:
                    next.append(n.left)
                if n.right:
                    next.append(n.right)

        tmp.append(local)
        nodes = next

    print(tmp)

if __name__ == "__main__":
    s = Solution()
    t = build()
    s.recoverTree(t)
    pp(t)
