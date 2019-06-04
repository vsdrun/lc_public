#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/graph-valid-tree/description/

Given n nodes labeled from 0 to n - 1 and a list of undirected edges
(each edge is a pair of nodes),
write a function to check whether these edges make up a valid tree.

For example:

Given n = 5 and edges = [[0, 1], [0, 2], [0, 3], [1, 4]], return true.

Given n = 5 and edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]], return false.

Note:
you can assume that no duplicate edges will appear in edges.
Since all edges are undirected,
[0, 1] is the same as [1, 0] and thus will not appear together in edges.

https://leetcode.com/problems/graph-valid-tree/discuss/69020/8-10-lines-Union-Find-DFS-and-BFS

1 union find
2 dfs
3 bfs

valid tree 須檢查:
Has n-1 edges and is acyclic.
Has n-1 edges and is connected.
"""


class Solution(object):
    def validTree_faster(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # Has n-1 edges and is acyclic.
        # Union find只負責找circle, 不負責判定是否為connected.
        # connected 以 len(edges) == n - 1 判定.
        # 也就是，如果為connected，則必有 n-1 個edge.

        # 以array index and value acts as like dict.
        parent = range(n)
        print("ha")

        def find(x):
            print(type(x))
            return x if parent[x] == x else find(parent[x])

        def union(xy):
            print("xy: {}".format(xy))
            map_result = map(find, xy)

            x, y = map_result

            if x == y:
                return False

            parent[x] = y

            return True

        # 1. check node number   2. check is there a cycle
        return len(edges) == n - 1 and all(map(union, edges))

    def validTree(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # Has n-1 edges and is acyclic.
        # Union find只負責找circle, 不負責判定是否為connected.
        # connected 以 len(edges) == n - 1 判定.
        # 也就是，如果為connected，則必有 n-1 個edge.

        # 以array index and value acts as like dict.
        parent = range(n)

        def find(x):
            print("x: {}".format(x))

            return x if parent[x] == x else find(parent[x])

        def union(xy):
            map_result = map(find, xy)

            print("map_result: {}".format(map_result))

            x, y = map_result

            parent[x] = y

            return x != y

        return len(edges) == n - 1 and all(map(union, edges))

    def validTree_dfs(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        """
        # Has n-1 edges and is connected.
        # DFS 只負責判斷是否為 connected
        # 不負責判斷 circle.
        # 即若有circle則 len(edges) == n

        # smart way of building up dict graph
        neighbors = {i: [] for i in range(n)}

        for v, w in edges:
            neighbors[v] += w,
            neighbors[w] += v,

        def visit(v):
            # 這是在查
            # all edges is connected.
            # 若 edges 沒有 connected, neighbors 會有剩下的值.
            # 因為 DFS 無法 travel 到...
            map(visit, neighbors.pop(v, []))

        visit(0)

        return len(edges) == n - 1 and not neighbors

    def rewrite(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        1. count edge  , n - 1
        2. union find
        """
        graph = dict()

        def union_find(node):
            if node not in graph:
                return node
            return union_find(graph[node])

        def dfs(edge):
            x, y = edge

            x = union_find(x)
            y = union_find(y)

            if x == y:
                return False

            graph[x] = y
            return True

        return len(edges) == (n - 1) and all(map(dfs, edges))

    def rewrite2(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: bool
        1. no circle
        2. 只有n-1個edge, 然, 非connect 也會有n-1個edge, 故以dfs檢查connected.
        3. 需要用union find , 而不能用visited.
        因為要找的是un-dircted circle, visited 用在direct circle.
        """
        if len(edges) != n - 1:
            return False

        dmap = {}

        def check(node):
            if dmap.get(node, None) is not None:
                return check(dmap.get(node))
            return node

        def dfs(edge):

            x = check(edge[0])
            y = check(edge[1])

            if x == y:
                return False

            dmap[x] = y
            return True

        for e in edges:
            if not dfs(e):
                return False

        return True


def build():
    return 5, [[0, 1], [0, 2], [0, 3], [1, 4]]  # True
    return 5, [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]  # False
    return 5, [[0, 1], [0, 4], [1, 4], [2, 3]]  # False
    return 2, [[0, 1]]  # True
    return 3, [[0, 1], [1, 2], [2, 0]]  # False


if __name__ == "__main__":
    s = Solution()
    print(s.validTree_faster(*build()))
    #  print(s.rewrite(*build()))
    #  print(s.rewrite2(*build()))
