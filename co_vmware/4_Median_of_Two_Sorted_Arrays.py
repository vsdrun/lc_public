#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/median-of-two-sorted-arrays/

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays.
The overall run time complexity should be O(log (m+n)).

Example 1:
nums1 = [1, 3]
nums2 = [2]
The median is 2.0


Example 2:
nums1 = [1, 2]
nums2 = [3, 4]
The median is (2 + 3)/2 = 2.5

奇怪~~

用heapq 就好啦!
但是不是O(lg(m+n))

https://leetcode.com/problems/median-of-two-sorted-arrays/discuss/2481/Share-my-O(log(min(mn))-solution-with-explanation


To solve this problem, we need to understand "What is the use of median". In
statistics, the median is used for dividing a set into two equal length subsets,
that one subset is always greater than the other.

If we understand the use of
median for dividing, we are very close to the answer.


      left_part          |        right_part
A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

If we can ensure:
1) len(left_part) == len(right_part)
2) max(left_part) <= min(right_part)


Then we divide all elements in {A, B} into two parts with equal length,
and one part is always greater than the other.
Then median = (max(left_part) + min(right_part))/2.

To ensure these two conditions, we just need to ensure:
(1) i + j == m - i + n - j (or: m - i + n - j + 1)
    if n >= m, we just need to set: i = 0 ~ m, j = (m + n + 1)/2 - i

(2) B[j-1] <= A[i] and A[i-1] <= B[j]
"""


class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        A: m, x, m-x
        B: n, y, n-y
        A[x] < B[y+1]
        B[y] < A[x+1]
        """

        m, n = len(A), len(B)

        if m > n:
            # A 小 B 大.
            # m 小 n 大.
            A, B, m, n = B, A, n, m

        if n == 0:
            raise ValueError

        imin, imax, half_len = 0, m, (m + n + 1) / 2

        # here
        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i

            if i < m and B[j - 1] > A[i]:
                # i is too small, must increase it
                # i 增加代表j減少.
                imin = i + 1
            elif i > 0 and A[i - 1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect
                if i == 0:
                    max_of_left = B[j - 1]
                elif j == 0:
                    max_of_left = A[i - 1]
                else:
                    max_of_left = max(A[i - 1], B[j - 1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

def build():
    return [1, 2, 9], [3, 4, 5]
    return [4, 5], [1, 2, 3]


if __name__ == "__main__":
    s = Solution()
    print(s.findMedianSortedArrays(*build()))
