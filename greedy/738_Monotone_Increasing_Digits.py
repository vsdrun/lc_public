#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/monotone-increasing-digits/description/


Given a non-negative integer N,
find the largest number that is less than or equal to
N with monotone increasing digits.

(Recall that an integer has monotone increasing digits if and only if
each pair of adjacent digits x and y satisfy x <= y.)


Example 1:
Input: N = 10
Output: 9

Example 2:
Input: N = 1234
Output: 1234

Example 3:
Input: N = 332
Output: 299


https://leetcode.com/problems/monotone-increasing-digits/discuss/124192/Simple-Python-solution-starting-from-the-most-significant-digit
"""


class Solution(object):
    def monotoneIncreasingDigits(self, N):
        """
        :type N: int
        :rtype: int
        """

        """
        1. check N is increasing or not
        2. through observation,  once pass the check for index number,
            the rest could be all 9s.
        """
        from __builtin__ import xrange
        import math as m

        digits = int(m.log(N, 10)) + 1

        result = [9] * digits

        def gen_number(ary):
            ary = ary[::-1]
            num = 0

            for i, n in enumerate(ary):
                num += n * (10 ** i)

            return num

        for i in xrange(digits):
            current = result[:i]  # const in the while loop
            rest_digits = digits - i

            while result[i] > 0 and \
                    gen_number(current + [result[i]] * rest_digits) > N:
                result[i] -= 1

        return gen_number(result)


def build():
    return 1287
    return 1988


if __name__ == "__main__":
    s = Solution()
    print(s.monotoneIncreasingDigits(build()))
