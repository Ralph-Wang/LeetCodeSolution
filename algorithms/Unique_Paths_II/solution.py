class Solution:
    # @param obstacleGrid, a list of lists of integers
    # @return an integer
    def uniquePathsWithObstacles(self, obstacleGrid):
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        dp = [[0] * n for dummy in xrange(m)]
        for i in xrange(m):
            for j in xrange(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] == 0
                elif i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1]
                elif j == 0:
                    dp[i][j] = dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]

s = Solution()

cases = [
        [
            [0,0,0],
            [0,1,0],
            [0,0,0]
            ],
        [[1]],
        ]

for case in cases:
    print s.uniquePathsWithObstacles(case)
