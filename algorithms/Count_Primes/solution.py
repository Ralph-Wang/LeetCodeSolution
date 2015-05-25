#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution(object):
    def countPrimes(self, n):
        t = [True] * n
        t[0:2] = [False] * 2
        for i in xrange(2, int(n ** 0.5) + 1):
            if not t[i]:
                continue
            # 因为 2 ~ (i-1) 已经在前面的循环中标记过了
            # 所以从 i * i 开始循环
            # i * i, i * (i + 1), i * (i + 2) ~~~~
            # for j in xrange(i * i, n, i):
            #     t[j] = False
            # 用切片赋值更 Pythonic, 也更快
            t[i*i:n:i] = [False] * len(t[i*i:n:i])
        return t.count(True)



s = Solution()
for i in xrange(100):
    print s.countPrimes(i)
