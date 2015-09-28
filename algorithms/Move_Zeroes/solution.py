class Solution(object):

    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        # # pythonic # 180ms
        # c = 0
        # while 0 in nums:
        #     nums.remove(0)
        #     c += 1
        # for _ in xrange(c):
        #     nums.append(0)

        # two pointer # 68ms
        n = len(nums)
        first_zero = 0
        first_non_zero = 0
        while first_non_zero < n:
            if nums[first_non_zero] == 0 or first_non_zero < first_zero:
                first_non_zero += 1
            elif nums[first_zero] != 0:
                first_zero += 1
            else:
                nums[first_non_zero], nums[first_zero] = nums[first_zero], nums[first_non_zero]
                first_zero += 1
                first_non_zero += 1

        # # bubble # time limit exceeded
        # n = len(nums)
        # for i in xrange(n):
        #     for j in xrange(i, n-1):
        #         if nums[j] == 0 and nums[j+1] != 0:
        #             nums[j], nums[j+1] = nums[j+1], nums[j]


cases = [
    ([0, 1, 0, 3, 12], [1, 3, 12, 0, 0])
]

s = Solution()

for data, expect in cases:
    s.moveZeroes(data)
    assert data == expect, data
