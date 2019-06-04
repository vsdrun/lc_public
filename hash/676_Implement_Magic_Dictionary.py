#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/implement-magic-dictionary/description/

Implement a magic directory with buildDict, and search methods.

For the method buildDict,
you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word,
and judge whether if you modify exactly one character into another character
in this word,
the modified word is in the dictionary you just built.

Example 1:
Input: buildDict(["hello", "leetcode"]), Output: Null
Input: search("hello"), Output: False
Input: search("hhllo"), Output: True
Input: search("hell"), Output: False
Input: search("leetcoded"), Output: False
"""


class MagicDictionary(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cnt = 1
        self.dmap = dict()
        self.max_length_ = 0

    def buildDict(self, words):
        """
        Build a dictionary through a list of words
        :type words: List[str]
        :rtype: void
        """
        for word in words:
            self.max_length_ = max(self.max_length_, len(word))
            root = self.dmap
            for c in word:
                if c in root:
                    root = root[c]
                else:
                    root[c] = dict()
                    root = root[c]

            root[None] = None

    def search(self, word):
        """
        Returns if there is any word in the trie that
        equals to the given word after modifying exactly one character
        :type word: str
        :rtype: bool
        """
        if len(word) > self.max_length_:
            return False

        root = self.dmap

        def find(wd, current_dmap):
            root = current_dmap

            if not root:
                return False

            if not wd:
                if None in root:
                    return True
                else:
                    return False

            for i, c in enumerate(wd):
                if c in root:
                    root = root[c]
                else:
                    return False

            if None in root:
                return True
            else:
                return False

        for i, c in enumerate(word):
            # run every path in this layer
            for ll in root.keys():
                if ll == c:
                    continue

                if find(word[i + 1:], root[ll]):
                    return True

            if c not in root:
                return False
            else:
                root = root[c]

        return False


def build():
    return ["hello", "hallo", "leetcode", "judge"]
    #  return ["hello", "leetcode"]


if __name__ == "__main__":
    s = MagicDictionary()
    s.buildDict(build())
    print(s.search("hxllo"))
    print(s.search("hallo"))
    print(s.search("hell"))
    print(s.search("leetcodd"))
    print(s.search("judgeea"))
