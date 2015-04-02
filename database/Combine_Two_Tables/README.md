# 题
表: Person; PersonId 主键.
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| PersonId    | int     |
| FirstName   | varchar |
| LastName    | varchar |
+-------------+---------+

表: Address AddressId 主键.
+-------------+---------+
| Column Name | Type    |
+-------------+---------+
| AddressId   | int     |
| PersonId    | int     |
| City        | varchar |
| State       | varchar |
+-------------+---------+

查询出以下信息, 如果没有地址的人员 City, State 留空
FirstName, LastName, City, State

# 思路
最简单的左联表查询
