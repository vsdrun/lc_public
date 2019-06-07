#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/word-search/description/

Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once.

For example,
Given board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED", -> returns true,
word = "SEE", -> returns true,
word = "ABCB", -> returns false.
"""


class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        Given board =
        [
          ['A','B','C','E'],
          ['S','F','C','S'],
          ['A','D','E','E']
        ]
        word = "ABCCED", -> returns true,
        word = "SEE", -> returns true,
        word = "ABCB", -> returns false.
        """
        if len(board) * len(board[0]) < len(word):
            return False

        direct = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(i, j, idx):
            if idx == len(word) or \
                not 0 <= i < len(board) or not 0 <= j < len(board[0]) \
                or board[i][j] is None or board[i][j] != word[idx]:
                return False

            if idx == len(word) - 1:
                return True

            char = board[i][j]
            board[i][j] = None

            for x, y in direct:
                nx, ny = i + x, j + y
                if dfs(nx, ny, idx + 1):
                    return True

            board[i][j] = char

            return False


        for i in range(len(board)):
            for j in range(len(board[0])):
                if dfs(i, j, 0):
                    return True

        return False

def build():
    return [["A", "B", "C", "E"],
            ["S", "F", "E", "S"],
            ["A", "D", "E", "E"]], "ABCESEEEFSAA"
    return [['A', 'V']], "AV"
    return [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], "ABCED"
    return [], 'AB'


if __name__ == "__main__":
    s = Solution()
    print(s.exist(*build()))
