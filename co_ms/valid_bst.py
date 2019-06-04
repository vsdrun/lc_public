#!/usr/bin/env python
# -*- coding: utf-8 -*-


class TN(object):
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def build():
#       50
#     /    \
#  30       60
# /  \     /  \ 
#5   20   45    70
#              /  \
#            65    80

    root = TN(50)
    root.left = TN(30)
    root.left.left = TN(5)
    root.left.right = TN(20)

    root.right = TN(60)
    root.right.left = TN(45)
    root.right.right = TN(70)
    root.right.right.left = TN(65)
    root.right.right.left.left = TN(63)
    root.right.right.right = TN(80)
    return root

MN = float("-inf")
MX = float("inf")

GMAX = [float("-inf")]

def check(node):
    """
    :ret: bool
    """
    if not node:
        return None, None, 0

    llmax = llmin = rrmax = rrmin = None
    llmin, llmax, lcnt = check(node.left)
    rrmin, rrmax, rcnt = check(node.right)

    if llmin is None:
        llmin = node
    if rrmax is None:
        rrmax = node

    if llmax is None:
        llmax = node

    if rrmin is None:
        rrmin = node

    tcnt = lcnt + rcnt

    if llmax and rrmin and llmax.val <= node.val <= rrmin.val:
        tcnt += 1
        GMAX[0] = max(GMAX[0], tcnt)

    return llmin, rrmax, tcnt # this node cnt


if __name__ == "__main__":
    check(build())
    print(GMAX[0])
