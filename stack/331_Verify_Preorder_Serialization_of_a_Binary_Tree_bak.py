#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
One way to serialize a binary tree is to use pre-order traversal. When we
encounter a non-null node, we record the node's value. If it is a null node, we
record using a sentinel value such as #.

     _9_
    /   \
   3     2
  / \   / \
 4   1  #  6
/ \ / \   / \
# # # #   # #


For example, the above binary tree can be serialized to the string
"9,3,4,#,#,1,#,#,2,#,6,#,#", where # represents a null node.

Given a string of comma separated values, verify whether it is a
correct preorder traversal serialization of a binary tree.
**
Find an algorithm without reconstructing the tree.
**

Each comma separated value in the string must be either an
integer or a character '#' representing null pointer.

You may assume that the input format is always valid,
for example it could never contain two consecutive commas such as "1,,3".

Example 1:
"9,3,4,#,#,1,#,#,2,#,6,#,#"
Return true

Example 2:
"1,#"
Return false

Example 3:
"9,#,#,1"
Return false
"""
"""
Concept:
1. 若為preorder, 若有Null/# 為end node, 則可以產生唯一的bin-tree.
2. 若為preorder, 若沒有Null/# 為end node, 則不可能產生唯一的bin-tree.
3. expect #為左/右的結束.
"""


class Solution(object):

    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """

        length = len(preorder)
        print("length: {0}".format(length))

        #  return "90,13,14,#,#,10"

        def check(root_str, moving_index):
            start = moving_index

            while moving_index < length and root_str[moving_index] != ",":
                moving_index += 1

            root = root_str[start: moving_index]
            print("root: {0}".format(root))
            print("root index: {0}".format(moving_index))

            if root == "#":
                return "#", moving_index

            # 判斷是否超過index
            if moving_index + 1 > length:
                return root, moving_index

            left, moving_index = check(root_str,
                                       moving_index + 1)

            print("left: {0}".format(left))

            # 判斷是否超過index
            if moving_index + 1 > length:
                return root, moving_index

            right, moving_index = check(root_str,
                                        moving_index + 1)
            print("right: {0}".format(right))
            print("right index: {0}".format(moving_index))

            if left == right and left == "#":
                return "#", moving_index

            return root, moving_index

        root, moving_index = check(preorder, 0)

        print(root)
        print(moving_index)

        if root == "#" and moving_index == length:
            return True
        return False


def build():
    return "1,#", False
    return "#,1,2", False
    return "91,13,14,#,#,10", False
    return "19,3,24,#,#,1,#,#,2,#,6,#,#", True
    return "223,#,#", True
    return "9,#,#,1", False


if __name__ == "__main__":
    n, _ = build()
    s = Solution()
    r = s.isValidSerialization(n)

    print(r)
