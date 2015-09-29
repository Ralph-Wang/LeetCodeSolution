# 题面
判断数组 `nums` 是否满足以下条件:
存在不同的索引量 i, j. 使得 nums[i] 和 nums[j] 之差不大于 t, 且 i 和 j
之差不大于 k

# 思路
### buckets sort
1. 将元素按 t 差值分到`桶`里
2. 只有相邻/相同桶里的元素才满足, abs(nums[i] - nums[j]) <= t
3. 排除那些 i - j > k 的元素


### binary search tree
1. 将元素插入查找树
2. 插入过程中每访问一个点, 比较一次是否满足 abs(nums[i] - nums[j]) <= t
3. 通过控制树的大小来满足 i - j <= k
