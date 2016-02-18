#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # res = [[]]
        # for i in sorted(nums):
        #     res += [item + [i] for item in res]
        # return res
        res = []
        nums.sort()
        for i in xrange(len(nums) + 1):
            res.extend(list(itertools.combinations(nums,i)))
        return res
