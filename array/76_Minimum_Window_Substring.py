#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/minimum-window-substring/description/

Given a string S and a string T,
find the minimum window in S which will contain all
the characters in T in complexity O(n).


使用 dict[key] = cnt
cnt 可為 複數


注意! T 會有重複:
e.g:
"AA", "ABA", "CCC"


For example,
S = "ADOBECODEBANC"
T = "ABC"
Minimum window is "BANC".


Note:
If there is no such window in S that covers all characters in T,
return the empty string "".

If there are multiple such windows,
you are guaranteed that there will always be
only one unique minimum window in S.
"""


class Solution(object):

    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        * 注意corner cases, i.e index 0, empty t, duplicate t.
        """
        import collections as cc

        # it's a defaultdict with value == 0
        tdict = cc.Counter(t)
        tset = set(t)

        missing = len(t)  # 一旦補滿便是補滿!

        result = [-1, -1]

        mi = 0

        for i, c in enumerate(s):
            if tdict[c] > 0:
                missing -= 1

            tdict[c] -= 1

            change = False

            # 目前char 存在於t
            if c in tset:
                change = True

            # 此c 為一t, 且所有t都已經滿足.
            if change and not missing:
                # 縮緊 把不是t的排除.
                # 也把先前重複的t排除.
                while mi < i and tdict[s[mi]] < 0:
                    tdict[s[mi]] += 1
                    mi += 1

                if result == [-1, -1] or \
                        i - mi < result[-1] - result[0]:
                    result[0] = mi
                    result[1] = i

        return s[result[0]: result[-1] + 1]

    def rewrite(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        * 注意corner cases, i.e index 0, empty t, duplicate t.
        """

def build():
    return "cbdabc", "ab"
    return "bc", "c"
    return "a", "aa"
    return "a", "a"
    return "abaabc", "aac"
    return "ADOBECODEBANC", "ACD"
    return "ADOBEC ODEBANC", "ABC"


if __name__ == "__main__":

    s = Solution()
    result = s.minWindow(*build())

    print(result)
