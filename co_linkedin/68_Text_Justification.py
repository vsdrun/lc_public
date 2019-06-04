#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/text-justification/description/

Given an array of words and a length L,
format the text such that each line has exactly L
characters and is fully (left and right) justified.

You should pack your words in a greedy approach; that is,
pack as many words as you can in each line.
Pad extra spaces ' ' when necessary so that each line has exactly L characters.

Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words,
the empty slots on the left will be assigned more spaces than
the slots on the right.

For the last line of text,
it should be left justified and no extra space is inserted between words.

For example,
words: ["This", "is", "an", "example", "of", "text", "justification."]
L: 16.

Return the formatted lines as:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]
"""


class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        cur = []  # 此行目前獨立含的words
        num_of_letters = 0  # 目前此行的 letters count

        for w in words:
            # 如果 此行的letters + 目前加入的word + words 之間至少一個空白.
            if num_of_letters + len(w) + len(cur) > maxWidth:

                for i in range(maxWidth - num_of_letters):

                    # 使用餘數定理將空白平均(以最左邊為最多) 加到此行
                    # 的words 最後...
                    cur[i % (
                        len(cur) - 1 or  # 注意!! 若只有兩字 則空白全在兩字之間
                        1)
                        ] += ' '

                res.append(''.join(cur))

                # 此行已滿，清掉換下一行...
                cur = []
                num_of_letters = 0

            # 新的一行
            cur += [w]  # 目前有那些獨立的words
            num_of_letters += len(w)

        # 注意!!! 使用ljust~
        return res + [' '.join(cur).ljust(maxWidth)]

    def rewrite(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        this_line = []  # 此行目前獨立含的words

        this_line_word_cnt = 0  # 目前此行的 letters count

        result = []

        for w in words:
            # 此行目前的字母的個數 + 以字數來算的區間空白 + 目前此字字數
            if this_line_word_cnt + len(this_line) + len(w) > maxWidth:

                for i in range(maxWidth - this_line_word_cnt):

                    # 使用餘數定理將空白平均(以最左邊為最多) 加到此行
                    # 的words 最後...
                    this_line[
                        i % (len(this_line) - 1 or 1)] += ' '

                result.append(''.join(this_line))

                # 此行已滿，清掉換下一行...
                this_line = []
                this_line_word_cnt = 0

            this_line.append(w)
            this_line_word_cnt += len(w)

        #  ljust(...)
        #  S.ljust(width[, fillchar]) -> string
        #  Return S left-justified in a string of length width. Padding is
        #  done using the specified fill character (default is a space).
        # 注意!!! 使用ljust~
        return result + [' '.join(this_line).ljust(maxWidth)]


def build():
    return ["This", "is", "an", "example", "of", "text", "justification."], 16


if __name__ == "__main__":

    s = Solution()
    print(s.fullJustify(*build()))
    print(s.rewrite(*build()))
