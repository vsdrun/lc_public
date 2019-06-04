#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/word-ladder-ii/

Given two words (beginWord and endWord), and a dictionary's word list,
find all shortest transformation sequence(s) from beginWord to endWord,
such that:

Only one letter can be changed at a time
Each transformed word must exist in the word list.

Note that beginWord is not a transformed word.
Note:

Return an empty list if there is no such transformation sequence.
All words have the same length.
All words contain only lowercase alphabetic characters.
You may assume no duplicates in the word list.
You may assume beginWord and endWord are non-empty and are not the same.

Example 1:
Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output:
[
  ["hit","hot","dot","dog","cog"],
  ["hit","hot","lot","log","cog"]
]

Example 2:
Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]
Output: []

Explanation:
The endWord "cog" is not in wordList, therefore no possible transformation.
"""

class Solution(object):
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """
        import collections

        wordList = set(wordList)
        res = []
        layer = {}
        layer[beginWord] = [[beginWord]]

        while layer:
            newlayer = collections.defaultdict(list)

            for w in layer:
                if w == endWord:
                    res.extend(k for k in layer[w])
                else:
                    for i in range(len(w)):
                        for c in 'abcdefghijklmnopqrstuvwxyz':
                            neww = w[:i]+c+w[i+1:]
                            if neww in wordList:
                                newlayer[neww]+=[j+[neww] for j in layer[w]]

            wordList -= set(newlayer.keys())
            layer = newlayer

        return res


    def rewrite(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        最小 path, 用BFS
        """

        # build dmap
        dmap = {}
        wordList = set(wordList)

        for w in wordList:
            for i in range(len(w)):
                if dmap.get(w[:i] + "_" + w[i + 1:], None) is None:
                    dmap[w[:i] + "_" + w[i + 1:]] = []

                dmap[w[:i] + "_" + w[i + 1:]].append(w)

        result = []
        rDmap = {beginWord:[[beginWord]]}

        while rDmap:
            nextDmap = {}

            for word in rDmap:
                if word == endWord:
                    for r in rDmap[word]:
                        result.append(r)
                    continue

                for i in range(len(word)):
                    thisWord = word[:i] + "_" + word[i+1:]

                    if thisWord in dmap:
                        for w in dmap[thisWord]:
                            if w not in wordList:
                                continue

                            if nextDmap.get(w, None) is None:
                                nextDmap[w] = []

                            for r in rDmap[word]:
                                nextDmap[w].append(r + [w])

            wordList -= set(nextDmap.keys())
            rDmap = nextDmap


        return result

def build():
    return "hit", "cog", ["hot", "dot", "dog", "lot", "log"]
    return "hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]


if __name__ == "__main__":
    s = Solution()
    print(s.findLadders(*build()))
    print(s.rewrite(*build()))
