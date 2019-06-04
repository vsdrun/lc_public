#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/redundant-connection-ii/description/

In this problem,
a rooted tree is a directed graph such that, there is exactly one node
(the root) for which all other nodes are descendants of this node,
plus every node has exactly one parent,
except for the root node which has no parents.

The given input is a directed graph that started as a rooted tree
with N nodes (with distinct values 1, 2, ..., N),
with one additional directed edge added.

The added edge has two different vertices chosen from 1 to N,
and was not an edge that already existed.

The resulting graph is given as a 2D-array of edges.
Each element of edges is a pair [u, v] that represents a directed edge
connecting nodes u and v, where u is a parent of child v.

**
Return an edge that can be removed so that the resulting graph is a
rooted tree of N nodes.

一個node只能有一個parent.

**
If there are multiple answers,
return the answer that occurs last in the given 2D-array.

Example 1:
Input: [[1,2], [1,3], [2,3]]
Output: [2,3]
Explanation: The given directed graph will be like this:
  1
 / \
v   v
2-->3


Example 2:
Input: [[1,2], [2,3], [3,4], [4,1], [1,5]]
Output: [4,1]
Explanation: The given directed graph will be like this:
5 <- 1 -> 2
     ^    |
     |    v
     4 <- 3


The size of the input 2D-array will be between 3 and 1000.
Every integer represented in the 2D-array will be between 1 and N,
where N is the size of the input array.

https://leetcode.com/problems/redundant-connection-ii/discuss/108070/Python-O(N)-concise-solution-with-detailed-explanation-passed-updated-testcases


情況:
1. node has > 1 parents.
2. node form a circle.
3. node has > 1 parents and form a circle.
"""


class Solution(object):
    def findRedundantDirectedConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        #  1. node has > 1 parents.
        #  2. node form a circle.
        #  3. node has > 1 parents and form a circle.
        from collections import defaultdict as dd

        ufDmap = dict()
        dmap = dd(list)
        circle = set()
        # parent node record
        plist = [False for _ in range(len(edges) + 1)]

        def find(x):
            if not ufDmap.get(x, None):
                return x

            return find(ufDmap[x])

        def uf(e):

            x, y = find(e[0]), find(e[1])

            if x == y:
                return True

            ufDmap[x] = y

        def findCircle(node):
            """
            ret: (x, y) if circle edge, else (),
            """
            circle.add(node)

            for nextNode in dmap[node]:
                if nextNode in circle:
                    return [node, nextNode]

                ret = findCircle(nextNode)

                if ret:
                    return ret

            return []

        # more then 1 parent
        moreParentEdge = [None]
        lastCircleEdge = [None]

        for e in edges:
            # 注意! 須跑完所有edges, 不能提早 return, 因為 multiple parent
            # 可能在loop發生之後才加入.

            # Build graph
            dmap[e[0]].append(e[1])

            # 紀錄 lastest parents
            if plist[e[1]]:
                moreParentEdge[0] = e
            else:
                plist[e[1]] = True

            if uf(e):
                # 紀錄最後一個導致circle的edge
                lastCircleEdge[0] = e

        if not moreParentEdge[0]:
            #  滿足條件 2. node form a circle.
            return lastCircleEdge[0]

        if moreParentEdge[0]:
            #  滿足條件 1. node has > 1 parents.
            #           3. node has > 1 parents and form a circle.
            headNode = moreParentEdge[0][1]
            ret = findCircle(headNode)

            if ret:
                return ret
            else:
                return moreParentEdge[0]

        return []


def build():
    return [[2, 1], [3, 1], [4, 2], [1, 4]]  # [2,1]
    return [[1, 2], [2, 3], [3, 4], [4, 1], [1, 5]]  # [4,1]
    return [[1, 2], [1, 3], [2, 3]]  # [2, 3]


if __name__ == "__main__":
    s = Solution()
    print(s.findRedundantDirectedConnection(build()))
    #  print(s.rewrite(build()))
