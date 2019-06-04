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

"""


class Solution(object):
    def countComponents(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: int
        """
        from __builtin__ import xrange

        graph = {i: [] for i in xrange(n)}

        # build graph
        for e in edges:
            graph[e[0]] += e[1],
            graph[e[1]] += e[0],

        def dfs(key):
            child = graph.pop(key, [])

            for c in child:
                dfs(c)

        cnt = 0

        while graph:
            key = graph.keys()[0]

            dfs(key)
            cnt += 1

        return cnt


def build():
    return 5, [[0, 1], [1, 2], [3, 4]]


if __name__ == "__main__":
    s = Solution()
    print(s.countComponents(*build()))
    #  print(s.findRedundantConnection(build()))
