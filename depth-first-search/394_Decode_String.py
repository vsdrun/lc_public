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
    def decodeString_mycode(self, val):
        """
        :type s: str
        :rtype: str
        """
        stack = []

        # 初始化~
        stack += ["", 1],
        num = ""

        for c in val:
            if c.isdigit():
                num += c
            elif c == "[":
                stack.append(["", int(num)])
                num = ""
            elif c == "]":
                st, k = stack.pop()
                stack[-1][0] += st * k
            else:
                stack[-1][0] = stack[-1][0] + c

        return stack[0][0]

    def decodeString(self, val):
        """
        :type s: str
        :rtype: str
        """

        stack = []
        stack.append(["", 1])
        num = ""

        for ch in val:
            if ch.isdigit():
                num += ch
            elif ch == '[':
                stack.append(["", int(num)])
                num = ""
            elif ch == ']':
                st, k = stack.pop()
                stack[-1][0] += st * k
            else:
                stack[-1][0] += ch
        return stack[0][0]

    def rewrite(self, val):
        """
        :type s: str
        :rtype: str
        s = "3[a2[c]]", return "accaccacc".
        """
        stack = [[0, []]]  # number, result
        val = list(val)

        while val:
            tmp_digit = ""
            v = None

            while True:
                v = val.pop(0)
                if not v.isdigit():
                    break
                tmp_digit += v

            if tmp_digit:
                stack.append([int(tmp_digit), []])
            elif v == '[':
                continue
            elif v == ']':
                num, result = stack.pop()
                stack[-1][1].extend(num * result)
            else:
                stack[-1][1].append(v)

        return "".join(stack[0][1])

    def rewrite2(self, val):
        """
        :type s: str
        :rtype: str
        s = "3[a2[c]]", return "accaccacc".
        優美... please...
        """
        stack = [['1', '']]
        num = ''
        content = ''

        for c in val:
            if c.isdigit():
                num += c
            elif c == '[':
                stack.append([int(num), ''])
                num = ''
            elif c == ']':
                cnt, content = stack.pop()
                stack[-1][1] = stack[-1][1] + cnt * content
            else:
                stack[-1][1] = stack[-1][1] + c

        return stack[0][1]


def build():
    return "2[abc]3[cd]ef"
    return "100[leetcode]"
    return "3[z]2[2[y]pq4[2[jk]e1[f]]]ef"
    return "xx"
    return "xx3[ab2[cd]]ef3[a]ggg"
    return "3[a2[c]]"


if __name__ == "__main__":
    n = build()

    s = Solution()
    result = s.decodeString(n)
    print(result)
    result = s.decodeString_mycode(n)
    print(result)
    result = s.rewrite(n)
    print(result)
    result = s.rewrite2(n)
    print(result)
