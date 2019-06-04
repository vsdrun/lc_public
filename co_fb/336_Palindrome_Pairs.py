#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/palindrome-pairs/description/

Given a list of unique words, find all pairs of distinct indices (i, j)
in the given list, so that the concatenation of the two words,
i.e. words[i] + words[j] is a palindrome.


Example 1:
Given words = ["bat", "tab", "cat"]
Return [[0, 1], [1, 0]]
The palindromes are ["battab", "tabbat"]


Example 2:
Given words = ["abcd", "dcba", "lls", "s", "sssll"]
Return [[0, 1], [1, 0], [3, 2], [2, 4]]
The palindromes are ["dcbaabcd", "abcddcba", "slls", "llssssll"]
"""


class Solution(object):

    def palindromePairs(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """
        """
        Idea:

        [ab    c]
        [pre suf]
        1. Test suf is a palindrome or not.
        'c' is itself parlindrome.
        we need to find 'ba' in Words thus concatenate to work [ab c]
        =>  [ab c ba]  would become a parindrome.

        2. Same above, test pre a palindrome or not.
        """
        def is_palindrome(check):
            # if empty, return True
            return check == check[::-1]

        words = {word: i for i, word in enumerate(words)}
        valid_pals = []

        for word, k in words.iteritems():
            n = len(word)

            for j in range(n + 1):

                pref = word[:j]  # 可以為無
                suf = word[j:]  # 可以為無

                if is_palindrome(pref):
                    back = suf[::-1]
                    # 測試 != 是不用的?
                    # 還是需要 因為有single char.
                    if back != word and back in words:
                        valid_pals.append([words[back], k])

                # j != n 因為全字已經在前面的if處理過了...
                if j != n and is_palindrome(suf):
                    back = pref[::-1]

                    if back != word and back in words:
                        valid_pals.append([k, words[back]])

        return valid_pals

    def rewrite(self, words):
        """
        :type words: List[str]
        :rtype: List[List[int]]
        """

        def test_palindrome(w):
            for i in range(len(w)):
                if w[i] != w[~i]:
                    return False

            return True



def build():
    return ["abcd", "dcba"]
    return ["", "a"]
    return ["a", ""]
    return ["bat", "tab", "cat"]
    return ["abc", "cba"]
    return ["", "ab"]


if __name__ == "__main__":
    s = Solution()
    print(s.palindromePairs(build()))
    print(s.rewrite(build()))
