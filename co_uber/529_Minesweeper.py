#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/minesweeper/

Let's play the minesweeper game (Wikipedia, online game)!

You are given a 2D char matrix representing the game board.
'M' represents an unrevealed mine, 'E' represents an unrevealed empty square,
'B' represents a revealed blank square that has no adjacent
(above, below, left, right, and all 4 diagonals) mines,
digit ('1' to '8') represents how many mines are adjacent to this revealed square,
and finally 'X' represents a revealed mine.

Now given the next click position (row and column indices) among all the
unrevealed squares ('M' or 'E'),
return the board after revealing this position according to the following rules:

If a mine ('M') is revealed, then the game is over - change it to 'X'.
If an empty square ('E') with no adjacent mines is revealed,
then change it to revealed blank ('B') and all of its adjacent unrevealed
squares should be revealed recursively.

If an empty square ('E') with at least one adjacent mine is revealed,
then change it to a digit ('1' to '8') representing the number of adjacent mines.

Return the board when no more squares will be revealed.

Example 1:

Input:

[['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]

Click : [3,0]

Output:

[['B', '1', 'E', '1', 'B'],
 ['B', '1', 'M', '1', 'B'],
 ['B', '1', '1', '1', 'B'],
 ['B', 'B', 'B', 'B', 'B']]
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
            mine, change to number and stop (注意: stop 很重要)
        3. if mine, change to X and stop
        """
        # 直接命中
        if board[click[0]][click[1]] == 'M':
            board[click[0]][click[1]] = 'X'
            return board

        # 8 directions
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
            # stops if cnt != 0
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
