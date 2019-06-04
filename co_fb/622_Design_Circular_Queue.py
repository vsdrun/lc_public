#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/design-circular-queue/

Design your implementation of the circular queue.

The circular queue is a linear data structure in which the operations are
performed based on FIFO (First In First Out) principle and the last position
is connected back to the first position to make a circle.
It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the
spaces in front of the queue.


In a normal queue, once the queue becomes full,
we cannot insert the next element even if there is a space in front of the queue.
But using the circular queue, we can use the space to store new values.


Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.

Front: Get the front item from the queue. If the queue is empty, return -1.

Rear: Get the last item from the queue. If the queue is empty, return -1.

enQueue(value): Insert an element into the circular queue.
    Return true if the operation is successful.

deQueue(): Delete an element from the circular queue.
    Return true if the operation is successful.

isEmpty(): Checks whether the circular queue is empty or not.

isFull(): Checks whether the circular queue is full or not.

Example:
MyCircularQueue(3); // set the size to be 3
circularQueue.enQueue(1);  // return true
circularQueue.enQueue(2);  // return true
circularQueue.enQueue(3);  // return true
circularQueue.enQueue(4);  // return false, the queue is full
circularQueue.Rear();  // return 3
circularQueue.isFull();  // return true
circularQueue.deQueue();  // return true
circularQueue.enQueue(4);  // return true
circularQueue.Rear();  // return 4

Note:
All values will be in the range of [0, 1000].
The number of operations will be in the range of [1, 1000].
Please do not use the built-in Queue library.
"""

# ["MyCircularQueue","enQueue","Front","isFull","enQueue","enQueue","enQueue","deQueue","enQueue","enQueue","isEmpty","Rear"]
#  [[4],[3],[],[],[7],[2],[5],[],[4],[2],[],[]]

class MyCircularQueue(object):
    def __init__(self, k):
        """
        Initialize your data structure here.
        Set the size of the queue to be k.
        :type k: int
        記得先設定 boundary.
        """
        self.Q = [None] * k
        self.B = 0  # contains value of the head, but init. is still at 0 index
        self.E = 0  # do not contains value of the end, exclusive.
        self.FullState = False  # Full state is important.

    def enQueue(self, value):
        """
        Insert an element into the circular queue.
        Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.E == self.B and self.FullState:
            return False

        self.Q[self.E] = value
        if self.E + 1 > len(self.Q) - 1:
            self.E = 0
        else:
            self.E += 1

        if self.B == self.E:
            self.FullState = True

        return True

    def deQueue(self):
        """
        Delete an element from the circular queue.
        Return true if the operation is successful.
        :rtype: bool
        """
        if self.FullState is False and self.B == self.E:
            return False

        if self.B + 1 > len(self.Q) - 1:
            self.B = 0
        else:
            self.B += 1

        self.FullState = False

        return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.B == self.E:
            if not self.FullState:
                return -1

        return self.Q[self.B]


    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.FullState is False:
            if self.B == self.E:
                return -1

        return self.Q[self.E - 1] if self.E > 0 else self.Q[-1]


    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        if self.FullState:
            return False
        else:
            return self.B == self.E

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.FullState



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()



def build():
    return "(*))"


if __name__ == "__main__":
    m = MyCircularQueue(6)
    print("en 6: {} {}:{}".format(m.enQueue(6), m.B, m.E))
    print("rear: {} {}:{}".format(m.Rear(), m.B, m.E))
    print("rear: {} {}:{}".format(m.Rear(), m.B, m.E))
    print("dequeue: {} {}:{}".format(m.deQueue(), m.B, m.E))
    print("enqueue: {} {}:{}".format(m.enQueue(5), m.B, m.E))
    print("rear: {} {}:{}".format(m.Rear(), m.B, m.E))
    print("dequeue: {} {}:{}".format(m.deQueue(), m.B, m.E))
    print("front: {} {}:{}".format(m.Front(), m.B, m.E))
    print("dequeue: {} {}:{}".format(m.deQueue(), m.B, m.E))
    print("dequeue: {} {}:{}".format(m.deQueue(), m.B, m.E))
    print("dequeue: {} {}:{}".format(m.deQueue(), m.B, m.E))
