class Solution:
    # @param {string} s
    # @param {string} t
    # @return {boolean}
    def isIsomorphic(self, s, t):
        table = {}
        for i, j in zip(s, t):
            if i in table:
                if j != table[i]:
                    return False
            else:
                if j in table.values():
                    return False
                else:
                    table[i] = j
        return True




s = Solution()

cases = [
        (('egg', 'add'), True),
        (('foo', 'bar'), False),
        (('paper', 'title'), True),
        ]


for data, expect in cases:
    assert s.isIsomorphic(*data) == expect, data
