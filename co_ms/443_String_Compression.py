#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/string-compression/description/


Given an array of characters, compress it in-place.


The length after compression must always be smaller
than or equal to the original array.

Every element of the array should be a character (not int) of length 1.

After you are done modifying the input array in-place,
return the new length of the array.


Follow up:
Could you solve it using only O(1) extra space?


Example 1:
Input:
["a","a","b","b","b", c","c","c"]
Output:
Return 6, and the first 6 characters of the input array should be:
["a","2","b","3","c","3"]

Explanation:
"aa" is replaced by "a2". "bb" is replaced by "b2". "ccc" is replaced by "c3".


Example 2:
Input:
["a"]
Output:
Return 1, and the first 1 characters of the input array should be: ["a"]
Explanation:
Nothing is replaced.


Example 3:
Input:
["a","b","b","b","b","b","b","b","b","b","b","b","b"]
Output:
Return 4,
and the first 4 characters of the input array should be: ["a","b","1","2"].

Explanation:
Since the character "a" does not repeat, it is not compressed.
"bbbbbbbbbbbb" is replaced by "b12".
Notice each digit has it's own entry in the array.
"""


class Solution(object):
    def compress(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        Could you solve it using only O(1) extra space?
        """
        from __builtin__ import xrange

        cnt = 1
        rpc_idx = len(chars) - 1

        for i in xrange(len(chars) - 2, -1, -1):
            if chars[i] == chars[i + 1]:
                cnt += 1
                continue

            if cnt == 1:
                chars[rpc_idx] = chars[i + 1]
            else:
                scnt = str(cnt)
                scnt_idx = len(scnt) - 1

                for j in xrange(scnt_idx, -1, -1):
                    chars[rpc_idx] = scnt[j]
                    rpc_idx -= 1
                chars[rpc_idx] = chars[i + 1]

            rpc_idx -= 1
            cnt = 1

        if cnt == 1:
            chars[rpc_idx] = chars[0]
        else:
            scnt = str(cnt)
            scnt_idx = len(scnt) - 1

            for i in xrange(scnt_idx, -1, -1):
                chars[rpc_idx] = scnt[i]
                rpc_idx -= 1
            chars[rpc_idx] = chars[0]

        for _ in xrange(rpc_idx):
            chars.pop(0)

        #  print(chars)

        return len(chars)

    def rewrite(self, chars):
        """
        :type chars: List[str]
        :rtype: int
        Could you solve it using only O(1) extra space?
        """
        if len(chars) == 1:
            return 1

        from __builtin__ import xrange
        wcnt = 1
        last_idx = len(chars)

        for bidx in xrange(len(chars) - 2, -1, -1):
            if chars[bidx] == chars[bidx + 1]:
                wcnt += 1
                continue

            if wcnt == 1:
                length = 1
            else:
                length = 1 + len(list(str(wcnt)))

            previous_last_idx = last_idx
            last_idx = last_idx - length

            chars[last_idx: previous_last_idx] = chars[bidx + 1: bidx + 2] + \
                (list(str(wcnt)) if wcnt != 1 else [])

            wcnt = 1

        # wrap up.
        if wcnt == 1:
            length = 1
        else:
            length = 1 + len(list(str(wcnt)))

        previous_last_idx = last_idx
        last_idx = last_idx - length
        chars[last_idx: previous_last_idx] = chars[0: 1] + \
            (list(str(wcnt)) if wcnt != 1 else [])

        chars[:] = chars[last_idx:]
        return len(chars)


def build():
    return ["a"]
    return ["a", "a", "a", "b", "b", "c", "c", "d"]
    return ["a", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b", "b"]


if __name__ == "__main__":
    s = Solution()
    print(s.compress(build()))
    print(s.rewrite(build()))
