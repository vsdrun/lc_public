#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/string-to-integer-atoi/description/


Implement atoi which converts a string to an integer.


The function first discards as many whitespace characters as necessary until
the first non-whitespace character is found.


Then, starting from this character,
takes an optional initial plus or minus sign followed by as many
numerical digits as possible,
and interprets them as a numerical value.


The string can contain additional characters after those that form the
integral number,
which are ignored and have no effect on the behavior of this function.


If the first sequence of non-whitespace characters in str is not a
valid integral number,
or if no such sequence exists because either str is empty or
it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.

Only the space character ' ' is considered as whitespace character.


Example 1:
Input: "42"
Output: 42


Example 2:
Input: "   -42"
Output: -42
Explanation: The first non-whitespace character is '-', which is the minus sign.
             Then take as many numerical digits as possible, which gets 42.


Example 3:
Input: "4193 with words"
Output: 4193
Explanation: Conversion stops at digit '3' as the next character is
not a numerical digit.


Example 4:
Input: "words and 987"
Output: 0
Explanation: The first non-whitespace character is 'w', which is not a numerical
             digit or a +/- sign.
             Therefore no valid conversion could be performed.

Example 5:
Input: "-91283472332"
Output: -2147483648
Explanation: The number "-91283472332" is out of the range of a
32-bit signed integer.
             Thefore INT_MIN (−231) is returned.
"""


class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        if not str:
            return 0

        # https://docs.python.org/2/library/itertools.html
        # takewhile()	pred, seq	seq[0], seq[1], until pred fails
        # takewhile(lambda x: x<5, [1,4,6,4,1]) --> 1 4
        from itertools import takewhile as tw

        s = str.lstrip()

        sign = list(tw(lambda x: x in '+-', s))

        digits = list(tw(lambda x: x in '0123456789', s[1:] if sign else s))

        try:
            result = int((sign[0] if sign else "") + "".join(digits))
        except Exception:
            return 0

        return max(min(result, 2**31 - 1), -2**31)


def build():
    return "+words and 987"
    return "42"
    return "+-o"
    return "-42"
    return " "
    return "   -42"
    return "-91283472332"
    return "-123"


if __name__ == "__main__":
    s = Solution()
    print(s.myAtoi(build()))
