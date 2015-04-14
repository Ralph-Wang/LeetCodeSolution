class Solution:
    # @param s, a string
    # @return a boolean
    def isValid(self, s):
        p = { '(': ')', '[': ']', '{': '}' }
        stack = []
        for c in s:
            if c in p:
                stack.append(c)
            else:
                if stack == []:
                    return False
                left = stack.pop()
                if p[left] != c:
                    return False
        return stack == []


cases = [
        ('[]', True),
        ('[[]', False),
        ('[]()', True),
        ('[]]', False),
        ('{}[]()', True),
        ]

s = Solution()

for case, expect in cases:
    assert s.isValid(case) is expect, case
