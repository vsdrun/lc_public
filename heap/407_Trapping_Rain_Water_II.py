#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/trapping-rain-water-ii/description/

Given an (m x n) matrix of positive integers representing the height of each
unit cell in a 2D elevation map,
compute the volume of water it is able to trap after raining.


Note:
Both m and n are less than 110.
The height of each unit cell is greater than 0 and is less than 20,000.


Example:
Given the following 3x6 height map:
[
  [1,4,3,1,3,2],
  [3,2,1,3,2,4],
  [2,3,3,2,3,1]
]
Return 4.
"""


class Solution(object):
    def trapRainWater(self, heightMap):
        """
        :type heightMap: List[List[int]]
        :rtype: int
        """
        if not heightMap or not heightMap[0]:
            return 0

        import heapq

        m, n = len(heightMap), len(heightMap[0])

        heap = []

        # 要有visited 紀錄走過得路徑.
        visited = [[0] * n for _ in range(m)]

        # Push all the block on the border into heap
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i == m - 1 or j == n - 1:
                    # (value, location, i.e i, j)
                    heapq.heappush(heap, (heightMap[i][j], i, j))
                    visited[i][j] = 1

        result = 0

        # get the smallest first, which rule out the higher border contributes
        # larger result.

        """
        由最小的邊界開始.
        也就是，此邊界不會累積水, 且比之高的邊界我們可以rule out,
        以此小的邊界為主累積水.

        1. heapq 由小的開始意義重大...
            確保 小的 hight 為主導...
        2. 將 小的 以 大的填滿.
        """

        while heap:
            height, i, j = heapq.heappop(heap)

            for x, y in ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)):

                if 0 <= x < m and 0 <= y < n and not visited[x][y]:

                    result += max(0, height - heightMap[x][y])

                    heapq.heappush(heap, (max(heightMap[x][y], height), x, y))

                    visited[x][y] = 1

        return result


def build_matrix():
    matrix = [
        [1, 4, 3, 1, 3, 2],
        [3, 2, 1, 3, 2, 4],
        [2, 3, 3, 2, 3, 1]
    ]
    return matrix


if __name__ == "__main__":
    m = build_matrix()

    s = Solution()
    result = s.trapRainWater(m)
    # 4
    print(result)
