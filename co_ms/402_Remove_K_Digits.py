#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/remove-k-digits/description/

Given a non-negative integer num represented as a string,
remove k digits from the number so that the new number
is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.

Example 1:
Input: num = "1432219", k = 3
Output: "1219"
Explanation: Remove the three digits 4, 3, and 2 to form the
new number 1219 which is the smallest.

Example 2:
Input: num = "10200", k = 1
Output: "200"
Explanation: Remove the leading 1 and the number is 200.
Note that the output must not contain leading zeroes.

Example 3:
Input: num = "10", k = 2
Output: "0"
Explanation: Remove all the digits from the number and it is left with nothing
which is 0.
"""


class Solution(object):

    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        if len(num) == k:
            return "0"

        drop = k
        result = []

        "320"

        for n in num:
            n = int(n)

            while result and drop and n < result[-1]:
                result.pop()
                drop -= 1
                print("result: {} drop: {}".format(result,drop))

            while result:
                if result[0] == 0:
                    result = result[1:]
                    continue
                break

            result.append(n)
            print("result: {}".format(result))

        # 如果input 數字為 1234, k = 2 時，從後去掉2個
        for i in xrange(drop):
            result.pop()

        result = "".join([str(m) for m in result])

        return result


def build_input():
    return "1920", 1
    return "4121", 2
    return "1432219", 3
    #  return "9376"
    #  return "10200"
    #  return "10"
    #  return "9"
    #  return "112"
    return "100000", 3


if __name__ == "__main__":
    s = Solution()
    print(s.removeKdigits(*build_input()))
