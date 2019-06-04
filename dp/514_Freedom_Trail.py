#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/freedom-trail/description/
"""


class Solution(object):
    def findRotateSteps(self, ring, key):
        """
        :type ring: str
        :type key: str
        :rtype: int
        """
        from collections import defaultdict

        # the distance between two points (i, j) on the ring
        def dist(i, j):
            # 往前/往後 熟近
            return min(abs(i - j), len(ring) - abs(i - j))

        # build the position list for each character in ring
        pos = defaultdict(list)

        for i, c in enumerate(ring):
            pos[c].append(i)

        # the current possible state: {position of the ring: the cost}
        state = {}
        state[0] = 0

        for c in key:
            temp_state = {}

            for j in pos[c]:  # every possible target position
                temp_state[j] = float('inf')

                for i in state:  # every possible start position 注意
                    # 此為update過的state 即current
                    # key的上一個key的可以開始位置.
                    # i is key for dict: state
                    temp_state[j] = min(temp_state[j], dist(i, j) + state[i])

            state = temp_state

        return min(state.values()) + len(key)


def build_input():
    return "godding", "gd"


if __name__ == "__main__":
    ring, key = build_input()

    s = Solution()
    result = s.findRotateSteps(ring, key)

    print(result)
