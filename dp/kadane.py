#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
kadane's algorithm.
https://www.youtube.com/watch?v=yCQN096CwWM
https://goo.gl/5rLQpD
"""


class Solution(object):

    def kadane(self, array):
        """
        :type array: List[int]
        :rtype: int
        """
        import bisect as bb

        ri = [-1, -1]

        tmp_max = total = 0

        tmp_list = []

        bb.insort(tmp_list, (total, -1))

        for i, v in enumerate(array):
            total += v

            tmp_total = total - tmp_list[0][0]

            if tmp_total > tmp_max:
                tmp_max = tmp_total
                ri[0] = tmp_list[0][1] + 1
                ri[1] = i

            bb.insort(tmp_list, (total, i))

        return tmp_max, ri

    def kadane_2(self, array):
        """
        :type array: List[int]
        :rtype: int
        """
        tmax = 0
        tmin = 0
        tmin_idx = -1
        tmax_idx = 0
        total = 0

        for i, n in enumerate(array):
            total += n

            if total < tmin:
                tmin = total
                tmin_idx = i

            if total - tmin > tmax:
                tmax = total - tmin
                tmax_idx = i

        return tmax, (tmin_idx + 1 if tmin_idx < tmax_idx else 0, tmax_idx)


def build():
    return [3]
    return [2, -10, 2, 9, -100, 200, -40, 203]
    return [1, 2, 3, -7, 3]


if __name__ == "__main__":

    s = Solution()
    result, ri = s.kadane_2(build())

    print(result)
    print(ri)
