#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Stack:
    # initialize your data structure here.
    def __init__(self):
        self._q = []


    # @param x, an integer
    # @return nothing
    def push(self, x):
        self._q.append(x)


    # @return nothing
    def pop(self):
        return self._q.pop()


    # @return an integer
    def top(self):
        return self._q[-1]


    # @return an boolean
    def empty(self):
        return len(self._q) == 0

