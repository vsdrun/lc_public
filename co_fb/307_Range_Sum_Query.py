#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/range-sum-query-mutable/

Given an integer array nums,
find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the
element at index i to val.

Example:
Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8


Note:
The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.


-----------------------------------------------------------------------------
Fenwick tree.

編碼:
後面的值為exclusive, 即2^0 = 1 包含自己為1
3 = 2^1 + 2^0 = 由2^1 index的值 加上 2^0(1) 即自己而已，以上range內的和。
如果為2的倍數，則編碼為:
0 + 2^x 的和


要找到(0 ~ 9) 的 sum
由index 9 的值 加上其 parent... 的值即是
如何知道index 9的parent index? 簡單! Flip the right most bit.


Fenwick tree的概念:
1
10
100
1000


以上為parent 其下為子
11
101, 110, 111
1001, 1010, 1100, 1110, 1111


找parent:
減一去
v & (v-1)

找next for update/add:
負i保
再加回原來的數. 得到next idx.
"""
    #  def update(self, i, x):  # add x to the ith position
        #  while i <= self.N:
            #  self.BIT[i - 1] += x  # because we're working with an 1-based array
            #  i += i & (-i)  # magic! don't touch!

    #  def query(self, i):  # find the ith prefix sum
        #  s = 0

        #  while i > 0:
            #  s += self.BIT[i - 1]
            #  i -= i & (-i)

        #  return s

    #  def __init__(self, ll=[]):  # initialize the fenwick tree

        #  self.N = len(ll)
        #  self.BIT = [0 for i in xrange(self.N)]

        #  for i in xrange(1, self.N + 1):
            #  self.update(i, ll[i - 1])


class NumArray(object):

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.N = len(nums) + 1  # 加 1 starts with 0.
        self.tree = [0] * self.N
        self.nums = nums

        self.init = True

        for idx, val in enumerate(nums):
            self.update(idx, val*2)  #  初始時 double value 因為我們以輸入的
            # value 為 差異的來源.

        self.init = False

    def update(self, i, val):
        """
        Input intends to replace the value, not adding the value.
        However, this function adds the value, not replacing it in the
        Fenwick tree.

        :type i: int
        :type val: int
        :rtype: void
        """
        diff = val - self.nums[i]

        if not self.init:
            self.nums[i] = val

        i += 1

        while i < self.N:
            self.tree[i] += diff
            # next idx, 由既有的right most bit 為 1的加1往前
            i += i & (-i)


    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        j += 1
        si = 0
        sj = 0

        # 算左邊的sum
        while i > 0:
            si += self.tree[i]
            i = i & (i - 1)

        # 算右邊的sum
        while j > 0:
            sj += self.tree[j]
            j = j & (j - 1)

        print("si: {}".format(si))
        print("sj: {}".format(sj))

        # 求差額
        return sj - si

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)


def build():
    return [1,2,1,3,2,5]


if __name__ == "__main__":
    s = NumArray(build())
    print(s.sumRange(1,2))
    print(s.sumRange(0,5))
    s.update(3, 5)
    print(s.sumRange(0,5))
    s.update(3, 3)
    print(s.sumRange(0,5))
