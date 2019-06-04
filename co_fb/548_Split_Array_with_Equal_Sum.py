#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/split-array-with-equal-sum/

Given an array with n integers, you need to find if there are triplets
(i, j, k) which satisfies following conditions:
i, j, k 為 index, n 為實數

1.
0 < i,
i + 1 < j,
j + 1 < k < n - 1

2. Sum of subarrays
(0, i - 1),
(i + 1, j - 1),
(j + 1, k - 1) and
(k + 1, n - 1) should be equal. 即不包含i, j, k, 以上為exclusive.

條件最小長度:
0 1 2 3 4 5 6
  i   j   k

where we define that subarray (L, R) represents a slice of the original array
starting from the element indexed L to the element indexed R.


Example:
Input: [1,2,1,2,1,2,1]
Output: True

Explanation:
i = 1, j = 3, k = 5.
sum(0, i - 1) = sum(0, 0) = 1
sum(i + 1, j - 1) = sum(2, 2) = 1
sum(j + 1, k - 1) = sum(4, 4) = 1
sum(k + 1, n - 1) = sum(6, 6) = 1


Note:
1 <= n <= 2000.
Elements in the given array will be in range [-1,000,000, 1,000,000].


[a b c d e f g h]
[  i   j   k    ]
"""



class Solution(object):
    def splitArray(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        [a b c d e f g h]
        [  i   j   k    ]

        devide and conquer 概念
        有三個pivot. 以中間那個為主要pivot來移動
        """
        ll = len(nums)
        # input 最小長度檢查
        if ll < 7:
            return False

        def subq(subnum):
            """
            算右的和 與 左的和 左的和的upper boundary為主要for loop的 i
            """
            # accumulate
            for i in range(1, len(subnum)):
                subnum[i] += subnum[i-1]

            # create set of number which left == right
            result = set(
                    subnum[i-1]
                    for i in range(1, len(subnum) - 1)
                        if subnum[i-1] == subnum[-1] - subnum[i]
                )

            return result

        # 1 1 1 1 1 1 1 1
        #   i   j   k

        #  1.
        #  0 < i,
        #  i + 1 < j,
        #  j + 1 < k < n - 1

        #  2. Sum of subarrays
        #  (0, i - 1),
        #  (i + 1, j - 1),
        #  (j + 1, k - 1) and
        #  (k + 1, n - 1) should be equal. 即不包含i, j, k, 以上為exclusive.

        # 由中間為pivot
        for i in range(3, ll - 3):
            left = subq(nums[:i])
            right = subq(nums[i+1:])

            if left & right:
                return True

        return False




def build():
    return [1, 2, 1, 2, 1, 2, 1]


if __name__ == "__main__":
    s = Solution()
    print(s.splitArray(build()))
