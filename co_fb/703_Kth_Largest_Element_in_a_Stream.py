#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/kth-largest-element-in-a-stream/

Design a class to find the kth largest element in a stream.
Note that it is the kth largest element in the sorted order,
not the kth distinct element.


Your KthLargest class will have a constructor which accepts an integer k
and an integer array nums, which contains initial elements from the stream.
For each call to the method KthLargest.add,
return the element representing the kth largest element in the stream.


Example:
int k = 3;
int[] arr = [4,5,8,2];
KthLargest kthLargest = new KthLargest(3, arr);
kthLargest.add(3);   // returns 4
kthLargest.add(5);   // returns 5
kthLargest.add(10);  // returns 5
kthLargest.add(9);   // returns 8
kthLargest.add(4);   // returns 8

Note:
You may assume that nums' length ≥ k-1 and k ≥ 1.
"""
import heapq


class KthLargest(object):
    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        heapq.heapify(self.pool)

        while len(self.pool) > k:
            heapq.heappop(self.pool)


    def add(self, val):

        if len(self.pool) < self.k:
            heapq.heappush(self.pool, val)
        else:
            heapq.heappushpop(self.pool, val)

        return self.pool[0]



# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)


def build():
    return [4,5,8,2]


if __name__ == "__main__":

    k = KthLargest(3, build())
    print(k.add(3))
    print(k.add(5))
    print(k.add(10))
    #  print(k.add(9))
    #  print(k.add(4))
    print(k.add(5))
    print(k.add(5))
    print(k.add(5))
