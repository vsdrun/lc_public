#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/


Given a string S of '(' and ')' parentheses,
we add the minimum number of parentheses ( '(' or ')', and in any positions )
so that the resulting parentheses string is valid.


Formally, a parentheses string is valid if and only if:
It is the empty string, or
It can be written as AB (A concatenated with B),
    where A and B are valid strings, or
It can be written as (A), where A is a valid string.


Given a parentheses string,
return the minimum number of parentheses we must add to
make the resulting string valid.


Example 1:
Input: "())"
Output: 1

Example 2:
Input: "((("
Output: 3

Example 3:
Input: "()"
Output: 0

Example 4:
Input: "()))(("
Output: 4


Note:
S.length <= 1000
S only consists of '(' and ')' characters.
"""


class Solution(object):
    def minAddToMakeValid(self, S):
        """
        :type S: str
        :rtype: int

        Use stack, and peak of the stack.
        """
        stack = []

        for s in S:
            if s == "(":
                stack.append(s)
            elif s == ")":
                if stack and stack[-1] == "(":
                    stack.pop()
                else:
                    stack.append(s)

        return len(stack)

def build():
    return "((()"
    return "()"
    return "()))(("
    return "())"


if __name__ == "__main__":
    s = Solution()
    print(s.minAddToMakeValid(build()))
