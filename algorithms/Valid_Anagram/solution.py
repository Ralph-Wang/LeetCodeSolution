#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isAnagram(self, s, t):
        # cheat
        # return sorted(s) == sorted(t)

        # hashtable
        ss = {}
        tt = {}
        for i in s:
            ss[i] = ss.get(i, 0) + 1

        for i in t:
            tt[i] = tt.get(i, 0) + 1
        return ss == tt





cases = [
        ('abc', 'cab', True),
        ('aaa', 'aaa', True),
        ('aegf', 'acbg', False),
        ('a', 'ab', False),
        ('acc', 'aac', False),
        ]

so = Solution()
for s, t, e in cases:
    r = so.isAnagram(s, t)
    assert r == e, '%s %s %s %s' % (s, t, e, r)
