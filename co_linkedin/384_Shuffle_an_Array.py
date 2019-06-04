#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
https://leetcode.com/problems/shuffle-an-array/

Shuffle a set of numbers without duplicates.

Example:

// Init an array with set 1, 2, and 3.
int[] nums = {1,2,3};
Solution solution = new Solution(nums);

// Shuffle the array [1,2,3] and return its result.
// Any permutation of [1,2,3] must equally likely to be returned.
solution.shuffle();

// Resets the array back to its original configuration [1,2,3].
solution.reset();

// Returns the random shuffling of array [1,2,3].
solution.shuffle();
"""

import random

class Solution(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.nums = nums


    def reset(self):
        """
        Resets the array to its original configuration and return it.
        :rtype: List[int]
        """
        return self.nums


    def shuffle(self):
        """
        Returns a random shuffling of the array.
        :rtype: List[int]
        """
        ans = self.nums[:]                     # copy list

        for i in range(len(ans)-1, 0, -1):     # start from end
            j = random.randrange(0, i+1)    # generate random index
            ans[i], ans[j] = ans[j], ans[i]    # swap

        return ans



# Your Solution object will be instantiated and called as such:
# obj = Solution(nums)
# param_1 = obj.reset()
# param_2 = obj.shuffle()

if __name__ == "__main__":

    s = Solution([1,2,3])
    print(s.shuffle())
    print(s.shuffle())
    print(s.shuffle())
    print(s.shuffle())
    print(s.shuffle())
    print(s.shuffle())
    print(s.shuffle())
    print(s.shuffle())
    s.reset()
