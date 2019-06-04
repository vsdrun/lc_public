#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/maximum-length-of-pair-chain/description/


You are given n pairs of numbers.
In every pair, the first number is always smaller than the second number.

Now, we define a pair (c, d) can follow another pair (a, b)
iff b < c. Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed.
You needn't use up all the given pairs. You can select pairs in any order.



Example 1:
Input: [[1,2], [2,3], [3,4]]
Output: 2
Explanation: The longest chain is [1,2] -> [3,4]
"""


class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int

        instead of DP's try them all, consider
        smarter move here:
        since each pair has the constrain of s[1] > s[0], thus
        we focus on s[1].
        sort based on s[1] from small to large.
        the smaller s[1] indicates smaller s[0]
        Since we are sorting base on s[1], even though there's
        multiple same s[0], we still guarantee that smaller s[1] is
        considered as lastest end.
        """

        cnt = 1

        pairs.sort(key=lambda x: x[1])

        end = pairs[0][1]

        for i in range(1, len(pairs)):
            if pairs[i][0] > end:
                end = pairs[i][1]
                cnt += 1

        # print(pairs)
        return cnt


def build():
    return [[1, 2], [2, 3], [3, 4]]


if __name__ == "__main__":

    s = Solution()
    print(s.findLongestChain(build()))
