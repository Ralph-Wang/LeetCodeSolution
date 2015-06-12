#!/usr/bin/env python
# -*- coding: utf-8 -*-


class Solution:
    # @param {string} s
    # @return {integer}
    def calc(self, sub):
        OP = {
                '+': lambda a, b: int(a) + int(b),
                '-': lambda a, b: int(a) - int(b),
                }
        q = []
        for i in sub:
            if i == '-' and q and q[-1] == '-':
                q[-1] = '+'
            elif i == '-' and q and q[-1] == '+':
                q[-1] = '-'
            elif i.isdigit() and q and q[-1].isdigit():
                q[-1] += i
            else:
                q.append(i)
        while len(q) > 2:
            a, o, b = q[:3]
            q[:3] = [OP[o](a, b)]
        if len(q) == 2:
            q[0] = q[0] + q[1]
        return str(q[0])

    def calculate(self, s):
        # 直接解
        s = '(%s)' %s
        stack = []
        for i in s:
            if i == ' ':
                continue
            if i == ')':
                sub = ''
                while stack[-1] != '(':
                    sub = stack.pop() + sub
                stack.pop()
                result = self.calc(sub)
                stack.append(result)
            else:
                stack.append(i)
        return int(stack[0])


        ## reduction 把减法也当加法处理
        # 添加正号的哨兵
        # s = '+(+' + s + ')'
        # stack = [] # 栈里面存的全是数字和括号
        # for i in s:
        #     if i == ')':
        #         total = 0
        #         while stack[-1] != '(':
        #             total += int(stack.pop())
        #         stack.pop()
        #         sign = 1 if stack.pop() == '+' else -1
        #         stack.append(sign * total)
        #     # 把所有运算看成是加法, 问题就变成了负数的处理而已
        #     elif i.isdigit() and stack[-1][-1] in '+-0123456789':
        #         stack[-1] += i
        #     elif i != ' ':
        #         stack.append(i)
        # return stack[0]




cases = [
        ("1 + 1" , 2),
        (" 2-1 + 2 " , 3),
        ("(1+(4+5+2)-3)+(6+8)" , 23),
        ("2-(5-6)" , 3),
        ("(5-(1+(5)))" , -1),
        ("1-(2+3-(4+(5-(1-(2+4-(5+6))))))" , -1),
        ]

s = Solution()
for string, e in cases:
    a = s.calculate(string)
    assert a == e, '%s = %s !'%( string, a)
