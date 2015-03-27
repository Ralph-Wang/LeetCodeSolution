class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        res = 0
        while n:
        #     res += n%2
        #     n //= 2
            res += n & 1
            n >>=1
        return res


s = Solution()
assert s.hammingWeight(0) == 0
assert s.hammingWeight(1) == 1
assert s.hammingWeight(2) == 1
assert s.hammingWeight(3) == 2
assert s.hammingWeight(4) == 1
assert s.hammingWeight(11) == 3
