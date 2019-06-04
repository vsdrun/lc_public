#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/find-smallest-letter-greater-than-target/

Given a list of sorted characters letters containing only lowercase letters,
and given a target letter target,

find the
1. smallest element in the list
2. that is larger than the given target.

幹.. 就是 c++ 的 upper_bound
只是有 wrap around.

真簡單 沒有則回傳 list[0]

Letters also wrap around.

For example,
if the target is target = 'z' and letters = ['a', 'b'], the answer is 'a'.


Input:
letters = ["c", "f", "j"]
target = "a"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "c"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "d"
Output: "f"

Input:
letters = ["c", "f", "j"]
target = "g"
Output: "j"

Input:
letters = ["c", "f", "j"]
target = "j"
Output: "c"

Input:
letters = ["c", "f", "j"]
target = "k"
Output: "c"

Note:
letters has a length in range [2, 10000].
letters consists of lowercase letters, and contains at least 2 unique letters.
target is a lowercase letter.
"""


class Solution(object):
    def nextGreatestLetter(self, letters, target):
        """
        :type letters: List[str]
        :type target: str
        :rtype: str
        CPU prefetch thus fast; however, binary search could be faster.
        """
        if target >= letters[-1]:
            return letters[0]

        for c in letters:
            if c > target:
                return c


def build():
    return ["c", "f", "j"], "k"
    return ["c", "f", "j"], "j"
    return ["c", "f", "j"], "d"


if __name__ == "__main__":
    s = Solution()
    print(s.nextGreatestLetter(*build()))
