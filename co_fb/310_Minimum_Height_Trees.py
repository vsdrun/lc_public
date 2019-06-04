#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/minimum-height-trees/description/

For a undirected graph with tree characteristics, we can choose any node
as the root.

The result graph is then a rooted tree. Among all possible
rooted trees, those with minimum height are called minimum height trees
(MHTs).

即哪個點為root時其高度最小(不是所有高度的和! 是單一最長高度最小!)


Given such a graph, write a function to find all the MHTs and
return a list of their root labels.

**
The basic idea is "keep deleting leaves layer-by-layer, until reach the root."

--
Format
The graph contains n nodes which are labeled from 0 to n - 1.
You will be given the number n and a list of undirected edges
(each edge is a pair of labels).

You can assume that no duplicate edges will appear in edges.
Since all edges are undirected, [0, 1] is the same as [1, 0]
and thus will not appear together in edges.

Example 1:
Given n = 4, edges = [[1, 0], [1, 2], [1, 3]]

        0
        |
        1
       / \
      2   3

return [1]


Example 2:
Given n = 6, edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]

     0  1  2
      \ | /
        3
        |
        4
        |
        5

return [3, 4]
"""


class Solution(object):

    def findMinHeightTrees(self, n, edges):
        from collections import defaultdict as dd

        nodes = set(range(n))
        dmap = dd(set)

        for (f, e) in edges:
            dmap[f].add(e)
            dmap[e].add(f)

        # 所謂leaf node為connection只有一個link

        while len(nodes) > 2:
            # 找出leaf nodes
            leave = []
            remove = dd(set)

            for k in dmap.keys():
                if len(dmap[k]) == 1:
                    leave.append(k)
                    for p in dmap[k]:
                        remove[p].add(k)
                    dmap.pop(k)

            nodes -= set(leave)

            # remove leaves
            for k in remove:
                for v in remove[k]:
                    dmap[k].remove(v)

        return list(nodes)


def build():
    return 6, [[0,1],[0,2],[0,3],[3,4],[4,5]]
    return 6, [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
    return 5, [[0, 1], [1, 2], [1, 3], [3, 4]]
    return 4, [[1, 0], [1, 2], [1, 3]]


if __name__ == "__main__":
    s = Solution()
    print(s.findMinHeightTrees(*build()))
