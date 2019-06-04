#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/minimum-swaps-to-make-sequences-increasing/description/


We have two integer sequences A and B of the same non-zero length.

We are allowed to swap elements A[i] and B[i].
Note that both elements are in the same index position in
their respective sequences.


At the end of some number of swaps, A and B are both strictly increasing.
(A sequence is strictly increasing if and
only if A[0] < A[1] < A[2] < ... < A[A.length - 1].)


Given A and B,
return the minimum number of swaps to make both sequences strictly increasing.
It is guaranteed that the given input always makes it possible.


Example:
Input: A = [1,3,5,4], B = [1,2,3,7]
Output: 1
Explanation:
Swap A[3] and B[3].  Then the sequences are:
A = [1, 3, 5, 7] and B = [1, 2, 3, 4]
which are both strictly increasing.
"""


class Solution(object):
    def minSwap(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: int

        保證有解! 所以~~~
        一定有可以swap的
        """

        # wide contract check
        if not A or not B:
            return 0

        # dp[0]
        # dp[1]
        dp = [[0 for i in range(len(A))] for j in range(2)]
        dp[0][0], dp[1][0] = 0, 1

        for j in range(1, len(A)):
            if A[j] <= B[j - 1] or B[j] <= A[j - 1]:
                # shall not swap, otherwise will violate the order
                dp[0][j] = dp[0][j - 1]  # no change
                # or if swap, we should swap the previous one as well
                dp[1][j] = dp[1][j - 1] + 1
            elif B[j] <= B[j - 1] or A[j] <= A[j - 1]:
                # we need a swap here for sure!
                dp[0][j] = dp[1][j - 1]  # not swap dp[0] updated to previous
                # swapped dp[1]

                dp[1][j] = dp[0][j - 1] + 1  # swapped dp[1] update to previous
                # not swapped dp[0] + 1 (current swap)
            else:
                mins = min(dp[0][j - 1], dp[1][j - 1])
                # if we dont' swap, it's fine here.
                dp[0][j] = mins
                # or if we swap, it's also fine, + 1 to the dp[1]
                dp[1][j] = mins + 1

        return min(dp[0][-1], dp[1][-1])


def build():
    return [1, 3, 5, 4], [1, 2, 3, 7]


if __name__ == "__main__":
    s = Solution()
    result = s.minSwap(*build())
    print(result)
