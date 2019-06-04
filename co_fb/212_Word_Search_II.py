#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/word-search-ii/description/

Given a 2D board and a list of words from the dictionary,
find all words in the board.

Each word must be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.
The same letter cell may not be used more than once in a word.

For example,
Given words = ["oath","pea","eat","rain"] and board =

[
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]

Return ["eat","oath"].

Note:
You may assume that all inputs are consist of lowercase letters a-z.
"""


class TrieNode(object):
    def __init__(self):
        self.word = None
        self.children = {}


class Trie(object):
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        root = self.root

        for char in word:
            # if key exist, return key's value, otherwise return newly inserted
            # key 'char''s default value: TrieNode instance.
            root = root.children.setdefault(char, TrieNode())

        # 最後一個char node 存整個到此的word
        root.word = word


class Solution(object):
    def search(self, i, j, root, board, m, n, r):
        """
        DFS
        Given words = ["oath","pea","eat","rain"] and board =
        [
          ['o','a','a','n'],
          ['e','t','a','e'],
          ['i','h','k','r'],
          ['i','f','l','v']
        ]
        """
        # 備份
        char = board[i][j]

        if not (char and char in root.children):
            return

        # since DFS, visited is a must!
        # assign board[i][j] to None as a STOP!
        board[i][j] = None

        root = root.children[char]

        if root.word:
            r.append(root.word)

            # 不要重複找到字!!
            root.word = None

        for x, y in ((0, -1), (-1, 0), (0, 1), (1, 0)):
            ii, jj = i + x, j + y
            if 0 <= ii < m and 0 <= jj < n:
                self.search(ii, jj, root, board, m, n, r)

        # 回存備份
        board[i][j] = char

    def findWords(self, board, words):
        if not board:
            return []

        tree = Trie()

        # build Trie
        [tree.insert(word) for word in words]

        m, n, = len(board), len(board[0])
        result = []

        for i, row in enumerate(board):
            for j, char in enumerate(row):
                self.search(i, j, tree.root, board, m, n, result)

        return result

class Solution_2(object):
    def findWords(self, board, words):
        """
        DFS
        Given words = ["oath","pea","eat","rain"] and board =
        [
          ['o','a','a','n'],
          ['e','t','a','e'],
          ['i','h','k','r'],
          ['i','f','l','v']
        ]

        注意corner case:
        aaa, aaab  最後一個char 有 None 與 b
        """
        direct = ((0, 1), (0, -1), (1, 0), (-1, 0))
        result = set()
        root = dict()

        # 建構 trie
        for w in words:
            ow = w
            r = root

            while w:
                if w[0] not in r:
                    r[w[0]] = dict()

                r = r[w[0]]
                w = w[1:]

            r[None] = ow  # smart design. 最後存字.



        def search(i, j, root):
            # handle corner case: aaa, aaab
            if None in root:
                result.add(root[None])  # smart design, 回存字.

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]) or \
                    board[i][j] is None:
                return

            char = board[i][j]
            board[i][j] = None

            for c in root:
                if char == c:
                    for x, y in direct:
                        search(i + x, j + y, root[c])

            board[i][j] = char

        for i in range(len(board)):
            for j in range(len(board[0])):
                search(i, j, root)

        return list(result)


def build_input():
    board = [['o', 'a', 'a', 'n'],
             ['e', 't', 'a', 'e'],
             ['i', 'h', 'k', 'r'],
             ['i', 'f', 'l', 'v']]

    board = [['a']]
    words = ["a"]
    #  words = ["oath"]
    #  words = ["pea"]
    #  words = ["oath", "pea", "eat", "rain"]
    return board, words


if __name__ == "__main__":
    b, w = build_input()

    s = Solution()
    print(s.findWords(b, w))

    s = Solution_2()
    print(s.findWords(b, w))
