class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hash = {}
        for idx, num in enumerate(nums):
            if num not in hash:
                hash[num] = idx
            elif idx - hash[num] <= k:
                return True
            else:
                hash[num] = idx
            idx += 1
        else:
            return False
