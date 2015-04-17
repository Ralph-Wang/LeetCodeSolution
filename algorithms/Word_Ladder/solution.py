#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    # @param start, a string
    # @param end, a string
    # @param dict, a set of string
    # @return a list of lists of string
    def findLadders(self, start, end, dict):
        dict.add(end)
        level = {start}
        path = {}
        while level and end not in path:
            next_level = {}
            for word in level:
                for c in 'abcdefghijklmnopqrstuvwxyz':
                    for i in xrange(len(word)):
                        w = word[:i] + c + word[i+1:]
                        if w not in path and w in dict:
                            if w in next_level:
                                next_level[w].add(word)
                            else:
                                next_level[w] = {word}
            level = next_level
            path.update(next_level)

        result = [[end]]
        while result and result[0][0] != start:
            result = [[p] + r for r in result for p in path.get(r[0], [])]
        return len(result[0]) if len(result) > 0 else 0




s = Solution()

cases = [('hit', 'cog', {'hot', 'dot', 'dog', 'lot', 'log'}),
("red", "tax", {"ted","tex","red","tax","tad","den","rex","pee"}),
("hot", "dog", {"hot", "dog"})
]

for start, end, dictionary in cases:
    print s.findLadders(start, end, dictionary)

# [['hit', 'hot', 'lot', 'log', 'cog'], ['hit', 'hot', 'dot', 'dog', 'cog']]
# [['red', 'rex', 'tex', 'tax'], ['red', 'ted', 'tex', 'tax'], ['red', 'ted', 'tad', 'tax']]
# []
