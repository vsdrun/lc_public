#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/verifying-an-alien-dictionary/

In an alien language, surprisingly they also use english lowercase letters,
but possibly in a different order.
The order of the alphabet is some permutation of lowercase letters.

Given a sequence of words written in the alien language,
and the order of the alphabet,
return true if and only if the given words are sorted lexicographicaly in
this alien language.



Example 1:
Input: words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz"
Output: true
Explanation: As 'h' comes before 'l' in this language,
then the sequence is sorted.

Example 2:
Input: words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz"
Output: false
Explanation:
As 'd' comes after 'l' in this language, then words[0] > words[1],
hence the sequence is unsorted.

Example 3:
Input: words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz"
Output: false
Explanation:
The first three characters "app" match, and the second string is shorter
(in size.)
According to lexicographical rules "apple" > "app", because 'l' > '∅',
where '∅' is defined as the blank character which is less than
any other character (More info).

Note:
1 <= words.length <= 100
1 <= words[i].length <= 20
order.length == 26
All characters in words[i] and order are english lowercase letters.

# hashtable
"""


class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """

        def comp(a, b):
            if order.index(a) > order.index(b):
                return False
            return True

        for a, b in zip(words, words[1:]):
            idx = 0

            while idx < len(a):
                if idx >= len(b):
                    return False

                if a[idx] == b[idx]:
                    idx += 1
                    continue
                if comp(a[idx], b[idx]):
                    print("a[{}] b[{}] idx:{}".format(idx, idx, idx))
                    break
                else:
                    return False

        return True

def build():
    return ["ehlc","elhd"], "hlabcdefgijkmnopqrstuvwxyz"
    return ["eeec","eeed"], "hlabcdefgijkmnopqrstuvwxyz"
    return ["hello","leetcode"], "hlabcdefgijkmnopqrstuvwxyz"
    return ["word","world","row"], "worldabcefghijkmnpqstuvxyz"
    return ["apple","app"], "abcdefghijklmnopqrstuvwxyz"


if __name__ == "__main__":
    s = Solution()
    print(s.isAlienSorted(*build()))
