#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/

Given an array of numbers,
verify whether it is the correct preorder traversal sequence of a
binary search tree.

You may assume each number in the sequence is unique.

Consider the following binary search tree:
     5
    / \
   2   6
  / \
 1   3


Example 1:
Input: [5,2,6,1,3]
Output: false


Example 2:
Input: [5,2,1,3,6]
Output: true

Follow up:
Could you do it using only constant space complexity?

449 與 serialize/unserialize BST 不一樣! 因為這裡有錯
而 s/u bst沒有錯!!
"""

class Solution(object):
    def verifyPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        deserialize
        看到BST想到 while 最左邊...
        """
        stack = []
        low = float('-inf')

        for p in preorder:
            # 往回走了~~~
            if p < low:
                return False
            while stack and p > stack[-1]:
                low = stack.pop()
            stack.append(p)

        return True

    def rewrite(self, preorder):
        """
        :type preorder: List[int]
        :rtype: bool
        deserialize
        [5,2,1,3,6] # true
        [5,2,6,1,3] # false
        """
        data = preorder[::-1]


def build():
    """
         5
        / \
       2   6
      / \
     1   3

    2 1 3
    """
    return [5,2,1,3,6] # true
    return [5,2,6,1,3] # false

if __name__ == "__main__":
    s = Solution()
    print(s.verifyPreorder(build()))
    print(s.rewrite(build()))
