#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/search-in-rotated-sorted-array-ii/description/

Suppose an array sorted in ascending order is rotated at some pivot
unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search.
If found in the array return true, otherwise return false.

Example 1:
Input: nums = [2,5,6,0,0,1,2], target = 0
Output: true

Example 2:
Input: nums = [2,5,6,0,0,1,2], target = 3
Output: false

Follow up:
This is a follow up problem to Search in Rotated Sorted Array,
where nums may contain duplicates.
Would this affect the run-time complexity? How and why?
"""


class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        bisect: 注意!! [)
        """

        l, r = 0, len(nums)-1

        while l <= r:
            mid = (l + r) / 2

            if nums[mid] == target:
                return True

            if nums[mid] == nums[l]:
                # 吃掉相同的...
                l += 1
            elif nums[mid] > nums[l]:
                if nums[l] <= target < nums[mid]:
                    r = mid - 1
                else:
                    l = mid + 1
            elif nums[mid] <= nums[r]:
                if nums[mid] < target <= nums[r]:
                    l = mid + 1
                else:
                    r = mid - 1

        return False

    def fuck(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        bisect: 注意!! [)
        """
        import bisect as bi
        t = target

        # [1, 3, 1, 1], 3
        class Find(object):
            def __getitem__(self, idx):
                print("m idx:{}".format(idx))
                if t >= nums[0]:
                    if nums[0] <= nums[idx]:
                        # 額外check 因為:
                        # [3,3,0,1,3], 1
                        if max(nums[0:idx] if idx != 0 else nums[0:idx + 1]) > nums[idx]:
                            return float("inf")
                        else:
                            return nums[idx]
                    else:
                        return float("inf")
                else:  # t < nums[0]
                    # [3,3,0,1,3], 1
                    # [1,1,1,1,1,3,1,1,1,1], 3
                    if nums[0] <= nums[idx]:
                        if max(nums[0:idx] if idx != 0 else nums[0:idx + 1]) < nums[idx]:
                            return float("-inf")

                    return nums[idx]

        idx = bi.bisect_left(Find(), t, 0, len(nums))

        if idx < len(nums) and nums[idx] == t:
            return True
        else:
            return False

def build():
    return [3, 1], 1
    return [3, 1], 0
    return [1,1,1,1,1,3,1,1,1,1], 3
    return [1, 3, 1, 1], 3
    return [3,3,0,1,3], 1

    return [3, 1], 3
    return [2,5,6,0,0,1,2], 3
    return [2,5,6,0,0,1,2], 0
    return [1], 1
    return [1,3], 1

if __name__ == "__main__":

    s = Solution()
    print(s.search(*build()))
    print(s.fuck(*build()))
