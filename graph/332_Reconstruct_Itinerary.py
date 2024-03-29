#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/reconstruct-itinerary/description/

Given a list of airline tickets represented by pairs of departure
and arrival airports [from, to], reconstruct the itinerary in order.

All of the tickets belong to a man who departs from JFK.
Thus, the itinerary must begin with JFK.

Note:
If there are multiple valid itineraries,
you should return the itinerary that has the smallest
lexical order when read as a single string.

For example,
the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].

All airports are represented by three capital letters (IATA code).

You may assume all tickets form at least one valid itinerary.

--
Example 1:
tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
Return ["JFK", "MUC", "LHR", "SFO", "SJC"].


Example 2:
tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
Return ["JFK","ATL","JFK","SFO","ATL","SFO"].

Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"].
But it is larger in lexical order.


***
https://www.geeksforgeeks.org/eulerian-path-and-circuit/
Eulerian Path is a path in graph that visits every edge exactly once.
Eulerian Circuit is an Eulerian Path which starts and ends on the same vertex.

Hierholzer’s Algorithm for directed graph
http://www.geeksforgeeks.org/hierholzers-algorithm-directed-graph/
http://www.geeksforgeeks.org/eulerian-path-and-circuit/
https://discuss.leetcode.com/topic/36370/short-ruby-python-java-c

Eulerian Cycle( all about EDGE!!! )
An undirected graph has Eulerian cycle if following two conditions are true.
….a) All vertices with non-zero degree are connected.
We don’t care about vertices with zero degree because they don’t belong
to Eulerian Cycle or Path (we only consider all edges).
….b) All vertices have even degree.

Eulerian Path
An undirected graph has Eulerian Path if following two conditions are true.
….a) Same as condition (a) for Eulerian Cycle
….b) If zero or two vertices have odd degree and all other vertices
have even degree. Note that only one vertex with odd degree is not
possible in an undirected graph
(sum of all degrees is always even in an undirected graph)

How does this work?
In Eulerian path, each time we visit a vertex v, we walk through two unvisited
edges with one end point as v. Therefore, all middle vertices in Eulerian Path
must have even degree. For Eulerian Cycle, any vertex can be middle vertex,
therefore all vertices must have even degree.

Note that a graph with no edges is considered Eulerian because there are no
edges to traverse.

Remember that a directed graph has an Eulerian cycle if following conditions are
true (1) All vertices with nonzero degree belong to a single strongly connected
component. (2) In degree and out degree of every vertex is same. The algorithm
assumes that the given graph has Eulerian Circuit.

步驟:
1. Build graph.
2. Start from a node, say, JFK.
3. Maintain 2 lists. path list(act as stack 紀錄每個node path),
    circuit list(當hit end, end node put into this list)
4. Append path list till the node hit the end.
5. move the end node from path list to circuit list.
6. Retract node one by one. If the node has no other path,
 remove the node from path list to circuit list.

7. If the node has other path, follow the path, and put nodes
into path list.

8. Till hitting the end, back to 4.

9. Thus, all the nodes in path list shall be put into circuit list.

10. Reverse the circuit list and return.
"""


class Solution(object):

    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        概念:
        訪問vertex時代表其even edge of degree已經被訪問.
        - Vertex -
        """
        from collections import defaultdict as dd

        dmap = dd(list)

        for t in sorted(tickets)[::-1]:
            dmap[t[0]].append(t[1])

        result = []

        def dfs(node):
            while dmap[node]:
                dfs(dmap[node].pop())

            result.append(node)

        dfs('JFK')
        return result[::-1]


def build():
    # ['JFK', 'ATL', 'JFK', 'SFO', 'ATL', 'SFO']
    return [["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"],
            ["ATL", "JFK"], ["ATL", "SFO"]]

    return [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]


if __name__ == "__main__":
    s = Solution()
    print(s.findItinerary(build()))
    # ["JFK", "MUC", "LHR", "SFO", "SJC"]

    print(s.rewrite2(build()))
    # ["JFK", "MUC", "LHR", "SFO", "SJC"]
