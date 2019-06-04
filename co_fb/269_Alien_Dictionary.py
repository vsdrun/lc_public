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

        for pair in zip(words, words[1:]):
            for a, b in zip(*pair):
                if a != b:
                    less += a + b,
                    break

        chars = set(''.join(words))
        order = []

        while less:
            free = chars - set(zip(*less)[1])

            if not free:
                return ''

            order += free
            less = filter(free.isdisjoint, less)
            chars -= free

        return ''.join(order + list(chars))

    def rewrite(self, words):
        """
        :type words: List[str]
        :rtype: str
        注意 data structure 的 type
        [
          "wrt",
          "wrf",
          "er",
          "ett",
          "rftt"
        ]
        """

        if not words:
            return ""

        # build pair
        filtered = []

        for wp in zip(words, words[1:]):
            for a, b in zip(*wp):
                if a != b:
                    filtered.append(a+b)
                    break

        allchar = set("".join(words))
        result = []

        while filtered:
            head = allchar - set([w[1] for w in filtered])

            # 重要!
            if not head:
                return ''

            allchar -= head

            filtered = [s for s in filtered if not set(s) & head]
            result.append("".join(head))

        result.append("".join(allchar))

        return "".join(result)


def build():
    return ["z","x","z"]
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
    print(s.rewrite(build()))
