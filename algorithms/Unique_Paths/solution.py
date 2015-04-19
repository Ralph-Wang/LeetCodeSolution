class Solution:
    def math(self, m, n):
        all  = m + n - 2
        select = n if n < m else m
        result = 1
        for i in xrange(1, select):
            result = result * all / i
            all -= 1
        return result

    # @param m, an integer
    # @param n, an integer
    # @return an integer
    def uniquePaths(self, m, n):
        dp = [[1] * n for i in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if i == 0 and j == 0:
                    continue
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]



s = Solution()

print s.uniquePaths(2, 2)
