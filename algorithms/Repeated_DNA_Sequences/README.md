# 题面
DNA 都是由 A/C/G/T 四种脱氧核糖核酸组成的. 比如: "ACGAATTCCG".
研究 DNA 中, 找出重复段的 DNA 有时非常有用

写一个方法, 找出所有重复出现的长度为10的 DNA 片段

示例,

s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT",

得到:
["AAAAACCCCC", "CCCCCAAAAA"].


# 思路
1. 因为定长, 从头遍历整个串就可以了
2. 用 hash (set) 记录出现过的和重复的即可
