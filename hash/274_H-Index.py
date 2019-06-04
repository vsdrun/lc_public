#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/h-index/description/

Given an array of citations (each citation is a non-negative integer)
of a researcher, write a function to compute the researcher's h-index.

According to the definition of h-index on Wikipedia:
"A scientist has index h
if h of his/her N papers have at least
h citations each,
and the other N − h papers have no more than h citations each."

For example, given citations = [3, 0, 6, 1, 5],
which means the researcher has 5 papers in total and each of them had
received 3, 0, 6, 1, 5 citations respectively.
Since the researcher has 3 papers with at least 3
citations each and the remaining two with no more than 3
citations each, his h-index is 3.

Note: If there are several possible values for h, the maximum one is taken as
the h-index.

h: 即須有h個paper其citation要大於等於h
剩下的 N-h paper 其 citation < h citations.
"""


class Solution(object):

    def hIndex(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        # 大至小
        citations.sort(reverse=True)
        hindex = 0

        for i, c in enumerate(citations):

            if c >= 0:
                hindex += 1
            if (len(citations[:i]) + 1) == hindex and c >= hindex:
                continue
            else:
                hindex -= 1
                break

        return hindex


def build_input():
    return [100]
    return [1, 2]
    return [0, 1, 3, 5, 6]
    return [0]
    return [1]
    return [3, 0, 6, 1, 5]


if __name__ == "__main__":
    n = build_input()

    s = Solution()
    result = s.hIndex(n)

    print(result)
