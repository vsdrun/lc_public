#!/usr/bin/env python


"""
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x, nxt):
        self.val = x
        self.next = nxt


class stack(object):
    def __init__(self):
        self.head = None

    def pop(self):
        if self.head:
            tmp_v = self.head.val
            self.head = self.head.next
            return tmp_v

    def push(self, val):
        ln = ListNode(val, self.head)
        self.head = ln


def build():
    pass


if __name__ == "__main__":
    s = stack()
    s.push(10)
    s.push(20)
    s.push(30)
    print(s.pop())
    print(s.pop())
    print(s.pop())
    print(s.pop())
