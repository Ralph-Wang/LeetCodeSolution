#!/usr/bin/env python
# -*- coding: utf-8 -*-

from collections import deque

class Stack:
    # initialize your data structure here.
    def __init__(self):
        self._q = deque()
        self._top = None


    # @param x, an integer
    # @return nothing
    def push(self, x):
        self._q.append(x)


    # @return nothing
    def pop(self):
        temp = deque()
        while self._q:
            temp.append(self._q.popleft())

        while len(temp) > 1:
            self._q.append(temp.popleft())

    # @return an integer
    def top(self):
        return self._q[-1]


    # @return an boolean
    def empty(self):
        return self._q == deque()


s = Stack()

for i in xrange(10):
    s.push(i)

while not s.empty():
    print s.top()
    s.pop()
