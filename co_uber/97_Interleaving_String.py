#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/interleaving-string/

Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true

Example 2:
Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

as BFS
https://leetcode.com/problems/interleaving-string/discuss/31948/8ms-C%2B%2B-solution-using-BFS-with-explanation
"""

class Solution(object):
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        TLE...
        Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
        """
        if len(s1) + len(s2) != len(s3):
            return False

        def recursive(lidx, flip, s1, s2):
            if lidx == len(s3):
                return True

            #  print("------")
            #  print("s3: {}".format(s3))
            #  print("lidx: {}, flip: {}, s1: {}, s2: {}".format(
                #  lidx, flip, s1, s2))

            for ridx in range(lidx + 1, len(s3) + 1):
                if not flip:
                    if s3[lidx: ridx] == s1[:len(s3[lidx: ridx])]:
                        #  print("s3: {} s1: {} s2: {} flip: {}".format(
                            #  s3[lidx: ridx], s1, s2, flip))

                        ret = recursive(
                                ridx,
                                flip ^ True,
                                s1[len(s3[lidx: ridx]):],
                                s2)
                        if ret:
                            return True
                    else:
                        #  print("False")
                        return False
                else:
                    if s3[lidx: ridx] == s2[:len(s3[lidx: ridx])]:
                        #  print("s3: {} s1: {} s2: {} flip: {}".format(
                            #  s3[lidx: ridx], s1, s2, flip))
                        ret = recursive(
                                ridx,
                                flip ^ True,
                                s1,
                                s2[len(s3[lidx: ridx]):])
                        if ret:
                            return True
                    else:
                        #  print("False")
                        return False

            return False

        return recursive(0, False if s1 else True, s1, s2) or \
                recursive(0, True if s2 else False, s1, s2)

def build():
    return "aa", "ab", "abaa"
    return "", "b", "b"
    return "b", "", "b"
    return "aabcc", "dbbca", "aadbbbaccc"
    return "aabca", "dbbcc", "aadbbcbcca" # aa db bc bc a c


if __name__ == "__main__":
    s = Solution()
    print(s.isInterleave(*build()))
