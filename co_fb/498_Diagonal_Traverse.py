#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/diagonal-traverse/

Given a matrix of M x N elements (M rows, N columns),
return all elements of the matrix in diagonal order as shown in the below image.


Example:

Input:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

[
 [ 1, 2, 3 , 10],
 [ 4, 5, 6 , 11],
 [ 7, 8, 9 , 12]
]

Output:  [1,2,4,7,5,3,6,8,9]
"""


class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]

        2 categories
        right -> left down
        no end:
        +r
        +d+l
        end:
        +d
        +d+l

        left -> right up
        no end:
        +d
        +r+u
        end:
        +r
        +r+u
        """
        if not matrix:
            return []

        result = []
        # rule 1 右上左下
        # rule 2 左下右上

        R, C, RL, CL = 0, 0, len(matrix), len(matrix[0])
        rule = 2

        while True:
            if rule == 1:
                if 0 <=  R < RL and 0 <= C < CL:
                    result.append(matrix[R][C])

                    if R + 1 >= RL or C - 1 < 0:
                        rule = 2
                        # 左下不行便先往下
                        if R + 1 >= RL:
                            C += 1
                        else:
                            R += 1
                    else:
                        # 往左下走
                        R += 1
                        C -= 1

                else:
                    break

            if rule == 2:
                if 0 <= R < RL and 0 <= C < CL:
                    result.append(matrix[R][C])

                    if R - 1 < 0 or C + 1 >= CL:
                        rule = 1
                        # 右上不行便右平移
                        if C + 1 >= CL:
                            # 平移不行往下
                            R += 1
                        else:
                            # 平移
                            C += 1
                    else:
                        # 往右上走
                        R -= 1
                        C += 1
                else:
                    break

        return result

def build():
    return []
    return [
         [ 1, 2, 3 , 10],
         [ 4, 5, 6 , 11],
         [ 7, 8, 9 , 12]]
    return [
         [ 1, 2, 3 , 10]]
    return [[1]]
    return [
         [1],
         [2]]
    return [
     [ 1, 2, 3 ],
     [ 4, 5, 6 ],
     [ 7, 8, 9 ]]


if __name__ == "__main__":
    s = Solution()
    print(s.findDiagonalOrder(build()))
