#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/game-of-life/description/

Given a board with m by n cells,
each cell has an initial state live (1) or dead (0).

Each cell interacts with its eight neighbors (horizontal, vertical, diagonal)
using the following four rules (taken from the above Wikipedia article):


(<2)Any live cell with fewer than two live neighbors dies,
    as if caused by under-population.

(2-3)Any live cell with two or three live neighbors lives
    on to the next generation.

(>3)Any live cell with more than three live neighbors dies,
    as if by over-population..

(=3)Any dead cell with exactly three live neighbors becomes a live cell,
    as if by reproduction.

Write a function to compute the next state (after one update)
of the board given its current state.

Follow up:
1. Could you solve it in-place? Remember that the board needs to be updated
at the same time: You cannot update some cells first and then use their
updated values to update other cells.

2. In this question, we represent the board using a 2D array. In principle, the
board is infinite, which would cause problems when the active area encroaches
the border of the array. How would you address these problems?
"""


class Solution(object):

    def gameOfLife(self, board):
        """
        :type board: List[List[int]]
        :rtype: void Do not return anything, modify board in-place instead.
        要有 0 -> 2 , 1 -> 3 state轉換的概念
        我們只在乎轉換前的state, 只count轉換前的state.
        """
        m, n = len(board), len(board[0])

        for i in range(m):
            for j in range(n):
                # 0: 初始死 2: 人造活 3: 人造死
                if board[i][j] == 0 or board[i][j] == 2:
                    if self.nnb(board, i, j) == 3:
                        board[i][j] = 2  # 2 為 活
                # 1: 初始活 3: 人造死
                else:  # 初始為活 轉換前為活
                    if self.nnb(board, i, j) < 2 or self.nnb(board, i, j) > 3:
                        board[i][j] = 3  # 3 人造死

        for i in range(m):
            for j in range(n):
                # 將我們人造的state 改成初始0, 1
                if board[i][j] == 2:
                    board[i][j] = 1
                if board[i][j] == 3:
                    board[i][j] = 0

    def nnb(self, board, i, j):
        m, n = len(board), len(board[0])
        count = 0

        if i - 1 >= 0 and j - 1 >= 0:
            count += board[i - 1][j - 1] % 2
        if i - 1 >= 0:
            count += board[i - 1][j] % 2
        if i - 1 >= 0 and j + 1 < n:
            count += board[i - 1][j + 1] % 2
        if j - 1 >= 0:
            count += board[i][j - 1] % 2
        if j + 1 < n:
            count += board[i][j + 1] % 2
        if i + 1 < m and j - 1 >= 0:
            count += board[i + 1][j - 1] % 2
        if i + 1 < m:
            count += board[i + 1][j] % 2
        if i + 1 < m and j + 1 < n:
            count += board[i + 1][j + 1] % 2
        return count


def build():
    return [0, 1, 2, 4, 5, 7]


if __name__ == "__main__":
    nums = build()

    s = Solution()
    result = s.summaryRanges(nums)

    print(result)
