#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/friends-of-appropriate-ages/

Some people will make friend requests.
The list of their ages is given and ages[i] is the age of the ith person.

Person A will NOT friend request person B (B != A)
if any of the following conditions are true:

age[B] <= 0.5 * age[A] + 7
age[B] > age[A]
age[B] > 100 && age[A] < 100
Otherwise, A will friend request B.

Note that if A requests B, B does not necessarily request A.
Also, people will not friend request themselves.

How many total friend requests are made?
Example 1:
Input: [16,16]
Output: 2
Explanation: 2 people friend request each other.

Example 2:
Input: [16,17,18]
Output: 2
Explanation: Friend requests are made 17 -> 16, 18 -> 17.


Example 3:
Input: [20,30,100,110,120]
Output:
Explanation: Friend requests are made 110 -> 100, 120 -> 110, 120 -> 100.


https://leetcode.com/problems/friends-of-appropriate-ages/discuss/127029/C%2B%2BJavaPython-Easy-and-Straight-Forward
"""


class Solution(object):
    def numFriendRequests(self, ages):
        """
        :type ages: List[int]
        :rtype: int

        Person A will NOT friend request person B (B != A)
        if any of the following conditions are true:
        age[B] <= 0.5 * age[A] + 7
        age[B] > age[A]
        age[B] > 100 && age[A] < 100

        Otherwise, A will friend request B.

        Note that if A requests B, B does not necessarily request A.
        Also, people will not friend request themselves.

        1/2(X) + 7 < X
        X > 14
        X >= 15

        Rule 1
        Rule 2
        Rule 3

        Use bisect do binary search.
        """
        import collections

        def request(a, b):
            return not (b <= a // 2 + 7 or b > a)

        c = collections.Counter(ages)

        return sum(request(a, b) * c[a] * (c[b] - (a == b))
                for a in c for b in c)


    def rewrite(self, ages):
        """
        利用累加的概念...

        條件:
        age[B] <= 0.5 * age[A] + 7
        age[B] > age[A]
        age[B] > 100 && age[A] < 100
        Otherwise, A will friend request B.
        """
        res = 0
        age_nums, age_accums = [0] * 121, [0] * 121

        # 此age有幾人
        for age in ages:
            age_nums[age] += 1

        # 此age之前到此age的總共人數
        for i in range(1, 121):
            age_accums[i] = age_accums[i-1] + age_nums[i]

        for i in range(15, 121):
            count = age_accums[i] - age_accums[i // 2 + 7]
            print("i: {} age_accume[i]: {} age_accumei//2: {} count: {}".format(i,
                age_accums[i], age_accums[i//2 +7], count))

            res += age_nums[i] * (count - 1)
            print("age_nums[i]: {} res: {}".format(age_nums[i], res))

        return res



def build():
    return [17, 18]
    return [15, 15, 15, 16, 16, 16]
    return [16, 16]
    return [20,30,100,110,120]
    return [16, 17, 18]
    return [68, 13, 18, 20, 105]


if __name__ == "__main__":
    s = Solution()
    print(s.rewrite(build()))
