# 题
找出所有比前一天温度高的记录id
表: Weather
+---------+------------+------------------+
| Id(INT) | Date(DATE) | Temperature(INT) |
+---------+------------+------------------+
|       1 | 2015-01-01 |               10 |
|       2 | 2015-01-02 |               25 |
|       3 | 2015-01-03 |               20 |
|       4 | 2015-01-04 |               30 |
+---------+------------+------------------+
  |
  v
+----+
| Id |
+----+
|  2 |
|  4 |
+----+


# 注意
要用 `TO_DAYS` 将时间转化成天...
