#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/strobogrammatic-number/description/


A strobogrammatic number is a number that looks the
same when rotated 180 degrees (looked at upside down).

Write a function to determine if a number is strobogrammatic.
The number is represented as a string.

For example, the numbers "69", "88", and "818" are all strobogrammatic.

"""


class Solution(object):
    def isStrobogrammatic(self, num):
        """
        :type num: str
        :rtype: bool
        0 0  不能為第一個.
        1 1
        6 9
        9 6
        8 8
        """
        from __builtin__ import xrange

        dmap = dict((('0', '0'), ('1', '1'), ('6', '9'),
                     ('9', '6'), ('8', '8')))

        if num[0] == '0' and len(num) > 1:
            return False

        if len(num) % 2:
            # corner cases
            if num[len(num) / 2] not in ('0', '1', '8'):
                return False

        for i in xrange(len(num) / 2):
            if num[i] not in dmap or num[~i] != dmap[num[i]]:
                return False
        # -i 保 減 1 去
        return True


def build():
    return '25'
    return '080'


if __name__ == "__main__":
    s = Solution()
    print(s.isStrobogrammatic(build()))
