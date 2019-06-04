#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/random-pick-with-weight/


Given an array w of positive integers,
where w[i] describes the weight of index i,
write a function pickIndex which randomly picks an index in
proportion to its weight.



Note:
1 <= w.length <= 10000
1 <= w[i] <= 10^5
pickIndex will be called at most 10000 times.



Example 1:
Input:
["Solution","pickIndex"]
[[[1]],[]]
Output: [null,0]



Example 2:
Input:
["Solution","pickIndex","pickIndex","pickIndex","pickIndex","pickIndex"]
[[[1,3]],[],[],[],[],[]]
Output: [null,0,1,1,1,0]



Explanation of Input Syntax:
The input is two lists: the subroutines called and their arguments.
Solution's constructor has one argument, the array w.
pickIndex has no arguments.



Arguments are always wrapped with a list, even if there aren't any.
[null,0,0,1,3,1,3,1,3,3,1,1,0,1,1,3,1,1,1,0,1,1,1,1,1,3,1,2,0,1,1,0,1,3,0,1,2,1,0,1,0,1,1,3,3,1,1,3,1,3,2,1,3,3,1,1,3,1,1,1,1,1,3,1,3,1,3,1,1,1,1,1,1,3,1,3,3,1,1,0,3,0,3,3,3,1,0,1,3,1,1,2,3,3,1,1,3,3,1,0,1,1,3,1,3,0,2,1,1,1,3,1,2,0,1,1,3,1,3,0,3,1,1,3,3,1,1,1,3,3,3,0,1,1,1,3,1,3,3,3,1,3,1,1,3,3,1,1,1,3,1,3,3,1,1,2,0,0,1,1,0,1,1,1,3,0,3,1,1,3,0,1,1,3,1,1,3,1,0,3,1,1,1,3,3,3,3,1,3,1,3,1,0,2,1,1,1,1,2,1,0,1,1,3,3,1,3,1,0,3,3,0,1,1,1,0,1,1,1,1,1,1,3,1,1,0,1,1,0,1,1,1,3,1,1,1,0,3,0,1,3,1,3,1,1,1,1,1,3,3,3,0,1,3,1,3,1,1,1,1,3,3,1,1,3,2,2,1,1,1,3,3,1,1,1,1,3,1,1,1,1,1,3,1,1,3,1,1,0,3,1,1,1,1,1,1,3,3,1,1,0,1,3,0,1,1,3,1,3,1,1,3,2,1,1,2,3,3,1,1,0,1,3,3,1,3,3,1,1,1,0,0,3,1,1,0,2,0,2,1,1,1,3,3,3,1,0,3,1,1,3,1,1,1,1,3,3,1,1,3,3,3,3,1,1,1,1,0,1,3,1,3,1,1,1,3,0,0,3,1,1,1,3,3,1,2,3,0,3,3,1,1,3,0,1,0,0,1,1,3,1,1,1,1,1,3,1,1,1,0,0,3,1,1,2,1,1,3,1,3,0,2,1,1,0,1,1,0,1,0,3,3,2,1,1,1,1,1,1,0,3,1,0,1,1,3,3,1,1,1,1,3,1,1,1,1,1,3,0,1,1,1,3,1,3,3,1,0,0,1,1,3,3,1,0,0,2,0,0,3,3,0,1,3,3,1,3,1,3,0,3,1,3,1,3,1,1,1,...

题目大意
要求按照权重挑选索引。
比如[1,99]中，有1%的概率挑选到索引0，有99%的概率挑选到索引1.

https://blog.csdn.net/fuxuemingzhu/article/details/81807215
"""
import random

class Solution:
    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.preSum = [0] * len(w)
        self.preSum[0] = w[0]

        # 累進和
        for i in range(1, len(w)):
            self.preSum[i] = self.preSum[i - 1] + w[i]

    def pickIndex(self):
        """
        :rtype: int
        """
        total = self.preSum[-1]
        rand = random.randint(0, total - 1)

        left, right = 0, len(self.preSum) - 1

        while left + 1 < right:
            mid = (left + right) // 2

            if rand >= self.preSum[mid]:
                left = mid
            else:
                right = mid

        if rand < self.preSum[left]:
            return left

        return right


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()


def build():
    return [1, 99]


if __name__ == "__main__":
    s = Solution(build())
    print(s.pickIndex())
    print(s.pickIndex())
    print(s.pickIndex())
