#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/sentence-screen-fitting/description/

Given a rows x cols screen and a sentence represented by a
list of non-empty words,
find how many times the given sentence can be fitted on the screen.


Note:
A word cannot be split into two lines.
The order of words in the sentence must remain unchanged.
Two consecutive words in a line must be separated by a single space.

Total words in the sentence won't exceed 100.
Length of each word is greater than 0 and won't exceed 10.
1 ≤ rows, cols ≤ 20,000.




Example 1:

Input:
rows = 2, cols = 8, sentence = ["hello", "world"]

Output:
1

Explanation:
hello---
world---

The character '-' signifies an empty space on the screen.




Example 2:

Input:
rows = 3, cols = 6, sentence = ["a", "bcd", "e"]

Output:
2

Explanation:
a-bcd-
e-a---
bcd-e-

The character '-' signifies an empty space on the screen.




Example 3:

Input:
rows = 4, cols = 5, sentence = ["I", "had", "apple", "pie"]

Output:
1

Explanation:
I-had
apple
pie-I
had--

The character '-' signifies an empty space on the screen.

https://leetcode.com/problems/sentence-screen-fitting/discuss/90869/
"""

# Definition for a binary tree node.


class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        # 作為全長的sentence
        s = ' '.join(sentence) + ' '
        # start 為 moving index
        # 主要為 算 總長度.
        start, ll = 0, len(s)

        for i in xrange(rows):
            start += cols

            while s[start % ll] != ' ':
                # 目前長度 % sentence length 有兩種case
                # 1. 目前長度短. 看看sentence此index是否為" "
                #  不是的話 start index 往前減，代表空出來的空缺給吃掉
                #  總長度變短.
                # 2. 目前長度長. 已經可以吃掉至少一個sentence,
                #  餘的 sentence 可以吃下多少? 若切點非 " ", 總start index
                #  再減少~
                start -= 1

            # +1 因為 要加一個 " "
            start += 1

        return start / ll


def build():
    return ["Iia", "had"], 4, 5


if __name__ == "__main__":
    s = Solution()
    result = s.wordsTyping(*build())

    print(result)
