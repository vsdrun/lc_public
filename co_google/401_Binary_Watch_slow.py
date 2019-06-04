#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
A binary watch has 4 LEDs on the top which represent the hours (0-11), and the
6 LEDs on the bottom represent the minutes (0-59).

Each LED represents a zero or one,
with the least significant bit on the right.

For example, the above binary watch reads "3:25".

Given a non-negative integer n which represents the number of LEDs
that are currently on, return all possible times the watch could represent.

Example:
Input: n = 1
Return: ["1:00", "2:00", "4:00", "8:00", "0:01", "0:02", "0:04", "0:08", "0:16",
"0:32"]

Note:
The order of output does not matter.

The hour must not contain a leading zero,
for example "01:00" is not valid, it should be "1:00".

The minute must be consist of two digits and may contain a leading zero, for
example "10:2" is not valid, it should be "10:02".
"""


class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        """
        4 for hour (0-11)
        6 for min (0-59)
        total: 10
        x x x x x x x x x x
        """
        delimit = ":"
        result = ["0"] * 10
        sol = []

        def count(si, num, result):
            if not num:
                hour = int("".join(result[0:4]), 2)
                minute = int("".join(result[4:]), 2)

                if hour > 11:
                    return
                if minute > 59:
                    return

                solstr = str(hour) + delimit

                if minute < 10:
                    solstr += "0" + str(minute)
                else:
                    solstr += str(minute)
                sol.append(solstr)
                return

            for i in xrange(si, 10):
                result[i] = "1"
                num -= 1
                count(i + 1, num, result)
                num += 1
                result[i] = "0"

        count(0, num, result)
        return sol


def build_input():
    return 1


if __name__ == "__main__":
    b = build_input()

    s = Solution()
    result = s.readBinaryWatch(b)

    #  Return ["eat","oath"].
    print(result)
