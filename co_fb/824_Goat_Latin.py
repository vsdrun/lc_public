#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/goat-latin/

A sentence S is given,
composed of words separated by spaces.
Each word consists of lowercase and uppercase letters only.

We would like to convert the sentence to "Goat Latin"
(a made-up language similar to Pig Latin.)


The rules of Goat Latin are as follows:
If a word begins with a vowel (a, e, i, o, or u),
append "ma" to the end of the word.


For example, the word 'apple' becomes 'applema'.


If a word begins with a consonant (i.e. not a vowel),
remove the first letter and append it to the end, then add "ma".


For example, the word "goat" becomes "oatgma".

Add one letter 'a' to the end of each word per its word index in the sentence,
starting with 1.

For example, the first word gets "a" added to the end,
the second word gets "aa" added to the end and so on.

Return the final sentence representing the conversion from S to Goat Latin.


Example 1:
Input: "I speak Goat Latin"
Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"


Example 2:
Input: "The quick brown fox jumped over the lazy dog"
Output:
"heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"


Notes:
S contains only uppercase, lowercase and spaces.
Exactly one space between each word.

1 <= S.length <= 150.
"""


class Solution(object):
    def toGoatLatin(self, S):
        """
        :type S: str
        :rtype: str

        If a word begins with a vowel (a, e, i, o, or u),
        append "ma" to the end of the word.

        If a word begins with a consonant (i.e. not a vowel),
        remove the first letter and append it to the end, then add "ma".

        Add one letter 'a' to the end of each word per its word index in
        the sentence, starting with 1.
        """

        def rule1(S):
            if S[0] in "aeiouAEIOU":
                S = S + "ma"
            else:
                S = S[1:] + S[0] + "ma"
            return S

        def rule2(S, idx):
            S = S + 'a' * idx + ' '
            return S

        result = ""

        for i, c in enumerate(S.split()):
            result += rule2(rule1(c), i + 1)

        return result.rstrip()


def build():
    return "The quick brown fox jumped over the lazy dog"
    #  "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
    return "I speak Goat Latin"
    #  Output: "Imaa peaksmaaa oatGmaaaa atinLmaaaaa"


if __name__ == "__main__":
    er = "heTmaa uickqmaaa rownbmaaaa oxfmaaaaa umpedjmaaaaaa overmaaaaaaa " + \
            "hetmaaaaaaaa azylmaaaaaaaaa ogdmaaaaaaaaaa"
    s = Solution()
    r = s.toGoatLatin(build())
    print(r == er)
