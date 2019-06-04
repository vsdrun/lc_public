#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/clone-graph/description/

Clone an undirected graph.
Each node in the graph contains a label and a list of its neighbors.


OJ's undirected graph serialization:
    Nodes are labeled uniquely.

We use # as a separator for each node, and ','
as a separator for node label and each neighbor of the node.

As an example, consider the serialized graph {0,1,2#1,2#2,2}.

The graph has a total of three nodes,
and therefore contains three parts as separated by #.

First node is labeled as 0. Connect node 0 to both nodes 1 and 2.
Second node is labeled as 1. Connect node 1 to node 2.
Third node is labeled as 2. Connect node 2 to node 2 (itself),
thus forming a self-cycle.

Visually, the graph looks like the following:
"""


# Definition for a undirected graph node
class UndirectedGraphNode:

    def __init__(self, x):
        self.label = x
        self.neighbors = []


class Solution:
    # @param node, a undirected graph node
    # @return a undirected graph node

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

    def rewrite(self, node):
        """
        Using dfs + memoir
        1
        / \
                /   \
                0 --- 2
        / \
                \_/
        """

        if not node:
            return

        memoir = dict()

        def clone(n):
            # 先chk memoir :-)
            if n.label in memoir:
                return memoir[n.label]

            new_n = UndirectedGraphNode(n.label)

            # 再存入memoir
            memoir[n.label] = new_n  # cache first avoid loop!

            for nei in n.neighbors:
                if nei.label in memoir:
                    new_n.neighbors.append(memoir[nei.label])
                else:
                    new_n.neighbors.append(clone(nei))

            return new_n

        return clone(node)

    def rewrite2(self, node):
        """
        Using dfs + memoir
        """
        if not node:
            return

        memoir = dict()

    #  class UndirectedGraphNode:
        #  def __init__(self, x):
        #  self.label = x
        #  self.neighbors = []
        def clone(node):
            if node.label in memoir:
                return memoir[node.label]

            new_node = UndirectedGraphNode(node.label)

            # 先存入memoir 不然無限迴圈~
            memoir[new_node.label] = new_node

            if node.neighbors:
                for n in node.neighbors:
                    if n.label in memoir:
                        new_node.neighbors.append(memoir[n.label])
                    else:
                        new_node.neighbors.append(clone(n))

            return memoir[new_node.label]


        return clone(node)

    def rewrite3(self, node):
        """
        Using dfs + memoir
        """
        if not node:
            return

        dmap = {}

        def clone(n):
            if not n:
                return

            if n.label in dmap:
                return dmap[n.label]

    #  class UndirectedGraphNode:
        #  def __init__(self, x):
        #  self.label = x
        #  self.neighbors = []
            newN = UndirectedGraphNode(n.label)
            dmap[newN.label] = newN

            for nn in n.neighbors:
                if nn.label in dmap:
                    newN.neighbors.append(dmap[nn.label])
                else:
                    newN.neighbors.append(clone(nn))

            return newN

        return clone(node)

def build_node():
    node0 = UndirectedGraphNode(0)
    node1 = UndirectedGraphNode(1)
    node2 = UndirectedGraphNode(2)

    node0.neighbors.append(node1)
    node0.neighbors.append(node2)

    node1.neighbors.append(node2)

    node2.neighbors.append(node2)
    #  As an example, consider the serialized graph {0,1,2#1,2#2,2}.
    return node0


if __name__ == "__main__":
    node = build_node()

    s = Solution()
    result = s.cloneGraph(node)
    print(result.label)
    print(result.neighbors[0].label)
    print(result.neighbors[1].label)

    result = s.rewrite(node)
    print(result.label)
    print(result.neighbors[0].label)
    print(result.neighbors[1].label)

    result = s.rewrite2(node)
    print(result.label)
    print(result.neighbors[0].label)
    print(result.neighbors[1].label)

    result = s.rewrite3(node)
    print(result.label)
    print(result.neighbors[0].label)
    print(result.neighbors[1].label)
