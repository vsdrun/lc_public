#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/max-stack/description/

Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.
pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.
peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack, and remove it. If you find more than one maximum elements, only remove the top-most one.
Example 1:
MaxStack stack = new MaxStack();
stack.push(5); 
stack.push(1);
stack.push(5);
stack.top(); -> 5
stack.popMax(); -> 5
stack.top(); -> 1
stack.peekMax(); -> 5
stack.pop(); -> 1
stack.top(); -> 5

Note:
-1e7 <= x <= 1e7
Number of operations won't exceed 10000.
The last four operations won't be called when stack is empty.
"""


class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        

    def pop(self):
        """
        :rtype: int
        """
        

    def top(self):
        """
        :rtype: int
        """
        

    def peekMax(self):
        """
        :rtype: int
        """
        

    def popMax(self):
        """
        :rtype: int
        """
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

def build():
    result = [['1', '1', '1', '1', '0'],
              ['1', '1', '0', '1', '0'],
              ['1', '1', '0', '0', '0'],
              ['0', '0', '0', '0', '0']]

    result = [['1', '1', '0', '0', '0'],
              ['1', '1', '0', '0', '0'],
              ['0', '0', '1', '0', '0'],
              ['0', '0', '0', '1', '1']]
    return result


if __name__ == "__main__":
    s = Solution()
