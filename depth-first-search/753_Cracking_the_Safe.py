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
Input: n = 2, k = 2
Output: "00110"
Note: "01100", "10011", "11001" will be accepted too.

1. Hamilton path
visits each vertex exactly once.

2. Euler Path
uses every edge of a graph exactly once.

The number of De Bruijin sequences is the number of Euler Circle.

Make a combination of length n, and all the combination that
devides n.

e.g n = 4
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
        hamilton edge:
        所有k個數字的連結為edge
        if k = 2, i.e 1,2

        11
        12
        22
        21
        想像 如果在一個edge後加一個數字 可以與下一個edge重疊...
        例如:
        11 + 2 => 11, 12
        Thus we get a graph. All we have to do is to find a path
        visit every node once!
        """
        # if n == 2
        ans = "0" * (n - 1)  # ans = 1  [0]

        visits = set()  # 含 長度為 n 的 解答

        for _ in range(k ** n):  # 因為有 k^n次方種

            # 固定 n - 1 個 每次測試 1 個, 和為 n 位解答.
            current = ans[-n + 1:] if n > 1 else ''  # [-1:] 即ans全包

            # 必須由大到小才能走訪 Hamilton path.
            # 如果直接找小 則會有大的被miss.
            for y in range(k - 1, -1, -1):  # k = 2, => 1,0

                if current + str(y) not in visits:  # '0' + '1'
                    visits.add(current + str(y))  # '01'
                    ans += str(y)  # '0' + '1' => '01' '11' '10' '00'
                    break
        return ans

    def rewrite(self, n, k):
        """
        :type n: int  密碼長度為n
        :type k: int  數字有k種
        :rtype: str
        hamilton edge:
        所有k個數字的連結為edge
        if k = 2, i.e 1,2

        11
        12
        22
        21
        想像 如果在一個edge後加一個數字 可以與下一個edge重疊...
        例如:
        11 + 2 => 11, 12
        Thus we get a graph. All we have to do is to find a path
        visit every node once!
        """
        ans = '0' * (n - 1)  # 由0開始.


def build():
    return 2, 3


if __name__ == "__main__":

    s = Solution()
    print(s.crackSafe(*build()))
