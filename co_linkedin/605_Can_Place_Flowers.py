#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/can-place-flowers/description/


Suppose you have a long flowerbed in which some of the plots are
planted and some are not.


However, flowers cannot be planted in adjacent plots -
they would compete for water and both would die.


Given a flowerbed (represented as an array containing 0 and 1,
where 0 means empty and 1 means not empty),
and a number n,
return if n new flowers can be planted in it without violating
the no-adjacent-flowers rule.


Example 1:
Input: flowerbed = [1,0,0,0,1], n = 1
Output: True

Example 2:
Input: flowerbed = [1,0,0,0,1], n = 2
Output: False
"""


class Solution(object):
    def canPlaceFlowers(self, flowerbed, n):
        """
        :type flowerbed: List[int]
        :type n: int
        :rtype: bool
        """

        cnt = n

        for i in xrange(len(flowerbed)):
            if flowerbed[i] == 1:
                continue

            if cnt and flowerbed[i if i == 0 else i - 1] == 0 and \
                    flowerbed[i + 1 if i + 1 < len(flowerbed) else i] == 0:
                cnt -= 1
                flowerbed[i] = 1

            if cnt == 0:
                break

        if not cnt:
            return True
        else:
            return False


def build():
    return [1, 0, 0, 0, 1], 2
    return [0, 0, 1, 0, 1], 1
    return [1, 0, 0, 0, 1], 1


if __name__ == "__main__":

    s = Solution()
    result = s.canPlaceFlowers(*build())

    print(result)
