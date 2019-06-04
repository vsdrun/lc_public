#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/find-anagram-mappings/description/


Given two lists A and B, and B is an anagram of A.
B is an anagram of A means B is made by randomizing the
order of the elements in A.

We want to find an index mapping P, from A to B.
A mapping P[i] = j means the ith element in A appears in B at index j.

These lists A and B may contain duplicates.
If there are multiple answers, output any of them.

For example, given

A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]

We should return
[1, 4, 3, 2, 0]

as P[0] = 1 because the 0th element of A appears at B[1],
and P[1] = 4 because the 1st element of A appears at B[4], and so on.
"""


class Solution(object):
    def anagramMappings(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict
        from __builtin__ import xrange

        hash_B = defaultdict(list)

        [hash_B[v].append(i) for i, v in enumerate(B)]

        for i in xrange(len(A)):
            A[i] = hash_B[A[i]].pop()

        return A

    def rewrite(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: List[int]
        """
        from collections import defaultdict as dd
        graphB = dd(list)

        for i, v in enumerate(B):
            graphB[v].append(i)

        result = []

        for v in A:
            result.append(graphB[v].pop())

        return result


def build():
    #  return (1, 99)
    #  return (-2, 3)
    #  return (0, 2)
    #  return (2, 1)
    #  return (1, 2)
    A = [50, 12, 28, 46, 32, 50]
    B = [50, 12, 32, 46, 28, 50]
    return A, B


if __name__ == "__main__":
    s = Solution()
    result = s.anagramMappings(*build())
    print(result)
    result = s.rewrite(*build())
    print(result)
