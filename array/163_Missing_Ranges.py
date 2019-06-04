#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/missing-ranges/description/

Given a sorted integer array where the range of elements
are in the inclusive range [lower, upper], return its missing ranges.

For example, given [0, 1, 3, 50, 75], lower = 0 and upper = 99, return ["2",
"4->49", "51->74", "76->99"].
"""


class Solution(object):
    def findMissingRanges(self, A, lower, upper):
        """
        :type nums: List[int]
        :type lower: int
        :type upper: int
        :rtype: List[str]
        """

        # 注意corner case, 負數.
        result = []

        A.append(upper + 1)

        pre = lower - 1

        for i in A:
            if (i == pre + 2):
                result.append(str(i - 1))
            elif (i > pre + 2):
                result.append(str(pre + 1) + "->" + str(i - 1))
            pre = i

        return result


def build():
    return [0, 1, 3, 50, 75], 0, 99


if __name__ == "__main__":

    s = Solution()
    result = s.findMissingRanges(*build())

    print(result)
