#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/basic-calculator-ii/

Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, /
operators and empty spaces . The integer division should truncate toward zero.

Example 1:
Input: "3+2*2"
Output: 7

Example 2:
Input: " 3/2 "
Output: 1

Example 3:
Input: " 3+5 / 2 "
Output: 5

Note:
You may assume that the given expression is always valid.
Do not use the eval built-in library function.

先處理 *,/ 最後再處理+, -
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        stack
        請永遠注意 number '42'
        不是只有單一數字
        """
        s = s.strip() + "+"
        stack = []
        prev = None

        for c in s:
            c = c.strip()

            if c == "":
                continue

            if c in "+-*/":
                if stack and stack[-1] == "*":
                    stack.pop()
                    val = stack.pop()
                    tmp = val * int(prev)
                    stack.append(tmp)
                elif stack and stack[-1] == "/":
                    stack.pop()
                    val = stack.pop()
                    tmp = val // int(prev)
                    stack.append(tmp)
                else:
                    stack.append(int(prev))
                stack.append(c)
                prev = None
            else:
                if prev is None:
                    prev = c
                else:
                    prev += c

        stack.pop()
        #  print("stack: {}".format(stack))

        result = 0
        op = "+"

        for c in stack:
            if type(c) is str:
                op = c
                continue

            if op == "+":
                result += c
            else:
                result -= c

        return result



def build():
    return "42 + 53 * 10 / 2 - 5"
    return "1-1+1"
    return " 3+5 / 2 "
    return "42"
    return "3+2*2"
    return " 3/2 "

if __name__ == "__main__":
    s = Solution()
    print(s.calculate(build()))
