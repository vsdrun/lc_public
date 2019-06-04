#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/the-maze-ii/description/


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

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: 12
Explanation:
One shortest way is : left -> down -> left -> down -> right -> down -> right.
The total distance is 1 + 1 + 3 + 1 + 2 + 2 + 2 = 12.

Example 2

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: -1
Explanation: There is no way for the ball to stop at the destination.


1. grow graph dynamically.

2. when hits wall, it's a node. (hit wall with same direction.)

3. if the node is a deadend, and it's not the destination,
    remove the node from graph.

4. Using BFS, act as multi-thread, one layer at a time.
    use heapq to start with the smallest (Djijaka algorithm)
"""


class Solution(object):
    def shortestDistance(self, maze, start, dest):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type dest: List[int]
        :rtype: int
        """
        import heapq as hq

        total_choices = set([1, 2, 3, 4])

        opposite = dict()
        opposite[1] = 3
        opposite[3] = 1
        opposite[2] = 4
        opposite[4] = 2

        # dkigita algorithm
        # use for make sure there's no loop.
        sptSet = set([(start[0], start[1])])

        dd = dict()
        dd[1], dd[2], dd[3], dd[4] = (-1, 0), (0, 1), (1, 0), (0, -1)

        def chk_choices(node):
            remain = set()

            for d in dd:
                if node[0] + dd[d][0] < 0 or \
                        node[0] + dd[d][0] >= len(maze) or \
                        node[1] + dd[d][1] < 0 or \
                        node[1] + dd[d][1] >= len(maze[0]) or \
                        maze[node[0] + dd[d][0]][node[1] + dd[d][1]] == 1 or \
                        (node[0] + dd[d][0], node[1] + dd[d][1]) in sptSet:
                    continue

                remain.add(d)

            return remain

        pqueue = [(0, (start[0], start[1]), chk_choices((start[0], start[1])))]

        # cnt that reach the destination
        fresult = set()

        def bfs(node, frm, cnt):
            cnt += 1

            # go to next node with same direction.
            next_n = (node[0] + dd[frm][0], node[1] + dd[frm][1])

            # if hit wall, make it a graph node.
            if next_n[0] < 0 or next_n[0] >= len(maze) or \
                    next_n[1] < 0 or next_n[1] >= len(maze[0]) or \
                    maze[next_n[0]][next_n[1]] == 1:

                sptSet.add(node)

                if node[0] == dest[0] and node[1] == dest[1]:
                    fresult.add(cnt)
                    return True

                # end node, mark as a graph node.
                t_choices = chk_choices(node) - set([opposite[frm]])

                if t_choices:
                    hq.heappush(pqueue, (cnt, node, t_choices))
            else:
                if next_n not in sptSet:
                    bfs(next_n, frm, cnt)

        while pqueue:
            cnt, node, choices = hq.heappop(pqueue)

            for c in choices:
                bfs((node[0] + dd[c][0], node[1] + dd[c][1]), c, cnt)

        return min(fresult) if fresult else -1


def build():
    return \
        [[0, 0, 0, 0, 1, 0, 0],
         [0, 0, 1, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 1],
         [0, 1, 0, 0, 0, 0, 0],
         [0, 0, 0, 0, 0, 0, 0]], [0, 0], [5, 6]

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

    matrix = [
        [0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 1, 0],
        [1, 1, 0, 1, 1],
        [0, 0, 0, 0, 0]
    ]
    return matrix, [0, 4], [4, 4]


if __name__ == "__main__":
    result = Solution().shortestDistance(*build())
    print(result)
