class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        min_price = prices[0]
        max_profit = 0
        for i in prices[1:]:
            max_profit = max(max_profit, i - min_price)
            min_price = min(min_price, i)
        return max_profit


cases =  [
        ([5, 2, 7], 5),
        ([1], 0),
        ([2, 1], 0),
]

s = Solution()
for c, e in cases:
 assert s.maxProfit(c) == e
