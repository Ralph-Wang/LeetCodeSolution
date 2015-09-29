#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque

class Node(object):

    """ Binary Search Tree Node"""

    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def __str__(self):
        return "Node({0})".format(self.val)


class BST(object):

    """ Binary Search Tree"""

    def __init__(self, t=0):
        self.t = t
        self.root = None
        self.size = 0

    def insert(self, val):
        """ insert value to this tree

        Args:
            val (int): the value to insert

        Returns: True if val - node.val < t

        """
        node = Node(val)
        self.size += 1
        if self.root is None:
            self.root = node
            return False
        parent = None
        left_leaf = None
        cur = self.root
        while cur is not None:
            if abs(cur.val - node.val) <= self.t:
                return True
            parent = cur
            if node.val < cur.val:
                cur = cur.left
                left_leaf = True
            else:
                cur = cur.right
                left_leaf = False
        if left_leaf:
            parent.left = node
        else:
            parent.right = node
        return False

    def search(self, val):
        cur = self.root
        parent = None
        left_leaf = None
        while cur is not None and val != cur.val:
            parent = cur
            if val < cur.val:
                left_leaf = True
                cur = cur.left
            else:
                left_leaf = False
                cur = cur.right
        return cur, parent, left_leaf

    @staticmethod
    def min_val(node):
        """ search min val from node subtree """
        cur = node
        while cur.left is not None:
            cur = cur.left
        return cur

    def remove(self, val):
        self.size -= 1
        self.root = self._remove_helper(self.root, val)

    def _remove_helper(self, node, val):
        if node is None:
            return None
        if val < node.val:
            node.left = self._remove_helper(node.left, val)
            return node
        elif val > node.val:
            node.right = self._remove_helper(node.right, val)
            return node
        else:
            if node.left is None and node.right is None:
                return None

            if node.left is None:
                return node.right
            if node.right is None:
                return node.left

            tmpNode = self.min_val(node.right)
            node.val = tmpNode.val
            node.right = self._remove_helper(node.right, tmpNode.val)
            return node


    def dump(self):
        queue = deque()
        queue.append(self.root)
        while queue:
            root = queue.popleft()
            print root,
            if root is not None:
                queue.append(root.left)
                queue.append(root.right)
        print
        print self.size
        print "*" * 80



class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        tree = BST(t)
        for i, num in enumerate(nums):
            if tree.insert(num):
                return True

            if tree.size > k:
                tree.remove(nums[i-k])
        return False


cases = [
        ([-1, -1], 1, -1, False),
        ([1, 4, 2], 1, 1, False),
        ]

s = Solution()
for nums, k, t, expect in cases:
    assert s.containsNearbyAlmostDuplicate(nums, k, t) == expect, "{0} {1} {2}".format(nums, k, t)
