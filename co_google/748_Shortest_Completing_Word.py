#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/shortest-completing-word/description/


Find the minimum length word from a given dictionary words,
which has all the letters from the string licensePlate.
Such a word is said to complete the given string licensePlate


Here, for letters we ignore case.
For example, "P" on the licensePlate still matches "p" on the word.

It is guaranteed an answer exists.
If there are multiple answers, return the one that occurs first in the array.

The license plate might have the same letter occurring multiple times.

For example, given a licensePlate of "PP",
the word "pair" does not complete the licensePlate, but the word "supper" does.

Example 1:
Input: licensePlate = "1s3 PSt", words = ["step", "steps", "stripe", "stepple"]
Output: "steps"
Explanation: The smallest length word that contains the letters "S", "P", "S", and "T".
Note that the answer is not "step", because the letter "s" must occur in the word twice.
Also note that we ignored case for the purposes of comparing whether a letter exists in the word.


Example 2:
Input: licensePlate = "1s3 456", words = ["looks", "pest", "stew", "show"]
Output: "pest"
Explanation: There are 3 smallest length words that contains the letters "s".
We return the one that occurred first.
"""


class Solution(object):
    def shortestCompletingWord(self, licensePlate, words):
        """
        :type licensePlate: str
        :type words: List[str]
        :rtype: str
        """
        from collections import Counter

        ll = Counter([c for c in licensePlate.lower() if c.isalpha()])

        min_size = float("inf")
        result = None

        for w in words:
            c = Counter(w)

            if not ll - c:
                prev_min = min_size
                min_size = min(min_size, len(w))

                if min_size != prev_min:
                    result = w

        return result


def build():
    return "1s3 PSt", ["step", "steps", "stripe", "stepple"]
    return "1s3 456", ["looks", "pest", "stew", "show"]


if __name__ == "__main__":
    s = Solution()
    print(s.shortestCompletingWord(*build()))
