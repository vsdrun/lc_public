#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/clone-graph/description/

Clone an undirected graph.
Each node in the graph contains a label and a list of its neighbors.

OJ's undirected graph serialization:
    Nodes are labeled uniquely.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself),
thus forming a self-cycle.

Note:
The number of nodes will be between 1 and 100.
The undirected graph is a simple graph, which means no repeated edges and no self-loops in the graph.
Since the graph is undirected, if node p has node q as neighbor, then node q must have node p as neighbor too.
You must return the copy of the given node as a reference to the cloned graph.
"""


# Definition for a undirected graph node
class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    def cloneGraph(self, node):
        """
        Using dfs + memoir
        """
        if not node:
            return node

        memoir = {}

        def clone(node):
            if node.label in memoir:
                return memoir[node.label]

            new_node = UndirectedGraphNode(node.label)

            memoir[node.label] = new_node  # cache first to avoid loop..

            for n in node.neighbors:
                if n.label == new_node.label:
                    # connected to itself..
                    new_node.neighbors.append(new_node)
                else:
                    # DFS
                    new_node.neighbors.append(clone(n))

            return new_node

        return clone(node)


def build_node():
    node0 = UndirectedGraphNode(0)
    node1 = UndirectedGraphNode(1)
    node2 = UndirectedGraphNode(2)

    node0.neighbors.append(node1)
    node0.neighbors.append(node2)

    node1.neighbors.append(node2)

    node2.neighbors.append(node2)
    return node0


if __name__ == "__main__":
    node = build_node()

    s = Solution()
    result = s.cloneGraph(node)
