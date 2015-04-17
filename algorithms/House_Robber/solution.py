class Solution:
    # @param num, a list of integer
    # @return an integer
    def rob(self, num):
        if len(num) == 0:
            return 0
        not_rob = 0
        rob = 0
        for i in num:
            cur_rob = not_rob + i
            not_rob = max(rob, not_rob)
            rob = cur_rob
        return max(cur_rob, not_rob)



cases = [
        ([], 0),
        ([1], 1),
        ([2, 1], 2),
        ([2, 1, 3], 5),
        ([1, 4, 2], 4),
        ]

s = Solution()
for num, expect in cases:
    assert s.rob(num) == expect
