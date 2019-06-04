#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/count-and-say/description/


The count-and-say sequence is the sequence of integers with
the first five terms as following:


1.     1
2.     11
3.     21
4.     1211
5.     111221


1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.


Given an integer n, generate the nth term of the count-and-say sequence.


Note: Each term of the sequence of integers will be represented as a string.


Example 1:
Input: 1
Output: "1"

Example 2:
Input: 4
Output: "1211"
"""


class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"

        def count(result):
            count = 1
            tmp = ""

            for i in xrange(1, len(result)):
                if result[i] == result[i - 1]:
                    count += 1
                else:
                    tmp += str(count) + result[i - 1]
                    count = 1
            tmp += str(count) + result[len(result) - 1]
            return tmp

        for i in xrange(n - 1):
            result = count(result)

        return result

    def rewrite(self, n):
        """
        :type n: int
        :rtype: str
        """
        result = "1"

        def cnt(r):
            count = 1
            result = ""

            for idx in range(1, len(r)):
                if r[idx] == r[idx - 1]:
                    count += 1
                else:
                    result += (str(count) + r[idx - 1])
                    count = 1

            result += str(count) + r[-1]
            return result


        for i in range(n - 1):
            result = cnt(result)

        return result

def build():
    return 9


if __name__ == "__main__":

    s = Solution()
    print(s.countAndSay(build()))
    print(s.rewrite(build()))
