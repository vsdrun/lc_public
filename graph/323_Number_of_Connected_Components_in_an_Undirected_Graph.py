#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/

Given n nodes labeled from 0 to n - 1 and a list of undirected edges
(each edge is a pair of nodes),

write a function to find the number of
connected components in an undirected graph.

Example 1:
     0          3
     |          |
     1 --- 2    4
Given n = 5 and edges = [[0, 1], [1, 2], [3, 4]], return 2.

Example 2:
     0           4
     |           |
     1 --- 2 --- 3
Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [3, 4]], return 1.


Note:
You can assume that no duplicate edges will appear in edges.
Since all edges are undirected,
[0, 1] is the same as [1, 0] and thus will not appear together in edges.


記得!!!
undirect graph 請將兩邊node均放入graph 的 key 中!
不然
e.g [0,1]
0:[]
1:0
會被視為兩個traverse!!! 因為 0:[] traverse不到 1.
"""


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        from __builtin__ import xrange
        # 因為有 n, 可能 單獨一個 node 沒有 edge!
        graph = {i: [] for i in xrange(n)}

        # build graph
        for e in edges:
            graph[e[0]] += e[1],
            graph[e[1]] += e[0],

        def dfs(key):
            # act as visited.
            child = graph.pop(key, [])

            for c in child:
                dfs(c)

        cnt = 0

        while graph:
            key = graph.keys()[0]

            dfs(key)
            cnt += 1

        return cnt

    def rewrite(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        from collections import defaultdict as dd

        graph = dd(list)

        for i in range(n):
            graph[i] = []

        for e in edges:
            graph[e[0]] += e[1],
            graph[e[1]] += e[0],

        def dfs(n):
            keys = graph.pop(n, [])

            for k in keys:
                dfs(k)

        cnt = 0

        while graph:
            k = graph.keys()[0]

            dfs(k)
            cnt += 1

        return cnt

    def rewrite2(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """

        # build graph
        from collections import defaultdict as dd

        dmap = dd(list)

        for e in edges:
            dmap[e[0]].append(e[1])
            dmap[e[1]].append(e[0])

        def dfs(node):

            if node not in dmap:
                return

            cnodes = dmap[node]
            del dmap[node]

            for n in cnodes:
                dfs(n)

        cnt = 0

        while dmap:
            cnt += 1
            dfs(dmap.keys()[0])

        return cnt


def build():
    return 2, [[1, 0]]
    return 5, [[0, 1], [1, 2], [3, 4]]


if __name__ == "__main__":
    s = Solution()
    print(s.countComponents(*build()))
    print(s.rewrite(*build()))
    print(s.rewrite2(*build()))
