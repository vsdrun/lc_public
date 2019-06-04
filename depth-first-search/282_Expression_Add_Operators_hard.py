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
        from __builtin__ import xrange

        result = []

        def dfs(previous_total,
                previous_value,
                pop,
                low_index,
                previous_str):
            """
            :param int previous_total: previous total, shoud not be modified.
            :param int previous_value: previous single value.
            :param str pop: previous op.
            :param int low_index: previous index
            :param str previous_str: accumulate str.
            """

            # 止
            if low_index == len(num) and previous_total == target:
                result.append(previous_str)

            for high_index in xrange(low_index + 1, len(num) + 1):

                cval = int(num[low_index:high_index])

                # 若為0開頭 則表留一個0即可.
                # 其他的由下一個recursive去處理.
                if high_index > low_index + 1 and \
                        str(cval) != num[low_index:high_index]:
                    break

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

                # 因為先乘除後加減...
                # * 有higher priority.
                dfs(previous_total - previous_value + previous_value * cval
                    if pop == "+" else
                    previous_total + previous_value - previous_value * cval
                    if pop == "-" else
                    previous_value * cval,  # init.
                    previous_value * cval,
                    pop,  # pass through last +/- operator.
                    high_index,
                    previous_str + "*" + num[low_index:high_index])

        # starts here:
        for high_index in xrange(1, len(num) + 1):
            cval = int(num[0:high_index])

            # 吃掉0為始的數字
            if high_index > 1 and str(cval) != num[0:high_index]:
                break

            cur_str = num[0:high_index]

            dfs(cval,
                cval,
                "",
                high_index,
                cur_str)

        return sorted(result)

    def rewrite(self, num, target):
        """
        思考: 為一個 dfs TREE!
        + - * 為 edge , 數字為node.
        """
        result = []
        length = len(num)

        def dfs(previousTotal,
                previousVal,
                previousOp,
                previousIdx,
                previousStr):
            """
            要做啥?
            1. 將上一個值 的 子 處理.
            2. 將上一個值 的 str 與 此子值 str 處理.
            """

            if previousIdx == length and previousTotal == target:
                result.append(previousStr)
                return

            # build tree.
            for idx in range(previousIdx + 1, length + 1):
                currentVal = int(num[previousIdx: idx])

                # 跳過超過一個0的數 讓其他的0由下一個recursive處裡.
                if idx >= previousIdx + 1 and \
                        str(currentVal) != num[previousIdx:idx]:
                    break
                # +
                dfs(previousTotal + currentVal,
                    currentVal,
                    "+",
                    idx,
                    previousStr + "+" + num[previousIdx:idx])

                # -
                dfs(previousTotal - currentVal,
                    currentVal,
                    "-",
                    idx,
                    previousStr + "-" + num[previousIdx:idx])

                # *
                dfs(previousTotal - previousVal + previousVal * currentVal
                    if previousOp == "+" else
                    previousTotal + previousVal - previousVal * currentVal
                    if previousOp == "-" else
                    previousVal * currentVal,
                    previousVal * currentVal,
                    previousOp,
                    idx,
                    previousStr + "*" + num[previousIdx:idx])

        # start
        for idx in range(1, length + 1):
            currentVal = int(num[0:idx])
            currentStr = num[0:idx]

            # 若為0 保留一個0即可 剩下的交由下個recursive 處理.
            if idx > 1 and str(int(num[:idx])) != currentStr:
                break

            dfs(currentVal,
                currentVal,
                "",
                idx,
                currentStr)

        return result


def build():
    return "10023", 6
    return "3456237490", 9191
    return "12342", 26
    return "00", 0
    return "105", 0
    return "00", 0


if __name__ == "__main__":

    s = Solution()
    print(s.addOperators(*build()))
    print(s.rewrite(*build()))
