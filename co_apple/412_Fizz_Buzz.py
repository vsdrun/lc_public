#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/fizz-buzz/description/

Write a program that outputs the string representation of numbers from 1 to n.

But for multiples of three it should output “Fizz”
instead of the number and for the multiples of five output “Buzz”.

For numbers which are multiples of both three and five output “FizzBuzz”.

Example:

n = 15,

Return:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
[1, 2, 'Fizz', 4, 'Buzz', 'Fizz', 7, 8, 'Fizz', 'Buzz', 11, 'Fizz', 13, 14, 'FizzBuzz']
"""


class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n < 1:
            return

        result = []

        for i in range(1, n + 1):
            if not i % 3 and not i % 5:
                result.append("FizzBuzz")
                continue
            if not i % 3:
                result.append('Fizz')
            elif not i % 5:
                result.append('Buzz')
            else:
                result.append(str(i))

        return result


def build():
    return 15


if __name__ == "__main__":
    s = Solution()
    print(s.fizzBuzz(build()))
