#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/daily-temperatures/description/

Given a list of daily temperatures, produce a list that,
for each day in the input, tells you how many days you would
have to wait until a warmer temperature.
If there is no future day for which this is possible, put 0 instead.

For example,
given the list temperatures = [73, 74, 75, 71, 69, 72, 76, 73],
your output should be [1, 1, 4, 2, 1, 1, 0, 0].

[73, 74, 75, 71, 69, 72, 76, 73]
[1, 1, 4, 2, 1, 1, 0, 0]

Note: The length of temperatures will be in the range [1, 30000].
Each temperature will be an integer in the range [30, 100].
"""


class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        # 思考:
        # 利用 stack 存 單調函數 decendent numbers
        # 重要!!!
        # 當問題中有 '最近的' 概念時
        # 考慮使用 stack.
        # 或者 recursive call 當作存 stack variable的資訊.
        from collections import defaultdict as dd

        stack = []

        # key: value, value: list of result due to
        # duplicate values.
        result_dmap = dd(dict)

        for i, v in enumerate(temperatures):
            if not stack:
                stack.append((v, i))
                continue

            if v <= stack[-1][0]:
                stack.append((v, i))
            else:
                while stack and v > stack[-1][0]:
                    value, idx = stack.pop()
                    result_dmap[value][idx] = (i - idx)
                stack.append((v, i))

        while stack:
            value, idx = stack.pop()
            result_dmap[value][idx] = 0

        return [result_dmap[v][i] for i, v in enumerate(temperatures)]

    def fast(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """
        n = len(temperatures)
        res = [0] * n

        stack = []

        for i in range(n - 1, -1, -1):

            while stack and temperatures[i] >= temperatures[stack[-1]]:
                stack.pop()

            if stack:
                res[i] = stack[-1] - i

            stack.append(i)

        return res


def build():
    return [89, 62, 70, 58, 47, 47, 46, 76, 100, 70]
    # [8,1,5,4,3,2,1,1,0,0]
    return [73, 74, 75, 71, 69, 72, 76, 73]
    return [73, 74, 75, 71, 69, 69, 72, 76, 73]
    #  [1, 1, 4, 2, 1, 1, 0, 0]


if __name__ == "__main__":

    s = Solution()
    print(s.dailyTemperatures(build()))
