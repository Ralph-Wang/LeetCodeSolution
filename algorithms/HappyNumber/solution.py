class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        if n == 1:
            return True
        table = set([n])
        cur = n
        while True:
            s = 0
            while cur != 0:
                s += (cur % 10) ** 2
                cur /= 10
            if s in table:
                return False
            if s == 1:
                return True
            table.add(s)
            cur = s



n = 1

s = Solution()

print s.isHappy(n)
