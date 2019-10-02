#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/top-k-frequent-words/description/

Given a non-empty list of words, return the k most frequent elements.
Your answer should be sorted by frequency from highest to lowest.

If two words have the same frequency,
then the word with the lower alphabetical order comes first.

Example 1:
Input: ["i", "love", "leetcode", "i", "love", "coding"], k = 2
Output: ["i", "love"]
Explanation: "i" and "love" are the two most frequent words.
    Note that "i" comes before "love" due to a lower alphabetical order.



Example 2:
Input:
["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"], k = 4

Output: ["the", "is", "sunny", "day"]
Explanation: "the", "is", "sunny" and "day" are the four most frequent words,
    with the number of occurrence being 4, 3, 2 and 1 respectively.

善用api
https://docs.python.org/2/library/itertools.html
"""


class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        dmap = {}

        for w in words:
            if dmap.get(w, None) is None:
                dmap[w] = 0
            dmap[w] += 1

        result = []

        import heapq as hq

        for key, val in dmap.iteritems():
            hq.heappush(result, (-val, key))

        ret = []
        for _ in range(k):
            ret.append(hq.heappop(result)[1])

        return ret

    def rewrite(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        from collections import Counter as cc

        result = cc(words)



def build():
    return ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is",
            "is", "is"], 4
    return ["aaa", "aa", "a"], 1
    return ["i", "love", "leetcode", "i", "love", "coding"], 2


if __name__ == "__main__":
    s = Solution()
    print(s.topKFrequent(*build()))
