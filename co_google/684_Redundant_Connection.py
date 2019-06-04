#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/redundant-connection/description/

In this problem,
a tree is an *undirected graph* that is connected and has no cycles.

The given input is a graph that started as a tree with N nodes
(with distinct values 1, 2, ..., N), with one additional edge added.


The added edge has two different vertices chosen from 1 to N,
and was not an edge that already existed.


The resulting graph is given as a 2D-array of edges.

** 重要!!
Each element of edges is a pair [u, v] with u < v,
that represents an undirected edge connecting nodes u and v.


Return an edge that can be removed so that the resulting graph is
a tree of N nodes.


If there are multiple answers,
return the answer that occurs last in the given 2D-array.
The answer edge [u, v] should be in the same format, with u < v.


Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given undirected graph will be like this:
  1
 / \
2 - 3


Example 2:
Input: [[1,2], [2,3], [3,4], [1,4], [1,5]]
Output: [1,4]
Explanation: The given undirected graph will be like this:
5 - 1 - 2
    |   |
    4 - 3


Note:
The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N,
where N is the size of the input array.
"""


class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """

        # 只要發現circle便return
        # 因為 1. 只有一個edge造成circle
        # 2. 每加一個edge便檢查是否有circle形成.
        import collections as cc
        union = cc.defaultdict(list)

        def find(node):
            if not union[node]:
                return node
            return find(union[node][0])

        def uf(edge):
            x, y = edge[0], edge[1]
            x = find(x)
            y = find(y)

            if x == y:
                return edge

            union[x].append(y)

        for e in edges:
            r = uf(e)
            if r:
                return r

    def findRedundantConnection_smart(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # quorum 的概念. 由於每個edge為 u<v 所以能確保quorum的形成
        # 而無須backtrack去改之前的quorum.
        # 最後一個edge 的兩端若屬於同一個quorum 則circle形成.
        # 故移除.
        tree = ''.join(map(chr, range(1001)))

        for u, v in edges:
            if tree[u] == tree[v]:
                return [u, v]
            tree = tree.replace(tree[u], tree[v])


def build():
    return [[1, 5], [1, 2], [1, 4], [3, 4], [2, 3]]
    return [[1, 2], [2, 3], [3, 4], [1, 4], [1, 5]]


if __name__ == "__main__":
    s = Solution()
    print(s.findRedundantConnection(build()))
    print(s.findRedundantConnection_smart(build()))
    #  print(s.findRedundantConnection(build()))
