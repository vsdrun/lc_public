#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/bus-routes/

We have a list of bus routes.
Each routes[i] is a bus route that the i-th bus repeats forever.

For example if routes[0] = [1, 5, 7],
this means that the first bus (0-th indexed)
travels in the sequence 1->5->7->1->5->7->1->... forever.

We start at bus stop S (initially not on a bus),
and we want to go to bus stop T.
Travelling by buses only,
what is the least number of buses we must take to reach our destination?
Return -1 if it is not possible.

Example:
Input:
routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
Output: 2

Explanation:
The best strategy is take the first bus to the bus stop 7,
then take the second bus to the bus stop 6.

Note:
1 <= routes.length <= 500.
1 <= routes[i].length <= 500.
0 <= routes[i][j] < 10 ^ 6.
"""

class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        if S == T:
            return 0

        from collections import defaultdict as dd

        # build dmap
        stopDmap = dd(set)
        routeDmap = dd(set)

        for idx, rts in enumerate(routes):
            for r in rts:
                stopDmap[r].add(idx)
                routeDmap[idx].add(r)

        travel = set()
        visitedRoute = set()

        for r in stopDmap[S]:
            visitedRoute.add(r)
            for stop in routeDmap[r]:
                travel.add(stop)

        cnt = 0

        while travel:
            nextT = set()
            cnt += 1

            if T in travel:
                return cnt

            for t in travel:
                for r in stopDmap[t]:
                    if r in visitedRoute:
                        continue

                    visitedRoute.add(r)

                    for s in routeDmap[r]:
                        nextT.add(s)

            travel = nextT

        return -1

def build():
    return [[1,7],[3,5]], 5, 5
    return [[1, 2, 7], [3, 6, 7]], 1, 6
    return [
            [1,9,12,20,23,24,35,38],
            [10,21,24,31,32,34,37,38,43],
            [10,19,28,37],
            [8],
            [14,19],
            [11,17,23,31,41,43,44],
            [21,26,29,33],
            [5,11,33,41],
            [4,5,8,9,24,44]], 37, 28



if __name__ == "__main__":
    s = Solution()
    print(s.numBusesToDestination(*build()))
