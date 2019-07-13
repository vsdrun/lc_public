#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/decode-string/description/

Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string],
where the encoded_string inside the square brackets is being repeated
exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid;
No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits
and that digits are only for those repeat numbers, k. For example, there won't
be input like 3a or 2[4].

Examples:

s = "3[a]2[bc]", return "aaabcbc".
s = "3[a2[c]]", return "accaccacc".
s = "2[abc]3[cd]ef", return "abcabccdcdcdef".

這種問題首先要定義出條件.
1. 數字, push into stack
2. 將數字後[]放入stack
3. 沒有數字在前的string 放入 stack
4. 開始pop()
5. 遇到數字則回到1.

賤招:
https://discuss.leetcode.com/topic/57145/3-lines-python-2-lines-ruby-regular-expression

def decodeString(self, s):
    while '[' in s:
        s = re.sub(r'(\d+)\[([a-z]*)\]', lambda m: int(m.group(1)) * m.group(2), s)
    return s
"""


class Solution(object):
    def decodeString(self, s):
        """
        :type s: str
        :rtype: str
        return "22[abc]3[cd]ef"
        "3[a2[c]]", return "accaccacc".
        """
        cnt = ""
        stack = [[1, ""]]

        for c in s:
            if c.isdigit():
                cnt += c
            elif c == "[":
                stack.append([int(cnt), ""])
                cnt = ""
            elif c == "]":
                count, words = stack.pop()
                result = words * count
                stack[-1][1] += result
            else:
                stack[-1][1] += c

        return stack[-1][1] * stack[-1][0]

def build():
    return "3[a2[c]]"
    return "xx"
    return "100[leetcode]"
    return "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    return "2[abc]3[cd]ef"
    return "xx3[ab2[cd]]ef3[a]ggg"


if __name__ == "__main__":
    n = build()

    s = Solution()
    result = s.decodeString(n)
    print(result)
