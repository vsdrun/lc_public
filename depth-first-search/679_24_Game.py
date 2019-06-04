#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/24-game/description/


You have 4 cards each containing a number from 1 to 9.
You need to judge whether they could operated through
*, /, +, -, (, ) to get the value of 24.


Example 1:
Input: [4, 1, 8, 7]
Output: True
Explanation: (8-4) * (7-1) = 24


Example 2:
Input: [1, 2, 1, 2]
Output: False


Note:
The division operator / represents real division, not integer division.
    For example, 4 / (1 - 2/3) = 12.

Every operation done is between two numbers.

In particular, we cannot use - as a unary operator.
    For example, with [1, 1, 1, 1] as input,
        the expression -1 - 1 - 1 - 1 is not allowed.

You cannot concatenate numbers together.
    For example, if the input is [1, 2, 1, 2], we cannot write this as 12 + 12.

HAHAHA:
https://leetcode.com/problems/24-game/discuss/107670/
"""


class Solution(object):
    def judgePoint24_2(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        total = 24
        BETTER!
        """
        from __builtin__ import xrange
        level = {tuple(nums)}

        while level:
            new_level = set()

            for arr in level:
                for i in xrange(1, len(arr)):
                    for j in xrange(i):

                        newarr = arr[:j] + arr[j + 1:i] + arr[i + 1:]
                        a, b = arr[i], arr[j]
                        vs = {a + b, a - b, b - a, a * b}

                        if a:
                            vs.add(b * 1.0 / a)

                        if b:
                            vs.add(a * 1.0 / b)

                        if not newarr:

                            for v in vs:
                                if abs(v - 24) < 10**-5:
                                    return True
                        else:
                            for v in vs:
                                new_level.add(newarr + (v,))

            level = new_level
        return False

    def judgePoint24(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        total = 24
        """
        import itertools
        TARGET = 24
        EQN_LEN = 3  # (Operand, Operator, Operand) triplet.

        # Generate all possible number sequences. Convert to float string so that
        # division does not result in truncation.
        number_orders = set(
            tuple(itertools.permutations([str(num) + '.0' for num in nums])))

        # Generate all possible operator sequences.
        operator_orders = set(
            tuple(itertools.permutations('***///+++---', len(nums) - 1)))

        # Evaluate an equation with different permutation of brackets
        # and return True if any of them evaluate to the target.
        def possible(equation):
            found = [False]

            def evaluate(eqn):
                # Reduces an equation by length 2 each time:
                # An equation of ['1.0', '*', '2.0', '+', '3.0', '/', '4.0'] becomes:
                # - [2.0', '+', '3.0', '/', '4.0'] (1.0 * 2.0 reduced to 2.0)
                # - [1.0', '*', '5.0', '/', '4.0'] (2.0 + 3.0 reduced to 5.0)
                # - [1.0', '*', '2.0', '+', '0.75'] (3.0 / 4.0 reduced to 0.75)
                if found[0]:
                    return

                if len(eqn) == EQN_LEN:
                    val = eval(''.join(eqn))

                    # Compare against a delta because of floating point inaccuracies.
                    if abs(val - TARGET) < 0.0001:
                        found[0] = True

                    return
                # Recursively try different permutations
                # of operands + operators triplets, simulating brackets.
                for i in range(0, len(eqn) - 1, 2):
                    try:
                        # Wrap in try/except as there can be a division by 0 error.
                        evaluate(
                            eqn[:i] + [str(eval(''.join(eqn[i:i + EQN_LEN])))] + eqn[i + EQN_LEN:])
                    except:
                        pass
            evaluate(equation)
            return found[0]

        for number_order in number_orders:
            for operator_order in operator_orders:
                equation = [None] * (len(number_order) + len(operator_order))

                for i, number in enumerate(number_order):
                    equation[0 + i * 2] = number
                for i, operator in enumerate(operator_order):
                    equation[1 + i * 2] = operator

                # Generate an equation to test whether it is possible to get 24 using it.
                # Example equation: ['1.0', '*', '2.0', '+', '3.0', '/', '4.0']
                if possible(equation):
                    return True
        return False


def build():
    return [4, 1, 8, 7]


if __name__ == "__main__":
    s = Solution()
    print(s.judgePoint24(build()))
