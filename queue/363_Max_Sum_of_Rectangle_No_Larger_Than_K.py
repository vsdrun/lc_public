#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Given a non-empty 2D matrix matrix and an integer k, find the max sum of a
rectangle in the matrix such that its sum is no larger than k.

Example:
Given matrix = [
  [1,  0, 1],
  [0, -2, 3]
]
k = 2

The answer is 2. Because the sum of rectangle [[0, 1], [-2, 3]] is 2 and 2 is
the max number no larger than k (k = 2).

Note:
The rectangle inside the matrix must have an area > 0.
What if the number of rows is much larger than the number of columns?
"""

"""
kadane's algorithm. used to calulate max subarray sum.
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
        import bisect

        def maxSumSublist(vals):
            """
            :param vals: list of row length.
            這是一個連續的曲線.
            """
            maxSum = float('-inf')
            prefixSum = 0

            prefixSums = [float('inf')]

            for val in vals:
                bisect.insort(prefixSums, prefixSum)

                prefixSum += val

                i = bisect.bisect_left(prefixSums, prefixSum - k)

                maxSum = max(maxSum, prefixSum - prefixSums[i])

            return maxSum

        maxSum = float('-inf')

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
