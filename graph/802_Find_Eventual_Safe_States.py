#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/find-eventual-safe-states/description/


In a directed graph, we start at some node and every turn,
walk along a directed edge of the graph.
If we reach a node that is terminal
(that is, it has no outgoing directed edges), we stop.


Now, say our starting node is eventually safe if and only
if we must eventually walk to a terminal node.

More specifically,
there exists a natural number K so that for any choice of where to walk,
we must have stopped at a terminal node in less than K steps.

Which nodes are eventually safe?  Return them as an array in sorted order.

The directed graph has N nodes with labels 0, 1, ..., N-1,
where N is the length of graph.

The graph is given in the following form: graph[i] is a
list of labels j such that (i, j) is a directed edge of the graph.


Example:
Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
Output: [2,4,5,6]

Here is a diagram of the above graph.
"""


class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict as dd

        result = set()
        visited = dd(lambda: False)

        circle = set()

        def dfs(node):
            if node in circle:
                # there's a circle
                return False

            if node in visited:
                return visited[node]

            circle.add(node)

            mark = True

            for c in graph[node]:
                if not dfs(c):
                    mark = False

            circle.remove(node)

            if mark:
                result.add(node)

            visited[node] = mark

            return mark

        for head, child in enumerate(graph):
            if not child:
                result.add(head)
                visited[head] = True

            dfs(head)

        return sorted(result)


def build():
    return [[0], [2, 3, 4], [3, 4], [0, 4], []]  # [4]
    return [[1, 2], [2, 3], [5], [0], [5], [], []]  # [2,4,5,6]


if __name__ == "__main__":
    s = Solution()
    print(s.eventualSafeNodes(build()))
