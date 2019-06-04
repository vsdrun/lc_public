#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/group-shifted-strings/description/


Given a string, we can "shift" each of its letter to its successive letter,
for example: "abc" -> "bcd". We can keep "shifting" which forms the sequence:


"abc" -> "bcd" -> ... -> "xyz"
Given a list of strings which contains only lowercase alphabets,
group all strings that belong to the same shifting sequence.


Example:
Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
Output:
[
  ["abc","bcd","xyz"],
  ["az","ba"],
  ["acef"],
  ["a","z"]
]

reference:
https://leetcode.com/problems/group-shifted-strings/discuss/67459/1-4-lines-in-Java

group, 想到同一結構為key
"""


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]

        Example:
        Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
        Output:
        [
          ["abc","bcd","xyz"],
          ["az","ba"],
          ["acef"],
          ["a","z"]
        ]
        """

        from collections import defaultdict as dd
        dmap = dd(list)
        a_ord = ord('a')

        for w in strings:
            # calculate diff with 'a'
            shift = ord(w[0]) - a_ord

            if not shift:
                dmap[w].append(w)
                continue

            local_result = []

            for c in w:
                orig = ord(c) - shift

                if orig < a_ord:  # 代表 < a, 例如 "ba"
                    orig = ((orig - a_ord) % 26) + a_ord

                local_result.append(chr(orig))

            dmap["".join(local_result)].append(w)

        return dmap.values()

    def rewrite(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]

        Example:
        Input: ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"],
        Output:
        [
          ["abc","bcd","xyz"],
          ["az","ba"],
          ["acef"],
          ["a","z"]
        ]
        """
        from collections import defaultdict as dd

        dmap = dd(list)

        if not strings:
            return []

        base = ord('a')

        for w in strings:
            diff = ord(w[0]) - base

            tmp_w = "".join([chr(ord(l) - diff) if ord(l) - diff >= base else
               chr(((ord(l) - diff) - base) % 26 + base) for l in list(w)])

            dmap[tmp_w].append(w)

        return dmap.values()

    def rewrite2(self, strings):
        # SMART...
        # 重點是字母與字母間的差距.
        from collections import defaultdict
        result = defaultdict(list)

        for s in strings:
            # 須 % 26 因為 "az" -> (0, 25), "ba" -> (0, -1) 其實為一樣的diff
            result[tuple([(ord(c)-ord(s[0])) % 26 for c in s])].append(s)

        print(result)
        return result.values()

def build():
    return ["az", "ba"]
    return ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]
    return ["zx"]


if __name__ == "__main__":

    s = Solution()
    #  print(s.groupStrings(build()))
    print(s.rewrite(build()))
    print(s.rewrite2(build()))
