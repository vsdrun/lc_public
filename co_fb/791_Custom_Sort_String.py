#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/custom-sort-string/description/

S and T are strings composed of lowercase letters.
In S, no letter occurs more than once.

S was sorted in some custom order previously.
We want to permute the characters of T so that they match the order that
S was sorted.

More specifically, if x occurs before y in S,
then x should occur before y in the returned string.


Return any permutation of T (as a string) that satisfies this property.


Example :
Input:
S = "cba"
T = "abcd"
Output: "cbad"
Explanation:
"a", "b", "c" appear in S,
so the order of "a", "b", "c" should be "c", "b", and "a".

Since "d" does not appear in S, it can be at any position in T.
"dcba", "cdba", "cbda" are also valid outputs.
"""


class Solution(object):
    def customSortString(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """

        index = {c: i for i, c in enumerate(S)}

        result = []  # list of tuple (idx, char)

        for c in T:
            if c in index:
                result.append((index[c], c))
            else:
                result.append((float("inf"), c))

        return "".join([v for _, v in sorted(result, key=lambda v:v[0])])

    def rewrite(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        """

        dmap = {c:i for i, c in enumerate(S)}

        result = []


        for t in T:
            if t in dmap:
                result.append((t, dmap[t]))
            else:
                result.append((t, -1))


        result.sort(key=lambda k:k[1])
        return "".join([r[0] for r in result])

    def rewrite2(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: str
        Best solution :-)
        """
        dmap = {c:i for i, c in enumerate(S)}
        return "".join(sorted(T, key=lambda k:dmap.get(k, float("inf"))))

def build():
    return "cba", "abcd"


if __name__ == "__main__":
    s = Solution()
    print(s.customSortString(*build()))
    print(s.rewrite(*build()))
    print(s.rewrite2(*build()))
