#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/trapping-rain-water/description/

Given n non-negative integers representing an elevation map where
the width of each bar is 1,
compute how much water it is able to trap after raining.

For example,
Given [0,1,0,2,1,0,1,3,2,1,2,1], return 6.
"""


class Solution(object):

    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        """
        Idea:
        1. l < r , progressing l or r base on which one is shorter.
        2. Reason? because the higher one would definitely cover the
            lower one's volume.
        """
        """
        int trap(vector<int>& height) {
            int l = 0, r = height.size()-1, level = 0, water = 0;
            while (l < r) {
                int lower = height[height[l] < height[r] ? l++ : r--];
                level = max(level, lower);
                water += level - lower;
            }
            return water;
        }
        """
        l = 0
        r = len(height) - 1
        level = 0  # 前次
        lower = 0  # 此次
        water = 0

        while l < r:
            if height[l] < height[r]:
                lower = height[l]
                l += 1
            else:
                lower = height[r]
                r -= 1

            level = max(lower, level)
            water += (level - lower)

        return water

    def rewrite(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        # 將 idx 列出來

        lidx = 0
        ridx = len(height) - 1

        current_level = 0  # moving idx 會比 local max 小...
        maximum_local_level = 0
        water_captured = 0

        while lidx < ridx:
            # 一個while loop 嘗試解決什麼問題?
            # 找最低的 並且紀錄其低點
            # moving idx forward

            if height[lidx] < height[ridx]:
                current_level = height[lidx]
                lidx += 1
            else:  # >=
                current_level = height[ridx]
                ridx -= 1

            maximum_local_level = max(maximum_local_level, current_level)
            water_captured += (maximum_local_level - current_level)

        return water_captured


def build():
    return [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]


if __name__ == "__main__":
    s = Solution()
    print(s.trap(build()))
    print(s.rewrite(build()))
