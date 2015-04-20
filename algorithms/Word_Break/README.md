给定一个字符串, 和一个字典. 判断字符串是否可以被分割成字典中的单词

示例:
s = "leetcode",
dict = ["leet", "code"].

因为 "leetcode" 可以分割成 "leet code" 所以返回 True



# 思路

0..i 组成的字符串可以被分割的情况
* 0..i 自身在字典里
* 0 < k <= i. 0..k 可以分割, 且 k+1..i 在字典里

写成递推式:
f(i) = (s[:i+1] in dict) or any(dp[:k] and s[k+1:i+1] in dict)
