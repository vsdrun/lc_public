#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/keys-and-rooms/description/

There are N rooms and you start in room 0.
Each room has a distinct number in 0, 1, 2, ..., N-1,
and each room may have some keys to access the next room.

Formally, each room i has a list of keys rooms[i],
and each key rooms[i][j] is an integer in [0, 1, ..., N-1]
where N = rooms.length.

A key rooms[i][j] = v opens the room with number v.

Initially, all the rooms start locked (except for room 0).

You can walk back and forth between rooms freely.

Return true if and only if you can enter every room.

Example 1:
Input: [[1],[2],[3],[]]
Output: true

Explanation:
We start in room 0, and pick up key 1.
We then go to room 1, and pick up key 2.
We then go to room 2, and pick up key 3.
We then go to room 3.  Since we were able to go to every room, we return true.


Example 2:
Input: [[1,3],[3,0,1],[2],[0]]
Output: false
Explanation: We can't enter the room with number 2.
"""


class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        from collections import defaultdict as dd
        # bulid graph and erase + what's left

        dmap = dd(list)

        for x, y in enumerate(rooms):
            dmap[x].extend(y)

        def dfs(node):
            if node not in dmap:
                return

            child = dmap.pop(node)

            for c in child:
                dfs(c)

        for n in list(dmap):
            dfs(n)
            if dmap:
                return False
            else:
                return True


def build():
    return [[1], [2], [3], []]  # True
    return [[1, 3], [3, 0, 1], [2], [0]]  # false


if __name__ == "__main__":
    s = Solution()
    print(s.canVisitAllRooms(build()))
