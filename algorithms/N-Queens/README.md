在 n X n 的国际象棋棋盘上放上 n 个王后, 并且让它们不能互相攻击

输出所有方案



# 解决
基本设定: 因为不能攻击, 所以必然有 第 i 个王后放在第 i 行上

其它数学知识:
* 对角线数目 = 2 * n - 1
* 对象线索引 = y - x (加偏移量使其满足 [0:2n]), y + x

如果满足解 {
    填充结果集并返回
} 不满足解 {
    遍历所有列 {
        标记列, 标记左向对象线, 标记右向对象线
        递归下一行
        *回退* 结果集中最后一行, 取消对应标记
    }
}
