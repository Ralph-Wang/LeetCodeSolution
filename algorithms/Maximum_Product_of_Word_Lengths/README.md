# 题面
一个字符串数组, 找出 length(word[i]) * length(word[j]) 的最大值,
其中这两个字符串要求不能有重复字符.
所有字符串都是小写字母


示例 1:
["abcw", "baz", "foo", "bar", "xtfn", "abcdef"]
返回 16
对应字符串: "abcw", "xtfn".

示例 2:
["a", "ab", "abc", "d", "cd", "bcd", "abcd"]
返回 4
对应字符串: "ab", "cd".

示例 3:
["a", "aa", "aaa", "aaaa"]
返回 0
没有满足需求的字符串



# 思路
1. 为所有小写字母建立 mask. a 对应 0x00000001, b 对应 0x00000002, c 对应 0x00000004 ...
2. 求所有字符串的 mask.
3. 建立 mask -> len 的映射
4. 组合所有 mask. 求满足条件(mask\_i & mask\_j ==0) 的长度积, 并找最大值
