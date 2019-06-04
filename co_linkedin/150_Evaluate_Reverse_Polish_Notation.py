#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/evaluate-reverse-polish-notation/description/

Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /.

Each operand may be an integer or another expression.

Some examples:
  ["2", "1", "+", "3", "*"] -> ((2 + 1) * 3) -> 9
  ["4", "13", "5", "/", "+"] -> (4 + (13 / 5)) -> 6
"""


class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        思考 雖然為postfix 仍由前面traverse 先找operand.
        再找operator.
        """
        stack = []

        for t in tokens:
            if t not in ["+", "-", "*", "/"]:
                # operands.
                stack.append(int(t))
            else:
                # get operands / expression
                rr, ll = stack.pop(), stack.pop()
                if t == "+":
                    stack.append(ll + rr)
                elif t == "-":
                    stack.append(ll - rr)
                elif t == "*":
                    stack.append(ll * rr)
                else:
                    # here take care of the case like "1/-22",
                    # in Python 2.x, it returns -1, while in
                    # Leetcode it should return 0
                    if ll * rr < 0 and ll % rr != 0:
                        stack.append(ll / rr + 1)
                    else:
                        stack.append(ll / rr)
        return stack.pop()


def build():
    return ["10", "6", "9", "3", "+", "-11",
            "*", "/", "*", "17", "+", "5", "+"]
    return ["15", "7", "1", "1", "+", "-", "/", "3", "*", "2", "1", "1",
            "+", "+", "-"]
    #  ((15 ÷ (7 − (1 + 1))) × 3) − (2 + (1 + 1))
    return ["2", "1", "+", "3", "*"]
    return ["4", "13", "5", "/", "+"]
    return ["18"]


if __name__ == "__main__":
    s = Solution()
    print(s.evalRPN(build()))
