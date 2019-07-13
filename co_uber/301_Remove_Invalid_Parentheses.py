#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/remove-invalid-parentheses/description/

移除最少~
Remove the minimum number of invalid parentheses in order to
make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Examples:

"()())()" -> ["()()()", "(())()"]
"(a)())()" -> ["(a)()()", "(a())()"]
")(" -> [""]

暴力解法
一次拿掉一個char 測試
若拿掉一個char 不夠 拿掉兩個
不夠 拿掉三個.
"""


class Solution(object):
    def removeInvalidParentheses(self, s):
        """
        :type s: str
        :rtype: List[str]

        BFS 起手勢變形~ 將 root 加入 list.
        """
        # all into a single set.
        level = {s}  # set(["(())"])
        #  print("level: {}".format(level))

        while True:
            valid = []

            for s in level:
                # s 為 整個string: "(()"
                try:
                    # filter return the string that matches
                    eval(
                        # '0,' is necessary due to is s is empty,
                        # we need a stop point here, which is that
                        # '0,' is valid thus end the while True loop.
                        '0,' + filter('()'.count, s).replace(')', '),')
                    )

                    valid.append(s)
                except Exception:
                    pass

            if valid:
                return valid

            # 重點!
            # 取代掉level~
            # 每一個均測試.
            # THIS IS BFS, 一次一layer.
            level = {s[:i] + s[i + 1:] for s in level for i in range(len(s))}
            # 跑一次這裡代表拿掉一個char.
            # 若需要拿掉兩個char 則這裡會被hit 兩次。
            #  print("level 2: {}".format(level))

    def rewrite(self, s):
        """
        :type s: str
        :rtype: List[str]
        my best and clear solution :-)
        BFS 起手勢變形~ 將 root 加入 list.
        """
        def check(s):
            """
            :ret: bool
            """
            stack = []

            for c in s:
                if c == '(':
                    stack.append(c)
                else:
                    if stack:
                        stack.pop()
                    else:
                        return False

            if stack:
                return False
            else:
                return True


        roots = set([s])
        result = []

        while roots:
            tmp = set()

            for r in roots:
                r = filter("()".count, r)

                if check(r):
                    result.append(r)


                for i in range(len(r)):
                    tmp.add(r[:i] + r[i+1:])

            if result:
                return result

            roots = tmp

        return result


def build():
    """
    ['()()()()()', '(())()()()']
    ['(())()()()']
    """
    return "()())()()(()"
    return "("
    return ")("
    return "())"


if __name__ == "__main__":
    s = Solution()
    print(s.removeInvalidParentheses(build()))
    print(s.rewrite(build()))
