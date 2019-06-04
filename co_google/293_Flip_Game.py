#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/flip-game/description/

You are playing the following Flip Game with your friend:
Given a string that contains only these two characters: + and -,
you and your friend take turns to flip two consecutive "++" into "--".

The game ends when a person can no longer make a move
and therefore the other person will be the winner.

Write a function to compute all possible states of the string
after one valid move.

For example, given s = "++++", after one move,
it may become one of the following states:

[
  "--++",
  "+--+",
  "++--"
]

If there is no valid move, return an empty list [].
"""


class Solution(object):
    def generatePossibleNextMoves(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        return [s[:i] + "--" + s[i + 2:] for i in xrange(len(s) - 1)
                if s[i:i + 2] == '++']


def build():
    return "++++"


if __name__ == "__main__":

    s = Solution()
    result = s.generatePossibleNextMoves(build())
    print(result)
