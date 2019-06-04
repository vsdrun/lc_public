#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/compare-version-numbers/description/

Compare two version numbers version1 and version2.
If version1 > version2 return 1;
if version1 < version2 return -1;otherwise return 0.

You may assume that the version strings are non-empty and contain only
digits and the . character.

The . character does not represent a decimal point and is used to
separate number sequences.

For instance, 2.5 is not "two and a half" or "half way to version three",
it is the fifth second-level revision of the second first-level revision.

Example 1:
Input: version1 = "0.1", version2 = "1.1"
Output: -1


Example 2:
Input: version1 = "1.0.1", version2 = "1"
Output: 1


Example 3:
Input: version1 = "7.5.2.4", version2 = "7.5.3"
Output: -1

"""


class Solution(object):
    def compareVersion(self, version1, version2):
        """
        :type version1: str
        :type version2: str
        :rtype: int
        """
        """
        Corner cases:
        version . with 0
        """

        v1 = version1.split(".")
        v2 = version2.split(".")

        while v1 and v2:
            if int(v1[0]) > int(v2[0]):
                return 1

            if int(v1[0]) < int(v2[0]):
                return -1

            v1.pop(0)
            v2.pop(0)

        if v1 and reduce(lambda x, y: int(x) + int(y), v1, 0) == 0:
            return 0

        if v2 and reduce(lambda x, y: int(x) + int(y), v2, 0) == 0:
            return 0

        if v1:
            return 1
        if v2:
            return -1

        return 0


def build():
    return "7.5.2", "7.5.3"
    return "01", "1"
    return "1.0.000.00", "1"
    return "0.1", "0.0.1"
    return "1.0", "1.10"


if __name__ == "__main__":

    s = Solution()
    result = s.compareVersion(*build())
    print(result)
