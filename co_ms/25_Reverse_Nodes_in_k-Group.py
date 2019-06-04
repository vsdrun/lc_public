#!/usr/bin/env python


"""
https://leetcode.com/problems/reverse-nodes-in-k-group/description/


Given a linked list, reverse the nodes of a linked list k at a
time and return its modified list.

k is a positive integer and is less than or equal to the length of
the linked list.

If the number of nodes is not a multiple of k then left-out nodes
in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

https://leetcode.com/problems/reverse-nodes-in-k-group/discuss/11491/Succinct-iterative-Python-O(n)-time-O(1)-space
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        def reverse(node, k):
            # test if there's enough k
            # if there's enought k, reverse it, otherwise, return what it is.
            test_node = node
            tcnt = 0
            valid = False

            while test_node:
                tcnt += 1

                if tcnt == k:
                    valid = True
                    break
                test_node = test_node.next

            if not valid:
                return node, None, None

            cnt = 0
            onode = node
            pnode = None
            nnode = None

            while node:
                nnode = node.next
                node.next = pnode
                pnode = node

                if cnt == k - 1:
                    break

                node = nnode
                cnt += 1

            return pnode, onode, nnode

        nnode = head
        tmpnode = None
        ret_node = None

        while nnode:
            pnode, onode, nnode = reverse(nnode, k)

            if not ret_node:
                ret_node = pnode

            if tmpnode:
                tmpnode.next = pnode

            tmpnode = onode

        return ret_node

    def reverseKGroup_sol2(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        dummy = jump = ListNode(0)
        dummy.next = l = r = head

        while True:
            count = 0

            while r and count < k:   # use r to locate the range
                r = r.next
                count += 1

            if count == k:  # if size k satisfied, reverse the inner linked list
                pre, cur = r, l

                # 聰明! 學起來~~
                for _ in range(k):
                    cur.next, cur, pre = pre, cur.next, cur  # standard reversing

                jump.next, jump, l = pre, l, r  # connect two k-groups
            else:
                return dummy.next


def build():
    li = ListNode(1)
    li.next = ListNode(2)
    li.next.next = ListNode(3)
    li.next.next.next = ListNode(4)
    li.next.next.next.next = ListNode(5)
    return li, 3


if __name__ == "__main__":

    s = Solution()
    ll = s.reverseKGroup(*build())

    while ll:
        print(ll.val)
        ll = ll.next
