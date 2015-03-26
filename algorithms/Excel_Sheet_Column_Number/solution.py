#!/usr/bin/env python
# -*- coding: utf-8 -*-

class Solution:
    # @param s, a string
    # @return an integer
    def titleToNumber(self, s):
        ret = 0
        for char in s:
            ret = 26 * ret + ord(char) - 64
        return ret


s = Solution()

assert s.titleToNumber('A') == 1
assert s.titleToNumber('B') == 2
assert s.titleToNumber('C') == 3
assert s.titleToNumber('Z') == 26
assert s.titleToNumber('AA') == 27
assert s.titleToNumber('AB') == 28
assert s.titleToNumber('BA') == 53
