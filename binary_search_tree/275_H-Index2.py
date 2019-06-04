#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/h-index-ii/description/


Follow up for H-Index:
What if the citations array is sorted in ascending order?

Could you optimize your algorithm?

---------
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
        n = len(citations)
        ll, r = 0, n - 1

        while ll <= r:
            mid = (ll + r) / 2

            if citations[mid] > n - mid:
                r = mid - 1
            elif citations[mid] < n - mid:
                ll = mid + 1
            else:
                return n - mid

        return n - ll

    def hIndex_2(self, citations):
        """
        :type citations: List[int]
        :rtype: int
        """
        if not citations:
            return 0

        length = len(citations)
        left = 0
        right = length - 1

        while left <= right:  # 考慮只有 [100], [0]等 這種case.
            mid = left + (right - left) / 2

            if citations[mid] >= (length - mid) and \
                    len(citations[mid:]) == (length - mid):
                right = mid - 1  # mid 是中了 故下一個不含mid
            else:
                left = mid + 1  # mid 沒中 下一個不含mid

        ans = length - left

        return ans


def build_input():
    return [1, 2]
    return [1]
    return [0]
    return [0, 1, 3, 5, 6]
    return [100]
    return [3, 0, 6, 1, 5]


if __name__ == "__main__":
    n = build_input()

    s = Solution()
    result = s.hIndex(n)

    print(result)
