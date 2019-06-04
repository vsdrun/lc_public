#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/split-array-largest-sum/description/

Given an array which consists of non-negative integers and an integer m,
you can split the array into m non-empty !!continuous subarrays!!

NOT SORTED!

Write an algorithm to minimize the largest sum among these m subarrays.

Note:
If n is the length of array, assume the following constraints are satisfied:

1 ≤ n ≤ 1000
1 ≤ m ≤ min(50, n)


Examples:
Input:
nums = [7,2,5,10,8]
m = 2

Output:
18

Explanation:
There are four ways to split nums into two subarrays.
The best way is to split it into [7,2,5] and [10,8],
where the largest sum among the two subarrays is only 18.

https://leetcode.com/problems/split-array-largest-sum/discuss/89821/Python-solution-dp-and-binary-search
https://leetcode.com/problems/split-array-largest-sum/discuss/89846/Python-solution-with-detailed-explanation
"""


class Solution(object):
    def splitArray(self, nums, m):
        """
        :type nums: List[int]
        :type m: int
        :rtype: int
        """
        def valid(mid):
            cnt = 0
            current = 0

            for n in nums:
                current += n

                if current > mid:
                    cnt += 1

                    if cnt >= m:
                        return False

                    # 下一半由 n 開始累加, 因為加了 n 超過 mid 了!
                    current = n

            return True

        # 找 range 最大 - 總和.
        # 其中sub array的 和 最小 一定在此 range 內.
        low = max(nums)  # 任何值加上最大均超過最大
        high = sum(nums)

        while low < high:  # 注意 為 <...
            # 使用binary search.
            mid = low + (high - low) / 2

            if valid(mid):  # mid 符合 m 的條件 因為要找最小的和 故設為上限.
                high = mid
            else:  # mid 太小了 造成 > m,  設定low 為low bound.
                low = mid + 1

        return low


def build():
    return [7, 2, 5, 10, 8], 2


if __name__ == "__main__":

    s = Solution()
    result = s.splitArray(*build())
    print(result)
