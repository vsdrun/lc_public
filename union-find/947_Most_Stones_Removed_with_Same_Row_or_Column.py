#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/

On a 2D plane, we place stones at some integer coordinate points.
Each coordinate point may have at most one stone.

Now, a move consists of removing a stone that shares a column or
row with another stone on the grid.

What is the largest possible number of moves we can make?


Example 1:
Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
Output: 5

X X 0 0 0 0 0
X 0 X 0 0 0 0
0 X X 0 0 0 0
=>
wrong: (0, 1), (1, 2), (0, 0), (2, 1)
M M 0 0 0 0 0
X 0 M 0 0 0 0
0 M X 0 0 0 0

Example 2:
Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
Output: 3


Example 3:
Input: stones = [[0,0]]
Output: 0

Note:
1 <= stones.length <= 1000
0 <= stones[i][j] < 10000

https://leetcode.com/problems/most-stones-removed-with-same-row-or-column/discuss/197668/Count-the-Number-of-Islands-O(N)
"""


class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        將 row, col 個別看成自成一點
        """
        UF = {}

        def find(x):
            if x != UF[x]:
                UF[x] = find(UF[x])
            return UF[x]

        def union(x, y):
            UF.setdefault(x, x)
            UF.setdefault(y, y)
            UF[find(x)] = find(y)

        for i, j in points:
            union(i, ~j)

        # 所有的point 減去 無法去除的點(也就是一個相連的區域會潰縮成一個點)
        return len(points) - len({find(x) for x in UF})


def build():
    """
    0 X
    X X
    """
    return [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
    return [[0,1],[1,0],[1,1]]

if __name__ == "__main__":
    s = Solution()
    print(s.removeStones(build()))
