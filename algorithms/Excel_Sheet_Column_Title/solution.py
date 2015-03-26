#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @return a string
    def convertToTitle(self, num):
        ret = ''
        while num > 0:
            num -= 1 # 把 A-Z 对应到 0-25, 而不是原本的 1-26
            ret = chr(num%26 + 65) + ret
            num //= 26
        return ret



s = Solution()
assert s.convertToTitle(1) == 'A'
assert s.convertToTitle(2) == 'B'
assert s.convertToTitle(3) == 'C'
assert s.convertToTitle(26) == 'Z'
assert s.convertToTitle(27) == 'AA'
assert s.convertToTitle(28) == 'AB'
assert s.convertToTitle(52) == 'AZ'
assert s.convertToTitle(53) == 'BA'
