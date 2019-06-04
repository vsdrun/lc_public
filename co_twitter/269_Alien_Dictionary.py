#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/alien-dictionary/description/

There is a new alien language which uses the latin alphabet.
However, the order among letters are unknown to you.

You receive a list of non-empty words from the dictionary,
where words are sorted lexicographically by the rules of this new language.
Derive the order of letters in this language.

Example 1:
Given the following words in dictionary,
zip(
[
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

[
  "wrf",
  "er",
  "ett",
  "rftt"
  ""
])

The correct order is: "wertf".


Example 2:
Given the following words in dictionary,
[
  "z",
  "x"
]
The correct order is: "zx".


Example 3:
Given the following words in dictionary,
[
  "z",
  "x",
  "z"
]
The order is invalid, so return "".


You may assume all letters are in lowercase.
You may assume that if a is a prefix of b,
then a must appear before b in the given dictionary.

If the order is invalid, return an empty string.
There may be multiple valid order of letters, return any one of them is fine.

https://leetcode.com/problems/alien-dictionary/discuss/70137/1618-lines-Python-30-lines-C++
"""


class Solution(object):
    def alienOrder(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        less = []

        # build graph!!
        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:  # 都相同我無法build graph direction dependency...
                    less += a + b,
                    break

        chars = set(''.join(words))
        order = []

        print("less: {}".format(less))
        print("chars: {}".format(chars))

        while less:
            print(zip(*less)[1])
            head = chars - set(zip(*less)[1])  # 找 head

            if not head:
                return ''

            order += head

            less = filter(head.isdisjoint, less)  # 找出不含 head的 pair

            chars -= head

        return ''.join(order + list(chars))


def build():
    return [
        "wrt",
        "wrf",
        "er",
        "ett",
        "rftt"
    ]


if __name__ == "__main__":
    s = Solution()
    print(s.alienOrder(build()))
