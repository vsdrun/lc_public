#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/read-n-characters-given-read4/description/

The API: int read4(char *buf) reads 4 characters at a time from a file.

The return value is the actual number of characters read.
For example, it returns 3 if there is only 3 characters left in the file.

By using the read4 API,
implement the function int read(char *buf, int n)
that reads n characters from the file.

Note:
The read function will only be called once for each test case.


int read(char *buf, int n) {
    int res = 0;
    while (n > 0) {
        int tmp = min(read4(buf), n);
        res += tmp;
        buf += tmp;
        if (tmp < 4)
            break;
        n -= 4;
    }
    return res;
}

"""


# The read4 API is already defined for you.
# @param buf, a list of characters
# @return an integer
tmpstr = \
    "WRBqHdrOkyIDsdRMwRSYLBfaCYEdgxPlrlNppfkOKcqNnuwSmbUcJISmKtXxvRBJTSFzfMfdRsfbnvhFSqWQaeCZFKlOJppRXiZx"

tmpstr = ""

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
    def read_modify(self, buf, n):
        """
        :type buf: Destination buffer (List[str])
        :type n: Maximum number of characters to read (int)
        :rtype: The number of characters read (int)

        this solution will modify input buf, which, by leetcode,
        is not allowed...
        """

        lbuf = [""] * 4

        def assign(i):
            read_count = read4(lbuf)

            if read_count and i + 4 > n:
                buf[i: n] = lbuf[
                    0: n - i if read_count > n - i else read_count]
            else:
                buf[i:] = lbuf[0:read_count]

        [assign(i) for i in xrange(0, n, 4)]

        return len(buf)

    def read(self, buf, n):
        # 簡潔明瞭~
        idx = 0

        buf4 = [""] * 4

        while True:
            # curr is the number of chars that reads
            curr = min(read4(buf4), n - idx)

            for i in xrange(curr):
                buf[idx] = buf4[i]
                idx += 1

            # return if it reaches the end of file or reaches n
            if curr != 4 or idx == n:
                return idx


def build():
    count = 0
    ll = [""] * count
    return ll, count


if __name__ == "__main__":
    s = Solution()
    ll, n = build()
    print("before ll: {0}".format(ll))
    print("before ll type: {0}".format(type(ll)))
    result = s.read(ll, n)
    print("after ll: {0}".format(ll))
    print("after ll type: {0}".format(type(ll)))

    ll, n = build()
    print("before ll: {0}".format(ll))
    print("before ll type: {0}".format(type(ll)))
    result = s.read_dumb(ll, n)
    print("after ll type: {0}".format(type(ll)))

    print(result)
