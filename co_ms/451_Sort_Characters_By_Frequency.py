#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/sort-characters-by-frequency/description/


Given a string,
sort it in decreasing order based on the frequency of characters.


Example 1:
Input:
"tree"
Output:
"eert"
Explanation:
'e' appears twice while 'r' and 't' both appear once.
So 'e' must appear before both 'r' and 't'. Therefore "eetr" is also a valid
answer.


Example 2:
Input:
"cccaaa"
Output:
"cccaaa"
Explanation:
Both 'c' and 'a' appear three times, so "aaaccc" is also a valid answer.
Note that "cacaca" is incorrect, as the same characters must be together.


Example 3:
Input:
"Aabb"

Output:
"bbAa"

Explanation:
"bbaA" is also a valid answer, but "Aabb" is incorrect.
Note that 'A' and 'a' are treated as two different characters.
"""
import heapq


class Solution(object):

    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        # 先排序 由小至大
        sorted_s = sorted(s)

        h_list = []
        count = 0

        for c, i in enumerate(sorted_s):
            if (c + 1) <= (len(sorted_s) - 1) and \
                    sorted_s[c + 1] == sorted_s[c]:
                count += 1
            else:
                count += 1
                heapq.heappush(h_list, (-count, i))
                count = 0

        result = ''

        for _ in xrange(len(h_list)):
            c, s = heapq.heappop(h_list)
            result += s * (-c)

        return result

    def rewrite(self, s):
        """
        :type s: str
        :rtype: str
        """
        from collections import Counter as cc
        cs = cc(s)

        result = ""

        for str_char, times in cs.most_common():
            result += str_char * times

        return result


def build():
    string = "tree"
    return string


if __name__ == "__main__":
    s = Solution()
    print(s.frequencySort(build()))
    print(s.rewrite(build()))
