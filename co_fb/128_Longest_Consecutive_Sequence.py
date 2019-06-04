#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/longest-consecutive-sequence/description/


Given an unsorted array of integers, 有重複~
find the length of the longest consecutive elements sequence.

For example,
Given [100, 4, 200, 1, 3, 2],
The longest consecutive elements sequence is [1, 2, 3, 4].
Return its length: 4.

Your algorithm should run in O(n) complexity.

只往大的找 因為其後由後面的會找上來
"""


class Solution(object):

    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        s = set(nums)

        gcount = 0

        def tweak(n, op):
            count = 0
            tmp = n

            while s:
                if op == "add":
                    tmp += 1
                else:
                    tmp -= 1

                if tmp in s:
                    count += 1
                    s.remove(tmp)
                    continue
                break
            return count

        for i in nums:
            if i not in s:
                continue
            s.remove(i)
            count = 1 + tweak(i, "add") + tweak(i, "minus")
            gcount = max(gcount, count)

        return gcount

    def rewrite(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ns = set(nums)
        mcnt = 0

        for n in nums:
            if n not in ns:
                continue

            cnt = 1
            ns.remove(n)
            on = n

            while n + 1 in ns:
                cnt += 1
                ns.remove(n+1)
                n = n + 1

            n = on

            while n - 1 in ns:
                cnt += 1
                ns.remove(n-1)
                n = n - 1

            mcnt = max(mcnt, cnt)

        return mcnt



def build():
    return [100, 4, 200, 1, 3, 2]


if __name__ == "__main__":
    nums = build()

    s = Solution()
    print(s.longestConsecutive(nums))
    print(s.rewrite(nums))
