#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
重要 high freq.
https://leetcode.com/problems/utf-8-validation/description/

*** 至多 4 bytes
A character in UTF8 can be from 1 to 4 bytes long,
subjected to the following rules:

1. For 1-byte character, the first bit is a 0, followed by its unicode code.

2. For n-bytes character, the first n-bits are all one's,
the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.

This is how the UTF-8 encoding would work:
   Char. number range  |        UTF-8 octet sequence
      (hexadecimal)    |              (binary)
   --------------------+---------------------------------------------
   0000 0000-0000 007F | 0xxxxxxx
   0000 0080-0000 07FF | 110xxxxx 10xxxxxx
   0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
   0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx


Given an array of integers representing the data,
return whether it is a valid utf-8 encoding.


Note:
The input is an array of integers. Only the least significant 8 bits of each
integer is used to store the data. This means each integer represents only 1
byte of data.


Example 1:
data = [197, 130, 1], which represents the octet sequence:
11000101 10000010 00000001.
Return true.


It is a valid utf-8 encoding for a 2-bytes character followed by a 1-byte character.

Example 2:
data = [235, 140, 4], which represented the octet sequence:
11101011 10001100 00000100.
Return false.


The first 3 bits are all one's and the 4th bit is 0 means it is a 3-bytes character.
The next byte is a continuation byte which starts with 10 and that's correct.
But the second continuation byte does not start with 10, so it is invalid.
"""


class Solution(object):
    def validUtf8(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """

        follow = 0

        for byte in data:
            # single char.
            if not byte & 0b10000000:
                if follow:
                    return False
            # remaining
            elif byte & 0b11000000 == 0b10000000:
                if not follow:
                    return False
                follow -= 1
            # 2 chars.
            elif byte & 0b11100000 == 0b11000000:
                if follow:
                    return False
                follow = 1
            # 3 chars.
            elif byte & 0b11110000 == 0b11100000:
                if follow:
                    return False
                follow = 2
            # 4 chars.
            elif byte & 0b11111000 == 0b11110000:
                if follow:
                    return False
                follow = 3
            else:
                return False

        return not follow

    """
    1. For 1-byte character, the first bit is a 0, followed by its unicode code.

    2. For n-bytes character, the first n-bits are all one's,
    the n+1 bit is 0, followed by n-1 bytes with most significant 2 bits being 10.

    This is how the UTF-8 encoding would work:
       Char. number range  |        UTF-8 octet sequence
          (hexadecimal)    |              (binary)
       --------------------+---------------------------------------------
       0000 0000-0000 007F | 0xxxxxxx
       0000 0080-0000 07FF | 110xxxxx 10xxxxxx
       0000 0800-0000 FFFF | 1110xxxx 10xxxxxx 10xxxxxx
       0001 0000-0010 FFFF | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx


    Given an array of integers representing the data,
    return whether it is a valid utf-8 encoding.
    """
    def rewrite(self, data):
        """
        :type data: List[int]
        :rtype: bool
        """
        remain = 0

        for d in data:
            # if single char but has remains, return False
            if not (d & 0b10000000):
                if remain:
                    return False
            # if 2 chars, remains == 1
            elif d & 0b11000000 == 0b10000000:
                if not remain:
                    return False
                remain -= 1
            elif d & 0b11100000 == 0b11000000:
                if remain:
                    return False
                remain = 1
            elif d & 0b11110000 == 0b11100000:
                if remain:
                    return False
                remain = 2
            # 至多4 byes
            elif d & 0b11111000 == 0b11110000:
                if remain:
                    return False
                remain = 3
            else:
                return False

        return not remain


def build_input():
    return [197, 130, 1]
    return [235, 140, 4]
    return [1, 197, 130, 3, 197, 130]
    return [145]


if __name__ == "__main__":
    input = build_input()

    s = Solution()
    print(s.validUtf8(input))
    print(s.rewrite(input))
