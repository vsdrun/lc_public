#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/russian-doll-envelopes/description/

You have a number of envelopes with widths and heights given as a pair
of integers (w, h).

One envelope can fit into another if and only if
both the width and height of one envelope is greater than the width and
height of the other envelope.

What is the maximum number of envelopes can you Russian doll?
(put one inside other)

Example:
Given envelopes = [[5,4],[6,4],[6,7],[2,3]],
the maximum number of envelopes you
can Russian doll is 3 ([2,3] => [5,4] => [6,7]).
"""


class Solution(object):

    def maxEnvelopes(self, env):
        """
        :type env: List[List[int]]
        :rtype: int
        """

        """
        DP, try them all!
        When DP, create dp matrix.
        Sort!
        """
        m = len(env)

        if not m:
            return 0

        env.sort()
        result = [1] * m

        # DP, buttom up approach

        for i, v in enumerate(env):
            for j in xrange(0, i):
                if v[0] > env[j][0] and v[1] > env[j][1]:
                    result[i] = max(result[i], result[j] + 1)

        print(result)
        return max(result)


def build_input():
    return [[5, 4], [6, 4], [6, 7], [2, 3]]


if __name__ == "__main__":
    n = build_input()

    s = Solution()
    result = s.maxEnvelopes(n)

    # 3
    print(result)
