#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/two-sum-iii-data-structure-design/description/

Design and implement a TwoSum class.
It should support the following operations: add and find.

add - Add the number to an internal data structure.
find - Find if there exists any pair of numbers which sum is equal to the value.

For example,
add(1); add(3); add(5);
find(4) -> true
find(7) -> false
"""


class TwoSum(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.ts = dict()
        self.cache = dict()

    def add(self, number):
        """
        Add the number to an internal data structure..
        :type number: int
        :rtype: void
        """
        # 注意同一個數必須出現一次以上才能成pair
        if self.ts.get(number, False):
            self.ts[number] += 1
        else:
            self.ts[number] = 1

    def find(self, value):
        """
        Find if there exists any pair of numbers which sum is equal to the value.
        :type value: int
        :rtype: bool
        """
        if not self.ts:
            return False

        if self.cache.get(value, False):
            return True

        for n in self.ts:
            if (value - n) in self.ts and (value - n != n or
                                           self.ts[(value - n)] > 1):
                self.cache[value] = True
                return True

        return False


# Your TwoSum object will be instantiated and called as such:
# obj = TwoSum()
# obj.add(number)
# param_2 = obj.find(value)


def build(cnt):
    return "makes", "coding"


if __name__ == "__main__":

    s = TwoSum()
    s.add(3)
    s.add(4)
    s.add(1)
    s.add(-7)
    s.add(9)
    s.add(1)
    s.add(1)
    print(s.find(10))
    print(s.find(10))
    print(s.find(-3))
    print(s.find(5))
    print(s.find(15))
