#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/license-key-formatting/

You are given a license key represented as a string S which
consists only alphanumeric character and dashes.
The string is separated into N+1 groups by N dashes.

Given a number K, we would want to reformat the strings such
that each group contains exactly K characters, except for the
first group which could be shorter than K,

but still must contain at least one character.
Furthermore, there must be a dash inserted between two
groups and all lowercase letters should be converted to uppercase.

Given a non-empty string S and a number K, format the string according to the
rules described above.


Example 1:
Input: S = "5F3Z-2e-9-w", K = 4
Output: "5F3Z-2E9W"

Explanation: The string S has been split into two parts,
each part has 4 characters.
Note that the two extra dashes are not needed and can be removed.


Example 2:
Input: S = "2-5g-3-J", K = 2
Output: "2-5G-3J"

Explanation: The string S has been split into three parts, each part has 2
characters except the first part as it could be shorter as mentioned above.

The length of string S will not exceed 12,000, and K is a positive integer.

String S consists only of alphanumerical characters
    (a-z and/or A-Z and/or 0-9) and dashes(-).
String S is non-empty.
"""


class Solution(object):
    def licenseKeyFormatting(self, S, K):
        """
        :type S: str
        :type K: int
        :rtype: str
        """

        S = S.upper().replace("-", "")
        length = len(S)
        result = []
        dashcount = 0
        mod = length % K
        count = 0

        while mod:
            result += S[count],
            count += 1
            mod -= 1

        if len(result) and len(S) > K:
            result += "-",

        while count < len(S):
            if dashcount == K:
                result += "-",
                dashcount = 0

            dashcount += 1
            result += S[count],
            count += 1

        return "".join(result)


def build():
    ret = 'r', 1
    ret = "2-5g-3-J", 2
    ret = "2-5g-3-J", 2
    ret = "2", 2
    return ret


if __name__ == "__main__":
    s = Solution()
    result = s.licenseKeyFormatting(*build())

    print(result)
