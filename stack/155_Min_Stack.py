#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/min-stack/description/
easy.

Design a stack that supports push, pop, top,
and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        if self.stack:
            if x > self.stack[-1][1]:
                self.stack += (x, self.stack[-1][1]),
                return
        self.stack += (x, x),

    def pop(self):
        """
        :rtype: void
        """
        val, _ = self.stack.pop()
        return val

    def top(self):
        """
        :rtype: int
        """
        val, _ = self.stack[-1]
        return val

    def getMin(self):
        """
        :rtype: int
        """
        _, min = self.stack[-1]
        return min


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == "__main__":
    m = MinStack()
    m.push(-10)
    m.push(3)
    m.push(-27)
    m.push(7)
    v = m.pop()
    print(v)
    print(m.getMin())
