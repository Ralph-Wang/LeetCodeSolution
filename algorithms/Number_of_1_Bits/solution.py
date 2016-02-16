class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        # res = 0
        # while n:
        #     res += n & 1
        #     n >>=1

        # pure bit manipulation
        n = (n & 0x55555555) + (n>>1 & 0x55555555)
        n = (n & 0x33333333) + (n>>2 & 0x33333333)
        n = (n & 0x0f0f0f0f) + (n>>4 & 0x0f0f0f0f)
        n = (n & 0x00ff00ff) + (n>>8 & 0x00ff00ff)
        n = (n & 0x0000ffff) + (n>>16 & 0x0000ffff)
        return n


s = Solution()
assert s.hammingWeight(0) == 0
assert s.hammingWeight(1) == 1
assert s.hammingWeight(2) == 1
assert s.hammingWeight(3) == 2
assert s.hammingWeight(4) == 1
assert s.hammingWeight(11) == 3

print bin(s.hammingWeight(1314520))
