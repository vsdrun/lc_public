#!/usr/bin/env python


"""
https://leetcode.com/problems/split-linked-list-in-parts/description/

Given a (singly) linked list with head node root,
write a function to split the linked list into k consecutive linked
list "parts".

The length of each part should be as equal as possible:
no two parts should have a size differing by more than 1.
This may lead to some parts being null.

The parts should be in order of occurrence in the input list,
and parts occurring earlier should always have a size greater
than or equal parts occurring later.


Return a List of ListNode's representing the linked list parts that are formed.

Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]


Example 1:
Input:
root = [1, 2, 3], k = 5
Output: [[1],[2],[3],[],[]]
Explanation:
The input and each element of the output are ListNodes, not arrays.
For example, the input root has root.val = 1, root.next.val = 2,
root.next.next.val = 3, and root.next.next.next = null.

The first element output[0] has output[0].val = 1, output[0].next = null.
The last element output[4] is null,
but it's string representation as a ListNode is [].



Example 2:
Input:
root = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], k = 3
Output: [[1, 2, 3, 4], [5, 6, 7], [8, 9, 10]]
Explanation:
The input has been split into consecutive parts with size difference at most 1,
and earlier parts are a larger size than the later parts.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]

        idea:
        max-min share idea but diff with only 1.
        """
        if not root:
            return [[]] * k

        if not k:
            return []

        # O(n) count elements
        cnt = 0
        cnt_root = root

        while cnt_root:
            cnt += 1
            cnt_root = cnt_root.next

        base, rest = cnt / k, cnt % k

        ret = []
        tmp_root = root

        while k:
            k -= 1
            tmp = []

            for _ in range(base + (1 if rest > 0 else 0)):
                tmp += tmp_root.val,
                tmp_root = tmp_root.next

            rest -= 1
            ret += tmp,

        return ret


def build():
    return None, 3
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(3)
    l1.next.next.next = ListNode(4)
    l1.next.next.next.next = ListNode(5)
    l1.next.next.next.next.next = ListNode(6)
    l1.next.next.next.next.next.next = ListNode(7)
    l1.next.next.next.next.next.next.next = ListNode(8)
    return l1, 13


if __name__ == "__main__":
    s = Solution()
    print(s.splitListToParts(*build()))
