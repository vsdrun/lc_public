#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def work(self):

        import bisect as bi

        class Range(object):

            def __getitem__(self, idx):
                print(idx)
                return 1

        r = bi.bisect_left(Range(), 3, 0, 100)
        print(r)


if __name__ == "__main__":

    s = Solution()
    print(s.work())
