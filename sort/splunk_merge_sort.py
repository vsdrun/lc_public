#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
Merge Sort
"""


# Definition for an interval.


class Solution(object):
    def mergesort(self, ary):

        def merge(arg):
            if len(arg) > 1:
                half = len(arg) // 2
                lhalf = arg[:half]
                rhalf = arg[half:]

                llist = merge(lhalf)
                rlist = merge(rhalf)

                result = []

                li = ri = 0

                while li < len(llist) and ri < len(rlist):
                    if llist[li] < rlist[ri]:
                        result.append(llist[li])
                        li += 1
                    else:
                        result.append(rlist[ri])
                        ri += 1

                result += rlist[ri:] if ri < len(rlist) - 1 else llist[li:]

                return result
            else:
                return arg

        result = merge(ary)
        return result

    def findLargeSmall(self, ary):

        self.cnt = 0
        fr = []

        def merge(arg):
            if len(arg) > 1:
                half = len(arg) // 2
                lhalf = arg[:half]
                rhalf = arg[half:]

                llist = merge(lhalf)
                rlist = merge(rhalf)

                # do cnt here.
                li = len(llist) - 1
                ri = len(rlist) - 1

                print("llist: {}".format(llist))
                print("rlist: {}".format(rlist))

                while li >= 0 and ri >= 0:
                    if llist[li] > rlist[ri]:
                        self.cnt += len(rlist[:ri + 1])
                        fr.append((llist[li], rlist[:ri + 1]))
                        li -= 1
                        ri = len(rlist) - 1
                    else:
                        ri -= 1

                result = []

                li = ri = 0

                while li < len(llist) and ri < len(rlist):
                    if llist[li] < rlist[ri]:
                        result.append(llist[li])
                        li += 1
                    else:
                        result.append(rlist[ri])
                        ri += 1

                result += rlist[ri:] if ri < len(rlist) - 1 else llist[li:]

                return result
            else:
                return arg

        merge(ary)

        print("fr: {}".format(fr))
        return self.cnt


def build():
    # [5] [1]
    # [1, 5] [3, 4]
    # [1, 3, 5] [2, 4, 9]
    return [5, 1, 3, 4, 2, 9]


if __name__ == "__main__":
    s = Solution()
    result = s.mergesort(build())

    result = s.findLargeSmall(build())
    print(result)
