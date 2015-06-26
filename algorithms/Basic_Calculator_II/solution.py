class Solution:
    # @param {string} s
    # @return {integer}
    def calculate(self, s):
        OP = {
                '+': lambda a, b: int(a) + int(b),
                '-': lambda a, b: int(a) - int(b),
                '*': lambda a, b: int(a) * int(b),
                '/': lambda a, b: int(a) / int(b),
                }
        q = []
        for i in list(filter(lambda c: c != ' ', list(s))):
            if i in '0123456789' and len(q) > 0 and q[-1][-1] in '0123456789':
                q[-1] += i
            else:
                q.append(i)
        q.reverse()
        queue = []
        while q:
            c = q.pop()
            if c in '*/':
                a = queue.pop()
                b = q.pop()
                c = OP[c](a, b)
            queue.append(c)
        queue.reverse()
        while queue:
            c = queue.pop()
            if str(c) in '+-':
                a = q.pop()
                b = queue.pop()
                c = OP[c](a, b)
            q.append(c)
        return int(q[0])





cases = [
        ("3+2*2" , 7),
        (" 3/2 " , 1),
        (" 3+5 / 2 " , 5),
        (" 42 " , 42),
        (" 1337 " , 1337),
        ]

sol = Solution()
for s, exp in cases:
    res = sol.calculate(s)
    assert res == exp, '%s=%s' % (s, res)
