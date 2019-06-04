#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/maximum-swap/description/

Given a non-negative integer,
you could swap two digits at most once to get the maximum valued number.
Return the maximum valued number you could get.

Example 1:
Input: 2736
Output: 7236
Explanation: Swap the number 2 and the number 7.

Example 2:
Input: 9973
Output: 9973
Explanation: No swap.


https://leetcode.com/problems/maximum-swap/discuss/107073/C++-one-pass-simple-and-fast-solution:-1-3ms-O(n)-time


places = [10**i for i in range(len(str(num)))]
return max(num + num/p%10*(q-p) + num/q%10*(p-q)
           for p in places for q in places)
"""


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        from right to left.
        unless there's a slot which is less than current max will
        trigger a left/right index update.
        """
        num = list(str(num))

        max_idx = left = right = -1
        current_max = float("-inf")

        for i in xrange(len(num) - 1, -1, -1):
            if num[i] > current_max:
                current_max = num[i]
                max_idx = i
                continue

            if num[i] < current_max:
                left = i
                right = max_idx

        if left == -1:
            return int("".join(num))

        num[left], num[right] = num[right], num[left]

        return int("".join(num))

    def maximumSwap_math(self, num):
        """
        :type num: int
        :rtype: int
        math:
        10a + b - (10b + a) = 9a - 9b

        724 => +9*4 - 9*2 => 742

        723 => +99*3 - 99*7 => 327
        """
        places = [10**i for i in range(len(str(num)))]
        print("places: {0}".format(places))

        for p in places:
            for q in places:
                print("p: {0} q: {1}".format(p, q))
                print("num: {}".format(num))
                print("num / p % 10 * (q - p): {}".format(
                    num / p % 10 * (q - p)))
                print("num / q % 10 * (p - q): {}".format(
                    num / q % 10 * (p - q)))

                ret = num + num / p % 10 * (q - p) + num / q % 10 * (p - q)

                print("ret: {}".format(ret))

        return max(num + num / p % 10 * (q - p) + num / q % 10 * (p - q)
                   for p in places for q in places)


def build():
    return 99901
    return 2736
    return 7291
    return 9277
    return 546578
    return 4321
    return 1234
    return 1111
    return 728


if __name__ == "__main__":

    s = Solution()
    result = s.maximumSwap(build())
    print(result)
