#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/find-k-closest-elements/

Given a sorted array, two integers k and x, find the k closest
elements to x in the array.

The result should also be sorted in ascending order.
If there is a tie, the smaller elements are always preferred.

Example 1:
Input: [1,2,3,4,5], k=4, x=3
Output: [1,2,3,4]

Example 2:
Input: [1,2,3,4,5], k=4, x=-1
Output: [1,2,3,4]


Note:
The value k is positive and will always be
smaller than the length of the sorted array.

Length of the given array is positive and will not exceed 104
Absolute value of elements in the array and x will not exceed 104

UPDATE (2017/9/19):
The arr parameter had been changed to an array of integers
(instead of a list of integers).
Please reload the code definition to get the latest changes.
"""

class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]

        input: SORTED array
        """
        import heapq as hq

        diff = [(abs(a-x), a) for a in arr]

        hq.heapify(diff)

        result = [hq.heappop(diff)[1] for _ in range(k)]

        return sorted(result)

    def rewrite(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]

        input: SORTED array
        Use the trait of sorted array with binary search.
        """
        left = 0
        right = len(arr) - k

        while left < right:
            mid = (left + right) // 2
            print("left: {} right: {} mid: {}".format(left, right, mid))

            if abs(x - arr[mid]) > abs(arr[mid + k] - x):
                left = mid + 1
            else:
                right = mid

        print("left: {} right: {}".format(left, right))
        return arr[left:left + k]

    def rewrite2(self, arr, k, x):
        """
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]

        input: SORTED array
        Use the trait of sorted array with binary search.
        """
        left = 0
        # 先 減去 k
        right = len(arr) - k

        while left < right:
            mid = (left + right) / 2  # 是index 的mid, 不是取中位數...
            # 注意邊際 定義 inclusive/exclusive
            # 因為 arr[mid] - x 比較大 故 left = mid + 1
            # 將 mid exclusive.
            if abs(arr[mid] - x) > abs(arr[mid + k] - x):
                left = mid + 1 # 這裡會導致 如果 current mid大於 mid + k, left =
                #  mid + 1
            else:
                # right 只會往左 不會去右
                right = mid

        return arr[left: left + k]


def build():
    return [-100, 1, 2, 3, 4, 5], 2, 0
    return [1,2,3,4,5], 4, 3
    # [2, 1, 0, 1, 2]
    return [1,2,3,4,5], 4, -1
    # [16, 5, 1, 1, 3, 4]


if __name__ == "__main__":
    s = Solution()
    print(s.findClosestElements(*build()))
    print(s.rewrite(*build()))
    print(s.rewrite2(*build()))
