#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/battleships-in-a-board/description/


Given an 2D board, count how many battleships are in it.
The battleships are represented with 'X's,
empty slots are represented with '.'s.
You may assume the following rules:

**You receive a valid board,
made of only battleships or empty slots.

Battleships can only be placed horizontally or vertically.
In other words, they can only be made of the shape 1xN (1 row, N columns)
or Nx1 (N rows, 1 column), where N can be of any size.

At least one horizontal or vertical cell separates between two battleships
- there are no adjacent battleships.

Example:
X..X
...X
...X
In the above board there are 2 battleships.

Invalid Example:
...X
XXXX
...X
This is an invalid board that you will not receive
- as battleships will always have a cell separating between them.

Follow up:
Could you do it in one-pass,
using only O(1) extra memory and without modifying the value of the board?

收到的是 valid board!
"""


class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        from __builtin__ import xrange

        # save tuple of location
        visited = set()
        ddir = ((1, 0), (-1, 0), (0, -1), (0, 1))

        def dfs(i, j):
            """
            :ret: Bool. False: out of boundary, visited.
            """
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or \
                    (i, j) in visited:
                return False

            if board[i][j] == 'X':
                visited.add((i, j))
                # 搞半天 map 只能 傳一個argument 給function....
                #  map(dfs, *[(i + x, j + y) for x, y in ddir])
                [dfs(i + x, j + y) for x, y in ddir]

        cnt = 0

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                if (i, j) in visited:
                    continue

                if board[i][j] == 'X':
                    dfs(i, j)
                    cnt += 1

        return cnt

    def rewrite(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
            X..X
            ...X
            ...X
        """
        # travel and mark
        direction = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(m, n):
            if m < 0 or m >= len(board[0]) or n < 0 or n >= len(board) or \
                    board[n][m] == '.':
                return False

            board[n][m] = '.'

            for d in direction:
                next_m = m + d[0]
                next_n = n + d[1]
                dfs(next_m, next_n)

            return True

        cnt = 0

        for m in range(len(board[0])):
            for n in range(len(board)):
                if dfs(m, n):
                    cnt += 1

        return cnt


def build():
    return [['X', '.', '.', 'X'],
            ['X', '.', '.', 'X'],
            ['.', 'X', '.', 'X']]


if __name__ == "__main__":
    s = Solution()
    print(s.countBattleships(build()))
    print(s.rewrite(build()))
