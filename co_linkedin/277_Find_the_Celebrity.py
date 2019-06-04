#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/find-the-celebrity/description/


Suppose you are at a party with n people (labeled from 0 to n - 1)
and among them, there may exist one celebrity.

The definition of a celebrity is that all the other n - 1
people know him/her but he/she does not know any of them.

Now you want to find out who the celebrity is or verify that there is not one.
The only thing you are allowed to do is to ask questions like:
"Hi, A. Do you know B?" to get information of whether A knows B.

You need to find out the celebrity (or verify there is not one)
by asking as few questions as possible (in the asymptotic sense).

You are given a helper function bool knows(a, b) which tells you
whether A knows B.

Implement a function int findCelebrity(n),
your function should minimize the number of calls to knows.

Note: There will be exactly one celebrity if he/she is in the party.
Return the celebrity's label if there is a celebrity in the party.
If there is no celebrity, return -1.

"""


# The knows API is already defined for you.
# @param a, person a
# @param b, person b
# @return a boolean, whether a knows b
def knows(a, b):
    other = {0: True,
             1: True,
             2: True,
             4: True}
    if a in other and b == 3:
        return True
    else:
        return False


class Solution(object):
    def findCelebrity(self, n):
        """
        :type n: int
        :rtype: int
        1. pick a candidate
        2. test if candidate knows anyone
        """

        candidate = 0

        #  candidate only doesn't know > candidate number
        for i in xrange(1, n):
            if knows(candidate, i):
                candidate = i

        for i in xrange(n):
            if i != candidate:
                if not knows(i, candidate) or knows(candidate, i):
                    return -1

        return candidate


def build():
    return 5


if __name__ == "__main__":

    s = Solution()
    result = s.findCelebrity(build())

    print(result)
