#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/longest-absolute-file-path/description/

Suppose we abstract our file system by a string in the following manner:

一個'\t'代表一層

The string "dir\n\tsubdir1\n\tsubdir2\n\t\tfile.ext" represents:
dir
    subdir1
    subdir2
        file.ext

The directory dir contains an empty sub-directory subdir1 and a
sub-directory subdir2 containing a file file.ext.

The string
"dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\tsubdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"
represents:

dir
    subdir1
        file1.ext
        subsubdir1
    subdir2
        subsubdir2
            file2.ext

The directory dir contains two sub-directories subdir1 and subdir2.
subdir1 contains a file file1.ext and an empty second-level sub-directory
subsubdir1. subdir2 contains a second-level sub-directory subsubdir2
containing a file file2.ext.

We are interested in finding the longest (number of characters)
absolute path to a file within our file system.
For example, in the second example above, the longest absolute
path is "dir/subdir2/subsubdir2/file2.ext",
and its length is 32 (not including the double quotes).

Given a string representing the file system in the above format, return the
length of the longest absolute path to file in the abstracted file system. If
there is no file in the system, return 0.

Note:
注意!!
**The name of a file contains at least a . and an extension.
**The name of a directory or sub-directory will not contain a ..

Time complexity required: O(n) where n is the size of the input string.

Notice that a/aa/aaa/file1.txt is not the longest file path,
if there is another path aaaaaaaaaaaaaaaaaaaaa/sth.png.
"""


class Solution(object):
    def lengthLongestPath(self, input):
        """
        :type input: str
        :rtype: int
        """
        """
        Idea:
        current layer max
        global max
        """
        maxlen = 0
        pathlen = {0: 0}

        for line in input.splitlines():
            name = line.lstrip('\t')
            depth = len(line) - len(name)

            # 代表為檔案
            if '.' in name:
                maxlen = max(maxlen, pathlen[depth] + len(name))
            # 代表為path
            else:
                # + 1 代表 '\'
                pathlen[depth + 1] = pathlen[depth] + len(name) + 1

        return maxlen


def build():
    ret = \
        "dir\n\tsubdir1\n\t\tfile1.ext\n\t\tsubsubdir1\n\t" \
        "subdir2\n\t\tsubsubdir2\n\t\t\tfile2.ext"

    ret = "dir\n\tha\n\thaha"
    return ret


if __name__ == "__main__":
    s = Solution()
    result = s.lengthLongestPath(build())

    print(result)
