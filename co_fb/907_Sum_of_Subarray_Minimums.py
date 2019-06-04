#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/sum-of-subarray-minimums/description/

Given an array of integers A, find the sum of min(B),
where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.


Example 1:
Input: [3,1,2,4]
Output: 17

Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.
"""

"""
I use a monotonous increasing stack to store the left boundary and right
boundary where a number is the minimal number in the sub-array

e.g. given [3,1,2,4],
For 3, the boudary is: | 3 | ...
For 1, the boudray is: | 3 1 2 4 |
For 2, the boudray is: ... | 2 4 |
For 4, the boudary is: ... | 4 |

The times a number n occurs in the minimums is
|left_bounday-indexof(n)| * |right_bounday-indexof(n)|

The total sum is
sum([n * |left_bounday - indexof(n)| * |right_bounday - indexof(n)| for n in array])

After a number n pops out from an increasing stack,
the current stack top is n's left_boundary,
the number forcing n to pop is n's right_boundary.

A tricky here is to add MIN_VALUE at the head and end.

class Solution:
    def sumSubarrayMins(self, A):
        res = 0
        stack = []  # increasing
        A = [float('-inf')] + A + [float('-inf')]

        for i, n in enumerate(A):
            while stack and A[stack[-1]] > n:
                cur = stack.pop()
                res += A[cur] * (i - cur) * (cur - stack[-1])
            stack.append(i)
        return res % (10**9 + 7)

Think:
[3, 1, 2, 4]

Use stack.
if the previous number is larger then the current,
we should process that number NOW, since it's not going to be
the lowest anyway in the future set.

When processing the previous larger number, the previous of the
previous larger number should be small number's index on the stack.
However, there are Larger number then the 'previous larger number'
existed before but being processed, thus the current
'previous larger number' is also the smallest among the
'previous processed larger number', and that should also take
into account...
"""


class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        [3, 1, 2, 4]
        思路:
        1. 將array前後放入boundary方便處理.
        2. 邏輯思維
        """

        stack = []  # 存 array index, 不是value, 存比現在值小的index
        result = 0

        # install head/tail '-inf' as well.
        A = [float("-inf")] + A + [float("-inf")]

        for idx, num in enumerate(A):
            # Process previous number is larger then the current.
            while stack and A[stack[-1]] > num:
                print("stack: {}, num: {}".format(stack, num))
                previousNumIdx = stack.pop()
                previousNum = A[previousNumIdx]

                # 目前的最大值 * 這個最大值的唯一cnt * 這雖然是目前最大值
                # 但卻是最小值在之前的list中.這個最大值的唯一cnt *
                # 這雖然是目前最大值但卻是最小值在之前的list中..
                #  result += previousNum * (idx- previousNumIdx) * \
                        #  (previousNumIdx - stack[-1])
                print("stack poped: {}".format(stack))
                result += previousNum * (idx- previousNumIdx)

            stack.append(idx)

        return result % (10**9 + 7)

    def rewrite(self, A):
        """
        :type A: List[int]
        :rtype: int
        [3, 1, 2, 4]
        思路:
        1. 將array前後放入boundary方便處理.
        2. 邏輯思維
        """


def build():
    """
    [1, 3, 5, 7, 6, 4]
       [5, 7 ,6, 4]  # 這為 previousNumIdx - stack[-1] 的原因

    stack: [0, 1, 2, 3, 4], num: 6
    stack poped: [0, 1, 2, 3]

    stack: [0, 1, 2, 3, 5], num: 4
    stack poped: [0, 1, 2, 3]

    stack: [0, 1, 2, 3], num: 4
    stack poped: [0, 1, 2]

    stack: [0, 1, 2, 6], num: -inf
    stack poped: [0, 1, 2]

    stack: [0, 1, 2], num: -inf
    stack poped: [0, 1]

    stack: [0, 1], num: -inf
    stack poped: [0]
    """
    return [1, 3, 5, 7, 6, 4]
    return [3, 1, 2, 4]

if __name__ == "__main__":
    s = Solution()
    print(s.sumSubarrayMins(build()))
