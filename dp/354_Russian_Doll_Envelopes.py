#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
submitted.

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
        IDEA:
        The idea is to order the envelopes and then calculate the longest
        increasing subsequence (LISS).
        We first sort the envelopes by width, and we also make sure that when

        the width is the same, the envelope with greater height comes first.

        Why? This makes sure that when we calculate the LISS, we don't have a

        case such as [3, 4] [3, 5] (we could increase the LISS but this would be

        wrong as the width is the same. It can't happen when [3, 5]

        comes first in the ordering).


        We could calculate the LISS using the standard DP algorithm (quadratic

        runtime), but we can just use the tails array method with a twist: we

        store the index of the tail, and we do leftmost insertion point as usual

        to find the right index in nlogn time. Why not rightmost? Think about

        the case [1, 1], [1, 1], [1, 1].
        """
        import bisect

        if not env:
            return 0

        env.sort(key=lambda x: (x[0], -x[1]))
        # [[2, 3], [5, 5], [6, 7], [6, 4]]

        h = []

        for i, e in enumerate(env):
            j = bisect.bisect_left(h, e[1])

            if j < len(h):
                # 因為，之後進入的(x,y) x將會比此6大 所以以4取代7
                # 可以塞更多...
                h[j] = e[1]
            else:
                h.append(e[1])
            print("e[1]: {0}, h: {1}, j: {2}".format(e[1], h, j))

        return len(h)


def build_input():
    return [[5, 5], [6, 4], [6, 7], [2, 3]]


if __name__ == "__main__":
    n = build_input()

    s = Solution()
    result = s.maxEnvelopes(n)

    # 3
    print(result)
