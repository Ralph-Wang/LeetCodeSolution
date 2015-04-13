#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a list of lists of string
    def solveNQueens(self, n):
        result = []                      #  结果集
        a = []                           #  当前结果, 索引对应行, 值对应列
        column = [False] * n             #  列占用标记
        diagnol1 = [False] * (2 * n - 1) #  对角线1标记
        diagnol2 = [False] * (2 * n - 1) #  对角线2标记
        self.solve(a, n, column, diagnol1, diagnol2, result)
        return result

    def solve(self, a, n, column, diagnol1, diagnol2, result):
        if len(a) >= n: # 有结果了
            v = []
            for i in xrange(n):
                s = ['.'] * n
                s[a[i]] = 'Q'
                v.append(''.join(s))
            result.append(v)
            return

        for i in xrange(n):
            x = len(a)
            d1 = i + x
            d2 = i - x + n - 1
            if not column[i] and not diagnol1[d1] and not diagnol2[d2]:
                # 当前位置合法
                column[i] = diagnol1[d1] = diagnol2[d2] = True
                a.append(i)
                self.solve(a, n, column, diagnol1, diagnol2, result) # 处理下一行
                a.pop()
                column[i] = diagnol1[d1] = diagnol2[d2] = False

s = Solution()
print s.solveNQueens(1)
