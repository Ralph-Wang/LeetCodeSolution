#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Queue(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self._items = []


    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        temp = []
        while self._items:
            temp.append(self._items.pop())
        self._items.append(x)

        while temp:
            self._items.append(temp.pop())


    def pop(self):
        """
        :rtype: nothing
        """
        self._items.pop()


    def peek(self):
        """
        :rtype: int
        """
        return self._items[-1]


    def empty(self):
        """
        :rtype: bool
        """
        return self._items == []

