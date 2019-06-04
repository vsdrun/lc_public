#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/reverse-bits/description/

Reverse bits of a given 32 bits unsigned integer.

Example:

Input: 43261596
Output: 964176192
Explanation:
43261596 represented in binary as 00000010100101000001111010011100,
return 964176192 represented in binary as 00111001011110000010100101000000.

Follow up:
If this function is called many times, how would you optimize it?


>>> '{0:08b}'.format(6)
'00000110'
Just to explain the parts of the formatting string:

{} places a variable into a string
0 takes the variable at argument position 0
: adds formatting options for this variable (otherwise it would represent decimal 6)
08 formats the number to eight digits zero-padded on the left
b converts the number to its binary representation
"""


class Solution:
    def reverseBits(self, n):
        # @param n, an integer
        # @return an integer

        n = list("{0:032b}".format(n))

        for i in range(len(n) / 2):
            n[i], n[~i] = n[~i], n[i]

        return int("".join(n), 2)


def build():
    return 43261596  # 964176192
    return 11


if __name__ == "__main__":

    s = Solution()
    print(s.reverseBits(build()))
