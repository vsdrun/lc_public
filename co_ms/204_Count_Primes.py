#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/count-primes/description/

Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.


Sieve of Eratosthenes:

"""


class Solution(object):
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        primes = [True] * n
        primes[0] = primes[1] = False

        for i in range(2, int(n ** 0.5) + 1):  # 重要!!!
            if primes[i]:  # 因為都是由 n^square 開始 小於n的之前已跑過.
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

    def rewrite(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 2:
            return 0

        primes = [True] * n
        primes[0] = primes[1] = False

        for i in range(2, n):
            x = i

            if primes[i]:
                while x <= n:
                    if i * x < n:
                        primes[i * x] = False
                        x += 1
                        continue
                    break

        print(primes)
        return sum(primes)


def build():
    return 10
    return 2


if __name__ == "__main__":
    s = Solution()
    print(s.countPrimes(build()))
    print(s.rewrite(build()))
