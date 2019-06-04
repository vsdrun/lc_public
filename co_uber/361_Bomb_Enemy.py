#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/bomb-enemy/

Given a 2D grid, each cell is either a wall 'W',
an enemy 'E' or empty '0' (the number zero),
return the maximum enemies you can kill using one bomb.

The bomb kills all the enemies in the same row and column from
the planted point until it hits the wall since the wall
is too strong to be destroyed.

Note that you can only put the bomb at an empty cell.


Example:
For the given grid

0 E 0 0
E 0 W E
0 E 0 0

return 3. (Placing a bomb at (1,1) kills 3 enemies)
"""


class Solution(object):
    def maxKilledEnemies(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        def hits(grid):
            #  [[2, 2, 2, 0, 0], [1, 1, 0, 1, 0], [1, 1, 0, 1, 0]]
            # final adds [0] due to count 'E's and add [0] as wall slot.

            result = []
            for row in grid:
                tmp = []
                for block in "".join(row).split("W"):
                    Ecnt = block.count("E")
                    blocks = [Ecnt] * len(block) + [0] # add rightmost wall
                    tmp.extend(blocks)

                result.append(tmp)
            return result

        rowhits = hits(grid)
        #  print("rowhits: {}".format(rowhits))

        # turn 90 degrees
        turnedGrid = zip(*grid)
        colhits = hits(turnedGrid)
        # count 完轉回成 row based.
        colhits = zip(*colhits)

        result = 0

        for row in zip(grid, rowhits, colhits):
            #  print("row: {}".format(row))

            for cell, rh, ch in zip(*row):
                #  print("cell :{} rh: {} ch: {}".format(cell, rh, ch))

                if cell == '0':
                    result = max(result, rh + ch)

        return result


def build():
    return [["0", "E", "E", "W"],
            ["E", "0", "W", "E"],
            ["0", "E", "W", "E"]]


if __name__ == "__main__":
    s = Solution()
    print(s.maxKilledEnemies(build()))
