#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/valid-number/

Validate if a given string can be interpreted as a decimal number.

Some examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
" -90e3   " => true
" 1e" => false
"e3" => false
" 6e-1" => true
" 99e2.5 " => false
"53.5e93" => true
" --6 " => false
"-+3" => false
"95a54e53" => false


Note:
It is intended for the problem statement to be ambiguous.
You should gather all requirements up front before implementing one.
However, here is a list of characters that can be in a valid decimal number:
Numbers 0-9
Exponent - "e"
Positive/negative sign - "+"/"-"
Decimal point - "."
Of course, the context of these characters also matters in the input.

https://leetcode.com/problems/valid-number/discuss/23728/A-simple-solution-in-Python-based-on-DFA
"""


class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        #define a DFA
        state = [
            {}, # 0
            {'blank': 1, 'sign': 2, 'digit':3, '.':4}, # 1
            {'digit':3, '.':4}, # 2
            {'digit':3, '.':5, 'e':6, 'blank':9}, # 3
            {'digit':5}, # 4
            {'digit':5, 'e':6, 'blank':9}, # 5
            {'sign':7, 'digit':8}, # 6
            {'digit':8}, # 7
            {'digit':8, 'blank':9}, # 8
            {'blank':9} # 9
        ]

        currentState = 1

        for c in s:
            if c >= '0' and c <= '9':
                c = 'digit'
            if c == ' ':
                c = 'blank'
            if c in ['+', '-']:
                c = 'sign'

            if c not in state[currentState].keys():
                return False
            currentState = state[currentState][c]

        if currentState not in [3,5,8,9]:
            return False

        return True

def build():
    return "0..5"
    return "53.5e93"


if __name__ == "__main__":
    s = Solution()
    print(s.isNumber(build()))
