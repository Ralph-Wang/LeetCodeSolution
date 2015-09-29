# 题面
Given a linked list, return the node where the cycle begins. If there is no cycle, return null.

# 思路
### visited
1. 记录下所有访问的节点.
2. 出现二次访问时, 即为圈开始的节点.


### two pointer
1. 一快一慢两个指针, 向前移动
2. 快指针到达链表末, 即意味着没有圈
3. 快/慢相遇, 则有圈. 相遇点为 tail.
4. head -> ... -> ... -> tail 和 tail -> ...  -> ... tail, 是两条长度相同,
   且有相遇点的链表
    1. 此时, 将快指针放回起点.
    2. 快/慢同步调(一步)向前移, 相遇即为圈开始点
