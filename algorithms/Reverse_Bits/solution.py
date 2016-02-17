#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        # res = 0
        # for dummy in xrange(32):
        #     res <<= 1
        #     res += n&1
        #     n >>= 1
        # return res

        # pure bit manipulation
        n = (n >> 1 & 0x55555555) + (n << 1 & 0xaaaaaaaa)
        n = (n >> 2 & 0x33333333) + (n << 2 & 0xcccccccc)
        n = (n >> 4 & 0x0f0f0f0f) + (n << 4 & 0xf0f0f0f0)
        n = (n >> 8 & 0x00ff00ff) + (n << 8 & 0xff00ff00)
        n = (n >> 16 & 0x0000ffff) + ( n << 16 & 0xffff0000)
        return n


s = Solution()

assert 964176192 == s.reverseBits(43261596)
assert 43261596 == s.reverseBits(964176192)
