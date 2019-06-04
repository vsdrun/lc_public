#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/lonely-pixel-i/description/


Given a picture consisting of black and white pixels,
find the number of black lonely pixels.

The picture is represented by a 2D char array consisting of 'B' and 'W',
which means black and white pixels respectively.

A black lonely pixel is character 'B' that located at a specific position
where the same row and same column don't have any other black pixels.

Example:
Input:
[['W', 'W', 'B'],
 ['W', 'B', 'B'],
 ['B', 'W', 'W']]

Output: 3
Explanation: All the three 'B's are black lonely pixels.
"""


class Solution(object):
    def findLonelyPixel(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        from __builtin__ import xrange

        direction = ((1, 0), (-1, 0), (0, -1), (0, 1))

        cnt = 0

        def count(pos, dirct):
            x, y = pos
            mx, my = dirct

            x += mx
            y += my

            while 0 <= x < len(picture) and \
                    0 <= y < len(picture[0]):
                if picture[x][y] == 'B' or picture[x][y] == 'C':
                    picture[x][y] = 'C'
                    return True

                x += mx
                y += my

            return False

        def check(i, j):
            if picture[i][j] == 'B':
                picture[i][j] = 'C'

            for d in direction:
                if count((i, j), d):
                    return False

            return True

        for i in xrange(len(picture)):
            for j in xrange(len(picture[0])):
                if picture[i][j] == 'B':
                    if check(i, j):
                        cnt += 1

        return cnt

    def lc_answer(self, picture):
        """
        :type picture: List[List[str]]
        :rtype: int
        """
        return sum(col.count('B') == 1 == picture[col.index('B')].count('B')
                   for col in zip(*picture))


def build():
    return [['W', 'W', 'B'],
            ['W', 'B', 'B'],
            ['B', 'W', 'B']]


if __name__ == "__main__":
    s = Solution()
    print(s.findLonelyPixel(build()))
