#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/judge-route-circle/description/

Initially, there is a Robot at position (0, 0).
Given a sequence of its moves, judge if this robot makes a circle,
which means it moves back to the original place.

The move sequence is represented by a string.
And each move is represent by a character.
The valid robot moves are R (Right), L (Left), U (Up) and D (down).
The output should be true or false representing whether the robot
makes a circle.

Example 1:
Input: "UD"
Output: true

Example 2:
Input: "LL"
Output: false
"""


class Solution(object):
    def judgeCircle(self, moves):
        return (moves.count('L') == moves.count('R')) and \
            (moves.count('U') == moves.count('D'))

    def judgeCircle_stupid(self, moves):
        """
        :type moves: str
        :rtype: bool
        """
        init = [0, 0]

        moves = list(moves)

        dmap = dict((('U', (1, 0)), ('D', (-1, 0)),
                     ('R', (0, 1)), ('L', (0, -1))))

        while moves:
            mv = moves.pop(0)
            init = [init[0] + dmap[mv][0], init[1] + dmap[mv][1]]

        if init == [0, 0]:
            return True
        else:
            return False


def build():
    return "UDDDD"


if __name__ == "__main__":

    s = Solution()
    result = s.judgeCircle(build())
    print(result)
