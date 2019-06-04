#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/rotate-function/description/


Given an array of integers A and let n to be its length.

Assume Bk to be an array obtained by rotating the array A k
positions clock-wise, we define a "rotation function" F on A as follow:
F(k) = 0 * Bk[0] + 1 * Bk[1] + ... + (n-1) * Bk[n-1].


Calculate the maximum value of F(0), F(1), ..., F(n-1).

Note:
n is guaranteed to be less than 105.

Example:
A = [4, 3, 2, 6]

F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16
F(2) = (0 * 2) + (1 * 6) + (2 * 4) + (3 * 3) = 0 + 6 + 8 + 9 = 23
F(3) = (0 * 3) + (1 * 2) + (2 * 6) + (3 * 4) = 0 + 2 + 12 + 12 = 26

So the maximum value of F(0), F(1), F(2), F(3) is F(3) = 26.


https://leetcode.com/problems/rotate-function/discuss/111916/Python3-solution-with-O(n)-time-and-O(1)-space
"""


class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int

        consider:
        F(0) = (0 * 4) + (1 * 3) + (2 * 2) + (3 * 6) = 0 + 3 + 4 + 18 = 25
        F(1) = (0 * 6) + (1 * 4) + (2 * 3) + (3 * 2) = 0 + 4 + 6 + 6 = 16

        i.e for the next round, each item has added one more except the last
        one, which been removed.

        Thus, each added one more means: sum([4,3,2,6])
        minus the last one being removed, i.e (N-1) * A[N-1]
        However, the sum([4,3,2,6]) also contributed one 6, thus we should
        at last minus: (N) * A[N-1]
        """

        total = sum(A)

        # calculate F(0) as base
        base_sum = 0

        for i in range(len(A)):
            base_sum += i * A[i]

        mx = base_sum

        for i in range(1, len(A)):
            local_sum = base_sum + total - len(A) * A[len(A) - i]
            base_sum = local_sum  # for next round...
            mx = max(mx, local_sum)

        return mx


def build():
    return [4, 3, 2, 6]


if __name__ == "__main__":

    s = Solution()
    print(s.maxRotateFunction(build()))
