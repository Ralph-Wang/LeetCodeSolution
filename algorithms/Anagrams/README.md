## 题面
从数组中找出所有是同字异序词的字符串



## 思路
以排序后的字母为**键**, 以字符串列表为**值**做哈希表

## tips
```python
if a in hash:
    hash[a].append(s)
else:
    hash[a] = [s]
```

这里不要写成

```python
hash[a] = hash.get(a, []) + [s]
```

