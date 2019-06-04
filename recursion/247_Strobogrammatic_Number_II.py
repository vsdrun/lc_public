#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/strobogrammatic-number-ii/description/


A strobogrammatic number is a number that looks the same when
rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].
"""


class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        char_dict = dict()
        char_dict['0'] = '0'
        char_dict['1'] = '1'
        char_dict['8'] = '8'
        char_dict['6'] = '9'
        char_dict['9'] = '6'

        def build(i, j, ary):
            result = []
            if i != j:
                for k in char_dict:
                    if i == 0 and k == '0':
                        continue
                    ary[i] = k
                    ary[j] = char_dict[k]
                    result.append(ary[:])
            else:
                ary[j] = '0'
                result.append(ary[:])
                ary[j] = '1'
                result.append(ary[:])
                ary[j] = '8'
                result.append(ary[:])

            return result

        i = 0
        j = n - 1

        result_list = [[None] * n]
        result = []

        while i <= j:
            tmp_result_list = []

            for ll in result_list:
                tmp_result_list.extend(build(i, j, ll))

            result_list = tmp_result_list
            i += 1
            j -= 1

        for ll in result_list:
            result.append("".join(ll))

        return result


def build():
    return 4


if __name__ == "__main__":
    s = Solution()
    print(s.findStrobogrammatic(build()))
