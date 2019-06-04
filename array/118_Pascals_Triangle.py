#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/pascals-triangle/description/


Given a non-negative integer numRows,
generate the first numRows of Pascal's triangle.


In Pascal's triangle,
each number is the sum of the two numbers directly above it.

Example:

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""


class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        from __builtin__ import xrange

        nr = numRows
        base = [1]
        result = []

        def gen(bb, nr):
            if nr >= 1:
                result.append(bb)
                tmp_result = []

                bb = [0] + bb

                for i in xrange(0, len(bb)):
                    tmp_result.append(sum(bb[i: i + 2]))

                nr -= 1
                gen(tmp_result, nr)

        gen(base, nr)
        return result


def build():
    return 5


if __name__ == "__main__":

    s = Solution()
    print(s.generate(build()))
