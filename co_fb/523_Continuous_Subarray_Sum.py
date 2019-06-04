#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/continuous-subarray-sum/description/

Given a list of non-negative numbers and a target integer k,
write a function to check if the array has a ***continuous subarray***
of size at least 2 that sums up to the multiple of k,
that is, sums up to n*k where n is also an integer.

Example 1:
Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of
size 2 and sums up to 6.


Example 2:
Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an
continuous subarray of size 5 and sums up to 42.

https://en.wikipedia.org/wiki/Modular_arithmetic
https://betterexplained.com/articles/fun-with-modular-arithmetic/
https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/congruence-modulo

a%k = 2
b%k = 2
(a-b)%k = 0
"""


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        原因?
        因為!
        只要這個的和 - 之前的和的 module 必為 0 , 則這兩個差的和可以整除k
        """
        total = 0
        st = set()
        premod = 0

        #[23, 2, 0, 4, 7], 0
        for i, n in enumerate(nums):
            total += n
            remain = total % k if k else total

            if i > 0:
                if remain in st:
                    return True

            st.add(premod)
            premod = remain
        return False

    def rewrite(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        原因?
        因為!
        只要這個的和 - 之前的和的module 必為 0 , 則這兩個差的和可以整除k
        注意corner case: k = 0
        """

        modset = set()
        total = 0
        previous_remain = 0  # 不要第一次就加入modset因為minimum length為2

        for i, n in enumerate(nums):
            total += n
            remain = total % k if k else total

            if i > 0:  # 因為length 要大於2
                if remain in modset:
                    return True

            modset.add(previous_remain)
            previous_remain = remain

        return False

    def rewrite2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        注意corner case: k = 0
        """
        modset = set([0])
        total = 0

        for idx, n in enumerate(nums):
            total += n
            m = total % k if k else total

            if idx > 0:
                if m in modset:
                    return True

                modset.add(m)

        return False




def build():
    return [23, 2, 6, 4, 7], 0
    return [23, 2, 0, 0, 4, 7], 0  # true because there's a double 0.
    return [0, 0], 3
    return [0, 0], 0
    return [0, 0], 100
    return [23, 2, 4, 6, 7], 6
    return [0, 7, 3, 3, 6], 3
    return [1, 5], -6
    return [2, 4], 6
    return [23, 2, 6, 4, 7], 6


if __name__ == "__main__":

    s = Solution()
    print(s.checkSubarraySum(*build()))
    print(s.rewrite(*build()))
    print(s.rewrite2(*build()))
