#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        for dummy in xrange(32):
            res <<= 1
            res += n&1
            n >>= 1
        return res


s = Solution()

assert 964176192 == s.reverseBits(43261596)
assert 43261596 == s.reverseBits(964176192)
