# 题面
删除一个数组中的特定值, 并返回新长度
Given an array and a value, remove all instances of that value in place and
return the new length.

元素顺序可以改变, 在新长度后面的元素会被无视


# 思路

### pythonic
1. remove until `not in`

### use origin as result
1. 遍历数组, 将所有不需要删除的数移到数组前面
