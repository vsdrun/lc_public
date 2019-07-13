#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/is-graph-bipartite/description/

Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into
two independent subsets A and B such that every edge in
the graph has one node in A and another node in B.


The graph is given in the following form: graph[i] is a list of
indexes j for which the edge between nodes i and j exists.

Each node is an integer between 0 and graph.length - 1.

There are no self edges or parallel edges:
    graph[i] does not contain i,
    and it doesn't contain any element twice.


Example 1:
Input: [[1,3], [0,2], [1,3], [0,2]]
Output: true


Explanation:
The graph looks like this:
0----1
|    |
|    |
3----2

We can divide the vertices into two groups: {0, 2} and {1, 3}.


Example 2:
Input: [[1,2,3], [0,2], [0,1,3], [0,2]]
Output: false
Explanation:
The graph looks like this:
0----1
| \  |
|  \ |
3----2
We cannot find a way to divide the set of nodes into two independent subsets.
"""


class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        哈囉! 這裡input的graph array index為node, value為連到的node!
        """
        from collections import defaultdict

        # 初始化~
        color = defaultdict(lambda: -1)

        # 檢查為必須 不然第一個node下的改了為1
        # 此下去又設定為0 衝突 為 False 但其實是True...
        return all(
            self.dfs(graph, v, edges, 0, color)
            for v, edges in enumerate(graph)
            if color[v] == -1)

        # --------------------------------------------
        # debug: single [True] or [False]
        result = [
            self.dfs(graph, v, edges, 0, color)
            for v, edges in enumerate(graph)
            if color[v] == -1]  # 檢查為必須 不然第一個node下的改了為1
        # 此下去又設定為0 衝突 為 False 但其實是True...

    def dfs(self, graph, v, edges, cur_color, color):

        if color[v] != -1:
            return color[v] == cur_color

        color[v] = cur_color

        # all([]) 為 true
        return all(
            self.dfs(graph, e, graph[e], int(not cur_color), color)
            for e in edges)

    def rewrite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        哈囉! 這裡input的graph array index為node, value為連到的node!
        """
        from collections import defaultdict as dd

        def check(node, expect_currnet_color, connected_nodes, color, visited):
            if visited[node]:
                return color[node] == expect_currnet_color

            visited[node] = True
            #  print("node: {} expect: {}".format(node, expect_currnet_color))
            color[node] = expect_currnet_color

            return all([check(node, not expect_currnet_color,
                              graph[node], color, visited)
                        for node in connected_nodes])

        visited = dd(lambda: False)
        color = dict()
        expect_currnet_color = True

        # graph 想到circle.
        return all([check(this_node, expect_currnet_color, connected_nodes,
                          color, visited)
                    for this_node, connected_nodes in enumerate(graph)
                    if visited[this_node] is False])

    def rewrite2(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        哈囉! 這裡input的graph array index為node, value為連到的node!
        """
        # 用 enumerate
        visited = set()
        colorset = dict()

        def check(head, child, expectColor):
            visited.add(head)

            colorset[head] = expectColor

            for c in child:
                if c in colorset and (not expectColor) != colorset[c]:
                    return False

                colorset[c] = not expectColor
            # all([]) == True
            return all(check(c, graph[c], not expectColor)
                       for c in child
                       if c not in visited
                       )

        return all(
            check(head, child, False)
            for head, child in enumerate(graph)
            if head not in visited)

    def rewrite3(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        另一種策略 比較慢 但是仍有效
        使用dict(hash dict)仍是比較有效的方式 而此我們使用set,
        其實內部使用的implement應該也是hash map)
        """
        def check(child, flag):
            if not flag:
                for c in child:
                    if c in setA:
                        return False
            else:
                for c in child:
                    if c in visited and c not in setA:
                        return False
                    setA.add(c)

            for c in child:
                if c not in visited:
                    visited.add(c)

                    if not check(graph[c], not flag):
                        return False

            return True

        setA = set() # True flag nodes
        visited = set()

        for head, child in enumerate(graph):
            if head not in visited:
                visited.add(head)
                setA.add(head)
                if not check(child, False):
                    return False

        return True


def build():
    return [[1, 3], [0, 2], [1, 3], [0, 2]]
    return [[1, 2, 3], [0, 2], [0, 1, 3], [0, 2]]
    return [[1, 3], [0, 2], [1, 3], [0, 2]]  # [0,2] 重複...


if __name__ == "__main__":
    s = Solution()
    print(s.isBipartite(build()))
    print(s.rewrite(build()))
    print(s.rewrite2(build()))
    print(s.rewrite3(build()))
