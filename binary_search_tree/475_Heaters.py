#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/heaters/description/

Design a standard heater with fixed warm radius to warm all the houses.

Given positions of houses and heaters on a horizontal line,
find out minimum radius of heaters so that all houses could
be covered by those heaters.

input will be the positions of houses and heaters seperately,
and your expected output will be the minimum radius standard of heaters.

Note:
Numbers of houses and heaters you are given are
non-negative and will not exceed 25000.

Positions of houses and heaters you are given are
non-negative and will not exceed 10^9.

As long as a house is in the heaters' warm radius range, it can be warmed.
All the heaters follow your radius standard and the warm radius will the same.

Example 1:
Input: [1,2,3],[2]
Output: 1

Explanation: The only heater was placed in the position 2, and if we use the
radius 1 standard, then all the houses can be warmed.

Example 2:
Input: [1,2,3,4],[1,4]
Output: 1
Explanation: The two heater was placed in the position 1 and 4. We need to use
radius 1 standard, then all the houses can be warmed.
"""


class Solution(object):

    def findRadius(self, houses, heaters):
        """
        :type houses: List[int]
        :type heaters: List[int]
        :rtype: int
        """
        heaters = sorted(heaters) + [float('inf')]
        i = r = 0

        # i is used as house x's closest heater's index.
        for x in sorted(houses):
            print("x: {}".format(x))
            while x >= sum(heaters[i:i + 2]) / 2.:
                print("i: {}".format(x))
                i += 1

            r = max(r, abs(heaters[i] - x))

        return r


def build_pos():
    return [1, 2, 3, 4, 5, 6], [4, 6]
    return [1, 1, 1, 1, 1, 1, 999, 999, 999, 999, 999], [499, 500, 501]


if __name__ == "__main__":
    house, heater = build_pos()

    s = Solution()
    result = s.findRadius(house, heater)

    # 498
    print(result)
