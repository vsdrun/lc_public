#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/simplify-path/description/

Given an absolute path for a file (Unix-style), simplify it.

For example,
path = "/home/", => "/home"
path = "/a/./b/../../c/", => "/c"
"""


class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        hasroot = False

        if path[0] == "/":
            hasroot = True

        path = path.split("/")

        stack = ["/"] if hasroot else []

        while path:
            p = path[0]
            path = path[1:]

            if p == "..":
                if stack[-1] == "/":
                    continue
                elif stack:
                    stack.pop()
                continue
            if p == ".":
                continue
            if p == "":
                continue

            stack.append(p)

        return "/".join(stack)[1:] if hasroot and len(stack) > 1 \
            else "/".join(stack)

    def rewrite(self, path):
        """
        :type path: str
        :rtype: str
        thinking stack...

        path = "/home/", => "/home"
        path = "/a/./b/../../c/", => "/c"
        """
        if not path:
            return False

        # check if there's a root /
        hasRoot = True if path[0] == '/' else False

        path = path.split("/")[::-1]
        result = []

        while path:
            p = path.pop()

            if not p or p == '.':
                continue

            if p == "..":
                if result:
                    result.pop()
                continue

            result += p,

        return "/" + "/".join(result) if hasRoot else "/".join(result)


def build():
    return "/.."
    return "/abc/..."
    return "/"
    return "/a/./b/../../c/"


if __name__ == "__main__":
    s = Solution()
    print(s.simplifyPath(build()))
    print(s.rewrite(build()))
