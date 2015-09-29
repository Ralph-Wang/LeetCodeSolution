class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # # simple sum
        # return sum(xrange(len(nums)+1)) - sum(nums)

        # # bit manipulate
        # xor = 0
        # for idx, num in enumerate(nums):
        #     xor ^= idx ^ num
        # return xor ^ (idx + 1)

        # binary search
        sorted_nums = sorted(nums)
        left = 0
        right = len(sorted_nums)
        while left != right:
            middle = (left + right) / 2
            if middle == sorted_nums[middle]:
                left = middle + 1
            else:
                right = middle
        return left


s = Solution()
print s.missingNumber([0, 1, 3])
print s.missingNumber([0, 1, 3, 4])
print s.missingNumber([0])
