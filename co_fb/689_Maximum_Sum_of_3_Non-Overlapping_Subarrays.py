#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/description/

In a given array nums of positive integers,
find three non-overlapping subarrays with maximum sum.

Each subarray will be of size k, and we want to maximize the
sum of all 3*k entries.

Return the result as a list of indices representing the starting position
of each interval (0-indexed).
If there are multiple answers, return the lexicographically smallest one.


Example:
Input: [1,2,1,2,6,7,5,1], 2
Output: [0, 3, 5]

Explanation: Subarrays [1, 2], [2, 6], [7, 5] correspond to the starting indices [0, 3, 5].
We could have also taken [2, 1], but an answer of [1, 3, 5] would be lexicographically larger.

Note:
nums.length will be between 1 and 20000.
nums[i] will be between 1 and 65535.
k will be between 1 and floor(nums.length / 3).

https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/discuss/108231/C++Java-DP-with-explanation-O(n)
https://leetcode.com/problems/maximum-sum-of-3-non-overlapping-subarrays/discuss/108238/Python-o(n)-time-o(1)-space.-Greedy-solution.
"""


class Solution(object):
    def maxSumOfThreeSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        1. seq1Sum, seq2Sum, seq3Sum
        2. seq1Index, seq2Index, seq3Index
        3. best1Sum, best2Sum, best3Sum
        """
        seq1Index = 0
        seq2Index = k
        seq3Index = 2 * k
        seq4Index = 3 * k

        seq1Sum = sum(nums[seq1Index:seq2Index])
        #  seq2Sum = sum(nums[k:2 * k])
        #  seq3Sum = sum(nums[2 * k:3 * k])
        seq2Sum = sum(nums[seq2Index:seq3Index])
        seq3Sum = sum(nums[seq3Index:seq4Index])

        # 作為比較條件
        best1Sum = seq1Sum
        best2Sum = seq1Sum + seq2Sum
        best3Sum = seq1Sum + seq2Sum + seq3Sum

        # 各前進一個
        seq1Index += 1
        seq2Index += 1
        seq3Index += 1

        # 重要! const
        best1Index = 0,
        best2Index = best1Index + (k,)
        best3Index = best2Index + (2 * k,)

        while seq3Index <= len(nums) - k:
            # 勿用sum 會很慢~~~
            # 前進一個的和
            seq1Sum = seq1Sum - nums[seq1Index - 1] + \
                nums[seq1Index + k - 1]

            if seq1Sum > best1Sum:
                # 連動!
                best1Index = seq1Index,
                best1Sum = seq1Sum

            # 前進一個的和
            seq2Sum = seq2Sum - nums[seq2Index - 1] + \
                nums[seq2Index + k - 1]

            # 如果沒有 > best2Sum也不會蓋掉之前的best1Index因為!!
            # best2Index內的index為舊的best1Index :-)
            # !! 注意 我們是看總體和!
            if best1Sum + seq2Sum > best2Sum:
                # 連動!
                best2Index = best1Index + (seq2Index,)
                best2Sum = best1Sum + seq2Sum

            # 前進一個的和
            seq3Sum = seq3Sum - nums[seq3Index - 1] + \
                nums[seq3Index + k - 1]

            if best2Sum + seq3Sum > best3Sum:
                best3Index = best2Index + (seq3Index,)
                best3Sum = best2Sum + seq3Sum

            seq1Index += 1
            seq2Index += 1
            seq3Index += 1

        return list(best3Index)

    def rewrite(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        1. seq1Sum, seq2Sum, seq3Sum
        2. seq1Index, seq2Index, seq3Index
        3. best1Sum, best2Sum, best3Sum
        Input: [1,2,1,2,6,7,5,1], 2
        Output: [0, 3, 5]
        """
        if not nums or not k:
            return []

        a_idx = 0
        b_idx = 1 * k
        c_idx = 2 * k
        d_idx = 3 * k

        # moving index
        a_sum = sum(nums[a_idx:b_idx])
        b_sum = sum(nums[b_idx:c_idx])
        c_sum = sum(nums[c_idx:d_idx])

        # only update iff current sum is larger then previous sum
        at_sum = a_sum
        bt_sum = a_sum + b_sum
        ct_sum = a_sum + b_sum + c_sum

        # only update iff current sum is larger then previous sum
        besta_idx = (a_idx,)
        bestb_idx = besta_idx + (b_idx,)
        bestc_idx = bestb_idx + (c_idx,)

        # 重要! 不然 a_idx - 1 = -1, 則 nums[-1] 為最後一個值
        a_idx += 1
        b_idx += 1
        c_idx += 1


        while c_idx <= len(nums) - k:
            a_sum = a_sum - nums[a_idx - 1] + nums[a_idx + k - 1]

            if a_sum > at_sum:
                besta_idx = (a_idx,)
                at_sum = a_sum

            b_sum = b_sum - nums[b_idx - 1] + nums[b_idx + k - 1]
            # 不能單獨只看 b_sum, 要連a_sum一起考慮
            # 才不會step to previous a_sum's toe
            if b_sum + at_sum > bt_sum:
                bestb_idx = besta_idx + (b_idx,)
                bt_sum = b_sum + at_sum

            c_sum = c_sum - nums[c_idx - 1] + nums[c_idx + k - 1]

            if c_sum + bt_sum > ct_sum:
                bestc_idx = bestb_idx + (c_idx,)
                ct_sum = c_sum + bt_sum

            a_idx += 1
            b_idx += 1
            c_idx += 1

        return list(bestc_idx)


def build():
    return [1,2,1,2,6,7,5,1], 2
    return [7, 13, 20, 19, 19, 2, 10, 1, 1, 19], 3  # [1,4,7]
    return [1, 2, 1, 2, 6, 7, 5, 1], 2


if __name__ == "__main__":

    s = Solution()
    print(s.maxSumOfThreeSubarrays(*build()))
    print(s.rewrite(*build()))
