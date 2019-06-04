#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/remove-comments/description/

Example 1:
Input:
source = ["/*Test program */", "int main()", "{ ",
"  // variable declaration ", "int a, b, c;", "/* This is a test",
"   multiline  ", "   comment for ", "   testing */", "a = b + c;", "}"]

The line by line code is visualized as below:
/*Test program */
int main()
{
  // variable declaration
int a, b, c;
/* This is a test
   multiline
   comment for
   testing */
a = b + c;
}

Output: ["int main()","{ ","  ","int a, b, c;","a = b + c;","}"]

The line by line code is visualized as below:
int main()
{

int a, b, c;
a = b + c;
}


Explanation:
The string /* denotes a block comment, including line 1 and lines 6-9.
The string // denotes line 4 as comments.
"""


class Solution(object):
    def removeComments(self, source):
        """
        :type source: List[str]
        :rtype: List[str]

        1. contains // , remove what's after.
        2. contains /*, remove what's after.
        3. contains */, remove what's before.
        4. anchor, what's between /* and */ should be removed
        """

        c1 = "//"
        c2_1 = "/*"
        c2_2 = "*/"
        c2Flag = False

        idx = -1

        result = []

        while idx < len(source):
            idx += 1

            if idx >= len(source) or not source[idx]:
                continue

            current = source[idx]
            c1Idx = float("inf")
            c21Idx = float("inf")
            c22Idx = float("inf")
            #  print("current: {}".format(current))

            if not c2Flag and c1 in current:
                c1Idx = current.index(c1)
            if not c2Flag and c2_1 in current:
                c21Idx = current.index(c2_1)
            if c2_2 in current:
                c22Idx = current.index(c2_2)

            if c22Idx != float("inf"):
                c2Flag = False
                if current[c22Idx+2:]:
                    result.append(current[c22Idx+2:])
                continue

            if c2Flag:
                continue

            if c1Idx == c21Idx == c22Idx == float("inf"):
                result.append(current)
                continue

            rmIdx = min(c1Idx, c21Idx)
            if rmIdx < float("inf"):
                if rmIdx == c21Idx and c22Idx == float("inf"):
                    c2Flag = True

                if rmIdx == 0:
                    continue
                else:
                    result.append(current[:rmIdx])
                    continue


        return result



def build():
    return ["/*Test program */",
            "int main()",
            "{ ",
            "  // variable declaration ",
            "int a, b, c;",
            "/* This is a test",
            "   multiline  ",
            "   comment for ",
            "   testing */",
            "a = b + c;",
            "}"]


if __name__ == "__main__":
    s = Solution()
    print(s.removeComments(build()))
