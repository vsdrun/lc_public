#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/

Given a binary tree rooted at root,
the depth of each node is the shortest distance to the root.

A node is deepest if it has the largest depth possible among
any node in the entire tree.

The subtree of a node is that node,
plus the set of all descendants of that node.

Return the node with the largest depth such that it
contains all the deepest nodes in its subtree.


Example 1:
Input: [3,5,1,6,2,0,8,null,null,7,4]
Output: [2,7,4]

Explanation:
We return the node with value 2, colored in yellow in the diagram.
The nodes colored in blue are the deepest nodes of the tree.
The input "[3, 5, 1, 6, 2, 0, 8, null, null, 7, 4]"
is a serialization of the given tree.


The output "[2, 7, 4]" is a serialization of the subtree rooted at the node with
value 2.

Both the input and output have TreeNode type.

Note:
The number of nodes in the tree will be between 1 and 500.
The values of each node are unique.
"""


# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None


class Solution(object):
    def subtreeWithAllDeepest(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        Record the leaf node depth.
        """
        def dfs(node):
            """
            :ret: depth, node
            """
            if not node:
                return 0, None

            ld, lnode = dfs(node.left)
            rd, rnode = dfs(node.right)

            if ld == rd:
                return ld + 1, node

            if ld > rd:
                return ld + 1, lnode
            else:
                return rd + 1, rnode

        return dfs(root)[1]

def build():
    """
    PASS
    """
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n1 = TreeNode(1)
    n6 = TreeNode(6)
    n2 = TreeNode(2)
    n0 = TreeNode(0)
    n8 = TreeNode(8)
    n7 = TreeNode(7)
    n4 = TreeNode(4)

    n3.left = n5
    n3.right = n1
    n5.left = n6
    n5.right = n2
    n1.left = n0
    n1.right = n8

    n2.left = n7
    n2.right = n4
    return n3


def pp(node):
    result = []
    node = [node]

    while node:
        result.extend([n.val for n in node if n])
        node = [v for n in node if n for v in (n.left, n.right)]

    print(result)

if __name__ == "__main__":
    pp(build())

    s = Solution()
    r = s.subtreeWithAllDeepest(build())
    print(r.val)
    pp(r)
