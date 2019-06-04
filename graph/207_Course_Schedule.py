#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/course-schedule/description/

There are a total of n courses you have to take, labeled from 0 to n - 1.

Some courses may have prerequisites,
for example to take course 0 you have to first take course 1,
which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs,
is it possible for you to finish all courses?

For example:
2, [[1,0]]
There are a total of 2 courses to take.
To take course 1 you should have finished course 0. So it is possible.

2, [[1,0],[0,1]]
There are a total of 2 courses to take.
To take course 1 you should have finished course 0,
and to take course 0 you should also have finished course 1.
So it is impossible.

Note:
The input prerequisites is a graph represented by a list of edges,
not adjacency matrices. Read more about how a graph is represented.

You may assume that there are no duplicate edges in the input prerequisites.
"""


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict

        if not prerequisites:
            return True

        graph = defaultdict(list)

        # build graph
        for child, node in prerequisites:
            graph[node].append(child)

        # print("graph: {}".format(graph))

        # 避免time exceed 因為走訪過得不必再走訪一遍!
        visited = []
        circle = []

        def traverse(node):
            # DFS

            # there is a circle...
            if node in circle:
                return []

            if node not in visited:
                visited.append(node)
                circle.append(node)

                for child in graph[node]:
                    if traverse(child) == []:
                        return []

                circle.pop()

        for node in graph.keys():
            # 避免time exceed 因為走訪過得不必再走訪一遍!
            if node not in visited:
                visited.append(node)
                circle.append(node)

                for child in graph[node]:
                    if traverse(child) == []:
                        return False

                circle.pop()

        return True

    def rewrite(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # check input
        if not numCourses:
            return False
        if not prerequisites:
            return True

        prep = prerequisites

        # build graph
        from collections import defaultdict as dd
        dmap = dd(list)

        for p in prep:
            dmap[p[1]].append(p[0])

        def dfs(node, circle):
            if node in circle:
                return False

            if node not in visited:
                visited.add(node)
                circle.add(node)

                for n in dmap[node]:
                    if not dfs(n, circle):
                        return False

                circle.remove(node)

            return True

        # check graph
        visited = set()

        for n in dmap.keys():

            if n not in visited:
                visited.add(n)
                circle = set()
                circle.add(n)

                for c in dmap[n]:
                    if not dfs(c, circle):
                        return False
        return True

    def rewrite2(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        nc = numCourses
        prep = prerequisites

        if not nc:
            return False
        if not prep:
            return True

        # build graph
        from collections import defaultdict as dd

        dmap = dd(list)

        for p in prep:
            dmap[p[1]].append(p[0])

        # traverse graph
        def dfs(node, circle):
            # 條件:
            # True: if visited, no child
            # False: if circle

            if node in dmap:
                visited.add(node)
                circle.add(node)

                for cn in dmap[node]:
                    if cn in circle:
                        return False
                    elif cn in visited:
                        continue
                    elif not dfs(cn, circle):
                        return False

                circle.remove(node)

            return True

        visited = set()

        for n in dmap.keys():

            if n not in visited:
                visited.add(n)

                for cn in dmap[n]:
                    # 需要有circle, 不然無法區分 此node下多個child是曾經造訪
                    # 或者是迴圈.
                    circle = set([n])

                    if cn not in visited:
                        if not dfs(cn, circle):
                            return False

        return True


def build():
    return 5, [[1, 0], [2, 0], [3, 0], [3, 1]]
    return 5, [[1, 0], [2, 0], [3, 0], [3, 1], [0, 1]]
    return 8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]
    return 2, [[1, 0], [0, 1]]
    return 2, [[1, 0]]


if __name__ == "__main__":
    s = Solution()
    print(s.canFinish(*build()))
    print(s.rewrite(*build()))
    print(s.rewrite2(*build()))
