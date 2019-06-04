#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/the-maze-ii/description/

THIS iS A BFS Question!!!


There is a ball in a maze with empty spaces and walls.

The ball can go through empty spaces by rolling up, down, left or right,
but it won't stop rolling until hitting a wall.
When the ball stops, it could choose the next direction.

Given the ball's start position,
the destination and the maze,
**
find the shortest distance for the ball to stop at the destination.

The distance is defined by the number of empty spaces traveled by the
ball from the start position (excluded) to the destination (included).
If the ball cannot stop at the destination, return -1.

The maze is represented by a binary 2D array.
1 means the wall and 0 means the empty space.

You may assume that the borders of the maze are all walls.

The start and destination coordinates are represented by
row and column indexes.


Example 1
Input 1: a maze represented by a 2D array

0 0 1 0 S
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 D

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12
Explanation:
One shortest way is : left -> down -> left -> down -> right -> down -> right.
The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.


Example 2

Input 1: a maze represented by a 2D array

0 0 1 0 S
0 0 0 0 0
0 0 0 1 0
1 1 D 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1
Explanation: There is no way for the ball to stop at the destination.


! Forget about direction issue... It's not worth the complexity...
Just move forward and if the traverse distance is larger in the queue,
ignore it !
"""


class Solution(object):
    def shortestDistance(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type dest: List[int]
        :rtype: int
        """
        import heapq

        dest = tuple(destination)
        tm = len(maze)
        tn = len(maze[0])

        def go(start, direction):
            # return the stop position and length
            m, n = start
            dm, dn = direction
            step = 0

            while 0 <= m + dm < tm and 0 <= n + dn < tn and \
                    maze[m + dm][n + dn] != 1:
                m += dm
                n += dn
                step += 1

            return step, (m, n)

        # bfs (dijkstra: https://en.wikipedia.org/wiki/Dijkstra's_algorithm)
        visited = {}

        q = []
        heapq.heappush(q, (0, tuple(start)))

        while q:
            length, cur = heapq.heappop(q)

            if cur in visited and visited[cur] <= length:
                # if cur is visited and with a shorter length, skip it.
                continue

            visited[cur] = length

            if cur == dest:
                return length  # 確保是最小的~~~

            for direction in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
                s, np = go(cur, direction)
                heapq.heappush(q, (length + s, np))

        return -1

    def rewrite(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type dest: List[int]
        :rtype: int
        0 0 1 0 S
        0 0 0 0 0
        0 0 0 1 0
        1 1 0 1 1
        0 0 0 0 D
        """
        import heapq

        dest = destination

        direct = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def bfs(location, d):
            """
            ret: location, steps
            """
            steps = 0
            loc = location[:]

            while len(maze ) > loc[0] + d[0] >= 0 and \
                len(maze[0]) > loc[1] + d[1] >= 0 and \
                maze[loc[0] + d[0]][loc[1] + d[1]] != 1:
                steps += 1
                loc[0] = loc[0] + d[0]
                loc[1] = loc[1] + d[1]

            return loc, steps


        q = []
        heapq.heappush(q, (0, start))
        visited = {}  # key: position, value: length
        visited[tuple(start)] = 0

        while q:
            length, location = heapq.heappop(q)

            # do we need to test visited[tuple(location)] < length?
            # since we are using BFS
            if tuple(location) in visited and visited[tuple(location)] < length:
                continue

            visited[tuple(location)] = length

            if location == dest:
                return length

            for d in direct:
                loc, leng = bfs(location, d)
                if leng != 0:
                    heapq.heappush(q, (leng + length, loc))

        return -1

    def rewrite2(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type dest: List[int]
        :rtype: int
        當看到最短路徑，思考BFS
        0 0 1 0 S
        0 0 0 0 0
        0 0 0 1 0
        1 1 0 1 1
        0 0 0 0 D
        """
        import heapq as hq

        if not maze or start == destination:
            return 0

        visited = set()

        def bfs(position, d):
            """
            :ret: length, last position
            """
            m, n = position[0], position[1]
            cnt = -1

            while Mlen > m >= 0 and Nlen > n >= 0 and \
                    maze[m][n] != 1:
                m += d[0]
                n += d[1]
                cnt += 1

            return cnt, (m - d[0], n - d[1])

        direct = ((0, 1), (0, -1), (1, 0), (-1, 0))

        Mlen = len(maze)
        Nlen = len(maze[0])

        ss = tuple(start)
        dd = tuple(destination)

        # lets use heapq/PriorityQueue to get the smallest distance
        result = []
        hq.heappush(result, (0, ss))

        while result:
            length, position = hq.heappop(result)

            if position == dd:
                return length
            # i can't use -VAL to determine if the position has been visited
            # due to what about the start position, what's the value of that
            # position? 0? if it's 0, then I can't determine it's been visited
            # at first place!
            if position in visited and \
            abs(maze[position[0]][position[1]]) <= length:
                continue

            visited.add(position)

            for d in direct:
                nlength, nposition = bfs(position, d)

                if nlength != 0:
                    maze[nposition[0]][nposition[1]] = -nlength
                    hq.heappush(result, (nlength + length , nposition))

        return 0


def build():
    return \
        [[0, 0, 0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]], [0, 0], [5, 6]

    matrix = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    return matrix, [0, 4], [4, 4]


    return \
        [[0, 0, 0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 1, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 1, 0, 0, 0, 1],
         [0, 0, 0, 0, 1, 0, 0]], [0, 0], [8, 6]

    return [[0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0]], \
        [1, 1], \
        [1, 2]

#
#  [[0, 0, 0, 0, 1, 0, 0],
#   [0, 0, 1, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 1],
#   [0, 1, 0, 0, 0, 0, 0],
#   [0, 0, 0, 0, 0, 0, 0]], [0, 0], [5, 6]

#  [[-2, 0, 0, -5, 1, -5, -1],
 #  [0, 0, 1, 0, 0, 0, 0]
 #  [-6, 0, -3, 0, 0, 0, -2]
 #  [0, 0, 0, 0, 0, 0, 1]
 #  [0, 1, -4, 0, 0, 0,-4]
 #  [-5, 0, -3, -5, 0, -5, -1]]


if __name__ == "__main__":
    print(Solution().shortestDistance(*build()))
    print(Solution().rewrite(*build()))
    print(Solution().rewrite2(*build()))
