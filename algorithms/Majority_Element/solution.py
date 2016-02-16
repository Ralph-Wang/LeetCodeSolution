class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        key = None
        count = 0
        for num in nums:
            if count == 0:
                count += 1
                key = num
            elif key == num:
                count += 1
            else:
                count -= 1
        return key
