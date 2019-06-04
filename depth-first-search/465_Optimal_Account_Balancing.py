#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/optimal-account-balancing/

A group of friends went on holiday and sometimes lent each other money.
For example, Alice paid for Bill's lunch for $10.
Then later Chris gave Alice $5 for a taxi ride.
We can model each transaction as a tuple (x, y, z)
which means person x gave person y $z.
Assuming Alice, Bill, and Chris are person 0, 1, and 2 respectively
(0, 1, 2 are the person's ID),
the transactions can be represented as [[0, 1, 10], [2, 0, 5]].

Given a list of transactions between a group of people,
return the minimum number of transactions required to settle the debt.

Minimum? 想到 bfs? 不.. 使用dfs 每個dfs 做一個min(current, dfs())

Note:

A transaction will be given as a tuple (x, y, z). Note that x ≠ y and z > 0.
Person's IDs may not be linear,
e.g. we could have the persons 0, 1, 2 or
we could also have the persons 0, 2, 6.

Example 1:
Input:
[[0,1,10], [2,0,5]]

Output:
2

Explanation:
Person #0 gave person #1 $10.
Person #2 gave person #0 $5.

Two transactions are needed.
One way to settle the debt is person #1 pays person #0 and #2 $5 each.

Example 2:

Input:
[[0,1,10], [1,0,1], [1,2,5], [2,0,5]]

Output:
1

Explanation:
Person #0 gave person #1 $10.
Person #1 gave person #0 $1.
Person #1 gave person #2 $5.
Person #2 gave person #0 $5.

Therefore, person #1 only need to give person #0 $4, and all debt is settled.

https://leetcode.com/problems/optimal-account-balancing/discuss/95355/11-liner-9ms-DFS-solution-(detailed-explanation)
"""


class Solution(object):
    def minTransfers(self, transactions):
        """
        :type transactions: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict as dd

        dmap = dd(int)

        tt = transactions

        for t in tt:
            dmap[t[0]] -= t[2]
            dmap[t[1]] += t[2]

        debt = dmap.values()
        print("debt: {}".format(debt))

        # [-5, 10, -5]

        def dfs(s):
            # s is index
            print("debt: {}".format(debt))

            # 跳過沒有debt的
            while(s < len(debt) and debt[s] == 0):
                s+=1

            print("s: {}".format(s))
            print("---")

            # stops moving index
            if s == len(debt):
                return 0

            # 重要! 即跳過則max, 不會被考慮 as min()
            r = float('inf')

            for i in range(s+1, len(debt)):
                if debt[i] * debt[s] < 0:
                    # settle s with i
                    debt[i] += debt[s]
                    # 必須為 s + 1 而不能為 i 因為
                    # debt[s+1] 可以為負, 負數須繼續傳下去~
                    r = min(r, 1 + dfs(s + 1))
                    #  r = min(r, 1 + dfs(i))

                    # backtrack
                    debt[i] -= debt[s]

            print("after debp: {}".format(debt))
            return r

        # starts at index 0
        return dfs(0)

def build():
    return [[1,5,8],[8,9,8],[2,3,9],[4,3,1]]
    return [[0,1,10], [2,0,5]]
    return [[0,1,10], [1,0,1], [1,2,5], [2,0,5]]


if __name__ == "__main__":
    s = Solution()
    print(s.minTransfers(build()))
