#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/repeated-dna-sequences/description/

All DNA is composed of a series of nucleotides abbreviated as A, C, G,
and T, for example: "ACGAATTCCG".

When studying DNA,
it is sometimes useful to identify repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings)
that occur more than once in a DNA molecule.

For example,
Given s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

Return:
["AAAAACCCCC", "CCCCCAAAAA"].

ref:
https://leetcode.com/problems/repeated-dna-sequences/discuss/53877/I-did-it-in-10-lines-of-C++

https://leetcode.com/problems/repeated-dna-sequences/discuss/53855/7-lines-simple-Java-O(n)

SMART
vector<string> findRepeatedDnaSequences(string s) {
    unordered_map<int, int> m;
    vector<string> r;
    int t = 0, i = 0, ss = s.size();
    while (i < 9)
        t = t << 3 | s[i++] & 7;
    while (i < ss)
        if (m[t = t << 3 & 0x3FFFFFFF | s[i++] & 7]++ == 1)
            r.push_back(s.substr(i - 10, 10));
    return r;
}
"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]

        length = 10
        Can overlaps!!
        """
        from __builtin__ import xrange
        from collections import defaultdict as dd

        if len(s) < 10:
            return []

        result = []
        hdict = dd(int)
        i = 0
        sig = 0

        while i < 9:  # we need 9 char first. 0 - 8
            sig = sig << 3 | (ord(s[i]) & 7)
            i += 1

        #  print(sig)

        for si in xrange(i, len(s)):

            # 完滿 10 chars.
            sig = sig << 3 | (ord(s[si]) & 7)

            if hdict[sig] == 1:
                result.append(s[si - 9: si + 1])
                hdict[sig] += 1
            else:
                #  print("sig: {}".format(sig))
                #  print("hdict before: {}".format(hdict))
                hdict[sig] += 1
                #  print("hdict after: {}".format(hdict))

            sig = sig & 0x7FFFFFF  # sig 前進一個 成為 9 chars 的 sig.

        #  print(result)
        return result

    def findRepeatedDnaSequences_cheat(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        from __builtin__ import xrange

        n = len(s)
        ret = set()
        seq_map = set()

        for i in xrange(n - 9):
            seq = s[i:i + 10]
            if seq in seq_map:
                ret.add(seq)
            else:
                seq_map.add(seq)

        return list(ret)


def build():
    return "AAAAAAAAAAAA"
    return "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    return ""


if __name__ == "__main__":
    s = Solution()
    print(s.findRepeatedDnaSequences(build()))
