#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/basic-calculator/description/

Implement a basic calculator to evaluate a simple expression string.

The expression string may contain open ( and closing parentheses ),
the plus + or minus sign -, non-negative integers and empty spaces.

You may assume that the given expression is always valid.

Some examples:
"1 + 1" = 2
" 2-1 + 2 " = 3
"(1+(4+5+2)-3)+(6+8)" = 23

smarter solution:
consider:
1-(2+3) => 1 - 2 - 3
Aware about the sign and run in sequence.
No need to backtrack.
https://discuss.leetcode.com/topic/15806/easy-18-lines-c-16-lines-python
"""


class Solution(object):

    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = []

        def cal(lfs, rhs):
            print("lfs: {0}".format(lfs))
            print("rhs: {0}".format(rhs))

            op = lfs[-1]
            if op == "+":
                return str(int(lfs[:-1]) + int(rhs))
            if op == "-":
                return str(int(lfs[:-1]) - int(rhs))
            return lfs + rhs

        tmp_val = ""

        for c in s:
            if c == " ":
                continue

            if c == ")":
                if tmp_val:
                    stack += tmp_val,
                    tmp_val = ""

                last = len(stack) - stack[::-1].index("(") - 1
                sub = stack[last + 1:]
                result = reduce(cal, sub)
                stack = stack[:last]
                stack += result,
                continue

            if c in "+-(":
                if tmp_val:
                    stack += tmp_val,
                    tmp_val = ""
                stack += c,
                continue

            tmp_val += c

        if tmp_val:
            stack += tmp_val,

        print(stack)

        return int(reduce(cal, stack))


def build():
    return "1-11"
    return "13+(22-23) + 3"
    return "1 + 1"
    return " 2-1 + 2 "
    return "(1+(4+5+2)-3)+(6+8)"
    return "(1+(4+5+2)-3)"
    return "1+(3+2)"


if __name__ == "__main__":
    n = build()
    s = Solution()
    r = s.calculate(n)

    # 23
    print(r)
