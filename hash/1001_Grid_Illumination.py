#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/grid-illumination/

On a N x N grid of cells, each cell (x, y) with 0 <= x < N and
0 <= y < N has a lamp.

Initially, some number of lamps are on.
lamps[i] tells us the location of the i-th lamp that is on.
Each lamp that is on illuminates every square on its x-axis, y-axis,
and both diagonals (similar to a Queen in chess).

For the i-th query queries[i] = (x, y),
the answer to the query is 1 if the cell (x, y) is illuminated, else 0.

After each query (x, y) [in the order given by queries], we turn off any
lamps that are at cell (x, y) or are adjacent 8-directionally
關掉此query的四周開的燈
(ie., share a corner or edge with cell (x, y).)

Return an array of answers.
Each value answer[i] should be equal to the answer of the i-th query queries[i].


Example 1:

Input: N = 5, lamps = [[0,0],[4,4]], queries = [[1,1],[1,0]]
Output: [1,0]
Explanation:
Before performing the first query we have both lamps [0,0] and [4,4] on.
The grid representing which cells are lit looks like this,
where [0,0] is the top left corner, and [4,4] is the bottom right corner:
1 1 1 1 1
1 1 0 0 1
1 0 1 0 1
1 0 0 1 1
1 1 1 1 1

Then the query at [1, 1] returns 1 because the cell is lit.
After this query, the lamp at [0, 0] turns off, and the grid now looks like this:

1 0 0 0 1
0 1 0 0 1
0 0 1 0 1
0 0 0 1 1
1 1 1 1 1

Before performing the second query we have only the lamp [4,4] on.
Now the query at [1,0] returns 0, because the cell is no longer lit.


Note:
1 <= N <= 10^9
0 <= lamps.length <= 20000
0 <= queries.length <= 20000
lamps[i].length == queries[i].length == 2

https://leetcode.com/problems/grid-illumination/discuss/242899/python-solution-with-Chinese-explanation
https://buptwc.com/2019/02/24/Leetcode-1001-Grid-IIIumination/
"""

class Solution(object):
    def gridIllumination(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        定義 state
        1 light on
        0 no light
        > 1 : ref cnting
        idea of ref counting :-) Use ref counting for cell being illuminated
        """
        result = []
        lightsLoc = set()
        direction = (
                (0, 1), (0, -1), (1, 0), (-1, 0),
                (-1, -1), (-1, 1), (1, -1), (1, 1))
        dmap = [[0] * N for _ in range(N)]

        def travel(x, y, refCnt, direction):
            x += direction[0]
            y += direction[1]

            while 0 <= x < N and 0 <= y < N:
                dmap[x][y] += refCnt
                x += direction[0]
                y += direction[1]


        def light(x, y, state):
            """
            :state: bool
            """
            if state:
                refCnt = 1
                dmap[x][y] += refCnt

                for d in direction:
                    travel(x, y, refCnt, d)
            else:
                refCnt = -1
                dmap[x][y] += refCnt

                for d in direction:
                    travel(x, y, refCnt, d)

        def turnOff(x, y, direction):
            nx, ny = x + direction[0], y + direction[1]

            if (nx, ny) in lightsLoc:
                light(nx, ny, False)
                lightsLoc.remove((nx, ny))


        for l in lamps:
            light(l[0], l[1], True)
            lightsLoc.add((l[0], l[1]))

        #  print(dmap)

        for q in queries:
            result.append(1 if dmap[q[0]][q[1]] > 0 else 0)

            if (q[0], q[1]) in lightsLoc:
                light(q[0], q[1], False)
                lightsLoc.remove((q[0], q[1]))

            for d in direction:
                turnOff(q[0], q[1], d)


        #  print(dmap)
        return result

    def rewrite(self, N, lamps, queries):
        """
        :type N: int
        :type lamps: List[List[int]]
        :type queries: List[List[int]]
        :rtype: List[int]
        定義 state
        1 light on
        0 no light
        > 1 : ref cnting
        idea of ref counting :-) Use ref counting for cell being illuminated
        """
        from collections import Counter
        lamps = list(map(tuple, lamps))
        light_set = set(lamps)
        horizontal = Counter()  # 横
        vertical = Counter()    # 竖
        l_oblique = Counter()   # 左斜
        r_oblique = Counter()   # 右斜

        for x, y in lamps:
            horizontal[x] += 1
            vertical[y] += 1
            l_oblique[x+y] += 1
            r_oblique[y-x] += 1

        res = []
        for x,y in queries:
            if x in horizontal or y in vertical or x+y in l_oblique or y-x in r_oblique:
                res.append(1)
            else:
                res.append(0)
            for dx in [-1, 0 ,1]:
                for dy in [-1, 0, 1]:
                    xpos, ypos = x + dx, y + dy
                    if (xpos, ypos) in light_set: # 如果附近有灯，则熄灭，修改4个集合的内部值
                        light_set.remove((xpos, ypos))
                        horizontal[xpos] -= 1
                        if horizontal[xpos] == 0: del horizontal[xpos]

                        vertical[ypos] -= 1
                        if vertical[ypos] == 0: del vertical[ypos]

                        l_oblique[xpos+ypos] -= 1
                        if l_oblique[xpos+ypos] == 0: del l_oblique[xpos+ypos]

                        r_oblique[ypos-xpos] -= 1
                        if r_oblique[ypos-xpos] == 0: del r_oblique[ypos-xpos]
        return res

def build():
    return 5, [[0,0],[4,4]], [[1,1],[1,0]]


if __name__ == "__main__":
    s = Solution()
    print(s.gridIllumination(*build()))
