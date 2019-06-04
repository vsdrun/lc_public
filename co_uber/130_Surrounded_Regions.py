#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/surrounded-regions/

Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
A region is captured by flipping all 'O's into 'X's in that surrounded region.

Example:
X X X X
X O O X
X X O X
X O X X
After running your function, the board should be:

X X X X
X X X X
X X X X
X O X X

Explanation:
Surrounded regions shouldn’t be on the border, which means that any 'O'
on the border of the board are not flipped to 'X'.
Any 'O' that is not on the border and it is not connected to an 'O' on
the border will be flipped to 'X'. Two cells are connected if
they are adjacent cells connected horizontally or vertically.
"""

class Solution(object):
    def solve(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        direct = ((1, 0), (-1, 0), (0, -1), (0, 1))

        def dfs(i, j):
            bad.add((i, j))

            for d in direct:
                x, y = i + d[0], j + d[1]

                if 0 <= x < len(board) and 0 <= y < len(board[0]) and \
                    (x, y) not in bad and board[x][y] == 'O':
                    dfs(x, y)

        bad = set()

        for i in range(len(board)):
            if i == 0 or i == len(board) - 1:
                for j in range(len(board[0])):
                    if board[i][j] == 'O':
                        dfs(i, j)
            else:
                for j in (0, len(board[0]) - 1):
                    if board[i][j] == 'O':
                        dfs(i, j)

        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == 'O' and (i, j) not in bad:
                    board[i][j] = 'X'

        return board

def build():
    return [["O","X","X","O","X"],
            ["X","O","O","X","O"],
            ["X","O","X","O","X"],
            ["O","X","O","O","O"],
            ["X","X","O","X","O"]]
    """
    ['O', 'X', 'X', 'O', 'X']
['X', 'X', 'X', 'X', 'O']
['X', 'X', 'X', 'O', 'X']
['O', 'X', 'O', 'O', 'O']
['X', 'X', 'O', 'X', 'O']
    """
    return [["X","O","X"],
            ["X","O","X"],
            ["X","O","X"]]
    """
    [["X","O","X"],
     ["X","O","X"],
     ["X","X","X"]]
    """
    return [['X', 'X', 'X', 'X'],
            ['X', 'O', 'O', 'X'],
            ['X', 'X', 'O', 'X'],
            ['X', 'O', 'X', 'X']]
    return [["O","O","O","O","X","X"],
            ["O","O","O","O","O","O"],
            ["O","X","O","X","O","O"],
            ["O","X","O","O","X","O"],
            ["O","X","O","X","O","O"],
            ["O","X","O","O","O","O"]]
    """
    ['O', 'O', 'O', 'O', 'X', 'X']
    ['O', 'O', 'O', 'O', 'O', 'O']
    ['O', 'X', 'O', 'X', 'X', 'O']
    ['O', 'X', 'O', 'O', 'X', 'O']
    ['O', 'X', 'O', 'X', 'O', 'O']
    ['O', 'X', 'O', 'O', 'O', 'X']
    """


def pp(board):
    for b in board:
        print(b)

if __name__ == "__main__":
    s = Solution()
    pp(s.solve(build()))
