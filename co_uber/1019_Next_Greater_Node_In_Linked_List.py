#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/next-greater-node-in-linked-list/

We are given a linked list with head as the first node.
Let's number the nodes in the list: node_1, node_2, node_3, ... etc.

Each node may have a next larger value:
for node_i, next_larger(node_i) is the node_j.val such that
j > i, node_j.val > node_i.val, and j is the smallest possible choice.
If such a j does not exist, the next larger value is 0.

Return an array of integers answer, where answer[i] = next_larger(node_{i+1}).

Note that in the example inputs (not outputs) below,
arrays such as [2,1,5] represent the serialization of a linked list with a
head node value of 2, second node value of 1, and third node value of 5.


Example 1:
Input: [2,1,5]
Output: [5,5,0]

Example 2:
Input: [2,7,4,3,5]
Output: [7,0,5,5,0]

Example 3:
Input: [1,7,5,1,9,2,5,1]
Output: [7,9,9,9,0,5,0,0]


Note:
1 <= node.val <= 10^9 for each node in the linked list.
The given list has length in the range [0, 10000].

503. Next Greater Element II
"""

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def nextLargerNodes(self, head):
        """
        :type head: ListNode
        :rtype: List[int]
        存index!
        """
        res, stack = [], []

        while head:

            while stack and stack[-1][1] < head.val:
                res[stack.pop()[0]] = head.val

            stack.append([len(res), head.val])
            res.append(0)
            head = head.next

        return res


def build():
    """
    Input: [2,7,4,3,5]
    2,7,4,3,5 - 2,7,4,3,5
    Output: [7,0,5,5,0]
    """
    _2 = ListNode(2)
    _7 = ListNode(7)
    _4 = ListNode(4)
    _3 = ListNode(3)
    _5 = ListNode(5)
    _2.next = _7
    _7.next = _4
    _4.next = _3
    _3.next = _5
    return _2

if __name__ == "__main__":
    s = Solution()
    print(s.nextLargerNodes(build()))
