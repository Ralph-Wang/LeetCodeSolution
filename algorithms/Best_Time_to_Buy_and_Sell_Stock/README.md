Say you have an array for which the ith element is the price of a given stock on
有一个数组, 其第 i 个元素表示股票在第 i 天的价格

* 最多进行一次买和卖, 当然也可以不进行交易
* 求最大收益


# 思路
## 动态规划
1. 小于 2 个元素, 不能完成完整交易, 收益为 0
2. f[i] 表示第 i 天可能的最大收益, min\_price 是之前出现的最低价格(即最可能的买入价)
    => f[i] = max(f[i-1], i - min\_price)
3. 求最大的 f[i] 即可
ps. 因为 f[i] 是随循环更新, 只用 max\_profit 记录当前最大的收益即可
