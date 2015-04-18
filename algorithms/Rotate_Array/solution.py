class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)

        # nums[:] = [nums[(i-k)%n] for i in xrange(n)]
        # or
        k %= n
        for i in xrange(k):
            nums.insert(0, nums.pop())


case = ([1,2,3,4,5,6,7], 3, [5, 6, 7, 1, 2, 3, 4])

s = Solution()
s.rotate(case[0], case[1])
print case[0]
