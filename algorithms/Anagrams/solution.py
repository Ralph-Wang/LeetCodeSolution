#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    # @param {string[]} strs
    # @return {string[]}
    def anagrams(self, strs):
        hash = {}
        for s in strs:
            a = ''.join(sorted(s))
            if a in hash:
                hash[a].append(s)
            else:
                hash[a] = [s]

        ret = []
        [ret.extend(item) for item in hash.values() if len(item) > 1]
        return ret


cases = [
        (['ab', 'b', 'ba'], ['ab', 'ba']),
        ([''], []),
        (['', 'b'], []),
        ]

s = Solution()
for ss, e in cases:
    r = s.anagrams(ss)
    print r
