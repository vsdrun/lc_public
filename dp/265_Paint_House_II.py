#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/paint-house-ii/

There are a row of n houses,
each house can be painted with one of the k colors.
The cost of painting each house with a certain color is different.
You have to paint all the houses such that
no two adjacent houses have the same color.

The cost of painting each house with a certain color is represented by
a n x k cost matrix.

For example, costs[0][0] is the cost of painting house 0 with color 0;
costs[1][2] is the cost of painting house 1 with color 2, and so on...
Find the minimum cost to paint all houses.

Note:
All costs are positive integers.

Example:

Input: [[1,5,3],[2,9,4]]
Output: 5
Explanation:
Paint house 0 into color 0, paint house 1 into color 2.
Minimum cost: 1 + 4 = 5;
Or paint house 0 into color 2, paint house 1 into color 0.
Minimum cost: 3 + 2 = 5.

Follow up:
Could you solve it in O(nk) runtime?
"""

class Solution(object):
    def minCostII(self, costs):
        """
        :type costs: List[List[int]]
        :rtype: int
        """
        if not costs:
            return 0

        n= len(costs)
        k = len(costs[0])

        for i in xrange(1, n):
            # 前一個house最小
            min1 = min(costs[i-1])

            idx = costs[i-1].index(min1)
            # 前一個house次小
            min2 = min(costs[i-1][:idx] + costs[i-1][idx+1:])

            for j in xrange(k):
                if j == idx:
                    # 此house的這個顏色為之前選過的, 加上上一個次小的
                    costs[i][j] += min2
                else:
                    # 此house不能選之前的 故選此時的價值加上之前最小值
                    costs[i][j] += min1

        return min(costs[-1])


def build():
    return [[7, 6, 2], [3, 9, 3]]


if __name__ == "__main__":

    s = Solution()
    print(s.minCostII(build()))
