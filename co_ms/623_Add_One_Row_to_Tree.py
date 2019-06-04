#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/add-one-row-to-tree/description/

Given the root of a binary tree, then value v and depth d, you need to add a
row of nodes with value v at the given depth d. The root node is at depth 1.

The adding rule is: given a positive integer depth d, for each NOT null
tree nodes N in depth d-1, create two tree nodes with value v as N's left
subtree root and right subtree root.

And N's original left subtree should be the left subtree of the new
left subtree root, its original right subtree should be the right subtree
of the new right subtree root.

If depth d is 1 that means there is no
depth d-1 at all, then create a tree node with value v as the new root of
the whole original tree, and the original tree is the new root's left subtree.

Example 1:
Input: 
A binary tree as following:
       4
     /   \
    2     6
   / \   / 
  3   1 5   

v = 1

d = 2

Output: 
       4
      / \
     1   1
    /     \
   2       6
  / \     / 
 3   1   5   

Example 2:
Input: 
A binary tree as following:
      4
     /   
    2    
   / \   
  3   1    

v = 1

d = 3

Output:
      4
     /
    2
   / \
  1   1
 /     \
3       1
"""

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution(object):
    def addOneRow(self, root, v, d):
        """
        :type root: TreeNode
        :type v: int
        :type d: int
        :rtype: TreeNode
        laeyer by layer thus using bfs...

        先process d-1 layer!
        """
        dummy, dummy.left = TreeNode(None), root
        row = [dummy]

        for _ in range(d - 1):
            row = [kid for node in row for kid in (node.left, node.right) if kid]

        for node in row:
            node.left, node.left.left = TreeNode(v), node.left
            node.right, node.right.right = TreeNode(v), node.right

        return dummy.left

def build():
    """
          4
         /
        2
       / \
      3   1
    """
    root =  TreeNode(1)
    root.left = TreeNode(2)
    root.right= TreeNode(3)
    root.left.left = TreeNode(4)

    return root, 5, 4

def pp(node):
    tree = [node]

    while tree:
        print("layer: {}".format([n.val for n in tree if n]))

        tmp_tree = []

        while tree:
            t = tree[0]
            tree = tree[1:]
            if t.left:
                tmp_tree.append(t.left)
            if t.right:
                tmp_tree.append(t.right)
        tree = tmp_tree

if __name__ == "__main__":
    s = Solution()
    r = s.addOneRow(*build())
    pp(r)
