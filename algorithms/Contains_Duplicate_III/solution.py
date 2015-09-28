#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution(object):
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        # bucket sort
        buckets = {}

        for i, n in enumerate(nums):
            bucket_idx, offset = (n/t, 1) if t else (n, 0)

            # possible candinate should in neighbor or self bucket
            for idx in xrange(bucket_idx - offset, bucket_idx+offset+1):
                if idx in buckets and abs(buckets[idx] - n) <= t:
                    return True

            buckets[bucket_idx] = n

            if len(buckets) > k: # remove item too far away
                del buckets[nums[i-k]/t if t else nums[i-k]]

        return False
