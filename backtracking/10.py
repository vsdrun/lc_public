#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/regular-expression-matching/description/

Implement regular expression matching with support for '.' and '*'.


'.' Matches any single character.
'*' Matches zero or more of the preceding element.


The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)


Some examples:
isMatch("aa","a") → false
isMatch("aa","aa") → true
isMatch("aaa","aa") → false
isMatch("aa", "a*") → true
isMatch("aa", ".*") → true
isMatch("ab", ".*") → true
isMatch("aab", "c*a*b") → true
"""


class Solution(object):

    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        """
        Using DP.
        Prepare 2 dimention list.
        T[i][j], i as text, j as pattern

        type 1:
            當T[i][j] match, 也就是text[i] == pattern[j] or pattern[j] == '.',
                取: T[i-1][j-1]

        type 2:
            當pattern[j] == "*"
            1. text[i] == pattern[j-2]. 代表".*", "X*"為 0.
                取: T[i][j-2] 若為False 繼續2.

            2.
                取: T[i-1][j]

                舉例:
                    aab
                    a.*
                    ----
                    因為b == '.'
                    將text的b去掉，改下一個比對:
                    aa
                    a.*
                    ----
                    如果為True, 則 type 2為True.


        重點:
            列出條件
            buttom up approach.
        """
        # we need only:
        # current row, previous row.
        # current col, previous col.
        dp = [True] + [False] * len(p)
        print(dp)

        # init dp
        for i in xrange(2, len(p) + 1):
            # why start from 2? because .*
            dp[i] = dp[i - 2] and p[i - 1] == "*"
            print("i: {0}".format(i))
            print("dp: {0}".format(dp))

        for i in xrange(len(s)):
            current_row = [False]

            for j in xrange(len(p)):
                if s[i] == p[j] or p[j] == ".":
                    current_row.append(dp[j])  # Update with diagonal value.
                    continue
                elif p[j] == "*":
                    # see if p[j-2] and s[i] 's dp is true.
                    if j > 0 and current_row[j - 1]:
                        current_row.append(True)
                        continue
                    elif j > 0 and (s[i] == p[j - 1] or p[j - 1] == ".") and \
                            dp[j + 1]:
                        current_row.append(True)
                        continue

                current_row.append(False)

            dp = current_row
        return dp[len(dp) - 1]


def build_input():
    return "a", "a*aa"
    return "a", ".*..a*"
    return "abcd", "d*"
    return "a", "ab*a"
    return "", ".*"
    return "", "."
    return "a", ".*.*..*"
    return "ab", ".*"
    return "a", ".*"
    return "aa", "a*"
    return "aab", "c*a*b"
    return "aaa", "aa"


if __name__ == "__main__":
    s1, p1 = build_input()

    s = Solution()
    result = s.isMatch(s1, p1)

    print(result)
