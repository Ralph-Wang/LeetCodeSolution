#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def rangeBitwiseAnd(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m == n:
            return n
        diff = m ^ n
        for i in xrange(5):
            diff |= (diff >> (2^i))
        return m & ~diff
