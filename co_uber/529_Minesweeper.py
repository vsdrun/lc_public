#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/minesweeper/
"""

class Solution(object):
    def updateBoard(self, board, click):
        """
        :type board: List[List[str]]
        :type click: List[int]
        :rtype: List[List[str]]
        dfs
        1. if 1~8, show 1~8 and stop.
        2. if E, go all direction if state is E and change to B, if B has
            mine, change to number and stop
        3. if mine, change to X and stop
        """

        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        checkd = ((1, 0), (-1, 0), (0, -1), (0, 1), (1, 1), (-1, -1), (1, -1),
                (-1, 1))

        def check(i, j):
            cnt = 0

            for d in checkd:
                x, y = i + d[0], j + d[1]
                if 0 <= x < len(board) and 0 <= y < len(board[0]):
                    if board[x][y] == 'M':
                        cnt += 1

            return cnt

        def dfs(i, j):
            if not 0 <= i < len(board) or not 0 <= j < len(board[0]):
                return

            if board[i][j] == 'M' or board[i][j] == 'B':
                return

            cnt = check(i, j)
            if cnt != 0:
                board[i][j] = str(cnt)
                return

            board[i][j] = 'B'

            for d in checkd:
                x, y = i + d[0], j + d[1]
                dfs(x, y)


        dfs(click[0], click[1])
        return board


def build():
    return [["E","E","E","E","E","E","E","E"],
            ["E","E","E","E","E","E","E","M"],
            ["E","E","M","E","E","E","E","E"],
            ["M","E","E","E","E","E","E","E"],
            ["E","E","E","E","E","E","E","E"],
            ["E","E","E","E","E","E","E","E"],
            ["E","E","E","E","E","E","E","E"],
            ["E","E","M","M","E","E","E","E"]], [0,0]
    """
    ["B","B","B","B","B","B","1","E"],
    ["B","1","1","1","B","B","1","M"],
    ["1","2","M","1","B","B","1","1"],
    ["M","2","1","1","B","B","B","B"],
    ["1","1","B","B","B","B","B","B"],
    ["B","B","B","B","B","B","B","B"],
    ["B","1","2","2","1","B","B","B"],
    ["B","1","M","M","1","B","B","B"]]
    """

    return [['E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'M', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E'],
            ['E', 'E', 'E', 'E', 'E']], [3,0]
    """
    ['B', '1', 'E', '1', 'B']
    ['B', '1', 'M', '1', 'B']
    ['B', '1', '1', '1', 'B']
    ['B', 'B', 'B', 'B', 'B']

    [['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
    """

    return [['B', '1', 'E', '1', 'B'],
            ['B', '1', 'M', '1', 'B'],
            ['B', '1', '1', '1', 'B'],
            ['B', 'B', 'B', 'B', 'B']], [1, 2]

    """
    [['B', '1', 'E', '1', 'B'],
     ['B', '1', 'X', '1', 'B'],
     ['B', '1', '1', '1', 'B'],
     ['B', 'B', 'B', 'B', 'B']]
    """

def pp(board):
    for b in board:
        print(b)

if __name__ == "__main__":
    s = Solution()
    pp(s.updateBoard(*build()))
