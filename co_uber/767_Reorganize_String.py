#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/reorganize-string/

Given a string S,
check if the letters can be rearranged so that two characters that are
adjacent to each other are not the same.

If possible, output any possible result.
If not possible, return the empty string.

Example 1:
Input: S = "aab"
Output: "aba"

Example 2:
Input: S = "aaab"
Output: ""

Note:
S will consist of lowercase letters and have length in range [1, 500].


explain:
Say we were given input AAAA BBBB CCCC DDD EEE FF GG HH JJ KK, and N = 1.

We can start creating a schedule. A, B, and C occur the most times,
so let’s place them first.
We have to make each task of the same type N = 6 spaces apart.

(A _ )(A _ )(A _ )A _ _
 A B   A B   A B  A B C


example 2:
AAAB

ABAXA
"""


class Solution(object):
    def reorganizeString(self, S):
        """
        :type S: str
        :rtype: str
        AAAB
        ((most count - 1) * (N + 1)) + Counted value <= len(S), OK.
        ((most count - 1) * (N + 1)) + Counted value > len(S), Doomed.
        """
        N = len(S)
        tmp_list = []

        for char in set(S):
            counts = S.count(char)
            # 以 621 題目的角度來看.
            # aaacc -> acaca
            # aaab -> 4 + 1 = 5 -> abaa
            # (mostCount - 1) * 2 + count(mostCount) > len(S) 死.
            # (mostCount) * 2 > len(S) + 1 死.
            # (mostCount) > (len(S) + 1) / 2 死.
            # counts * 2 > N+1
            # aaa -> 3 * 2 = 6 a_a_a_
            if counts > (N+1)/2:
                return ""

            tmp_list.append(counts*char)

        print("tmp_list: {}".format(tmp_list))
        # small -> large length
        tmp_list = sorted(tmp_list, key = len)
        tmp_S = "".join(tmp_list)
        print("tmp_S: {}".format(tmp_S))

        ans = [0]*N

        ans[::2] = tmp_S[N/2:]
        print(ans)

        ans[1::2] = tmp_S[:N/2]
        print(ans)

        return "".join(ans)

def check(ss):
    for i in range(1, len(ss)):
        if ss[i] == ss[i-1]:
            print("i: {}, c: {}".format(i, ss[i]))


chk = "hthththththththththththththththththththththththththththncmncncncncncncncncncncncncncncncncncncncncncncncnmnmpkmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpmpkxkxkxkxkxkxkxkxkxkxkxkxkxkxkxkxkxkxkxkxaexaeiaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeaeioioioioioioioioioioioioioioioioioioiobjobjybjbjbjbjbjbjbjbjbjbjbjbjbjbjbjbjbyzfyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzyzfqzfqrfqfqfqfqfqfqfqfqfqfqfqfqfqfqrdqrdgrdrdrdrdrdrdrdrdrdrdrdrdrdrdgsgsgsgsgsgsgsgsgsgsgsgsgsgsgswvswvlwvwvwvwvwvwvwvwvwvwvwvwvwlulululululululululululu"

def build():
    return "aaabb"
    return "cbbaaaa"
    return "aaabbc"
    return "aaaabbbbcccddeef"
    return "vvvlo"  # vlovv


if __name__ == "__main__":
    #  check(chk)
    s = Solution()
    print(s.reorganizeString(build()))
