#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/pyramid-transition-matrix/description/

We are stacking blocks to form a pyramid.
Each block has a color which is a one letter string, like `'Z'`.

For every block of color `C` we place not in the bottom row,
we are placing it on top of a left block of color `A` and right block of
color `B`.

We are allowed to place the block there only if `(A, B, C)`
is an allowed triple.

We start with a bottom row of bottom, represented as a single string.
We also start with a list of allowed triples allowed.
Each allowed triple is represented as a string of length 3.

Return true if we can build the pyramid all the way to the top,
otherwise false.


Example 1:
Input: bottom = "XYZ", allowed = ["XYD", "YZE", "DEA", "FFF"]
Output: true

Explanation:
We can stack the pyramid like this:
    A
   / \
  D   E
 / \ / \
X   Y   Z

This works because ('X', 'Y', 'D'), ('Y', 'Z', 'E'), and ('D', 'E', 'A')
are allowed triples.


Example 2:
Input: bottom = "XXYX", allowed = ["XXX", "XXY", "XYX", "XYY", "YXZ"]
Output: false

Explanation:
We can't stack the pyramid to the top.
Note that there could be allowed triples (A, B, C) and (A, B, D) with C != D.
"""


class Solution(object):
    def pyramidTransition(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool
        """
        import collections
        import itertools
        from __builtin__ import xrange

        f = collections.defaultdict(list)

        for a, b, c in allowed:
            f[a + b].append(c)

        memo = {}

        def pyramid(bottom):
            if bottom not in memo:
                memo[bottom] = \
                    len(bottom) == 1 or \
                    any(
                    pyramid("".join(i)) for i in itertools.product(
                        *(f[bottom[x: x + 2]] for x in xrange(len(bottom) - 1))
                    )
                )

            return memo[bottom]

        return pyramid(bottom)

    def rewrite(self, bottom, allowed):
        """
        :type bottom: str
        :type allowed: List[str]
        :rtype: bool

        DP, try them all!
        """
        from itertools import product
        from collections import defaultdict
        from __builtin__ import xrange

        # build map:
        dmap = defaultdict(list)

        for a in allowed:
            dmap[a[:2]].append(a[-1])

        # store: key, bottim val: bool, True-> ok, False-> not ok.
        memo = {}

        def mm(key):
            if len(key) == 1:  # 重要!!
                memo[key] = True
                return memo[key]

            if key not in memo:

                bot = [key[i: i + 2] for i in xrange(len(key) - 1)]

                next_keys = [dmap[b] for b in bot]

                next_keys = ["".join(nk) for nk in product(*next_keys)]

                result = any(mm(n) for n in next_keys)

                memo[key] = result

            return memo[key]

        return mm(bottom)


def build():
    return "XYZ", ["XYD", "YZE", "DEA", "FFF"]
    return "XXYX", ["XXX", "XXY", "XYX", "XYY", "YXZ"]


if __name__ == "__main__":
    s = Solution()
    #  print(s.pyramidTransition(*build()))
    print(s.rewrite(*build()))
