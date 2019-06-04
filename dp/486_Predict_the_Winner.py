#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/predict-the-winner/description/

Given an array of scores that are non-negative integers.
Player 1 picks one of the numbers from either end of the array followed
by the player 2 and then player 1 and so on.

Each time a player picks a number,
that number will not be available for the next player.
This continues until all the scores have been chosen.
The player with the maximum score wins.

Given an array of scores, predict whether player 1 is the winner.
You can assume each player plays to maximize his score.


Example 1:
Input: [1, 5, 2]
Output: False

Explanation: Initially, player 1 can choose between 1 and 2.

If he chooses 2 (or 1), then player 2 can choose from 1 (or 2) and 5.
If player 2 chooses 5, then player 1 will be left with 1 (or 2).

So, final score of player 1 is 1 + 2 = 3, and player 2 is 5.
Hence, player 1 will never be the winner and you need to return False.


Example 2:
Input: [1, 5, 233, 7]
Output: True

Explanation: Player 1 first chooses 1.
Then player 2 have to choose between 5 and 7.
No matter which number player 2 choose, player 1 can choose 233.
Finally, player 1 has more score (234) than player 2 (12),
so you need to return True representing player1 can win.

Note:
1 <= length of the array <= 20.

Any scores in the given array are non-negative integers
and will not exceed 10,000,000.

If the scores of both players are equal, then player 1 is still the winner.




solve:
https://leetcode.com/problems/predict-the-winner/discuss/96835/Clean-3ms-C++-DP-solution-with-detailed-explanation


This problem can be solved in DP.

Let first outline the DP state:

dp[i][j] means that for a sub-game in between [i, j] inclusive,
the maximum score that Player 1 could get.

1.
也就是player 1需要拿到總和一半一上便贏的數!!
2.
交錯取樣. 也就是dp[i][j]是player1最大 dp[i-1][j] or dp[i][j-1]是player2最大.
3.
sum[i-1][j] 就是player1取了nums[i]之後剩下的總和
sum[i-1][j] - dp[i-1][j] 代表player1拿了nums[i]之後剩下的總和減去player2
    dp[i-1][j]拿最大的值 == player1 於dp[i][j]之後拿的最大值.

Our final goal is to find out whether Player 1 could score more than half of
the total score in the
game between [0, n-1], or in other words the dp[0][n-1].

Another thing to notice is that, because Player 1 and Player 2 pick numbers
one after each other, this means:

If dp[i][j] means maximum score Player 1 could get between [i, j] then dp[i-1][j]
could mean the maximum score Player 2 could get between [i-1, j],
and same thing for dp[i][j-1].

Another more important thing based on the above statement is that:

The sum[i-1][j] - dp[i-1][j] means the maximum score Player 1 can get
between [i-1, j] after
he picks nums[i] in between [i, j]. Also the same rule applies to dp[i][j-1].


Thus we have the following induction rule for this DP solution:

pickLeft = nums[i] + sum[i-1][j] - dp[i-1][j] //if left number is picked
pickRight = nums[j] + sum[i][j-1] - dp[i][j-1] //if right number is picked
dp[i][j] = max(pickLeft, pickRight)

Of course we can treat i == j and i == j-1 as special cases:
dp[i][j] = nums[i] // if i == j
dp[i][j] = max(nums[i], nums[j) // if i == j-1

For space complexity reason the sum[i][j] can be replaced with prefixSum.
sum[i][j] = prefixSum[j] - prefixSum[i-1]

    bool PredictTheWinner(vector<int>& nums) {
        vector<vector<int>> score(nums.size(), vector<int>(nums.size()));
        vector<int> prefixSum(nums.size()+1);
        prefixSum[0] = 0;
        for (int i=0; i<nums.size(); i++) {
            prefixSum[i+1] = prefixSum[i] + nums[i];
        }

        for (int len=1; len<=nums.size(); len++) {
            for (int lhs=0; lhs+len-1<nums.size(); lhs++) {
                int rhs = lhs + len - 1;
                if (lhs == rhs) {
                    score[lhs][rhs] = nums[lhs];
                } else if (lhs == rhs-1) {
                    score[lhs][rhs] = max(nums[lhs], nums[rhs]);
                } else {
                    int pickLeft = nums[lhs] + prefixSum[rhs+1] - prefixSum[lhs+1] - score[lhs+1][rhs];
                    int pickRight = nums[rhs] + prefixSum[rhs] - prefixSum[lhs] - score[lhs][rhs-1];
                    score[lhs][rhs] = max(pickLeft, pickRight);
                }
            }
        }

        return score[0][nums.size()-1] >= prefixSum.back()/2 + prefixSum.back()%2;
    }
"""


class Solution(object):
    def PredictTheWinner(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        """
        1. 拿最大代表拿到總和的一半以上.
        2. 和可用累進和處理.
        3. 平手仍算player1贏.
        """
        import operator as op
        import __builtin__

        if len(nums) < 3:
            return True

        # 算累進sum
        sums = []
        for i in nums:
            sums.append(sums[-1] + i if sums else i)

        dp = [[0]*len(nums) for j in range(len(nums))]

        # buttom up approach.
        # 由最小範圍 到 最大範圍
        for length in range(1, len(nums) + 1):
            # 確保不會有 dp[i][j]沒有跑過計算的狀況.
            # buttom up, 每個range都跑一次 range 為 2 的則 max(left, right)
            for lhs in range(len(nums) - length + 1):
                rhs = lhs + length - 1 # included

                if lhs == rhs:
                    dp[lhs][rhs] = nums[lhs]
                elif lhs == rhs - 1:
                    dp[lhs][rhs] = max(nums[lhs], nums[rhs])
                else:
                    leftSum = sums[lhs + length - 1] - sums[lhs]
                    rightSum = sums[rhs - 1] - sums[lhs]

                    pickLeft= nums[lhs] + leftSum - dp[lhs + 1][rhs]
                    pickRight= nums[rhs] + rightSum - dp[lhs][rhs - 1]

                    dp[lhs][rhs] = max(pickLeft, pickRight)

        return True if dp[0][len(nums) - 1] >= (sums[-1] / 2 + sums[-1] % 2) \
                else False

def build():
    return [1, 567, 1, 1, 99, 100]
    return [1, 1, 1]
    return [1, 5, 2]
    return [1, 5, 233, 7]


if __name__ == "__main__":
    s = Solution()
    print(s.PredictTheWinner(build()))
