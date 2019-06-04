#!/usr/bin/env python
# -*- coding: utf-8 -*-
# https://leetcode.com/problems/super-ugly-number/description/

"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are
in the given prime list primes of size k.

For example, [1, 2, 4, 7, 8, 13, 14, 16, 19, 26, 28, 32] is the sequence
of the first 12 super ugly numbers given primes = [2, 7, 13, 19] of size 4.

Note:
(1) 1 is a super ugly number for any given primes.
(2) The given numbers in primes are in ascending order.
(3) 0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
(4) The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
"""
import heapq


class Solution(object):

    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        uglies = [1]

        def gen(prime):
            # because it's generator, uglies can be modified during loop.
            for ugly in uglies:
                yield ugly * prime

        generators = map(gen, primes)  # generators

        print("tmp: {0}".format(generators))

        # https://docs.python.org/2/library/heapq.html
        merged = heapq.merge(*generators)

        while len(uglies) < n:
            ugly = next(merged)

            if ugly != uglies[-1]:
                uglies.append(ugly)

        return uglies[-1]


def build_primes():
    prime = [2, 7, 13, 19]
    return prime


if __name__ == "__main__":
    primes = build_primes()
    print("primes: {0}".format(primes))

    s = Solution()
    result = s.nthSuperUglyNumber(3, primes)
    print(result)
