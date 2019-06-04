#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/basic-calculator-iii/

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ),
the plus + or minus sign -, non-negative integers and empty spaces .

The expression string contains only non-negative integers, +, -, *, /
operators , open ( and closing parentheses ) and empty spaces.
The integer division should truncate toward zero.

You may assume that the given expression is always valid.
All intermediate results will be in the range of [-2147483648, 2147483647].

Some examples:
"1 + 1" = 2
" 6 - 4 / 24 + 10"
"2*(5+5*2)/3+(6/2+8)" = 21
"(2+6* 3+5- (3*14/7+2)*5)+3"=-12

https://www.geeksforgeeks.org/expression-evaluation/
"""

class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """

        def cal(ss):
            """
            handles -15 + 3
            """
            # [30, '+', 25, '+', 15, '+']
            # "30 + 50/2 + 15"
            #  print("cal's ss: {}".format(ss))
            ss = '0' + ss + '+'
            stack = []
            val = ""

            for c in ss:
                c = c.strip()

                if c and c in "+-*/":
                    if stack and stack[-1] == "*":
                        stack.pop()
                        leftOperant = stack.pop()
                        result = leftOperant * int(val)
                        stack.append(result)
                    elif stack and stack[-1] == "/":
                        stack.pop()
                        leftOperant = stack.pop()
                        result = leftOperant / int(val)
                        stack.append(result)
                    else:
                        stack.append(int(val))
                    stack.append(c)
                    val = ""
                else:
                    val += c

            result = 0
            operator = '+'

            for c in stack:
                if type(c) is str:
                    operator = c
                else:
                    if operator == "+":
                        result += c
                    elif operator == "-":
                        result -= c

            return result

        def parse(lidx):
            finalExp = ""

            while lidx < len(s) and s[lidx] != ')':
                c = s[lidx].strip()

                if c and c == '(':
                    lidx += 1
                    result, lidx = parse(lidx)
                    finalExp += str(result)
                else:
                    finalExp += c
                lidx += 1

            #  print("parse's finalExp: {}".format(finalExp))
            return cal(finalExp), lidx

        stack = []
        finalExp = ""
        subExp = ""
        idx = 0

        while idx < len(s):
            c = s[idx].strip()
            # "(2+6* 3+5- (3*14/7+2)*5)+3"
            if c and c == "(":
                idx += 1
                result, idx = parse(idx)
                finalExp += str(result)
            else:
                finalExp += c

            idx += 1

        return cal(finalExp)


def build():
    return " 6 - 4 / 24 + 10"
    return "1 + 1" # 2
    return "2*(5+5*2)/3+(6/2+8)" # 21
    return "(2+6* 3+5- (3*14/7+2)*5)+3" #-12
    return "2*(5+5*2)/3+(6/2+8)" # 21
    return "(2+6* 3+5- (3*14/7+2)*5)+3" # -12
    return "30 + 50/2 + 15"


if __name__ == "__main__":
    s = Solution()
    print(s.calculate(build()))
