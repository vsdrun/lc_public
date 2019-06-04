#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/


"""
Given a n*n matrix where each of the rows and columns are sorted in
ascending order, find the kth smallest element in the matrix.

Note that it is the kth smallest element in the sorted order,
not the kth distinct element.

Example:

matrix = [
 [ 1,  5,  9],
 [10, 11, 13],
 [12, 13, 15]
],
k = 8,

return 13.

https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/discuss/85182/My-solution-using-Binary-Search-in-C%2B%2B

class Solution
{
public:
	int kthSmallest(vector<vector<int>>& matrix, int k)
	{
		int n = matrix.size();
		int le = matrix[0][0], ri = matrix[n - 1][n - 1];
		int mid = 0;

		while (le < ri)
		{
			mid = le + (ri-le)/2;
			int num = 0;
			for (int i = 0; i < n; i++)
			{
				int pos = upper_bound(matrix[i].begin(), matrix[i].end(), mid) - matrix[i].begin();
				num += pos;
			}
			if (num < k)
			{
				le = mid + 1;
			}
			else
			{
				ri = mid;
			}
		}
		return le;
	}
};
"""

import heapq


class Solution(object):

    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        def gen(li):
            for i in li:
                yield i

        g = map(gen, matrix)

        m = heapq.merge(*g)

        result = None

        for i in xrange(k):
            result = next(m)

        return result

    def rewrite(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        using binary search
        以mid為pivot, 每個迴圈有新的mid
        在以count來看，此mid是否能達到count==k
        """
        mmin = matrix[0][0]
        mmax = matric[-1][-1]

        def bs():

            b = mmin
            e = mmax
            count = 0

            while b < e:
                mid = b + (e-b)/2  # 1, 15, mid = 8

                for l in matrix:
                    # use bisect and count mid in this single row





def build():
    matrix = [
        [1, 5, 12],
        [10, 11, 13],
        [12, 13, 15]
    ]
    return matrix, 4


if __name__ == "__main__":
    s = Solution()
    print(s.kthSmallest(*build()))
    print(s.rewrite(*build()))
