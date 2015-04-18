class Solution:
    # @return an integer
    def trailingZeroes(self, n):
        res = 0
        while n:
            res += n / 5
            n /= 5
        return res



cases = [25, 200]
s = Solution()

for case in cases:
    print s.trailingZeroes(case)
