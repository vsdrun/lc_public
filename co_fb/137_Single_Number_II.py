#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/single-number-ii/


Given a non-empty array of integers,
every element appears three times except for one,
which appears exactly once. Find that single one.


Note:
Your algorithm should have a linear runtime complexity.
Could you implement it without using extra memory?


Example 1:
Input: [2,2,3,2]
Output: 3

Example 2:
Input: [0,1,0,1,0,1,99]
Output: 99



https://leetcode.com/problems/single-number-ii/discuss/43332/My-own-explanation-of-bit-manipulation-method-might-be-easier-to-understand

Consider the following fact:
Write all numbers in binary form,
then for any bit 1 that appeared 3*n times (n is an integer),
the bit can only present in numbers that appeared 3 times

e.g. 0010 0010 0010 1011 1011 1011 1000 (assuming 4-bit integers)
2(0010) and 11(1011) appeared 3 times, and digit counts are:

Digits      3 2 1 0  (位置)

Counts      4 0 6 3  (1的count)

Counts%3    1 0 0 0  (只有位置3的count module 3 為1 代表不為3的倍數)
%3的值為 0, 1, 2

Counts on 2,1,0 are all times of 3, the only digit index that
has Counts % 3 != 0 is 3

Therefore, to find the number that appeared only 1 or 2 times,
we only need to extract all bits that has Counts %3 != 0

Now consider how we could do this by bit manipulation

***
since counts % 3 has only 3 states: 0(00),1(01),2(10)
we could use a TWO BIT COUNTER (Two, One) to represent Counts % 3,
now we could do a little research on state transitions, for each bit,
let B be the input bit, we can enumerate the all possible state transitions,
Two+, One+ is the new state of Two, One.
(here we need to use some knowledge in Digital Logic Design)


Two One B Two+ One+

0 0 0 0 0

0 0 1 0 1

0 1 0 0 1

0 1 1 1 0

1 0 0 1 0

1 0 1 0 0

1 1 0 X X (X represents we don't care)

1 1 1 X X

We could then draw the Karnaugh map to analyze the logic
(https://en.wikipedia.org/wiki/Karnaugh_map), and then we get:

One+ = (One ^ B) & (~Two)  若出現三次 則以出現兩次的數inverse為mask.

Two+ = (~One+) & (Two ^ B)  代表出現2次的數字. 離如(1,2,2) 則為2

Now for int_32, we need only 2 int_32 two represent Two and One
for each bit and update Two and One using the rules derived above.
"""


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        One+ = (One ^ B) & (~Two)
        Two+ = (~One+) & (Two ^ B)
        """

        ones = 0
        twos = 0

        for c in nums:
            ones = (ones ^ c) & ~ twos
            twos = (twos ^ c) & ~ ones

        return ones




def build():
    return [2,2,3,2]


if __name__ == "__main__":
    s = Solution()
    print(s.singleNumber(build()))
