#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def splitsql(self):
        from __builtin__ import xrange

        def strstr():
            tmp = ""
            for i in xrange(1000000):
                tmp += str(i)
            return tmp

        def strstr2():
            tmp = []
            for i in xrange(1000000):
                tmp.append(str(i))

            return "".join(tmp)

        import time
        start = time.time()
        strstr()
        end = time.time()
        print("str conct: {}".format(end - start))

        start = time.time()
        strstr2()
        end = time.time()
        print("list conct: {}".format(end - start))


def build():
    return "SELECT whatever FROM wherever WHERE this = " \
        "\"; 3 \\a\\b\"; DROP TABLE wherever; select * from \" read me; or\";"


if __name__ == "__main__":

    s = Solution()
    result = s.splitsql()
