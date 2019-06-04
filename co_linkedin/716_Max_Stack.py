#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/max-stack/

Design a max stack that supports push, pop, top, peekMax and popMax.

push(x) -- Push element x onto stack.

pop() -- Remove the element on top of the stack and return it.
top() -- Get the element on the top.

peekMax() -- Retrieve the maximum element in the stack.
popMax() -- Retrieve the maximum element in the stack,
    and remove it.

If you find more than one maximum elements, only remove the top-most one.


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

import heapq as hq

class MaxStack(object):
    def __init__(self):
        """
        initialize your data structure here.

        設計:
        stack 與 heap 的 modification 為獨立事件 各自mark各自的tag
        並且在modify時check對方的狀態
        """
        self.s = []  # stack
        self.m = []  # max heap
        self.sset = set()  # 存 s 刪除的 id, value
        self.mset = set()  # 存 m 刪除的 id, value
        self.id = 0  # 記得嗎? 我需要一個id來辨別


    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        self.s.append((x, self.id))
        hq.heappush(self.m, (-x, -self.id))
        self.id += 1


    def pop(self):
        """
        :rtype: int
        """
        if self.top() is not None:
            d = self.s.pop()
            id = d[1]
            val = d[0]

            self.sset.add(id)
            return val


    def top(self):
        """
        :rtype: int
        """
        if self.s:
            while self.s[-1][1] in self.mset:
                self.mset.remove(self.s[-1][1])
                self.s.pop()

            d = self.s[-1]
            val = d[0]
            return val


    def peekMax(self):
        """
        :rtype: int
        """

        if self.m:
            while -self.m[0][1] in self.sset:
                self.sset.remove(-self.m[0][1])
                hq.heappop(self.m)
            return -self.m[0][0]


    def popMax(self):
        """
        :rtype: int
        """
        if self.peekMax() is not None:
            d = hq.heappop(self.m)
            val = -d[0]
            id = -d[1]

            self.mset.add(id)

            return val


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()

#  ["MaxStack","push","peekMax","push","peekMax","push","pop","pop","push","peekMax","push","popMax","top","push","push","peekMax","popMax","popMax"]
#  [[],[92],[],[54],[],[22],[],[],[-57],[],[-24],[],[],[26],[-71],[],[],[]]

def build(cnt):
    pass

if __name__ == "__main__":

    s = MaxStack()
    s.push(92)
    print(s.peekMax()) # 92
    s.push(54)
    print(s.peekMax()) # 92
    s.push(22)
    print(s.pop()) # 22
    print(s.pop()) # 54
    s.push(-57)
    print(s.peekMax()) # 92
    s.push(-24)
    print(s.popMax())  # 92
    print(s.top())  #  -24
    s.push(26)
    s.push(-71)
    print(s.peekMax())
    print(s.popMax())
    print(s.popMax())
