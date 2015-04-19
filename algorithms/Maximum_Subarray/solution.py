#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    def normal_dp(self, nums):
        dp = 0
        a = float('-inf')
        for i in nums:
            dp = max(dp + i, i)
            a = max(a, dp)
        return a

    def divide_conquer(self, nums):
        n = len(nums)
        if n == 1:
            return nums[0]

        mid = n >> 1
        # divice 0..mid-1 mid..n
        a = max(self.divide_conquer(nums[:mid]), self.divide_conquer(nums[mid:]))

        # conque
        may = nums[mid-1]
        now = may
        for i in xrange(mid-2, -1, -1):
            now += nums[i]
            may = max(may, now)
        now = may
        for i in xrange(mid, n):
            now += nums[i]
            may = max(may, now)

        return max(may, a)

    def min_sum_dp(self, nums):
        all_sum = 0
        min_sum = 0
        a = float('-inf')
        for i in nums:
            all_sum += i
            a = max(a, all_sum - min_sum)
            min_sum = min(all_sum, min_sum)
        return a

    # @param {integer[]} nums
    # @return {integer}
    def maxSubArray(self, nums):
        return self.divide_conquer(nums)


case = [1, 2]

s = Solution()
print s.maxSubArray(case)
