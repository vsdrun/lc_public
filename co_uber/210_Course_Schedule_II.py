#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/course-schedule-ii/description/

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites,
for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]
** Graph 問題, 有方向性. DAG
1. 先build up DAG graph
2. 再由DFS 造訪.

Given the total number of courses and a list of prerequisite pairs,
return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them.
If it is impossible to finish all courses, return an empty array.

For example:
2, [[1,0]]
There are a total of 2 courses to take.
To take course 1 you should have finished course 0.
So the correct course order is [0,1]

4, [[1,0],[2,0],[3,1],[3,2]]
There are a total of 4 courses to take.
To take course 3 you should have finished both courses 1 and 2.
Both courses 1 and 2 should be taken after you finished course 0.
So one correct course order is [0,1,2,3].
Another correct ordering is[0,2,1,3].

The input prerequisites is a graph represented by a list of edges,

not adjacency matrices.
Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.
"""


class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]

        toposort.
        if there's a loop, return []
        """
        if not prerequisites:
            return [i for i in xrange(numCourses)][::-1]

        import collections as cc

        # 以dict+list 架構出matrix graph
        matrix = cc.defaultdict(list)
        # 一定要有visited.
        visited = set()
        # 檢查是否有circle
        circle = []

        stack = []  # as result.

        # build graph, uni-dir
        for a, b in prerequisites:
            # b 要先take的course as head node.
            matrix[b].append(a)

        def run(s):
            # topo sort
            for n in matrix[s]:
                if n in circle:
                    return []
                if n not in visited:
                    visited.add(n)
                    circle.append(s)

                    if run(n) == []:
                        return []

                    circle.pop()

            stack.append(s)

        # 用 matrix.keys 而不用 for s in matrix因為...這樣python
        # 會哇哇叫說dict被modified...
        for s in matrix.keys():
            # 因為為graph 檢查是否visit 過
            if s not in visited:
                visited.add(s)
                # 檢查是否有circle, 非DAG.
                circle.append(s)

                if run(s) == []:
                    return []

                circle.pop()

        if len(stack) != numCourses:
            # 於build graph時做更好!!
            return \
                sorted(list(set([i for i in xrange(numCourses)]) - set(stack)),
                       reverse=True) + stack[::-1]
        else:
            return stack[::-1]

    def rewrite(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        toposort.
        if there's a loop, return []
        """
        from collections import defaultdict as dd
        n = numCourses
        p = prerequisites

        # build dmap
        dmap = dd(list)

        for nodes in p:
            dmap[nodes[0]].append(nodes[1])

        def dfs(node):
            # create toposort, check circle
            # ret: bool, True is ok, False means circle exists
            print("node: {}".format(node))
            if node in circle:
                return False

            if node in visited:
                return True

            circle.add(node)
            visited.add(node)

            for c in dmap[node]:
                if dfs(c) is False:
                    return False

            circle.remove(node)
            topo.append(node)
            print(topo)
            return True

        topo = []
        circle = set()
        visited = set()
        print("dmap: {}".format(dmap))

        for k in dmap.keys():
            if k not in visited:
                if dfs(k) is False:
                    return []

        leftCourse = list(set(i for i in range(n)) - set(topo))

        return topo + leftCourse

def build():
    return 3, [[1,0],[2,1]]
    return 2, [[0,1],[1,0]]
    return 4, [[1, 0], [2, 0], [3, 1], [3, 2]]
    return 3, [[1, 0]]
    return 2, []  # [1,0]
    return 1, []  # [0]
    return 2, [[0, 1], [1, 0]]  # []


if __name__ == "__main__":
    s = Solution()
    #  print(s.findOrder(*build()))
    print(s.rewrite(*build()))
