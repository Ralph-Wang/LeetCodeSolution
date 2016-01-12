#!/usr/bin/env python
# -*- coding: utf-8 -*-

class _dlnode(object):

    """ node of a doubly linked list. """

    def __init__(self):
        self.empty = True

        self.key = None
        self.value = None

        self.prev = None
        self.next = None


class LRUCache(object):

    def __init__(self, capacity):
        """
        :type capacity: int
        """
        self.table = {}


        self.capacity = capacity

        # a circular doubly linked list.
        self.head = _dlnode()
        self.head.prev = self.head
        self.head.next = self.head

        for _ in xrange(self.capacity-1):
            node = _dlnode()
            node.next = self.head
            node.prev = self.head.prev
            node.next.prev = node
            node.prev.next = node

    @property
    def used(self):
        return len(self.table)

    def mtf(self, node):
        """ move the node directly precedes head.

        :type node: _dlnode

        """
        node.prev.next = node.next
        node.next.prev = node.prev

        node.prev = self.head.prev
        # in case of node is self.head. we need to refind the real next node
        node.next = self.head.prev.next

        node.next.prev = node
        node.prev.next = node


    def get(self, key):
        """
        :rtype: int
        """
        node = self.table.get(key, None)
        if node is None:
            return -1

        # update order
        self.mtf(node)
        self.head = node
        return node.value


    def set(self, key, value):
        """
        :type key: int
        :type value: int
        :rtype: nothing
        """
        if key in self.table: # update value
            node = self.table[key]
            node.value = value

            # update order
            self.mtf(node)
            self.head = node
        else:
            tail = self.head.prev

            if not tail.empty:
                self.table.pop(tail.key)
            tail.key = key
            tail.value = value
            tail.empty = False
            self.table[key] = tail
            self.head = tail

    def dli(self):
        """ visit all nodes """
        node = self.head
        for _ in xrange(self.capacity):
            yield node
            node = node.next



lru = LRUCache(10)


lru.set(7,28)
lru.set(7,1)
lru.set(8,15)
print lru.get(6)
lru.set(10,27)
lru.set(8,10)
print lru.get(8)
lru.set(6,29)
lru.set(1,9)
print lru.get(6)
lru.set(10,7)
print lru.get(1)
print lru.get(2)
print lru.get(13)
lru.set(8,30)
lru.set(1,5)
print lru.get(1)
lru.set(13,2)
print lru.get(12)

