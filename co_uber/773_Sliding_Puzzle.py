#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/sliding-puzzle/

On a 2x3 board, there are 5 tiles represented by the integers 1 through 5,
and an empty square represented by 0.

A move consists of choosing 0 and a 4-directionally adjacent
number and swapping it.

The state of the board is solved if and only if the board is
[[1,2,3],[4,5,0]].

Given a puzzle board, return the least number of moves required so that the
state of the board is solved.

If it is impossible for the state of the board to be solved, return -1.

Examples:

Input: board = [[1,2,3],[4,0,5]]
Output: 1
Explanation: Swap the 0 and the 5 in one move.

Input: board = [[1,2,3],[5,4,0]]
Output: -1
Explanation: No number of moves will make the board solved.

Input: board = [[4,1,2],[5,0,3]]
Output: 5
Explanation: 5 is the smallest number of moves that solves the board.

An example path:
After move 0: [[4,1,2],[5,0,3]]
After move 1: [[4,1,2],[0,5,3]]
After move 2: [[0,1,2],[4,5,3]]
After move 3: [[1,0,2],[4,5,3]]
After move 4: [[1,2,0],[4,5,3]]
After move 5: [[1,2,3],[4,5,0]]

Input: board = [[3,2,4],[1,5,0]]
Output: 14
Note:

board will be a 2 x 3 array as described above.
board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].
"""

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        The state of the board is solved if and only if the board is
        [[1,2,3],
         [4,5,0]].
        """

        def swap(qstr, idx1, idx2):
            lstr = list(qstr)
            lstr[idx1], lstr[idx2] = lstr[idx2], lstr[idx1]
            return "".join(lstr)

        target = "123450"
        # where 0 can go @ this idx position
        direct = ((1, 3), (0, 2, 4), (1, 5), (0, 4), (1, 3, 5), (2, 4))

        start = "".join(
                str(board[i][j])
                for i in range(len(board)) for j in range(len(board[0])))

        queue = [start]
        ret = 0
        visited = set()
        visited.add(start)

        while queue:
            tmp = []

            for q in queue:
                if q == target:
                    return ret

                zidx = q.index("0")

                for d in direct[zidx]:
                    nstr = swap(q, zidx, d)

                    if nstr not in visited:
                        tmp.append(nstr)
                        visited.add(nstr)

            ret += 1
            queue = tmp

        return -1

def build():
    return [[1,2,3],
            [5,4,0]]  # -1
    return [[1,2,3],
            [4,0,5]]  # 1
    return [[4,1,2],
            [5,0,3]]  # 5

if __name__ == "__main__":
    s = Solution()
    print(s.slidingPuzzle(build()))
