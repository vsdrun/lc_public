#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/valid-parentheses/description/

Given a string containing just the characters '(', ')', '{', '}', '[' and ']',
determine if the input string is valid.

The brackets must close in the correct order,
"()" and "()[]{}" are all valid but "(]" and "([)]" are not.
"""


class Solution(object):

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        def reverse(c):
            if c == "]":
                return "["
            if c == "}":
                return "{"
            if c == ")":
                return "("

        for c in s:
            stack += c,

            """{}({[]})"""
            if c == "]" or c == "}" or c == ")":
                if len(stack) > 1 and stack[-2] == reverse(c):
                    stack = stack[:-2]

        if len(stack) == 0:
            return True
        else:
            return False

    def rewrite(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []

        dmap = dict()
        dmap['['] = ']'
        dmap['{'] = '}'
        dmap['('] = ')'

        for c in s:
            if c in dmap.keys():
                stack.append(c)

            if c in dmap.values():
                if not stack:
                    return False
                if c != dmap[stack[-1]]:
                    return False
                stack.pop()

        if stack:
            return False
        else:
            return True

    def rewrite2(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        dmap = {'}': '{', ']': '[', ')': '('}

        for idx in range(len(s)):
            if s[idx] in "({[":
                stack.append(s[idx])
            elif s[idx] in ")}]":
                if not stack:
                    return False
                if stack[-1] == dmap[s[idx]]:
                    stack.pop()
                else:
                    return False

        return True if not stack else False


def build():
    return "[()]"
    return ""
    return "{}({[]})"
    return "([)]"
    return ']'
    return "{[}]"
    return "]"


if __name__ == "__main__":
    s = Solution()
    print(s.isValid(build()))
    print(s.rewrite(build()))
    print(s.rewrite2(build()))
