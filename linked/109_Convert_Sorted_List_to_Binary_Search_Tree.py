#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/

Given a singly linked list where elements are sorted in ascending order,
convert it to a height balanced BST.

For this problem,
a height-balanced binary tree is defined as a binary tree in which
the depth of the two subtrees of every node never differ by more than 1.


Example:
Given the sorted linked list: [-10,-3,0,5,9],

One possible answer is: [0,-3,9,-10,null,5],
which represents the following height balanced BST:

      0
     / \
   -3   9
   /   /
 -10  5
"""


# Definition for singly-linked list.
class ListNode(object):
   def __init__(self, x):
       self.val = x
       self.next = None

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        def getRoot(node):
            """
            :param node: ListNode
            :ret: TreeNode
            """
            if not node:
                return None

            head = node
            double_head = head.next.next if head and head.next else None
            prev = None

            while double_head:
                prev = head
                head = head.next
                double_head = double_head.next.next if double_head and \
                    double_head.next else None

            if prev:
                prev.next = None
            left = node if node != head else None
            right = head.next if head else None
            #  print("head: {}".format(head.val))
            #  print("left: {}".format(left.val if left else None))
            #  print("right: {}".format(right.val if right else None))
            #  print("\n\n")

            root = TreeNode(head.val)
            root.left = getRoot(left)
            root.right= getRoot(right)
            return root

        return getRoot(head)

    def rewrite(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        提中 recursive, 更快的方法為將 sigle linked list 轉為 array
        cache affinity, 快! 且為一個sorted array, 很快!
        """
        def start(node):
            if not node:
                return None
            # -10, -3
            onode = node

            fwdNode = node.next.next if node.next else None
            prev = None


            while fwdNode is not None and node is not None:
                fwdNode = fwdNode.next.next if fwdNode.next else None
                prev = node
                node = node.next

            if prev:
                prev.next = None

            root = TreeNode(node.val)

            root.left = start(onode if onode != node else None)
            root.right= start(node.next)

            return root

        return start(head)


def build():
    n1 = ListNode(-10)
    n2 = ListNode(-3)
    n3 = ListNode(0)
    n4 = ListNode(5)
    n5 = ListNode(9)
    n1.next = n2
    n2.next = n3
    n3.next = n4
    n4.next = n5
    return n1

def pl(node):
    result = []

    while node:
        result.append(node.val)
        node = node.next
    return result

def pt(node):
    result = []

    def dfs(node):
        if node:
            result.append(node.val)
            dfs(node.left)
            dfs(node.right)
    dfs(node)
    return result

if __name__ == "__main__":
    print("input: {}".format(pl(build())))
    print("---")

    s = Solution()
    print(pt(s.sortedListToBST(build())))

    print("---")

    s = Solution()
    print(pt(s.rewrite(build())))
