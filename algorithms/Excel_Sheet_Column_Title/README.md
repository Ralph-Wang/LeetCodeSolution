# 原题

给一个号, 把它转换成 excel 表格中的列标题

比如:

    1 -> A
    2 -> B
    3 -> C
    ...
    26 -> Z
    27 -> AA
    28 -> AB

# 思路:

直接看成单纯的进制转化问题可解.
excel 标题就是二十六进制数, 列号就是一般的十进制数
但需求里面, 对应关系是 1-26 对应 A-Z
所以在变更进制前, 把原数据从 1-26 变更成 0-25, 即: `num -=1` 操作的意义
