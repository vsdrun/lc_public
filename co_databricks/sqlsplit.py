#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
然后是一道coding 题目是这样的给你一个String 里面包含了一
些用分号“;" 隔开的Query  让你返回所有合法的query.
比如select name from courseinfo;; select * from "; " ;

Split by semicolons, except escaped semicolons.
(initially forgot semicolons in
quotes)
"""


class Solution(object):
    def splitsql(self, sql):
        """
        :type sql: str
        :rtype: list[str]
        """
        sql = list(sql)

        ignore_set = set()
        result = []

        tmp_result = []
        escape_stack = []

    #  return "SELECT whatever FROM wherever WHERE this = " \
        #  "\";\\\\\"; DROP TABLE wherever;"
        while sql:

            if escape_stack:
                escape_stack += sql.pop(0),
                tmp_result += "".join(escape_stack),
                escape_stack = []
                continue

            if sql[0] == "\\":
                escape_stack += sql.pop(0),
                continue

            if sql[0] == ";" and not ignore_set:
                sql.pop(0)
                result += "".join(tmp_result).strip(),
                tmp_result = []
                continue

            if sql[0] == "\"" and sql[0] not in ignore_set:
                ignore_set.add("\"")
                tmp_result += sql.pop(0),
                continue
            elif sql[0] == "\"" and sql[0] in ignore_set:
                ignore_set.remove(sql[0])
                tmp_result += sql.pop(0),
                continue

            tmp_result += sql.pop(0),
        return result


def build():
    return "SELECT whatever FROM wherever WHERE this = " \
        "\"; 3 \\a\\b\"; DROP TABLE wherever; select * from \" read me; or\";"


if __name__ == "__main__":

    s = Solution()
    result = s.splitsql(build())

    print(result)
