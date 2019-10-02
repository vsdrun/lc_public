#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/description/
reference:
https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/


Given an array nums and a target value k,
find the maximum length of a subarray that sums to k.
If there isn't one, return 0 instead.


Note:
The sum of the entire nums array is guaranteed to fit
within the 32-bit signed integer range.

連續的sum, 想到 sum 可以accumulate!

Example 1:
Given nums = [1, -1, 5, -2, 3], k = 3,
return 4. (because the subarray [1, -1, 5, -2] sums to 3 and is the longest)

Example 2:
Given nums = [-2, -1, 2, 1], k = 1,
return 2. (because the subarray [-1, 2] sums to 1 and is the longest)


Follow Up:
Can you do it in O(n) time?
"""


class Solution(object):
    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        import bisect as bi

        total = 0

        # 做 BST 故設定boundary.
        presum = [(0, 0), (float('inf'), 0)]
        mx = 0

        for c, n in enumerate(nums):
            total += n
            bi.insort(presum, (total, c))

            if total == k:
                mx = max(mx, c + 1)
            else:
                i = bi.bisect_left(presum, (total - k, float('-inf')))

                if total - presum[i][0] == k:
                    preindex = presum[i][1]
                    mx = max(mx, c - preindex)

        return mx


class Solution_2(object):
    # better.
    """
    將每個和都hashtable起來. 不要用 BST.
    """

    def maxSubArrayLen(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        ans, acc = 0, 0  # answer and the accumulative value of nums
        mp = {0: -1}  # key is acc value, and value is the index

        for i in xrange(len(nums)):
            acc += nums[i]

            if acc not in mp:
                mp[acc] = i  # 只存最早出現的 因為要最長...
                # 如果要找最短 則每個最近的都update!

            # 太聰明 直接看有沒有在dict裡面~
            if acc - k in mp:
                ans = max(ans, i - mp[acc - k])

        return ans


def build():
    return [], 0
    return [-2, -1, 2, 1], 1
    return [1, -1, 5, -2, 3], 3


if __name__ == "__main__":

    s = Solution()
    result = s.maxSubArrayLen(*build())
    print(result)

    s = Solution_2()
    result = s.maxSubArrayLen(*build())
    print(result)
