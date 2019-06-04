#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/generate-parentheses/description/

Given n pairs of parentheses,
write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        stack = [] # stack of char
        results = [] # result of stacks

        def gen(left, right):
            if left > 0:
                stack.append('(')
                gen(left - 1, right)
                stack.pop()

            if left < right:
                stack.append(')')
                gen(left, right - 1)
                stack.pop()


            if right == 0:
                results.append("".join(stack))

        gen(n, n)
        return results

def build():
    return 3


if __name__ == "__main__":
    s = Solution()
    print(s.generateParenthesis(build()))
