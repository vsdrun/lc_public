#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/binary-tree-upside-down/description/

ref:
https://leetcode.com/problems/binary-tree-upside-down/discuss/49410/Explain-the-question-and-my-solution-Python

Given a binary tree where all the right nodes are either leaf nodes
with a sibling (a left node that shares the same parent node) or empty,


1. flip it upside down and
2. turn it into a tree where the original right
    nodes turned into left leaf nodes.
3. Return the new root.


For example:
Given a binary tree {1,2,3,4,5},
    1
   / \
  2   3
 / \
4   5

[1]
[2 3]
[4 5]


    1
   / \
  2   3
 / \ /
4   5


return the root of the binary tree [4,5,2,#,#,3,1].

  4
 / \
5   2
   / \
  3   1
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def upsideDownBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        BFS? No!
        Devide and conquer.
        觀察到 root 往上傳.
        """

        # 目前的root 會成為 rmost.right!

        if not root or not root.left:
            return root

        # stop at 2
        lRoot = self.upsideDownBinaryTree(root.left)  # 4
        rMost = lRoot  # 4

        # 吃掉 right most
        while rMost.right:
            rMost = rMost.right

        # root = 2
        # root.right = 5
        # rMost = 4
        # lRoot = 4
        # 目前的root 會成為 rmost.right!
        root, rMost.left, rMost.right = lRoot, root.right, TreeNode(root.val)

        return root

    def rewrite(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        stack comes to the rescue
1. flip it upside down and
2. turn it into a tree where the original right
    nodes turned into left leaf nodes.
3. Return the new root.
            1
           / \
          2   3
         / \
        4   5

        [1]
        [2 3]
        [4 5]
          4
         / \
        5   2
           / \
          3   1
  using stack + bfs to do it
        """
        if not root:
            return

        r = [root]
        tmp = []

        while r:
            tmp.append(r)
            next = []

            for node in r:
                if node.left:
                    next.append(node.left)
                if node.right:
                    next.append(node.right)

            r = next

        """
            1
           / \
          2   3
         / \
        4   5

          4
         / \
        5   2
           / \
          3   1
        """
        prev = nroot = None

        while tmp:
            ll = tmp.pop()

            root = ll[0]
            if prev:
                prev.right = root

            root.left = ll[1] if len(ll) > 1 else None

            prev = root

            if not nroot:
                nroot = root

        if prev:
            prev.right = None

        return nroot



def build():
    """
    1
   / \
  2   3
 / \
4   5
    """
    return None
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    return root

def pp(root):
    """
      4
     / \
    5   2
       / \
      3   1
    """

    tmp = []
    r = [root]

    while r:
        tmp.append([n.val for n in r])

        r = [node for n in r for node in [p for p in n.left, n.right if p is not
            None]]

    print(tmp)


if __name__ == "__main__":
    s = Solution()
    pp(s.upsideDownBinaryTree(build()))
    pp(s.rewrite(build()))
