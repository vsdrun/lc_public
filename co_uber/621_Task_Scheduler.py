#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/task-scheduler/description/
https://leetcode.com/problems/task-scheduler/discuss/104507

Given a char array representing tasks CPU need to do.

It contains capital letters A to Z where different letters represent
different tasks.

Tasks could be done without original order.
Each task could be done in one interval.
For each interval, CPU could finish one task or just be idle.

However, there is a non-negative cooling interval n that means
between two same tasks,
there must be at least n intervals that CPU are
doing different tasks or just be idle.

You need to return the least number of intervals the
CPU will take to finish all the given tasks.

Example 1:
Input: tasks = ["A","A","A","B","B","B"], n = 2
Output: 8
Explanation: A -> B -> idle -> A -> B -> idle -> A -> B.


Note:
The number of tasks is in the range [1, 10000].
The integer n is in the range [0, 100].

explain:
Say we were given input AAAA BBBB CCCC DDD EEE FF GG HH JJ KK, and N = 6.

We can start creating a schedule. A, B, and C occur the most times,
so let’s place them first.
We have to make each task of the same type N = 6 spaces apart.

(A _ _ _ _ _ _ )(A _ _ _ _ _ _)(A _ _ _ _ _ _)A _ _
A B _ _ _ _ _ A B _ _ _ _ _ A B _ _ _ _ _ A B _
A B C _ _ _ _ A B C _ _ _ _ A B C _ _ _ _ A B C

Now, we’ll just start putting D’s, E’s, etc.
in left to right order similar to how we put the other letters.
By our justification above, they won’t collide - this will be a valid schedule.

A B C D _ _ _ A B C D _ _ _ A B C D _ _ _ A B C
A B C D E _ _ A B C D E _ _ A B C D E _ _ A B C
A B C D E F _ A B C D E F _ A B C D E _ _ A B C
A B C D E F G A B C D E F _ A B C D E G _ A B C
A B C D E F G A B C D E F H A B C D E G H A B C

Now this is a compact schedule, but we might still have stuff left over.
We can just place them however we want.

In the article there’s justification for why this is possible even
if say J already occurrs in the compact schedule but isn’t exhausted yet.

J K A B C D E F J K G A B C D E F H A B C D E G H A B C

explain:
Say we were given input AAAA BBBB CCCC DDD EEE FF GG HH JJ KK, and N = 1.

We can start creating a schedule. A, B, and C occur the most times,
so let’s place them first.
We have to make each task of the same type N = 6 spaces apart.

(A _ )(A _ )(A _ )A _ _
 A B   A B   A B  A B C
"""


class Solution(object):
    def leastInterval(self, tasks, N):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        import collections

        task_counts = collections.Counter(tasks).values()
        test = collections.Counter(tasks)
        print("test: {}".format(test))  # Counter({'A': 3, 'B': 3})

        M = max(task_counts)

        print("M: {0}".format(M))
        print("task_counts: {0}".format(task_counts))
        # task_counts 為 list
        # .count 為看看有幾個最大值為M的.
        Mct = task_counts.count(M)

        print("Mct: {0}".format(Mct))

        return max(len(tasks), (M - 1) * (N + 1) + Mct)


def build():
    return ["A", "A", "A", "B", "B", "B"], 2


if __name__ == "__main__":

    s = Solution()
    result = s.leastInterval(*build())

    print(result)
