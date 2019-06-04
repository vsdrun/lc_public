#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/design-phone-directory/

Design a Phone Directory which supports the following operations:

get: Provide a number which is not assigned to anyone.
check: Check if a number is available or not.
release: Recycle or release a number.

Example:
// Init a phone directory containing a total of 3 numbers: 0, 1, and 2.
PhoneDirectory directory = new PhoneDirectory(3);

// It can return any available phone number. Here we assume it returns 0.
directory.get();

// Assume it returns 1.
directory.get();

// The number 2 is available, so return true.
directory.check(2);

// It returns 2, the only number that is left.
directory.get();

// The number 2 is no longer available, so return false.
directory.check(2);

// Release number 2 back to the pool.
directory.release(2);

// Number 2 is available again, return true.
directory.check(2);
"""

class PhoneDirectory(object):
    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """
        self.ns = range(maxNumbers + 1)
        self.ns[0] = float("-inf")


    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        m = max(self.ns)

        if m >= 1:
            self.ns[m] = -m
            return m - 1

        return -1


    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        if 0 <= number < len(self.ns) - 1 and self.ns[number + 1] > 0:
            return True

        return False


    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: None
        """

        if 0 <= number < len(self.ns) - 1:
            if self.ns[number + 1] < 0:
                self.ns[number + 1] = number + 1



# Your PhoneDirectory object will be instantiated and called as such:
# obj = PhoneDirectory(maxNumbers)
# param_1 = obj.get()
# param_2 = obj.check(number)
# obj.release(number)

def build():
    pass


if __name__ == "__main__":
    s = PhoneDirectory(10)
    n = s.get()
    print(n)
    print(s.check(n))
    n = s.get()
    print(n)
    print(s.check(n))
    s.release(n)
    print(s.check(n))
