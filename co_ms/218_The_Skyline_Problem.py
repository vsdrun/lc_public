#!/usr/bin/env python


"""
https://leetcode.com/problems/the-skyline-problem/description/

A city's skyline is the outer contour of the silhouette formed by all the
buildings in that city when viewed from a distance. Now suppose you are given
the locations and height of all the buildings as shown on a cityscape photo
(Figure A), write a program to output the skyline formed by these buildings
collectively (Figure B).

The geometric information of each building is represented by a triplet of
integers [Li, Ri, Hi],
where Li and Ri are the x coordinates of the left and right edge of the ith
building, respectively, and Hi is its height.

It is guaranteed that 0 ≤ Li, Ri ≤ INT_MAX, 0 < Hi ≤ INT_MAX, and Ri - Li > 0.
You may assume all buildings are perfect rectangles grounded on an absolutely
flat surface at height 0.

For instance, the dimensions of all buildings in Figure A are recorded as:
[ [2 9 10], [3 7 15], [5 12 12], [15 20 10], [19 24 8] ] .


The output is a list of "key points" (red dots in Figure B) in the format of
[ [x1,y1], [x2, y2], [x3, y3], ... ] that uniquely defines a skyline.
A key point is the left endpoint of a horizontal line segment.
Note that the last key point, where the rightmost building ends,
is merely used to mark the termination of the skyline, and always has zero height.
Also, the ground in between any two adjacent buildings should be considered
part of the skyline contour.

For instance, the skyline in Figure B should be represented as:
[ [2 10], [3 15], [7 12], [12 0], [15 10], [20 8], [24, 0] ].

Notes:

The number of buildings in any input list is guaranteed to be in the range [0, 10000].
The input list is already sorted in ascending order by the left x position Li.
The output list must be sorted by the x position.
There must be no consecutive horizontal lines of equal height in the output skyline.
For instance, [...[2 3], [4 5], [7 5], [11 5], [12 7]...] is not acceptable;
the three lines of height 5 should be merged into one in the final output as such:
[...[2 3], [4 5], [12 7], ...]

"""
import heapq


class Solution(object):

    def getSkyline(self, LRH):
        """
        :type LRH: List[List[int]]
        :rtype: List[List[int]]
        !!! 沒有y的概念 只有左右X. y就是高.
        """
        skyline = []  # 存結果, (x, 高)

        i = 0

        n = len(LRH)  # how many buildings

        # 存的格式: (高，最右)
        # 最終liveHR要全部被pop up.
        # 一個liveHR 為一個所有building的set 新的set為新的liveHR,
        # 之前的liveHR會被pop up清空.
        liveHR = []  # list for building the heap. [[高, 右X]]

        while i < n or liveHR:
            """
            用 '-' 因為python 內建的heapq為min heap, 而此我們需要MaxHeap.
            """
            # 處理一個區塊.
            if not liveHR or i < n and LRH[i][0] <= -liveHR[0][1]:
                """
                1. 初始
                2. 同一個building set.
                """
                x = LRH[i][0]  # the X of this building.

                while i < n and LRH[i][0] == x:
                    # This while loop is saving building that has
                    # same X location into max-heap.
                    # save height and Y.
                    # using - since heapq is a min-heap.
                    # we need max-heap.
                    # (height, Y)
                    heapq.heappush(liveHR, (-LRH[i][2], -LRH[i][1]))
                    i += 1
            # 要進入下一個區塊 所以先把前一區快做個整理.
            else:
                """
                liveHR 是以 (最高, 最右) 作為排序單位
                """
                x = -liveHR[0][1]
                while liveHR and -liveHR[0][1] <= x:
                    heapq.heappop(liveHR)

            """
            不管在哪個區塊 都做skyline的結果處裡
            """
            height = len(liveHR) and -liveHR[0][0]

            if not skyline or height != skyline[-1][1]:
                skyline += [x, height],

        return skyline


def build():
    return [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]


if __name__ == "__main__":
    s = Solution()
    result = s.getSkyline(build())
    print(result)
