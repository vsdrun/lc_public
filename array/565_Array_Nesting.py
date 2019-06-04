#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/array-nesting/description/

A zero-indexed array A of length N contains all integers from 0 to N-1.
Find and return the longest length of set S,
where S[i] = {A[i], A[A[i]], A[A[A[i]]], ... } subjected to the rule below.

Suppose the first element in S starts with the selection of
element A[i] of index = i, the next element in S should be A[A[i]],
and then A[A[A[i]]]…

By that analogy, we stop adding right before a duplicate element occurs in S.

Example 1:
Input: A = [5,4,0,3,1,6,2]
Output: 4
Explanation:
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

One of the longest S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}


解釋:
The idea is to, start from every number,
find circles in those index-pointer-chains,
every time you find a set
(a circle) mark every number as visited (-1)
so that next time you won’t step on it again.

C++

class Solution {
public:
    int arrayNesting(vector<int>& a) {
        size_t maxsize = 0;
        for (int i = 0; i < a.size(); i++) {
            size_t size = 0;
            for (int k = i; a[k] >= 0; size++) {
                int ak = a[k];
                a[k] = -1; // mark a[k] as visited;
                k = ak;
            }
            maxsize = max(maxsize, size);
        }

        return maxsize;
    }
};
"""


class Solution(object):
    def arrayNesting(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        from __builtin__ import xrange

        mx = float("-inf")

        for i in xrange(len(nums)):
            csize = 0
            j = i

            while j < len(nums):
                if nums[j] < 0:
                    break

                val = nums[j]

                nums[j] = -1

                j = val

                csize += 1

            mx = max(csize, mx)

        return mx

    def rewrite(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        from __builtin__ import xrange

        mx = float("-inf")

        for i in xrange(len(nums)):

            l_cnt = 0

            j = i

            while nums[j] >= 0:
                l_cnt += 1
                l_j = j
                j = nums[j]
                nums[l_j] = -1

            mx = max(mx, l_cnt)

        return mx


def build():
    return [5, 4, 0, 3, 1, 6, 2]


if __name__ == "__main__":

    s = Solution()
    print(s.arrayNesting(build()))
    print(s.rewrite(build()))
