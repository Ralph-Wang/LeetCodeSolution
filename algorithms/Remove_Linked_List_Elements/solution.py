#!/usr/bin/env python
# -*- coding: utf-8 -*-


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    # @param {ListNode} head
    # @param {integer} val
    # @return {ListNode}
    def removeElements(self, head, val):
        # # O(n)
        # dummy = pre = ListNode(0)
        # while head:
        #     if head.val != val:
        #         pre.next = ListNode(head.val)
        #         pre = pre.next
        #     head = head.next
        # return dummy.next

        # in-place
        dummy = pre = ListNode(0)
        dummy.next = head
        while head:
            if head.val == val:
                pre.next = head.next
            else:
                pre = pre.next
            head = head.next
        return dummy.next



head = ListNode(1)
h = head
for i in [2,2,1]:
    h.next = ListNode(i)
    h = h.next

h = head

while h is not None:
    print h.val
    h = h.next

print '-' * 20

s = Solution()
h = s.removeElements(head, 2)

print '-' * 20

while h is not None:
    print h.val
    h = h.next
