#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/beautiful-arrangement/description/

Suppose you have N integers from 1 to N.
We define a beautiful arrangement as an array that is constructed by
these N numbers successfully if one of the following is true for
the ith position (1 <= i <= N) in this array:


The number at the ith position is divisible by i.
OR
i is divisible by the number at the ith position.
Now given N, how many beautiful arrangements can you construct?

Example 1:
Input: 2
Output: 2
Explanation:


The first beautiful arrangement is [1, 2]:
Number at the 1st position (i=1) is 1, and 1 is divisible by i (i=1).
Number at the 2nd position (i=2) is 2, and 2 is divisible by i (i=2).


The second beautiful arrangement is [2, 1]:
Number at the 1st position (i=1) is 2, and 2 is divisible by i (i=1).
Number at the 2nd position (i=2) is 1, and i (i=2) is divisible by 1.

Note:
N is a positive integer and will not exceed 15.
"""

cache = {}


class Solution(object):
    def countArrangement(self, N):
        """
        :type N: int
        :rtype: int
        """

        def helper(i, X):
            """
            X 為 index tuple , starts from 1 ~ N
            """
            # i 為index, 由後往前。
            if i == 1:
                # 因為任何數 % 1 為0
                return 1

            # index: 從0 ~ 此index的所有數
            # 由後往前 i 初始為 N
            key = (i, X)

            if key in cache:
                return cache[key]

            recursive = []

            for j, x in enumerate(X):
                if x % i == 0 or i % x == 0:
                    recursive.append(helper(i - 1, X[:j] + X[j + 1:]))

            total = sum(recursive)
            cache[key] = total
            return total

        # 以index 為pivot支點。
        # 由後往前
        return helper(N, tuple(range(1, N + 1)))


def build_input():
    return 2


if __name__ == "__main__":
    b = build_input()

    s = Solution()
    result = s.countArrangement(b)

    #  Return ["eat","oath"].
    print(result)
