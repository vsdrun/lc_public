#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/read-n-characters-given-read4-ii-call-multiple-times/description/

The API:
int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read.
For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API, implement the function int read(char *buf, int n)
that reads n characters from the file.


Note:
The read function may be called multiple times.

**
this question is about internal buffer and external buffer
"""

# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer

tmpstr = \
    "WRBqHdrOkyIDsdRMwRSYLBfaCYEdgxPlrlNppfkOKcqNnuwSmbUcJISmKtXxvRBJTSFzfMfdRsfbnvhFSqWQaeCZFKlOJppRXiZx"

gi = 0
done = False

print("len: {0}".format(len(tmpstr)))


def read4(buf):
    global gi

    i = 0

    while i < 4:
        if gi == len(tmpstr):
            # gi is out of index
            break
        buf[i] = tmpstr[gi]
        i += 1
        gi += 1

    return i

class Solution(object):
    def __init__(self):
        self.highwaterIdx = 0
        self.lowwaterIdx = 0
        self.ibuff = [""] * 4 # list of 4

    def read(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)
        """

        idx = 0

        while idx < n:
            if self.lowwaterIdx == self.highwaterIdx:
                readi = read4(self.ibuff)

                if readi == 0:
                    break

                self.highwaterIdx = readi
                self.lowwaterIdx = 0

            buf[idx] = self.ibuff[self.lowwaterIdx]
            idx += 1
            self.lowwaterIdx += 1


        return idx


def build():
    return [0] * 10, 10


if __name__ == "__main__":
    s = Solution()

    buf = [""] * 99
    ret = s.read(buf, 99)
    print(buf)

    buf = [""] * 2
    ret = s.read(buf, 2)
    print(buf)

    buf = [""] * 1
    ret = s.read(buf, 1)
    print(buf)
