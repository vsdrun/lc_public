#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/24-game/description/

You have 4 cards each containing a number from 1 to 9.
You need to judge whether they could operated through
*, /, +, -, (, ) to get the value of 24.

Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24

Example 2:
Input: [1, 2, 1, 2]
Output: False

Note:
The division operator / represents real division, not integer division.
    For example, 4 / (1 - 2/3) = 12.

Every operation done is between two numbers.

In particular, we cannot use - as a unary operator.
    For example, with [1, 1, 1, 1] as input,
        the expression -1 - 1 - 1 - 1 is not allowed.

You cannot concatenate numbers together.
    For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.

HAHAHA:
https://leetcode.com/problems/24-game/discuss/107670/
"""


class Solution(object):
    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        total = 24
        Input: [4, 1, 8, 7]
        Output: True
        Explanation: (8-4) * (7-1) = 24

        BETTER!
        """
        level = {tuple(nums)}

        while level:
            new_level = set()

            for arr in level:
                for i in range(1, len(arr)):
                    for j in range(i):

                        # [4, 1, 8, 7]
                        newarr = arr[:j] + arr[j + 1:i] + arr[i + 1:]
                        print("i: {} j: {} newarr: {}".format(i, j, newarr))

                        a, b = arr[i], arr[j]
                        vs = {a + b, a - b, b - a, a * b}

                        if a:
                            vs.add(b * 1.0 / a)

                        if b:
                            vs.add(a * 1.0 / b)

                        if not newarr:
                            for v in vs:
                                if abs(v - 24) < 10**-5:
                                    return True
                        else:
                            for v in vs:
                                new_level.add(newarr + (v,))
                                print("new_level: {}".format(new_level))

            level = new_level
        return False

    def rewrite(self, nums):
        """
        :type nums: List[int]
        :rtype: bool

        total = 24
        Input: [4, 1, 8, 7]
        Output: True
        Explanation: (8-4) * (7-1) = 24

        BETTER!
        """
        ns = set()
        ns.add(tuple(nums))

        while ns:
            tmp = set()

            for n in ns:
                n = list(n)

                if len(n) == 1 and abs(n[0] - 24) < 1 :
                    print("n: {}".format(n))
                    return True

                for i in range(len(n)):
                    for j in range(i + 1, len(n)):
                        a, b = n[i], n[j]
                        vals = []

                        vals.append(a + b)
                        vals.append(a - b)
                        vals.append(b - a)
                        vals.append(a * b)

                        if a:
                            vals.append(b * 1.0 / a)
                        if b:
                            vals.append(a * 1.0 / b)

                        for v in vals:
                            tmp.add(tuple(n[:i] + n[i+1:j] + n[j+1:] + [v]))

            ns = tmp

        return False


def build():
    return [1,1,7,7]
    return [1, 2, 1, 2]
    return [9, 9, 9, 7]
    return [4, 1, 8, 7]


if __name__ == "__main__":
    s = Solution()
    #  print(s.judgePoint24(build()))
    print(s.rewrite(build()))
