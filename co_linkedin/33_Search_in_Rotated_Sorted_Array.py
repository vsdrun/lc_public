#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/search-in-rotated-sorted-array/description/


Suppose an array sorted in ascending order is rotated at some
pivot unknown to you beforehand.

(i.e., 0 1 2 4 5 6 7 might become 4 5 6 7 0 1 2).

You are given a target value to search.
If found in the array return its index, otherwise return -1.

You may assume no duplicate exists in the array.

discuss:
https://leetcode.com/problems/search-in-rotated-sorted-array/discuss/14435/Clever-idea-making-it-simple
"""


class Solution(object):

    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        BEST
        """
        # 注意右邊是 exclusive
        l,r=0,len(nums)

        while l<r:
            mid=(l+r)/2

            if target < nums[0] < nums[mid]:
                l = mid + 1
            # 注意等於
            elif target >= nums[0] > nums[mid]:
                r = mid

            # 沒有等於
            elif nums[mid] < target:
                l = mid + 1

            # 沒有等於
            elif nums[mid] > target:
                r = mid

            # 最後回傳...
            else:
                return mid

        return -1

def build():
    return [4, 5, 6, 7, 0, 1, 2], 5
    return [7, 8, 1, 3], 3  # wrong
    return [1, 3], 3  # wrong
    return [8,9,2,3,4], 9
    return [], 5
    return [4,5,6,7,0,1,2], 0
    return [3, 1], 3
    return [4, 5, 6, 7, 0, 1, 2], 3
    return [3, 1], 1
    return [4, 5, 6, 7, 0, 1, 2], 5
    return [3, 1], 2
    return [1], 1
    return [4, 5, 6, 7, 0, 1, 2], 8


if __name__ == "__main__":

    s = Solution()
    result = s.search(*build())
    print(result)
