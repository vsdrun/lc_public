#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/next-closest-time/description/


Given a time represented in the format "HH:MM",
form the next closest time by reusing the current digits.
There is no limit on how many times a digit can be reused.


You may assume the given input string is always valid. For example, "01:34",
"12:09" are all valid. "1:34", "12:9" are all invalid.


Example 1:
Input: "19:34"
Output: "19:39"

Explanation: The next closest time choosing from digits 1, 9, 3, 4, is 19:39,
which occurs 5 minutes later.
It is not 19:33, because this occurs 23 hours and 59 minutes later.


Example 2:
Input: "23:59"
Output: "22:22"
Explanation: The next closest time choosing from digits 2, 3, 5, 9, is 22:22.
It may be assumed that the returned time is next day's time since it is smaller
than the input time numerically.

https://leetcode.com/problems/next-closest-time/discuss/107776/
"""


class Solution(object):
    def nextClosestTime(self, time):
        """
        :type time: str
        :rtype: str
        """

        return min(((t <= time), t)
                   for m in xrange(24 * 60)
                   for t in ["{0:02}:{1:02}".format(*divmod(m, 60))]
                   if set(t) <= set(time))[1]

    def rewrite(self, time):
        """
        :type time: str
        :rtype: str
        """
        result = []
        for m in range(24 * 60):
            for t in ["{0:02}:{1:02}".format(*divmod(m, 60))]:
                if set(t) <= set(time):
                    result.append(((t <= time), t))

        print(result)
        return min(result)[1]


def build():
    return "19:34"
    return "23:59"


if __name__ == "__main__":
    time = build()

    s = Solution()
    print(s.nextClosestTime(time))
    print(s.rewrite(time))

