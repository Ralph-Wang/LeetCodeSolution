表达式解析

1. 运算符只包含加号(+), 减号(-), 乘号(\*) 和 除号(/)
2. 运算数只包含正整数


示例:
        "3+2*2" = 7
        " 3/2 " = 1
        " 3+5 / 2 " = 5
        " 42 " = 42
        " 1337 " = 1337


# 思路
1. 解析字符串, 使其变成数字和运算符的列表

2. 计算所有乘法和除法

3. 计算所有加法和减法