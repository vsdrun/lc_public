#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/total-hamming-distance/description/

The Hamming distance between two integers is the number of positions at
which the corresponding bits are different.

Now your job is to find the total Hamming distance between all pairs of
the given numbers.

Example:
Input: 4, 14, 2

Output: 6

Explanation:
In binary representation, the 4 is 0100, 14 is 1110, and 2 is 0010 (just
showing the four bits relevant in this case).

So the answer will be:
HammingDistance(4, 14) + HammingDistance(4, 2) + HammingDistance(14, 2) = \
2 + 2 + 2 = 6.

https://leetcode.com/problems/total-hamming-distance/discuss/96243/Share-my-O(n)-C++-bitwise-solution-with-thinking-process-and-explanation

https://leetcode.com/problems/total-hamming-distance/discuss/96226/Java-O(n)-time-O(1)-Space


Notice the total hamming distance is the sum of the total
hamming distance for each of the i-th bits separately.

So, let’s consider the i-th column, which consists of numbers chosen
from {0, 1}.

The total hamming distance would be the number of pairs of numbers
that are different. That is,

Total hamming distance for the i-th bit =
(the number of zeros in the i-th position) *
(the number of ones in the i-th position).

We then add all of these together to get our answer.
"""


class Solution(object):
    def totalHammingDistance(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

    def totalHammingDistance_with_str(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sum(b.count('0') * b.count('1') for b in
                   zip(*map('{:032b}'.format, nums)))


def build():
    return [4, 14, 2]


if __name__ == "__main__":

    s = Solution()
    result = s.totalHammingDistance(build())
    print(result)
