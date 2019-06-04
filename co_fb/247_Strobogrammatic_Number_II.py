#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/strobogrammatic-number-ii/description/


A strobogrammatic number is a number that looks the same when
rotated 180 degrees (looked at upside down).

Find all strobogrammatic numbers that are of length = n.

For example,
Given n = 2, return ["11","69","88","96"].

corner cases:
0 1 6 8 9
"""


class Solution(object):
    def findStrobogrammatic(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        char_dict = dict()
        char_dict['0'] = '0'
        char_dict['1'] = '1'
        char_dict['8'] = '8'
        char_dict['6'] = '9'
        char_dict['9'] = '6'

        def build(i, j, ary):
            result = []
            if i != j:
                for k in char_dict:
                    if i == 0 and k == '0':
                        continue
                    ary[i] = k
                    ary[j] = char_dict[k]
                    result.append(ary[:])
            else:
                ary[j] = '0'
                result.append(ary[:])
                ary[j] = '1'
                result.append(ary[:])
                ary[j] = '8'
                result.append(ary[:])

            return result

        i = 0
        j = n - 1

        result_list = [[None] * n]
        result = []

        while i <= j:
            tmp_result_list = []

            for ll in result_list:
                tmp_result_list.extend(build(i, j, ll))

            result_list = tmp_result_list
            i += 1
            j -= 1

        for ll in result_list:
            result.append("".join(ll))

        return result

    def rewrite(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        dmap = dict([('0','0'), ('1','1'), ('6','9'), ('8','8'), ('9','6')])
        result = []

        placeHolder = [None] * n

        def build(i, j):
            if n%2 == 0 and i == n/2 or i > n/2:
                result.append("".join(placeHolder[:]))
                return

            for k in dmap:
                if k == '0' and i == 0 and n > 1:
                    continue


                if i != (n + j):
                    placeHolder[i] = k
                    placeHolder[j] = dmap[k]
                else:
                    if k == '0' or k == '1' or k == '8':
                        placeHolder[i] = k
                    else:
                        continue

                build(i+1, ~(i+1))


        build(0, ~0)
        return result


    def rewriteFast(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        evenMidCandidate = ["11","69","88","96", "00"]
        oddMidCandidate = ["0", "1", "8"]

        if n == 1:
            return oddMidCandidate
        if n == 2:
            return evenMidCandidate[:-1]

        if n % 2:
            pre, midCandidate = self.findStrobogrammatic(n-1), oddMidCandidate
        else:
            pre, midCandidate = self.findStrobogrammatic(n-2), evenMidCandidate

        premid = (n-1)/2

        return [p[:premid] + c + p[premid:] for c in midCandidate for p in pre]


def build():
    return 7
    return 1  # corner case
    return 4


if __name__ == "__main__":
    s = Solution()
    print(sorted(s.findStrobogrammatic(build())))
    print(sorted(s.rewrite(build())))
