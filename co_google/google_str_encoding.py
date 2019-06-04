#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
banana => cololo  1 to 1 ok, reverse 1 to 1 , ok
banana => dddddd 1 to 1 ok, reverse 1 to many, not ok
"""


class Solution(object):
    def check(self, tw, ew):

        if len(tw) != len(ew):
            return False

        tw = list(tw)
        ew = list(ew)

        from collections import defaultdict as dd

        dmap_fwd = dd(set)
        dmap_bk = dd(set)

        while tw:
            e = ew.pop()
            t = tw.pop()
            dmap_fwd[t].add(e)
            dmap_bk[e].add(t)

        for v in dmap_fwd.values():
            if len(v) > 1:
                return False

        for v in dmap_bk.values():
            if len(v) > 1:
                return False
        return True


def build():
    return "banana", "coldlo"
    return "banana", "cololo"
    return "banana", "dddddd"


if __name__ == "__main__":
    s = Solution()
    print(s.check(*build()))
