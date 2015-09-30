#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :returns: bool
        """
        return self.helper(root, (-sys.maxint-1, sys.maxint))

    def helper(self, root, limit):
        if root is None:
            return True
        left_valid = root.val > limit[0] and self.helper(root.left, (limit[0], root.val))
        right_valid = root.val < limit[1] and self.helper(root.right, (root.val, limit[1]))
        return left_valid and right_valid
        # if root is None:
        #     return True
        # if root.left is not None:
        #     left_valid = self.find_max(root.left).val < root.val and self.isValidBST(root.left)
        # else:
        #     left_valid = True
        # if root.right is not None:
        #     right_valid = self.find_min(root.right).val > root.val and self.isValidBST(root.right)
        # else:
        #     right_valid = True
        # return left_valid and right_valid

    # def find_min(self, root):
        # """ find min val from root

        # :type root: TreeNode
        # :returns: TreeNode or None

        # """
        # if root is None:
        #     return None
        # while root.left is not None:
        #     root = root.left
        # return root

    # def find_max(self, root):
        # """ find max val from root
        # :type root: TreeNode
        # :returns: TreeNode or None
        # """
        # if root is None:
        #     return None
        # while root.right is not None:
        #     root = root.right
        # return root



# root = TreeNode(1)
# root.right = TreeNode(1)

root = TreeNode(10)
root.left = TreeNode(5)
root.right = TreeNode(15)
root.right.left = TreeNode(6)
root.right.right = TreeNode(20)

s = Solution()
print s.isValidBST(root)
