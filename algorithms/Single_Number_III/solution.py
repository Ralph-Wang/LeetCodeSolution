#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # get a ^ b
        m = 0
        for i in nums:
            m ^= i

        # pick one of diff in a ^ b
        differ = m & -m

        # xor all numbers in nums if it have 1 in differ position
        n = 0
        for i in nums:
            if i & differ:
                n ^= i
        return [n, m ^ n]




s = Solution()
print s.singleNumber([1, 2, 1, 3, 2, 5])
