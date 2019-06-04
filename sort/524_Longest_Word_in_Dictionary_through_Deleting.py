#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/longest-word-in-dictionary-through-deleting/description/

Given a string and a string dictionary, find the longest string in the
dictionary that can be formed by deleting some characters of the given
string.

If there are more than one possible results, return the longest
word with the smallest lexicographical order.

If there is no possible result, return the empty string.

Input:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

Output:
"apple"

Input:
s = "ablepcpa", d = ["a","b","c"]

Output:
"a"
"""


class Solution(object):

    def findLongestWord(self, s, d):
        """
        :type s: str
        :type d: List[str]
        :rtype: str
        """

        """
        1. 由dictionary中優先找最長的的字 也就是將dictionary給heap sort.
        2. 利用iterator往前不後的特性 一個個找 確保找到的屬於那個字.
        3. 看到deleting char 則想到iterator的特性 往前不後.
        """
        import heapq

        heap = [(-len(word), word) for word in d]  # max heap
        heapq.heapify(heap)

        # result = ["ale", "apple", "monkey", "plea"]
        # monkey, apple, plea, ale
        # "abpcplea"

        while heap:
            word = heapq.heappop(heap)[1]
            it = iter(s)  # this is _so_ smart.

            """
            in 的特性是一路call next(it)往下找到沒有為止
            也就是一般使用str in "abcd" 同樣的道理
            in 的後頭須接iterable的容器
            """

            if all(c in it for c in word):
                return word

        return ''


def build_input():
    #  result = [3, 5, 5, 5, 5, 2, 6]
    #  result = [100]
    #  result = [0, 1, 1, 4, 4, 5, 6]
    #  result = [11, 15]
    result = ["ale", "apple", "monkey", "plea"]
    result = ["apple", "ewaf", "awefawfwaf", "awef", "awefe", "ewafeffewafewf"]
    return result


if __name__ == "__main__":
    input = build_input()

    s = Solution()
    result = s.findLongestWord("aewfafwafjlwajflwajflwafj", input)

    print(result)
