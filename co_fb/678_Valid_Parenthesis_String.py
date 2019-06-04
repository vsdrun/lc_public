#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/valid-parenthesis-string/

Given a string containing only three types of characters: '(', ')' and '*',
write a function to check whether this string is valid.
We define the validity of a string by these rules:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.

'*' could be treated as a single right parenthesis ')' or a single
left parenthesis '(' or an empty string.


An empty string is also valid.
Example 1:
Input: "()"
Output: True

Example 2:
Input: "(*)"
Output: True

Example 3:
Input: "(*))"
Output: True

Note:
The string size will be in the range [1, 100].

https://leetcode.com/problems/valid-parenthesis-string/discuss/107570/Python-easy-understand-solution

( 最多的count, including *
( 至少的count, not including *
"""


class Solution(object):
    def checkValidString(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cmin = cmax = 0

        for i in s:
            if i == '(':
                cmax += 1
                cmin += 1
            if i == ')':
                cmax -= 1
                cmin = max(cmin - 1, 0)
            if i == '*':
                cmax += 1  # 將 * 視為 (
                cmin = max(cmin - 1, 0) # 將 * 視為 )

            # 每次都檢查cmax < 0, 避免 ())( 的情況
            if cmax < 0:
                return False

        return cmin == 0



def build():
    return "())("
    return "(*))"


if __name__ == "__main__":
    s = Solution()
    print(s.checkValidString(build()))
