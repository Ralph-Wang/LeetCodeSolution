求小于 n 的数中, 素数的个数





# 埃拉托斯特尼筛法 (什么破名字)

1. 建立一个从 2 开始到 n-1 的 hashtable
2. 从 2 开始, 标记所有 i 的倍数为非素数, 如果 i 已经被标记过了, 跳过
3. 没被标记过的数就都是素数了

P.S. 因为可以确定, 遍历完 p x q < n, (p <= q), 就遍历完所有 n 可能的约数, 即退出循环条件为 i x i < n
