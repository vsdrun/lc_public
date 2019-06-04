#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/sentence-similarity-ii/description/

Given two sentences words1, words2
(each represented as an array of strings),
and a list of similar word pairs pairs, determine if two sentences are similar.

For example,
words1 = ["great", "acting", "skills"] and
words2 = ["fine", "drama", "talent"] are similar,

if the similar word pairs are pairs =
[["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

Note that the similarity relation is transitive.
For example, if "great" and "good" are similar,
and "fine" and "good" are similar, then "great" and "fine" are similar.

Similarity is also symmetric.
For example,
"great" and "fine" being similar is the same as
"fine" and "great" being similar.

Also, a word is always similar with itself.
For example, the sentences words1 = ["great"], words2 = ["great"],
pairs = [] are similar,
even though there are no specified similar word pairs.

Finally,
sentences can only be similar if they have the same number of words.
So a sentence like
words1 = ["great"] can never be similar to
words2 = ["doubleplus","good"].
"""


class Solution(object):
    def areSentencesSimilarTwo(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        1. check length equality.
        2. w1[0] == w2[0]
        3. graph search.

        union find 很慢...
        注意! union find 為全局觀!
        故 每次均需要重新設定一個新的union find graph.
        不能沿用上次的 不然會bypass很多node.
        概念與visited一樣 每次均需要重新設定.
        故, visited快很多!
        """
        if len(words1) != len(words2):
            return False

        from collections import defaultdict as dd

        graph = dd(list)

        for p, c in pairs:
            graph[p].append(c)
            graph[c].append(p)

        i = j = 0

        def dfs(node1, node2, visited):

            for n in graph[node2]:
                if n in visited:
                    continue

                if n == node1:
                    return True

                visited.add(n)

                if dfs(node1, n, visited):
                    return True
            return False

        for _ in xrange(len(words1)):
            if words1[i] == words2[j]:
                i += 1
                j += 1
                continue

            visited = set()
            visited.add(words2[j])

            if not dfs(words1[i], words2[j], visited):
                return False

            i += 1
            j += 1

        return True

    def rewrite(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        1. check length equality.
        2. w1[0] == w2[0]
        3. graph search.
        union find 很慢...
        注意! union find 為全局觀!
        故 每次均需要重新設定一個新的union find graph.
        不能沿用上次的 不然會bypass很多node.
        概念與visited一樣 每次均需要重新設定.
        故, visited快很多!
        """
        if len(words1) != len(words2):
            return False

        # build 雙向 graph

        from collections import defaultdict as dd

        graph = dd(list)

        for p in pairs:
            graph[p[0]].append(p[1])
            graph[p[1]].append(p[0])

        def find(x, circle_graph):
            if x in circle_graph:
                return find(circle_graph[x], circle_graph)
            return x

        def uf(x, y, circle_graph):
            x, y = map(find, (x, y), (circle_graph, circle_graph))

            if x == y:
                return False

            circle_graph[x] = y
            return True

        def dfs(fromw, tow, circle_graph):
            for w in graph[fromw]:
                if w == tow:
                    return True

                if not uf(fromw, w, circle_graph):
                    continue

                if dfs(w, tow, circle_graph):
                    return True

            return False

        from __builtin__ import xrange

        for i in xrange(len(words1)):
            if words1[i] == words2[i]:
                continue

            if not dfs(words1[i], words2[i], dict()):
                return False
        return True

    def rewrite2(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        1. check length equality.
        2. w1[0] == w2[0]
        3. graph search.

        union find 很慢...
        注意! union find 為全局觀!
        故 每次均需要重新設定一個新的union find graph.
        不能沿用上次的 不然會bypass很多node.
        概念與visited一樣 每次均需要重新設定.
        故, visited快很多!
For example,
words1 = ["great", "acting", "skills"] and
words2 = ["fine", "drama", "talent"] are similar,

if the similar word pairs are pairs =
[["great", "good"], ["fine", "good"], ["acting","drama"], ["skills","talent"]].

        1. 檢查字串長度.
        2. 同字則相同.
        3. 相同字為transitive.
        """
        if len(words1) != len(words2):
            return False

        # build graph
        dmap = dict()

        for p in pairs:
            if not dmap.get(p[0]):
                dmap[p[0]] = set()

            if not dmap.get(p[1]):
                dmap[p[1]] = set()

            dmap[p[0]].add(p[1])
            dmap[p[1]].add(p[0])

        def dfs(word, expect, visited):
            if word in visited:
                return False

            if word == expect:
                return True

            visited.add(word)

            for w in dmap.get(word, []):
                if dfs(w, expect, visited):
                    return True

            return False

        for w1, w2 in zip(words1, words2):
            visited = set()
            if not dfs(w1, w2, visited):
                return False

        return True

    def smart(self, words1, words2, pairs):
        """
        :type words1: List[str]
        :type words2: List[str]
        :type pairs: List[List[str]]
        :rtype: bool
        """
        import collections

        if len(words1) != len(words2):
            return False

        graph = collections.defaultdict(list)

        for i, j in pairs:
            graph[i].append(j)
            graph[j].append(i)

        memo = {}

        def dfs(val, root):
            memo[val] = root

            for i in graph[val]:
                if i not in memo:
                    dfs(i, root)

        for key in graph:
            if key not in memo:
                dfs(key, key)

        for a, b in zip(words1, words2):
            if memo.get(a, a) != memo.get(b, b):
                return False

        return True


def build():
    return ["great", "acting", "skills"], ["fine", "drama", "talent"], \
        [["great", "good"], ["fine", "good"], ["acting", "drama"],
         ["skills", "talent"]]  # True
    return ["great", "acting", "skills"], ["fine", "drama", "talent"], \
        [["great", "good"], ["shit", "good"], ["acting", "drama"],
         ["skills", "talent"]]  # False
    return ["this", "summer", "thomas", "get", "really", "very", "rich", "and",
            "have", "any", "actually", "wonderful", "and", "good", "truck",
            "every", "morning", "he", "drives", "an", "extraordinary", "truck",
            "around", "the", "nice", "city", "to", "eat", "some", "extremely",
            "extraordinary", "food", "as", "his", "meal", "but", "he", "only",
            "entertain", "an", "few", "well", "fruits", "as", "single", "lunch",
            "he", "wants", "to", "eat", "single", "single", "and", "really",
            "healthy", "life"], \
        ["this", "summer", "thomas", "get", "very", "extremely", "rich", "and", "possess", "the", "actually", "great", "and", "wonderful", "vehicle", "every", "morning", "he", "drives", "unique", "extraordinary", "automobile", "around", "unique", "fine", "city",
         "to", "drink", "single", "extremely", "nice", "meal", "as", "his", "super",
         "but", "he", "only", "entertain", "a", "few", "extraordinary", "food", "as",
         "some", "brunch", "he", "wants", "to", "take", "any", "some", "and",
         "really", "healthy", "life"], \
        [["good", "nice"], ["good", "excellent"], ["good", "well"], ["good", "great"], ["fine", "nice"], ["fine", "excellent"], ["fine", "well"], ["fine", "great"], ["wonderful", "nice"], ["wonderful", "excellent"], ["wonderful", "well"], ["wonderful", "great"], ["extraordinary", "nice"], ["extraordinary", "excellent"], ["extraordinary", "well"], ["extraordinary", "great"], ["one", "a"], ["one", "an"], ["one", "unique"], ["one", "any"], ["single", "a"], ["single", "an"], ["single", "unique"], ["single", "any"], ["the", "a"], ["the", "an"], ["the", "unique"], ["the", "any"], ["some", "a"], ["some", "an"], ["some", "unique"], ["some", "any"], ["car", "vehicle"], ["car", "automobile"], ["car", "truck"], ["auto", "vehicle"], ["auto", "automobile"], [
            "auto", "truck"], ["wagon", "vehicle"], ["wagon", "automobile"], ["wagon", "truck"], ["have", "take"], ["have", "drink"], ["eat", "take"], ["eat", "drink"], ["entertain", "take"], ["entertain", "drink"], ["meal", "lunch"], ["meal", "dinner"], ["meal", "breakfast"], ["meal", "fruits"], ["super", "lunch"], ["super", "dinner"], ["super", "breakfast"], ["super", "fruits"], ["food", "lunch"], ["food", "dinner"], ["food", "breakfast"], ["food", "fruits"], ["brunch", "lunch"], ["brunch", "dinner"], ["brunch", "breakfast"], ["brunch", "fruits"], ["own", "have"], ["own", "possess"], ["keep", "have"], ["keep", "possess"], ["very", "super"], ["very", "actually"], ["really", "super"], ["really", "actually"], ["extremely", "super"], ["extremely", "actually"]]


if __name__ == "__main__":
    s = Solution()
    print(s.areSentencesSimilarTwo(*build()))
    print(s.rewrite(*build()))
    print(s.rewrite2(*build()))
    print(s.smart(*build()))
