#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/expression-add-operators/description/


Given a string that contains only digits 0-9 and a target value,
return all possibilities to add binary operators (not unary)
+, -, or * between the digits so they evaluate to the target value.


Examples:
"123", 6 -> ["1+2+3", "1*2*3"]
"232", 8 -> ["2*3+2", "2+3*2"]
"105", 5 -> ["1*0+5","10-5"]
"00", 0 -> ["0+0", "0-0", "0*0"]
"3456237490", 9191 -> []
"""


class Solution(object):
    def addOperators(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        1 23
        12 3
        123
        --
        1 23
        1 2 3
        1 23
        --
        12 3
        12 3
        --
        123
        123
        beware of "001" convert to int is '1'
        '00' -> '0'
        '01' -> '1'

        moving index
        """
        result = []

        def dfs(previous_total,
                previous_value,
                pop,
                low_index,
                previous_str):
            """
            :param previous_total: previous total, shoud not be modified.
            :param previous_value: previous single value.
            :param pop: previous op.
            """
            if low_index == len(num) and previous_total == target:
                result.append(previous_str)

            for high_index in xrange(low_index + 1, len(num) + 1):

                cval = int(num[low_index:high_index])

                # 兩位數以上其值卻小於10代表為
                # 00 or 0[1,9] 等數 須跳過.
                if high_index > low_index + 1 and \
                        str(cval) != num[low_index:high_index]:
                    continue

                dfs(previous_total + cval,
                    cval,
                    "+",
                    high_index,
                    previous_str + "+" + num[low_index:high_index])

                dfs(previous_total - cval,
                    cval,
                    "-",
                    high_index,
                    previous_str + "-" + num[low_index:high_index])

                dfs(previous_total - previous_value + previous_value * cval
                    if pop == "+" else
                    previous_total + previous_value - previous_value * cval
                    if pop == "-" else
                    previous_value * cval,  # init.
                    previous_value * cval,
                    pop,  # pass through last +/- operator.
                    high_index,
                    previous_str + "*" + num[low_index:high_index])

        for high_index in xrange(1, len(num) + 1):
            cval = int(num[0:high_index])

            if high_index > 1 and str(cval) != num[0:high_index]:
                continue

            cur_str = num[0:high_index]

            dfs(cval,
                cval,
                "",
                high_index,
                cur_str)

        return result

    def rewrite(self, num, target):
        """
        :type num: str
        :type target: int
        :rtype: List[str]
        1 23
        12 3
        123
        --
        1 23
        1 2 3
        1 23
        --
        12 3
        12 3
        --
        123
        123
        beware of "001" convert to int is '1'
        '00' -> '0'
        '01' -> '1'

        moving index
        """
        result = []

        def dfs(accum, preval, preop, rstr, lowbound):

            if lowbound == len(num) and accum == target:
                result.append(rstr)

            for idx in range(lowbound + 1, len(num) + 1):  # 注意boundary
                intvar = int(num[lowbound:idx])

                if str(intvar) != num[lowbound:idx]:
                    continue

                dfs(
                    accum + intvar,
                    intvar,
                    "+",
                    rstr + "+" + str(intvar),
                    idx
                )
                dfs(
                    accum - intvar,
                    intvar,
                    "-",
                    rstr + "-" + str(intvar),
                    idx
                )
                dfs(
                    accum - preval + preval * intvar if preop == "+" else
                    accum + preval - preval * intvar if preop == "-" else
                    preval * intvar,
                    preval * intvar,  # beware here, 1 + 2*2 * thisNum
                    preop,  # why? 1 + 2*2 * thisNum
                    rstr + "*" + str(intvar),
                    idx
                )


        for idx in range(1, len(num) + 1):  # 注意boundary
            intvar = int(num[0:idx])

            dfs(
                intvar, # added val
                intvar, # cur val
                "", # operator
                num[0:idx], # str, since it's string, index of string range is
                #  string.
                idx # low bound
            )

        return result


def build():
    return "12342", 26
    return "3456237490", 9191
    return "123", 6
    return "00", 0
    return "105", 0
    return "00", 0


if __name__ == "__main__":

    s = Solution()
    print(s.addOperators(*build()))
    print(s.rewrite(*build()))
