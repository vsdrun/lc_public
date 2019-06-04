#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/guess-number-higher-or-lower-ii/description/

We are playing the Guess Game.

The game is as follows:
I pick a number from 1 to n. You have to guess which number I picked.

Every time you guess wrong, I'll tell you whether the number I picked
is higher or lower.

However, when you guess a particular number x, and you guess wrong,
you pay $x. You win the game when you guess the number I picked.



Example:
n = 10, I pick 8.

First round:  You guess 5, I tell you that it's higher. You pay $5.
Second round: You guess 7, I tell you that it's higher. You pay $7.
Third round:  You guess 9, I tell you that it's lower. You pay $9.

Game over.
8 is the number I picked.

You end up paying $5 + $7 + $9 = $21.

Given a particular n ≥ 1,
find out how much money you need to have to guarantee a win.

"""


"""
Explain:
先由小的case開始分析:
1. 只有一個數, 則$為0, 因為不用猜
2. 兩個數，則$為最小的那個數.
*3. 三個數，則$為中間那個數，原因是猜中間那數雖錯但答案確定.
    $為中間那個數.


first introduce best strategy to guess:
for one number, like 1, best strategy is 0$
for two number, like 3,4, best strategy is 3$,


which can be understood in this way:
you have two way to guess:

a) start by guess 4 is the target, (the worst case is) if wrong,
you get charged $4, then immediately you know 3 is the target number,
get charged $0 by guessing that, and finally you get charged $4.

b) similarly, if you start by 3, (the worst case is) if wrong,
you get charged $3, then you immediately know that 4 is the target number,
and get charged $0 for guessing this, and finally you get charged $3.

In summary:
range - -------- > best strategy cost
3, 4 - -------- > $3
5, 6 - -------- > $5
...


for three number, the best strategy is guess the middle number first,
and (worst case is) if wrong, you get charged that middle number money,
and then you immediately know what target number is by using "lower" or
"higher" response, so in summary:
range - -------- > best strategy cost
3, 4, 5 - -------- > $4
7, 8, 9 - -------- > $8
...


當數字超過3時，則memoize kicks in.
"for more numbers", it can simply be reduced them into smaller ranges,
and here is why DP solution make more sense in solving this.
suppose the range is [start, end]

the strategy here is to iterate through all number possible and
select it as the starting point, say for any k between start and end,
the worst cost for this is:

以這樣來思考:
    (start, k, end)
看成三個數，則選擇k是拿到最小的$, which is k.

k + DP(start, k - 1) + DP(k + 1, end)

and the goal is minimize the cost, so you need the minimum one
among all those k between start and end.
"""


class Solution(object):

    def getMoneyAmount(self, n):
        """
        : type n: int
        : rtype: int
        """
        # 1 ~ n
        # buttom up approach.
        dp = [[0] * (n + 1) for _ in range(n + 1)]

        for left in range(n, 0, -1):  # 由右往左減少, 不含0
            for right in range(left + 1, n + 1):  # 由左往右增加, 不含n
                dp[left][right] = min(
                    # 加上x 因為 x 為中間那個值。
                    # 加上x 也因為如果left/right比鄰，則加入最左邊的數.
                    # 為何為max?
                    # (1,2) 3 (4,5) x 為3時 , 找
                    # 不能改成:
                    #  x + dp[x + 1][right]
                    # 因為 dp[x+1][right] 有可能為dp[5][5] , which is 0.
                    # 也就是: (2,3) 4 (5), 當x=4時
                    # 4+ (2,3) 要比 4+(5) 大.
                    x + max(dp[left][x - 1], dp[x + 1][right])
                    for x in range(left, right))
        print(dp)
        return dp[1][n]

        """
        # buttom up
        need = [[0] * (n + 1) for _ in range(n + 1)]

        for lo in range(n, 0, -1):
            for hi in range(lo + 1, n + 1):
                need[lo][hi] = min(x + max(need[lo][x - 1], need[x + 1][hi])
                                   for x in range(lo, hi))
        return need[1][n]

        Top down:

        class Need(dict):

            def __missing__(self, (lo, hi)):
                if lo >= hi:
                    return 0
                ret = self[lo, hi] = min(x + max(self[lo, x - 1], self[x + 1, hi])
                                         for x in range(lo, hi))
                return ret

        return Need()[1, n]
        """


def build_input():
    return 5


if __name__ == "__main__":
    n = build_input()

    s = Solution()
    result = s.getMoneyAmount(n)

    print(result)
