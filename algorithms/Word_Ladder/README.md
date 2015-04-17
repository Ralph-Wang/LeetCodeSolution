给一个起点单词/一个终点单词, 以及一个字典, 找到所有从起点变化到终点的最短路径:

* 一次只能变更一个字符
* 每一个中间单词必须在字典中

例子:
start = "hit"
end = "cog"
dict = ["hot","dot","dog","lot","log"]

最短路径是
[
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
]
