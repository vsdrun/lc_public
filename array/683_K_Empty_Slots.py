#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/k-empty-slots/description/

There is a garden with N slots.

In each slot, there is a flower.
The N flowers will bloom one by one in N days.

_ _ _ _ _  N = 5

state: blooming
flowers[i] = x  day i will bloom in x slot.

In each day, there will be exactly one flower blooming
and it will be in the status of blooming since then.

Given an array flowers consists of number from 1 to N.

Each number in the array represents the place where the
flower will open in that day.

For example, flowers[i] = x means that the unique flower that
blooms at day i will be at position x,
where i and x will be in the range from 1 to N.

Also given an integer k,

you need to output in which day there exists two flowers
in the status of blooming, and also the number of flowers
between them is k and these flowers are not blooming.

If there isn't such day, output -1.


Example 1:
Input:
flowers: [1,3,2]
k: 1
Output: 2
Explanation: In the second day, the first and the third flower have become
blooming.

Example 2:
Input:
flowers: [1,2,3]
k: 1
Output: -1
"""


class Solution(object):
    def kEmptySlots(self, flowers, k):
        """
        :type flowers: List[int]
        :type k: int
        :rtype: int
        """
        import bisect as bi

        li = []

        for d, f in enumerate(flowers):
            day = d + 1

            idx = bi.bisect_left(li, f)

            for n in li[idx - (idx > 0): idx + 1]:
                if abs(n - f) - 1 == k:
                    return day

            li.insert(idx, f)

            #  if ((idx + 1) < len(li) and abs(li[idx + 1] - f) - 1 == k) or \
            #  ((idx - 1) >= 0 and abs(li[idx - 1] - f) - 1 == k):
            #  return day

        return -1


def build():
    return [1, 5, 2, 4, 3], 2
    return [1, 3, 2], 1
    return [1, 3, 2], 2


if __name__ == "__main__":
    flowers, k = build()

    s = Solution()
    result = s.kEmptySlots(flowers, k)

    print(result)
