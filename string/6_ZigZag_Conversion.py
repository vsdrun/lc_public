#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/zigzag-conversion/

The string "PAYPALISHIRING" is written in a zigzag pattern on a given
number of rows like this:
(you may want to display this pattern in a fixed font for better legibility)


P   A   H   N
A P L S I I G
Y   I   R

And then read line by line: "PAHNAPLSIIGYIR"

Write the code that will take a string and make this conversion given a number of rows:

string convert(string s, int numRows);


Example 1:
Input: s = "PAYPALISHIRING", numRows = 3
Output: "PAHNAPLSIIGYIR"


Example 2:
Input: s = "PAYPALISHIRING", numRows = 4
Output: "PINALSIGYAHRPI"
Explanation:
P     I    N
A   L S  I G
Y A   H R
P     I
"""


class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        numRows = 4時
        使用
        [
        ""
        ""
        ""
        ""
        ]
        觸底反轉 1 向下 -1 向上
        """
        # rule out conditions

        if numRows == 1 or len(s) <= numRows or len(s) == 0:
            return s

        result = [''] * numRows
        idx = 0
        direct = 1 # 1 down, -1 up

        for c in s:
            result[idx] += c

            if idx + direct >= len(result) or idx + direct < 0:
                direct = -direct

            idx += direct

        return "".join(result)




def build():
    return "PAYPALISHIRING", 4


if __name__ == "__main__":
    s = Solution()
    print(s.convert(*build()))
