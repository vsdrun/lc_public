#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/maximal-square/description/

Given a 2D binary matrix filled with 0's and 1's,
find the largest square containing only 1's and return its area.


For example, given the following matrix:

1 0 1 0 0
1 0 1 1 1
1 1 1 1 1
1 0 0 1 0
Return 4.

https://leetcode.com/problems/maximal-square/discuss/61935/6-lines-Visual-Explanation-O(mn)

above  above-left  left

 1111     1111
 1111     1111     1111
 1111     1111     1111
 1111     1111     1111
    *         *    1111*
"""


class Solution(object):
    def maximalSquare(self, A):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        for i, r in enumerate(A):
            r = A[i] = map(int, r)

            for j, c in enumerate(r):

                if i * j * c:  # 重要!
                    r[j] = min(A[i - 1][j], r[j - 1], A[i - 1][j - 1]) + 1
        print(A)
        return max(map(max, A + [[0]])) ** 2  # + [[0]] 因為A可以為 []

    def rewrite(self, A):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # DP, buttom-up approach
        # 檢查 此 node 之 上, 左, 左上對角線的值. 並且取以上三點最小 + 1
        # 為此 node 之 新值.

        # 開始traverse每一個點, row by row

        for ri, r in enumerate(A):

            for ci, c in enumerate(r):

                A[ri][ci] = int(c)
                c = A[ri][ci]

                # 使用聰明的方法避開processing row 0 與 col 0 與 值為 0 的c
                # 即 ri * ci * c
                if ri * ci * c:
                    # 檢查 左, 上, 左上 的值
                    # 並且update c 為 min(左, 上, 左上) + 1
                    r[ci] = min(r[ci - 1], A[ri - 1][ci], A[ri - 1][ci - 1]) + \
                        1

        # 最後 traverse 整個update過後的 A, 找最大值的square返回

        if A:
            return max([max(r) for r in A]) ** 2
        return 0


def build():
    return [[1, 0, 1, 0, 0],
            [1, 0, 1, 1, 1],
            [1, 1, 1, 1, 1],
            [1, 0, 0, 1, 0]]


if __name__ == "__main__":

    s = Solution()
    print(s.maximalSquare(build()))
    print(s.rewrite(build()))
