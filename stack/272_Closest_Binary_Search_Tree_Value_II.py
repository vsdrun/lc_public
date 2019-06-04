#!/usr/bin/env python
# -*- coding: utf-8 -*-


"""
https://leetcode.com/problems/closest-binary-search-tree-value-ii/

Given a non-empty binary search tree and a target value,
find k values in the BST that are closest to the target.

Note:
Given target value is a floating point.
You may assume k is always valid, that is: k ≤ total nodes.
You are guaranteed to have only one unique set of k values in
the BST that are closest to the target.

Example:
Input: root = [4,2,5,1,3], target = 3.714286, and k = 2
    4
   / \
  2   5
 / \
1   3
Output: [4,3]

Think:
inorder:
1,2,3
reverse order:
5,4,3

Follow up:
Assume that the BST is balanced,
could you solve it in less than O(n) runtime (where n = total nodes)?
"""

# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
       self.val = x
       self.left = None
       self.right = None

class Solution(object):
    def closestKValues(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        思考:
        準備兩個stack, inorder, reverse order
        inorder: ... 到 <= target
        reverorder: ...到 > target
        類似兩個heap sorted stack 一個max heap, 一個min heap
        然後找k個值 closes to target.
        """
        if not root or k == 0:
            return []

        inStack = []
        revStack = []
        result = []

        def bfs(node, inorder):
            tmp = []

            while node:
                if inorder:
                    tmp.append(node)
                    node = node.left
                else:
                    tmp.append(node)
                    node = node.right

            while tmp:
                cn = tmp.pop()

                if inorder:
                    if cn.val <= target:
                        inStack.append(cn)
                    else:
                        break
                    if cn.right:
                        cr = cn.right
                        while cr:
                            tmp.append(cr)
                            cr = cr.left

                else:
                    if cn.val > target:
                        revStack.append(cn)
                    else:
                        break
                    if cn.left:
                        cl = cn.left
                        while cl:
                            tmp.append(cl)
                            cl = cl.right




        bfs(root, True)
        bfs(root, False)

        while k > 0:
            k -= 1

            if not inStack:
                result.append(revStack.pop().val)
            elif not revStack:
                result.append(inStack.pop().val)
            else:
                if abs(inStack[-1].val - target) > abs(revStack[-1].val -
                        target):
                    result.append(revStack.pop().val)
                else:
                    result.append(inStack.pop().val)

        return result

    def rewrite(self, root, target, k):
        """
        :type root: TreeNode
        :type target: float
        :type k: int
        :rtype: List[int]
        思考:
        只有一個stack
        traverse tree in inorder
        放入result
        如果current node val - target < result[0], result.popleft

        moving window概念
        """
        import collections

        res = collections.deque([])
        stack = []

        while root:
            stack.append(root)
            root = root.left

        while stack:
            node = stack.pop()
            # 先填滿在說~~~
            if len(res) < k:
                res.append(node.val)
            elif abs(res[0] - target) > abs(node.val - target):
                res.popleft()
                res.append(node.val)
            else:
                return list(res)

            if node.right:
                temp = node.right
                while temp:
                    stack.append(temp)
                    temp = temp.left

        return list(res)

def build():
    """
    4
   / \
  2   5
 / \
1   3
    """

    _4 = TreeNode(4)
    _2 = TreeNode(2)
    _5 = TreeNode(5)
    _1 = TreeNode(1)
    _3 = TreeNode(3)

    _4.left = _2
    _4.right = _5
    _2.left = _1
    _2.right = _3

    return _4, 3.14, 2


if __name__ == "__main__":
    s = Solution()
    print(s.closestKValues(*build()))
