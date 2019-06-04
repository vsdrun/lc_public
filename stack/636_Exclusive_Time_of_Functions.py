#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/exclusive-time-of-functions/description/

Given the running logs of n functions that are executed in a
nonpreemptive single threaded CPU, find the exclusive time of these functions.

Each function has a unique id, start from 0 to n-1.
A function may be called recursively or by another function.

A log is a string has this format : function_id:start_or_end:timestamp.

For example, "0:start:0" means function 0 starts from the very beginning of
time 0.

"0:end:0" means function 0 ends to the very end of time 0.

Exclusive time of a function is defined as the time spent within this function,
the time spent by calling other functions should not be considered as
this function's exclusive time.

You should return the exclusive time of each function sorted by their
function id.


Example 1:
Input:
n = 2
logs =
["0:start:0",
 "1:start:2",
 "1:end:5",  # inclusive 5 - 2 + 1
 "0:end:6"]
Output:[3, 4]

### 都是inclusive range. 一個數字代表一個時間點花費。

Explanation:
Function 0 starts at time 0,
then it executes 2 units of time and reaches the end of time 1.

Now function 0 calls function 1, function 1 starts at time 2,
executes 4 units of time and end at time 5.

Function 0 is running again at time 6, and also end at the time 6,
thus executes 1 unit of time.


So function 0 totally execute 2 + 1 = 3 units of time, and function 1 totally
execute 4 units of time.


Note:
Input logs will be sorted by timestamp, NOT log id.

Your output should be sorted by function id,
which means the 0th element of your output corresponds to
the exclusive time of function 0.

Two functions won't start or end at the same time.

Functions could be called recursively, and will always end.

1 <= n <= 100
"""


class Solution(object):
    def exclusiveTime(self, n, logs):
        """
        :type n: int  有多少functions
        :type logs: List[str]
        :rtype: List[int]
        """
        import collections as cc

        # 因為每個function (也就是 idx) 會跑多次...
        idx_time = cc.defaultdict(list)

        pstack = []

        for lg in logs:
            idx, entry, ts = lg.split(":")
            idx, ts = int(idx), int(ts)

            if entry == "end":
                parent_func = pstack.pop()
                func_sum = ts - parent_func[1] + 1

                idx_time[parent_func[0]].append(func_sum - parent_func[2])

                if pstack:
                    # 將此外部function 內含function 花的時間存入
                    # 之後遇上外部function end時減去內含function花的時間即
                    # 外部function跑的時間
                    pstack[-1][2] += func_sum

            if entry == "start":
                pstack.append([idx, ts, 0])  # 0 為此function 內涵 function call
                # 的時間和

        result = []

        # 因為idx為contineunously...
        for i in xrange(len(idx_time)):
            result.append(sum(idx_time[i]))

        return result

    def rewrite(self, n, logs):
        """
        :type n: int  有多少functions
        :type logs: List[str]
        :rtype: List[int]
        最佳解
        call function本來就是stack rewind
        """
        stack = []
        addtime = [0] * n


        for l in logs:
            fid, ftype, ftime = l.split(":")

            if ftype == "start":
                stack += [int(fid), int(ftime)],

            if ftype == "end":
                pfid, pftime = stack.pop()
                currentTotal = (int(ftime) - pftime + 1)
                addtime[pfid] += currentTotal

                if stack:
                    addtime[stack[-1][0]] -= currentTotal

        return addtime


def build():
    n = 5
    logs = [
        "0:start:3",  # 9 , 2
        "1:start:4",  # 3
        "2:start:6",  # 2
        "2:end:7",
        "1:end:8",

        "3:start:9",  # 2
        "3:end:10",
        "0:end:11",
        "4:start:12", # 8
        "4:end:19",
        "0:start:20", # 3
        "0:end:22"
    ]

    return n, logs


if __name__ == "__main__":
    s = Solution()
    print(s.exclusiveTime(*build()))
    print(s.rewrite(*build()))
