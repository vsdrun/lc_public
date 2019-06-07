#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/next-greater-element-ii/description/


Given a circular array
(the next element of the last element is the first element of the array),

print the Next Greater Number for every element.

The Next Greater Number of a number x is the first greater number to
its traversing-order next in the array, which means you could search
circularly to find its next greater number.
If it doesn't exist, output -1 for this number.


Example 1:
Input: [1,2,1]
Output: [2,-1,2]


Explanation: The first 1's next greater number is 2;
The number 2 can't find next greater number;
The second 1's next greater number needs to search circularly, which is also 2.

解法1:
看到circular array, 直覺double array size, 重複其值一遍。
2*len(nums) > j > i
if nums[i] < tmp[j] 中!


解法2:
stack.
e.g : 1 2 1 3 4 => into stack:

4
3
1
2
1
--------
scan the list from left to right:
if v > stack.pop() , pop the stack, why?
because current v is larger, why keep the smaller one for later
v' to compare?

"""


class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        stack = nums[::-1]
        result = []

        for n in nums[::-1]:
            while stack:
                if n < stack[-1]:
                    result.append(stack[-1])
                    stack.append(n)
                    break
                else:
                    stack.pop()
            else:
                stack.append(n)
                result.append(-1)

        return result[::-1]


def build():
    #  return "121"
    return [8, 1, 9, 7]


if __name__ == "__main__":
    s = Solution()
    print(s.nextGreaterElements(build()))
    print(s.rewrite(build()))
