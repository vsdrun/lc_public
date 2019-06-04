#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/first-bad-version/description/

You are a product manager and currently leading a team to develop a
new product.

Unfortunately, the latest version of your product fails the quality check.

Since each version is developed based on the previous version,
all the versions after a bad version are also bad.

Suppose you have n versions [1, 2, ..., n] and you want to find
out the first bad one, which causes all the following ones to be bad.

You are given an API bool isBadVersion(version) which will return whether
version is bad.

Implement a function to find the first bad version. You should
minimize the number of calls to the API.

回傳第一個bad version

使用binary search
"""


# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
def isBadVersion(version):
    return {1: False,
            2: False,
            3: False,
            4: False,
            5: True,
            6: True,
            7: True,
            8: True,
            9: True,
            10: True}[version]


class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        [)
        s: 含
        e: 不含
        """
        import bisect as bi

        class Wrapper(object):
            # True 左一半
            # False 右一半
            # same as:
            # all(val < x for val in a[lo:i])  左
            # all(val >= x for val in a[i:hi]) 右
            def __getitem__(self, i):
                return isBadVersion(i)

        i = bi.bisect(Wrapper(), False, 1, n + 1)
        return i

    def firstBadVersion2(self, n):
        """
        :type n: int
        :rtype: int
        """

        s = 1
        e = n

        while s < e:
            m = s + (e - s) / 2
            if isBadVersion(m):
                e = m  # 左邊一半
            else:  # 右邊一半
                s = m + 1  # 止區 最後剩兩個時 s + (e-s)/2 為 s
                # isBadVersion(m) 為 false 則 m+1 此時超過 e , 止
        return s


def build():
    return 10


if __name__ == "__main__":
    s = Solution()

    result = s.firstBadVersion2(build())

    print(result)
