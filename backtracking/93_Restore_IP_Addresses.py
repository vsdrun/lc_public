#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/restore-ip-addresses/

Given a string containing only digits,
restore it by returning all possible valid IP address combinations.

Example:
Input: "25525511135"
Output: ["255.255.11.135", "255.255.111.35"]
"""


class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        dfs
        """
        result = []

        def dfs(r, tmpr):
            if r == len(s) and len(tmpr) == 4:
                result.append(tmpr[:])
                return

            if len(tmpr) > 4:
                return

            for i in range(r+1, len(s) + 1):
                if i > i + 3:
                    break

                if 0 <= int(s[r:i]) <= 255:
                    if int(s[r:i]) == 0 and len(s[r:i]) > 1 or \
                        len(str(int(s[r:i]))) != len(s[r:i]): # 01 vs. 1
                        continue

                    tmpr.append(s[r:i])
                    dfs(i, tmpr)
                    tmpr.pop()

        tmpr = []
        for i in range(1, len(s) + 1):
            if i > 3:
                break

            if 0 <= int(s[:i]) <= 255:
                if int(s[:i]) == 0 and len(s[:i]) > 1 or \
                    len(str(int(s[:i]))) != len(s[:i]): # 01 vs. 1
                    continue

                tmpr.append(s[:i])
                dfs(i, tmpr)
                tmpr.pop()

        return [".".join(r) for r in result]

    def rewrite(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        def helper(ans, s, k, temp):
            if len(s) > k*3:
                return
            if k == 0:
                ans.append(temp[:])
            else:
                for i in range(min(3,len(s)-k+1)):
                    if i==2 and int(s[:3]) > 255 or i > 0 and s[0] == '0':
                        continue
                    helper(ans, s[i+1:], k-1, temp+[s[:i+1]])

        ans = []
        helper(ans, s, 4, [])
        return ['.'.join(x) for x in ans]


def build():
    return "001001"
    return "0001"
    return ""
    return "25525511135"


if __name__ == "__main__":
    s = Solution()
    print(s.restoreIpAddresses(build()))
    print(s.rewrite(build()))
