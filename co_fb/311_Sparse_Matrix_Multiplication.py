#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/sparse-matrix-multiplication/description/

Given two sparse matrices A and B, return the result of AB.

You may assume that A's column number is equal to B's row number.


Example:

A = [
  [ 1, 0, 0],
  [-1, 0, 3]
]

B = [
  [ 7, 0, 0 ],
  [ 0, 0, 0 ],
  [ 0, 0, 1 ]
]


     |  1 0 0 |   | 7 0 0 |   |  7 0 0 |
AB = | -1 0 3 | x | 0 0 0 | = | -7 0 3 |
                  | 0 0 1 |
"""


class Solution(object):
    def multiply(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]

        思考重點:
        1. row 全部為0的skip
        2. col 部份為0的skip, 全部為0的skip
        3. row 無法部份為0的skip 因為需要有一個anchor 基準點來process
        這裡我們用col 也就是，col的index將對應到row的index
        若row的index值為0 則必須process.
        """
        tighten_cols = [[(i, val) for i, val in enumerate(col) if val]
                        for col in zip(*B)]  # 先跑.

        AA = []

        for row in A:
            # 空的row
            if not any(row):
                AA.append([])
            else:
                AA.append(row)

        result = []

        for row in AA:
            if not row:
                result.append([0] * len(B[0]))
                continue

            tmp_row = []

            for c in tighten_cols:
                tmp_row.append(sum([row[i] * val for i, val in c]))

            result.append(tmp_row)

        return result


def build():
    A = [
        [1, 0, 0],
        [0, 0, 0],
        [-1, 0, 3]
    ]

    B = [
        [7, 0, 0],
        [0, 0, 0],
        [0, 0, 1]
    ]

    return A, B


if __name__ == "__main__":

    s = Solution()
    result = s.multiply(*build())

    print(result)
