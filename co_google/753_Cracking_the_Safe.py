#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/cracking-the-safe/description/

There is a box protected by a password.
The password is n digits,
where each letter can be one of the first k digits 0, 1, ..., k-1.

You can keep inputting the password,
the password will automatically be matched against the last n digits entered.

For example, assuming the password is "345",
I can open it when I type "012345", but I enter a total of 6 digits.

Please return any string of minimum length that is
guaranteed to open the box after the entire string is inputted.

Example 1:
Input: n = 1, k = 2
Output: "01"
Note: "10" will be accepted too.


Example 2:
Input: n = 2, k = 2, 也就是共有 2^2 種排列:
00
01
10
11
那麼怎樣把以上排列串成一串?
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.


概念:
1. Hamilton path
steps:
    Write every combination of length 'n' and visit every node
    exactly once.

2. Euler Path
steps:
    Write every combination of length 'n-1' and visit every edge exactly
    once.

The number of De Bruijin sequences is the number of Euler Circle.

Make a combination of length n, and all the combination that
devides n.

e.g n = 4
(1 與 2 可以除盡 4)
make a combination of length 4, and 1, and 2, which devides 4.

then cross off periodic sequences.
e.g

1
11  cross off
1111  cross off
1112

then cross off rotated which make the same sequence before.
e.g
1211 -> 1112 thus cross off.
"""


class Solution(object):
    def crackSafe(self, n, k):
        """
        :type n: int  密碼長度為n
        :type k: int  數字有k種
        :rtype: str

        使用Hamilton path來解題, visit every node once, append the largest
        number for every loop.
        """
        # We are using Hamilton path, thus preserve n - 1 numbers since
        # we are appending next number into the ans.
        ans = "0" * (n - 1)
        visits = set()  # 含長度為 n 的解答, 因為我們用 Hamilton path.

        for _ in range(k ** n):  # 因為有 k^n次方種

            # 拿ans最後 -n + 1 位的數字為此current
            current = ans[-n + 1:] if n > 1 else ''

            print("ans [-{} + 1:] : {}".format(n, ans[-n+1:]))
            print("current: {}".format(current))

            # 必須由大到小才能走訪 Hamilton path.
            # 如果直接找小 則會有大的被miss.
            for y in range(k - 1, -1, -1):  # k = 2, => 1,0
                if current + str(y) not in visits:  # '0' + '1'
                    visits.add(current + str(y))  # '01'
                    ans += str(y)  # '0' + '1' => '01' '11' '10' '00'
                    print("visits: {}".format(visits))
                    print("ans: {}".format(ans))
                    break

            print("----")
        return ans

def build():
    return 2, 2
    return 3, 2


if __name__ == "__main__":

    s = Solution()
    print(s.crackSafe(*build()))
