#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
HARD
https://leetcode.com/problems/max-sum-of-rectangle-no-larger-than-k/description/


Given a non-empty 2D matrix matrix and an integer k, find the max sum of a
rectangle in the matrix such that its sum is no larger than k.

Example:
Given matrix = [
  [1,  0, 1],
  [0, -2, 3],
  [10, -12, 13]
]
k = 2

The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is
the max number no larger than k (k = 2).

Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
"""

"""
kadane's algorithm.
https://www.youtube.com/watch?v=yCQN096CwWM
https://goo.gl/5rLQpD
"""


class Solution(object):

    def maxSumSubmatrix(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # 對 sorted list 做 insertion index
        # 同 C++ set.upper_bound/lower_bound
        import bisect

        # kadane's algorithm.
        def maxSumSublist(vals):
            """
            :param vals: list of value in column.
            """
            maxSum = float('-inf')
            prefixSum = 0

            # 這很重要... 如果 prefixSum 遠大於 k, 則
            # prefixSum - k > 所有之前的和，則 i 落在float('inf')
            # 則 prefixSum - float('inf') == float('-inf')
            prefixSums = [float('inf')]

            for val in vals:
                # this will add into prefixSums
                # 一開始將prefixSums 初始化為 [0, float('inf')]
                # *** 注意! 這裡是insert 之前的和!!!
                # 也就是避免摻除中間產生漏洞!
                bisect.insort(prefixSums, prefixSum)

                prefixSum += val

                # 重要! k
                # 如果 目前 和 小於k, 則 i == 0, prefixSums[0] == 0
                i = bisect.bisect_left(prefixSums, prefixSum - k)
                maxSum = max(maxSum, prefixSum - prefixSums[i])

            return maxSum

        # local max.
        maxSum = float('-inf')

        # 將columes 萃取出來.
        # [1,2,3] [4,5,6] => [1,4], [2,5], [3,6]
        columns = zip(*matrix)

        # Kadane's algorithm find max sub matrix in matrix
        for left in range(len(columns)):
            """
            rowSums:
            _
            _
            _
            _
            """
            # 初始化為0
            rowSums = [0] * len(matrix)

            for column in columns[left:]:
                rowSums = map(int.__add__, rowSums, column)
                # 以maxSumSublist來處理 max sub array in array.
                maxSum = max(maxSum, maxSumSublist(rowSums))

        return maxSum


def build_input():
    m = [[1, 0, 1],
         [0, -2, 3]]
    return m


if __name__ == "__main__":
    n = build_input()

    s = Solution()
    result = s.maxSumSubmatrix(n, 2)

    # 91
    print(result)
