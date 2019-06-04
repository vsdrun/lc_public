#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
https://leetcode.com/problems/queue-reconstruction-by-height/description/

Suppose you have a random list of people standing in a queue. Each
person is described by a pair of integers (h, k), where h is the height
of the person and k is the number of people in front of this person who
have a height greater than or equal to h.

Write an algorithm to reconstruct the queue.

Note:
The number of people is less than 1,100.

Example
Input:
[[7,0], [4,4], [7,1], [5,0], [6,1], [5,2]]

Output:
[[5,0], [7,0], [5,2], [6,1], [4,4], [7,1]]

1. sort people from min -> max
[7,0] [7,1] [6,1] [5,0] [5,2] [4,4]

2. insert from their k value index
[5,0] [7,0] [5,2] [6,1] [4,4] [7,1]
"""


class Solution(object):

    def reconstructQueue(self, people):
        """
        :type people: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        # reason?
        # we sort h from big->small, k from small->big
        people.sort(key=lambda (h, k): (-h, k))

        # 從大至小排序 因要求大的在前
        # 也就是[4,4]在insert至位置4時，確保前面均是大於p[0], 也就是4.
        # 因為大的在前面啊
        # 端看數組前面有幾個，便將自己放入 '幾個 + 1' 的位置
        # [[7, 0], [7, 1], [6, 1], [5, 0], [5, 2], [4, 4]]
        print(people)

        for p in people:
            # 由 index p[1] insert
            result.insert(p[1], p)

        return result


def build_input():
    return [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]


if __name__ == "__main__":
    n = build_input()
    s = Solution()
    result = s.reconstructQueue(n)
    print(result)
