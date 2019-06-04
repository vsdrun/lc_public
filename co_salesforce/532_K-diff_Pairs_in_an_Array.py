#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/k-diff-pairs-in-an-array/

Given an array of integers and an integer k,
you need to find the number of unique k-diff pairs in the array.
Here a k-diff pair is defined as an integer pair (i, j),
where i and j are both numbers in the array and their absolute difference is k.

Example 1:
Input: [3, 1, 4, 1, 5], k = 2
x - y = +-2
x +- 2 = y
Output: 2
Explanation:
There are two 2-diff pairs in the array, (1, 3) and (3, 5).
Although we have two 1s in the input,
we should only return the number of unique pairs.

Example 2:
Input:[1, 2, 3, 4, 5], k = 1
Output: 4
Explanation:
There are four 1-diff pairs in the array, (1, 2), (2, 3), (3, 4) and (4, 5).

Example 3:
Input: [1, 3, 1, 5, 4], k = 0
Output: 1
Explanation: There is one 0-diff pair in the array, (1, 1).

Note:
The pairs (i, j) and (j, i) count as the same pair.
The length of the array won't exceed 10,000.
All the integers in the given input belong to the range: [-1e7, 1e7].
"""

class Solution(object):
    def findPairs(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if k < 0:
            return 0

        dset = set()
        cnt = set()

        for i in range(len(nums)):
            pexpect = nums[i] + k
            mexpect = nums[i] - k

            if pexpect in dset:
                cnt.add(tuple(sorted([nums[i]] + [pexpect])))

            if mexpect in dset:
                cnt.add(tuple(sorted([nums[i]] + [mexpect])))

            dset.add(nums[i])

        return len(cnt)

    def rewrite(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        count = 0
        s = set(nums)

        if k < 0:
            return(0)
        elif k == 0:
            for i in s:
                # 重複只有在 k == 0 時有意義
                if nums.count(i) > 1:
                    count += 1
            return(count)
        elif k > 0:
            for i in s:
                # 避免算入重複的值, 因為我們用 s=set()
                if i+k in s:
                    count += 1
        return(count)

def build():
    return [1,3,1,5,4], 0 # 1
    return [1,2,3,4,5], -1 # 0
    return [3,1,4,1,5], 2 # 2
    return [1, 2, 3, 4, 5], 1 # 4
    return [1,1,1,1,1], 0 # 1


if __name__ == "__main__":
    s = Solution()
    print(s.findPairs(*build()))
