#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/walls-and-gates/description/


You are given a (m x n) 2D grid initialized with these three possible values.
-1      - A wall or an obstacle.
0       - A gate.
INF     - Infinity means an empty room.


We use the value 231 - 1 = 2147483647 to represent INF as you may assume
that the distance to a gate is less than 2147483647.


Fill each empty room with the distance to its nearest gate.
If it is impossible to reach a gate, it should be filled with INF.


For example, given the 2D grid:
INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF


After running your function, the 2D grid should be:
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4


BFS! 反向思考!!! 由gate開始長path!!!

只要找最近的 就思考 BFS!!
類似 Maze
與pafici/atlantic ocean 不一樣!
ocean 為 由兩側走DFS
這是走BFS.

"""


class Solution(object):
    def wallsAndGates(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        empty = 2147483647
        steps = ((0, 1), (0, -1), (1, 0), (-1, 0))

        # 先將gate的座標找出
        gate = [
            (ri, ci)
            for ri, r in enumerate(rooms)
            for ci, c in enumerate(r)
            if c == 0]

        # 一次向外擴張一個node 不是 DFS 無須擔心無限迴圈~
        # 並且確保最小.
        # python 裡 gate.append 可以用於for loop...
        for ri, ci in gate:
            for sr, sc in steps:
                if 0 <= ri + sr < len(rooms) and \
                   0 <= ci + sc < len(rooms[0]) and \
                   rooms[ri + sr][ci + sc] == empty:
                    # assign empty gates' value.
                    rooms[ri + sr][ci + sc] = rooms[ri][ci] + 1
                    gate.append((ri + sr, ci + sc))  # 重要! BFS, gate.append.

    def rewrite(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        from __builtin__ import xrange

        empty = 2147483647

        steps = ((0, 1), (0, -1), (1, 0), (-1, 0))

        gates = [(i, j) for i in xrange(len(rooms))
                 for j in xrange(len(rooms[0]))
                 if rooms[i][j] == 0]

        while gates:
            tmp_gates = []

            for g in gates:
                for d in steps:
                    n = (g[0] + d[0], g[1] + d[1])

                    if 0 <= n[0] < len(rooms) and \
                            0 <= n[1] < len(rooms[0]) and \
                            rooms[n[0]][n[1]] == empty:
                        rooms[n[0]][n[1]] = rooms[g[0]][g[1]] + 1
                        tmp_gates.append(n)

            gates = tmp_gates

    def rewrite_2(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: void Do not return anything, modify rooms in-place instead.
        """
        from __builtin__ import xrange

        # find gate position.
        gates = [(i, j) for i in xrange(len(rooms))
                 for j in xrange(len(rooms[0]))
                 if rooms[i][j] == 0]

        empty = 2147483647

        ddir = ((1, 0), (-1, 0), (0, 1), (0, -1))

        while gates:
            tmp_gates = []

            for g in gates:
                for d in ddir:
                    nxt = (g[0] + d[0], g[1] + d[1])
                    if 0 <= nxt[0] < len(rooms) and 0 <= nxt[1] < len(rooms[0]) \
                            and rooms[nxt[0]][nxt[1]] == empty:
                        rooms[nxt[0]][nxt[1]] = rooms[g[0]][g[1]] + 1
                        tmp_gates.append(nxt)

            gates = tmp_gates


def build():
    return [[2147483647, -1, 0, 2147483647],
            [2147483647, 2147483647, 2147483647, -1],
            [2147483647, -1, 2147483647, -1],
            [0, -1, 2147483647, 2147483647]]
    #  return [[2147483647, -1, 0, 2147483647],
    #  [2147483647, 2147483647, 2147483647, -1],
    #  [2147483647, -1, 2147483647, -1],
    #  [0, -1, 2147483647, 2147483647]]


if __name__ == "__main__":
    rooms = build()
    s = Solution()
    s.wallsAndGates(rooms)
    print(rooms)

    rooms = build()
    s.rewrite(rooms)
    print(rooms)

    rooms = build()
    s.rewrite_2(rooms)
    print(rooms)
