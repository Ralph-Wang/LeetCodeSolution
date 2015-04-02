# 题
删除重复的 Email, 保留最小的那个 Id

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
| 3  | john@example.com |
+----+------------------+

        |
        v

+----+------------------+
| Id | Email            |
+----+------------------+
| 1  | john@example.com |
| 2  | bob@example.com  |
+----+------------------+

# 思路
~查出需要删除的 Id, 再删除~ 
MySQL 不能在 Update/Delete 中先查询再更新/删除

===
MySQL 原来可以联表删除, 而且还是自联表
