#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/count-of-smaller-numbers-after-self/description/

You are given an integer array nums and you have to return a new counts array.
The counts array has the property where counts[i] is the number
of smaller elements to the right of nums[i].

Example:

Input: [5,2,6,1]
Output: [2,1,1,0]

Explanation:
To the right of 5 there are 2 smaller elements (2 and 1).
To the right of 2 there is only 1 smaller element (1).
To the right of 6 there is 1 smaller element (1).
To the right of 1 there is 0 smaller element.
"""


class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        def sort(enum):
            half = len(enum) / 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len(enum))[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smaller[left[-1][0]] += len(right)
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum
        smaller = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smaller

    def rewrite(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        """
        想法: 用merge sort
        """
        result = [0] * len(nums)

        def msort(enum):
            half = len(enum) / 2

            if half:
                left = msort(enum[:half])
                right = msort(enum[half:])

                for idx in range(len(enum))[::-1]: # (4,3,2,1,0)
                    if (not right) or (left and left[-1][1] > right[-1][1]):
                        result[left[-1][0]] += len(right)
                        enum[idx] = left.pop()
                    else:
                        enum[idx] = right.pop()

            return enum

        msort(list(enumerate(nums)))  # [(0, 3),(1,7),...]

        return result


def build():
    return [-1,-1]
    return [5,2,6,1]


if __name__ == "__main__":

    s = Solution()
    print(s.countSmaller(build()))
    print(s.rewrite(build()))
