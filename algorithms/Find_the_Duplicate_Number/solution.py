class Solution(object):
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        min_val = 1
        max_val = len(nums)
        while min_val != max_val:
            middle = (min_val + max_val) / 2
            count = sum(x <= middle for x in nums)

            if middle < count:
                max_val = middle
            else:
                min_val = middle + 1
        return min_val
