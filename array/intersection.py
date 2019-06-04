#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Given two arrays of integers of size M and N,
write a function that returns the intersection of the two arrays in
O(M + N) time.
"""


class Solution(object):
    def intersection(self, l1, l2):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        from __builtin__ import xrange

        l1.sort()
        l2.sort()
        result = []

        def gen_1():
            for i, n in enumerate(l1):
                yield i, n

        def gen_2():
            for i, n in enumerate(l2):
                yield i, n

        g1 = gen_1()
        g2 = gen_2()
        j, g_2 = next(g2)

        for i, g_1 in g1:
            print("g_1: {}".format(g_1))
            print("g_2: {}".format(g_2))
            if g_1 < g_2:
                continue

            if g_1 == g_2:
                result.append(g_1)
                continue
            try:
                j, g_2 = next(g2)

                if g_1 == g_2:
                    result.append(g_1)
            except Exception:
                pass

        return result


def build():
    return [3, 4, 5, 7], [1, 2, 4, 7, 9]
    return [1, 2, 4, 7, 9], [3, 4, 5]


if __name__ == "__main__":
    s = Solution()
    result = s.intersection(*build())
    print(result)
