class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        # # pythonic # 116ms
        # while val in nums:
        #     nums.remove(val)
        # return len(nums)

        # use origin array as result # 46ms
        idx = 0
        for item in nums:
            if item != val:
                nums[idx] = item
                idx += 1
        return idx
