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
        """
        from __builtin__ import xrange

        def dfs(ri, ci, word, count, board):
            if count == len(word):
                return True

            if len(board) - 1 < ri or ri < 0 or len(board[0]) - 1 < ci or \
                    ci < 0:
                return False

            if board[ri][ci] == word[count]:

                # act as visited.
                board[ri][ci] = None

                result = dfs(ri, ci + 1, word, count + 1, board) or \
                    dfs(ri, ci - 1, word, count + 1, board) or \
                    dfs(ri + 1, ci, word, count + 1, board) or \
                    dfs(ri - 1, ci, word, count + 1, board)

                board[ri][ci] = word[count]

                return result

            return False

        # go though each board node.
        for ri in xrange(len(board)):
            for ci in xrange(len(board[0])):
                if dfs(ri, ci, word, 0, board):
                    return True
        return False

    def rewrite(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        from __builtin__ import xrange

        ddir = ((1, 0), (-1, 0), (0, 1), (0, -1))

        def dfs(i, j, idx, visited):
            """
            ret: bool, True, found, False, nothing.
            """
            if (i, j) in visited or \
                    i < 0 or i >= len(board) or \
                    j < 0 or j >= len(board[0]):
                return False

            if board[i][j] == word[idx]:
                if idx == len(word) - 1:
                    return True

                visited.add((i, j))

                for d in ddir:
                    if dfs(i + d[0], j + d[1], idx + 1, visited):
                        return True

                visited.remove((i, j))

            return False

        for i in xrange(len(board)):
            for j in xrange(len(board[0])):
                visited = set()  # save tuple location

                if board[i][j] == word[0]:
                    if dfs(i, j, 0, visited):
                        return True

        return False


def build():
    return [], 'AB'
    return [
        ['A', 'B', 'C', 'E'],
        ['S', 'F', 'C', 'S'],
        ['A', 'D', 'E', 'E']
    ], "ABCED"
    return [['A', 'V']], "AV"
    return [["A", "B", "C", "E"],
            ["S", "F", "E", "S"],
            ["A", "D", "E", "E"]], "ABCESEEEFSAA"


if __name__ == "__main__":
    s = Solution()
    result = s.exist(*build())
    print(result)
    result = s.rewrite(*build())
    print(result)
