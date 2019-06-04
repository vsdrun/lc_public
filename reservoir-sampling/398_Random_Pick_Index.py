#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/random-pick-index/description/

Given an array of integers with possible duplicates,
randomly output the index of a given target number.
You can assume that the given target number must exist in the array.

Note:
The array size can be very large.
Solution that uses too much extra space will not pass the judge.

Example:
int[] nums = new int[] {1,2,3,3,3};
Solution solution = new Solution(nums);

// pick(3) should return either index 2, 3, or 4 randomly.
// Each index should have equal probability of returning.
solution.pick(3);

// pick(1) should return 0. Since in the array only nums[0] is equal to 1.
solution.pick(1);
"""


class Solution(object):

    def __init__(self, nums):
        self.nums = nums

    def pick(self, target):
        import random
        return random.choice([k for k, v in enumerate(self.nums) if v ==
                              target])
# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.pick(target)


def build():
    return [1, 2, 3, 3, 3, 3, 4, 5, 5, 5, 7, 7, 7]


if __name__ == "__main__":

    s = Solution(build())
    print(s.pick(3))
