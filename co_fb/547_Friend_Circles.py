#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/friend-circles/

There are N students in a class.
Some of them are friends, while some are not.
Their friendship is transitive in nature.
For example, if A is a direct friend of B, and B is a direct friend of C,
then A is an indirect friend of C.
And we defined a friend circle is a group of students who are direct
or indirect friends.

Given a N*N matrix M representing the friend relationship between students
in the class.

If M[i][j] = 1,
then the ith and jth students are direct friends with each other,
otherwise not.

And you have to output the total number of friend circles among
all the students.


Example 1:
Input:
[[1,1,0],
 [1,1,0],
 [0,0,1]]

Output: 2
Explanation:
The 0th and 1st students are direct friends, so they are in a friend circle.
The 2nd student himself is in a friend circle. So return 2.


Example 2:
Input:
[[1,1,0],
 [1,1,1],
 [0,1,1]]

Output: 1
Explanation:
The 0th and 1st students are direct friends, the 1st and 2nd students are direct friends,
so the 0th and 2nd students are indirect friends.
All of them are in the same friend circle, so return 1.
"""

class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(node):
            if node not in visited:
                visited.add(node)

                for i, val in enumerate(M[node]):
                    if i != node and val == 1:
                        dfs(i)

        visited = set()

        cnt = 0

        for i in range(len(M)):
            if i not in visited:
                dfs(i)
                cnt += 1

        return cnt

def build():
    return [[1,1,0],
            [1,1,0],
            [0,0,1]]

    return [[1,1,0],
            [1,1,1],
            [0,1,1]]


if __name__ == "__main__":
    s = Solution()
    print(s.findCircleNum(build()))
