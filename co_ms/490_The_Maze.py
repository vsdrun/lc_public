#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/the-maze/description/


There is a ball in a maze with empty spaces and walls.
The ball can go through empty spaces by rolling up, down, left or right,
but it won't stop rolling until hitting a wall.
When the ball stops, it could choose the next direction.

Given the ball's start position, the destination and the maze,
determine whether the ball could stop at the destination.

The maze is represented by a binary 2D array.
1 means the wall and 0 means the empty space.
You may assume that the borders of the maze are all walls.
The start and destination coordinates are represented by
row and column indexes.

Example 1

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true
Explanation:
One possible way is : left -> down -> left -> down -> right -> down -> right.

Example 2

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false
Explanation: There is no way for the ball to stop at the destination.


DFS 條件:
    1. 往同方向走. 遇到 Wall, Stop, check 周遭 wall, 做DFS.
    2. 必須有 '2' 當作拜訪過得stop node, 不然會迴圈.
"""


class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """
        #  print("start: {}".format(start))

        direction = dict()
        direction[1] = (0, 1)
        direction[2] = (0, -1)
        direction[3] = (1, 0)
        direction[4] = (-1, 0)

        dirset = set([1, 2, 3, 4])

        opposite = dict()
        opposite[1] = 2
        opposite[2] = 1
        opposite[3] = 4
        opposite[4] = 3

        """
         4
        2 1
         3
        """

        def chk_env(node):
            env = {dr for dr, val in direction.iteritems()
                   if len(maze) <= node[0] + val[0] or node[0] + val[0] < 0 or
                   len(maze[0]) <= node[1] + val[1] or node[1] + val[1] < 0 or
                   maze[node[0] + val[0]][node[1] + val[1]] == 1}

            return env

        def dfs(node, frm):
            if node[0] < 0 or node[0] >= len(maze) or node[1] < 0 or \
                    node[1] >= len(maze[0]):
                return False

            # if it's wall or stopped before(i.e == 2) return.
            if maze[node[0]][node[1]] == 1 or \
                    maze[node[0]][node[1]] == 2:
                return False

            # 要檢查! 不是等於就好 還要看停不停的下來!!!
            #  if node[0] == destination[0] and node[1] == destination[1]:
            #  return True

            can_go = []

            # chk direction hits a wall  or out of bound.
            if node[0] + direction[frm][0] < 0 or \
               node[0] + direction[frm][0] >= len(maze) or \
               node[1] + direction[frm][1] < 0 or \
               node[1] + direction[frm][1] >= len(maze[0]) or \
               maze[node[0] + direction[frm][0]][node[1] + direction[frm][1]] \
                    == 1:
                # we hit the obstacle and the position we are in is the
                # destination.
                if node[0] == destination[0] and node[1] == destination[1]:
                    return True

                walls = chk_env(node)
                maze[node[0]][node[1]] = 2  # can stop.
                can_go.extend(list(dirset - walls - set([opposite[frm]])))
            else:
                # continue with previous direction.
                can_go.append(frm)

            for c in can_go:
                if dfs([node[0] + direction[c][0],
                        node[1] + direction[c][1]], c):
                    return True
            return False

        walls = chk_env(start)
        #  print("walls: {}".format(walls))

        for can_go in dirset - walls:
            if dfs([start[0] + direction[can_go][0],
                    start[1] + direction[can_go][1]], can_go):
                #  print("maze: {}".format(maze))
                return True

        return False

    def rewrite(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        """

        def travel(x, y, nx, ny):
            """
            advance position to next recursive call.
            return x, y as the previous position before hitting the
                wall/boundary
            """
            # boundary check, wall check
            if x < 0 or x >= len(maze) or y < 0 or y >= len(maze[0]) or \
                    maze[x][y] == 1:
                return False

            while x >= 0 and x < len(maze) and \
                    y >= 0 and y < len(maze[0]) and maze[x][y] != 1:
                x += nx
                y += ny

            return x - nx, y - ny

        visited = set()  # (x, y)

        drct_opposite = dict()
        drct_opposite[(1, 0)] = (-1, 0)
        drct_opposite[(-1, 0)] = (1, 0)
        drct_opposite[(0, 1)] = (0, -1)
        drct_opposite[(0, -1)] = (0, 1)

        bfs_stack = [(start[0], start[1], None)]  # (x, y, incoming_direction)

        while bfs_stack:
            x, y, direction = bfs_stack.pop(0)

            if (x, y) in visited:
                continue

            for nx, ny in drct_opposite.keys():
                if direction:
                    if (nx, ny) == drct_opposite[direction]:
                        continue

                sx, sy = travel(x, y, nx, ny)

                if sx == destination[0] and sy == destination[1]:
                    return True

                bfs_stack.append((sx, sy, (nx, ny)))

            visited.add((x, y))

        return False

    def rewrite2(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        BFS, faster
        """
        s = tuple(start)
        d = tuple(destination)

        visited = set()
        direction = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def march(node, direct):
            """
            :ret: last position, False
            """
            node = list(node)

            while 0 <= node[0] < len(maze) and 0 <= node[1] < len(maze[0]) and \
                    maze[node[0]][node[1]] != 1:
                node[0] += direct[0]
                node[1] += direct[1]

            return (node[0] - direct[0], node[1] - direct[1])


        nodes = [s]

        while nodes:
            NEXT = []

            for n in nodes:
                if n == d:
                    return True

                for dd in direction:
                    nextNode = march(n, dd)

                    if nextNode == n:
                        continue

                    if nextNode in visited:
                        continue

                    visited.add(nextNode)
                    NEXT.append(nextNode)

            nodes = NEXT

        return False

    def rewrite3(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        DFS, slower
        """
        s = tuple(start)
        d = tuple(destination)

        direction = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def march(node, direct):
            """
            :ret: last position, False
            """
            if not node:
                return False

            node = list(node)

            while 0 <= node[0] < len(maze) and 0 <= node[1] < len(maze[0]) and \
                    maze[node[0]][node[1]] != 1:
                node[0] += direct[0]
                node[1] += direct[1]

            return (node[0] - direct[0], node[1] - direct[1])

        def dfs(node):
            """
            :ret: True if hit, False if not
            """
            if node == d:
                return True

            if node in visited:
                return False

            visited.add(node)

            for dd in direction:
                nextNode= march(node, dd)

                if nextNode != node:
                    if dfs(nextNode):
                        return True

            return False

        visited = set()

        if dfs(s):
            return True

        return False



def build():
    return [ \
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [0, 1, 1, 1, 1],
        [0, 0, 0, 0, 0]
    ], [0, 4], [4, 4]

    return [[0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0],
            [0, 0, 0, 1, 0],
            [1, 1, 0, 1, 1],
            [0, 0, 0, 0, 0]], \
        [0, 4], \
        [3, 2]

    return [[0,0,1,0,0],
            [0,0,0,0,0],
            [0,0,0,1,0],
            [1,1,0,1,1],
            [0,0,0,0,0]], \
        [0,4], \
        [1,2]


if __name__ == "__main__":
    print(Solution().hasPath(*build()))
    print(Solution().rewrite(*build()))
    print(Solution().rewrite2(*build()))
    print(Solution().rewrite3(*build()))
