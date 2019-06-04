#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/word-ladder/description/

Given two words (beginWord and endWord),
and a dictionary's word list,
find the length of shortest transformation sequence from beginWord to endWord,
such that:

Only one letter can be changed at a time.
Each transformed word must exist in the word list.
Note that beginWord is not a transformed word.

For example,

Given:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.


Return 0 if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.
"""


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        from collections import defaultdict as dd

        dmap = dd(list)

        for w in wordList:
            for idx in range(len(w)):
                key = w[:idx] + "_" + w[idx+1:]
                dmap[key].append(w)

        visited = set()

        # BFS
        words = [beginWord]
        cnt = 1

        while words:
            tmp = []
            cnt += 1

            for w in words:
                for idx in range(len(w)):
                    for nextw in dmap[w[:idx] + "_" + w[idx+1:]]:
                        if nextw in visited:
                            continue
                        if nextw == endWord:
                            return cnt

                        visited.add(nextw)
                        tmp.append(nextw)

            words = tmp

        return 0

def build():
    return "hit", "cog", ["hot", "dot", "dog", "lot", "log"]
    return "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]
    return "hit", "cog", ["hot","dot","dog","lot","log"]


if __name__ == "__main__":
    s = Solution()
    print(s.ladderLength(*build()))
