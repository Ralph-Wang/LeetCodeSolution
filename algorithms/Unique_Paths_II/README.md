从矩阵左上角走到右下角路径的数量

矩阵中有障碍物, 值为 1. 障碍物使得点不可到达/通过

# 思路
## 动态规划

1. dp[i][j] = dp[i-1][j] + dp[i][j-1]
2. base: dp[0][0] = 1, dp[0][j] = dp[0][j-1], dp[i][0] = dp[i-1][0]
3. dp[m-1][n-1] 即为解
ps. 处理障碍物, if grid[i][j] == 1: dp[i][j] == 0
