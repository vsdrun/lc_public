#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array, find the smallest missing positive integer.

Example 1:
Input: [1,2,0]
Output: 3


Example 2:
Input: [3,4,-1,1]
Output: 2

Example 3:
Input: [7,8,9,11,12]
Output: 1

Note:
***
Your algorithm should run in O(n) time and uses constant extra space.

https://leetcode.com/problems/first-missing-positive/discuss/17071/My-short-c%2B%2B-solution-O(1)-space-and-O(n)-time
put item in right position.

[3,4,-1,1] right position: [-1, 1, 3, 4]
[-1, 4, 3, 1]
[-1, 1, 3, 4]


class Solution {
public:
    int firstMissingPositive(vector<int>& nums) {
        int n = nums.size();

        for (int i = 0; i < n; i++)
            while (nums[i] > 0 && nums[i] <= n && nums[nums[i] - 1] != nums[i])
                swap(nums[i], nums[nums[i] - 1]);

        for (int i = 0; i < n; i++)
            if (nums[i] != i + 1)
                return i + 1;

        return n + 1;
    }
};
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        [7, 4, -1, 1] ->
        [7, 1, -1, 4] ->
        [1, 7, -1, 4]
        """

        for i in range(len(nums)):
            while nums[i] > 0 and nums[i] <= len(nums) and \
                nums[i] != nums[nums[i] - 1]:
                x = nums[i]
                y = nums[nums[i] - 1]
                nums[i] = y
                nums[x - 1] = x

        for i in range(len(nums)):
            if nums[i] != i + 1:
                return i + 1

        return len(nums) + 1

def build():
    return [1,2,0]
    return [7,4,-1,1]
    return [3,4,-1,1]
    return [7,8,9,11,12]


if __name__ == "__main__":
    s = Solution()
    print(s.firstMissingPositive(build()))
