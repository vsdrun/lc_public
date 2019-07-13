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
        if numCourses and not prerequisites:
            return True

        if not numCourses:
            return False

        # build graph
        dmap = dict()

        courses = set(i for i in range(numCourses))

        for p in prerequisites:
            if p[0] < 0 or p[1] < 0 or p[0] >= numCourses or p[1] >= numCourses:
                return False

            if not dmap.get(p[1]):
                dmap[p[1]] = []

            dmap[p[1]].append(p[0])

        # if circle, can't finish courses.
        # use visited to avoid duplicated visit.
        visited = set()

        def dfs(node, cir):
            """
            Use dfs to check circle.
            """
            if node in cir:
                return False

            if node in visited:
                return True

            visited.add(node)
            cir.add(node)

            for n in dmap.get(node, []):
                if not dfs(n, cir):
                    return False

            cir.remove(node)

            return True

        for n in courses:
            if n in dmap:
                cir = set()

                if not dfs(n, cir):
                    return False

        return True


def build():
    return 5, [[1, 0], [2, 0], [3, 0], [3, 1], [0, 1]]
    return 8, [[1, 0], [2, 6], [1, 7], [6, 4], [7, 0], [0, 5]]
    return 2, [[1, 0], [0, 1]]
    return 5, [[1, 0], [2, 0], [3, 0], [3, 1]]
    return 2, [[1, 0]]


if __name__ == "__main__":
    s = Solution()
    print(s.canFinish(*build()))
