#!/usr/bin/env python


"""
https://leetcode.com/problems/linked-list-cycle-ii/

Given a linked list,
return the node where the cycle begins. If there is no cycle, return null.

To represent a cycle in the given linked list,
we use an integer pos which represents the position (0-indexed) in
the linked list where tail connects to.
If pos is -1, then there is no cycle in the linked list.


Note: Do not modify the linked list.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: tail connects to node index 1
Explanation: There is a cycle in the linked list, where tail connects to the second node.

Example 2:
Input: head = [1,2], pos = 0
Output: tail connects to node index 0
Explanation: There is a cycle in the linked list, where tail connects to the first node.


Example 3:
Input: head = [1], pos = -1
Output: no cycle
Explanation: There is no cycle in the linked list.

Follow up:
Can you solve it without using extra space?
"""

# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        try:
            # 注意起始邏輯!
            fast = head.next
            slow = head
            while fast is not slow:
                fast = fast.next.next
                slow = slow.next
        except:
            # if there is an exception, we reach the end and there is no cycle
            return None

        # since fast starts at head.next, we need to move slow one step forward
        slow = slow.next
        while head is not slow:
            head = head.next
            slow = slow.next

        return head

def build():
    l3 = ListNode(3)
    l2 = ListNode(2)
    l0 = ListNode(0)
    l4 = ListNode(-4)
    l3.next = l2
    l2.next = l0
    l0.next = l4
    l4.next = l2

    return l3


if __name__ == "__main__":
    s = Solution()
    print(s.detectCycle(build()))
