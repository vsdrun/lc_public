#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Given a non-empty array of numbers, a0, a1, a2, … , an-1, where 0 ≤ ai < 231.
Find the maximum result of ai XOR aj, where 0 ≤ i, j < n.

Could you do this in O(n) runtime?
Example:
Input: [3, 10, 5, 25, 2, 8]
Output: 28

Explanation: The maximum result is 5 ^ 25 = 28.
00101
11100


This algorithm's idea is:
to iteratively determine what would be each bit of the
final result from left to right.

And it narrows down the candidate group iteration by iteration.

e.g. assume input are a,b,c,d,...z, 26 integers in total.
In first iteration, if you found that a, d, e, h, u differs on the MSB(
most significant bit), so you are sure your final result's MSB is set.

Now in second iteration, you try to see if among a, d, e, h, u
there are at least two numbers make the 2nd MSB differs, if yes,
then definitely, the 2nd MSB will be set in the final result.

And maybe at this point the candidate group shinks from a,d,e,h,u to a, e, h.

Implicitly, every iteration, you are narrowing down the candidate group,
 but you don't need to track how the group is shrinking,
 you only cares about the final result.
"""


class Solution(object):
    def findMaximumXOR(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        answer = 0

        for i in range(32)[::-1]:
            answer <<= 1

            prefixes = {num >> i for num in nums}

            answer += any(answer ^ 1 ^ p in prefixes for p in prefixes)

        return answer


def build_input():
    return [3, 10, 5, 25, 2, 8]


if __name__ == "__main__":
    b = build_input()

    s = Solution()
    result = s.findMaximumXOR(b)

    print(result)
