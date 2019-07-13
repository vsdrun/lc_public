#!/usr/bin/env python


"""
https://leetcode.com/problems/linked-list-cycle/description/

Given a linked list, determine if it has a cycle in it.

Follow up:
Can you solve it without using extra space?

一、尋找循環長度的倍數：
龜兔從起點同時出發，龜走一步、兔就走兩步。由於兔比龜快，
當龜兔皆進入循環之中，兔必然領先數圈、從後方追上龜。

當龜兔相遇，龜兔的行走距離差，即是循環長度的倍數。龜一倍速、兔兩倍速，
龜兔的行走距離差，剛好是龜的行進距離。龜的行進距離即是循環長度的倍數。

二、尋找循環起點：
龜退回起點，兔原地待命，龜兔同時出發，龜走一步、兔走一步。
龜兔相遇之處即是循環起點。

三、尋找循環長度：
從循環之中任意一處出發，一次走一步，繞一圈回到原處，即得循環長度。
"""

# Definition for singly-linked list.


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """

        if not head:
            return False

        first = head
        second = head.next.next if head.next else None

        if not second:
            return False

        while first != second:
            first = first.next
            second = second.next.next if second.next else None

            if not second:
                return False
        return True

    def rewrite(self, head):
        """
        :type head: ListNode
        :rtype: bool
        Best solution :-)
        """
        # double pase
        fwd = ohead = head

        cnt = 0

        while fwd and cnt < 2:
            fwd = fwd.next
            cnt += 1

        while fwd and fwd != head:
            fwd = fwd.next.next if fwd.next else None
            head = head.next

        if fwd == head and fwd != None:
            return True
        return False

def build():
    return None
    l1 = ListNode(1)
    #  return l1
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next = l2
    l2.next = l3
    l3.next = l4
    l4.next = l5
    l5.next = l3
    return l1


if __name__ == "__main__":
    s = Solution()
    print(s.hasCycle(build()))
    print(s.rewrite(build()))
