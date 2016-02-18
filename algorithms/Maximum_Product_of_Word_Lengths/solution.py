#!/usr/bin/env python
# -*- coding: utf-8 -*-

import itertools

class Solution(object):
    def ctob(self, c):
        return 1 << (ord(c)- 97)
    def stob(self, s):
        res = 0
        for c in s:
            res |= self.ctob(c)
        return res

    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        max_length_words = {self.stob(s): len(s) for s in sorted(words, key=len)}
        result = 0
        for (keyi, leni), (keyj, lenj) in itertools.combinations(max_length_words.items(),2):
            if not keyi & keyj:
                result = result if leni * lenj < result else leni * lenj
        return result
