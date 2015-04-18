#!/usr/bin/env python
# -*- coding: utf-8 -*-

# Definition for a  binary tree node
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    # @param root, a tree node
    # @return a boolean
    def isBalanced(self, root):
        return self.help(root)[1]

    def help(self, root):
        if root is None:
            return 0, True
        lh, lb = self.help(root.left)
        if not lb:
            return 0, lb
        rh, rb = self.help(root.right)
        if not rb:
            return 0, rb
        return max(rh, lh) + 1, lb and rb and abs(rh - lh) < 2


root = TreeNode(1)
root.right = TreeNode(3)
root.right.left = TreeNode(2)
# root.left.left = TreeNode(3)
# root.right.right = TreeNode(3)
# root.left.left.left = TreeNode(4)
# root.right.right.right = TreeNode(4)

s = Solution()
print s.isBalanced(root)
