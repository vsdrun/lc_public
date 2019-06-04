#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/closest-leaf-in-a-binary-tree/description/

Given a binary tree where
**every node has a unique value**,
and a target key k,
find the value of the nearest leaf node to target k in the tree.


Here, nearest to a leaf means the least number of edges travelled on
the binary tree to reach any leaf of the tree.


Also, a node is called a leaf if it has no children.


In the following examples,
the input tree is represented in flattened form row by row.
The actual root tree given will be a TreeNode object.


Example 1:
Input:
root = [1, 3, 2], k = 1
Diagram of binary tree:
          1
         / \
        3   2

Output: 2 (or 3)
Explanation: Either 2 or 3 is the nearest leaf node to the target of 1.


Example 2:
Input:
root = [1], k = 1

Output: 1
Explanation: The nearest leaf node is the root node itself.


Example 3:
Input:
root = [1,2,3,4,null,null,null,5,null,6], k = 2
Diagram of binary tree:
             1
            / \
           2   3
          /
         4
        /
       5
      /
     6

Output: 3
Explanation:
The leaf node with value 3 (and not the leaf node with value 6)
is nearest to the node with value 2.
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def findClosestLeaf(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        nearest, thus, consider BFS.
        1. 先bulid up graph
        2. traverse with BFS
        """
        import collections as cc

        graph = cc.defaultdict(list)
        leaf = []

        def build_graph(root):
            if not root.left and not root.right:
                leaf.append(root.val)
                return

            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                build_graph(root.left)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                build_graph(root.right)

        build_graph(root)

        root = [k]
        visited = set()

        while root:
            cur = root.pop(0)
            visited.add(cur)

            if cur in leaf:
                return cur

            for v in graph[cur]:
                if v not in visited:
                    root.append(v)

    def rewrite(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        nearest, thus, consider BFS.
        1. 先bulid up graph
        2. traverse with BFS
        """
        from collections import defaultdict as dd

        dmap = dd(list)
        rq = [root]

        leaves = set()

        while rq:
            for r in rq:
                if r.left:
                    dmap[r.val].append(r.left.val)
                    dmap[r.left.val].append(r.val)
                if r.right:
                    dmap[r.val].append(r.right.val)
                    dmap[r.right.val].append(r.val)
                if not r.left and not r.right:
                    dmap[r.val].append(r.val)  # recursive back to itself
                    leaves.add(r.val)

            rq = [i for r in rq for i in (r.left, r.right) if i]

        visited = set()

        def add_to_visited(ret, to_be_add):
            visited.add(to_be_add)
            return ret

        def bfs(node):
            rq = [node]

            while rq:
                rq = [add_to_visited(i, r) for r in rq if r not in visited
                      for i in dmap[r]]

                for r in rq:
                    if r in leaves:
                        return r

        return bfs(k)

    def rewrite_2(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int

        nearest, thus, consider BFS.
        1. 先bulid up graph
        2. traverse with BFS
        """
        from collections import defaultdict as dd
        dmap = dd(list)

        # create double direction list
        # for going to either way
        # use visited to prevent loop

        def build_graph(node):
            if node.left:
                dmap[node.val] += node.left.val,
                dmap[node.left.val] += node.val,
                build_graph(node.left)
            if node.right:
                dmap[node.val] += node.right.val,
                dmap[node.right.val] += node.val,
                build_graph(node.right)

            if not node.left and not node.right:
                dmap[node.val] += None,  # leaf node

        build_graph(root)

        root = [k]
        visited = set()

        while root:
            next_root = []

            for crnt in root:
                visited.add(crnt)
                if None in dmap[crnt]:
                    return crnt  # we hit leaf node

                for nxt in dmap[crnt]:
                    if nxt not in visited:
                        next_root += nxt,

            root = next_root


def build():
    """
    3
   / \
  9  20
    /  \
   15   7

             1
            / \
           2   3
          /
         4
        /
       5
      /
     6
    """
    root = TreeNode(1)
    root.right = TreeNode(3)
    root.left = TreeNode(2)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(5)
    root.left.left.left.left = TreeNode(6)
    return root, 2

    root = TreeNode(3)
    root.left = TreeNode(9)
    root.right = TreeNode(20)
    root.right.right = TreeNode(7)
    root.right.left = TreeNode(15)
    return root, 3

    return None

    root = TreeNode(1)
    return root, 1


if __name__ == "__main__":
    s = Solution()
    print(s.findClosestLeaf(*build()))
    print(s.rewrite_2(*build()))
