# DATE_ADD

## 基本用法

```sql
DATE_ADD(date, INTERVAL value addunit)
```

作用：

增减日期。

---

## 示例

```sql
SELECT DATE_ADD('2025-01-01', INTERVAL 1 DAY)
```

结果：

```text
2025-01-02
```

---

<br>

# DATE_FORMAT

## 基本用法

```sql
DATE_FORMAT(date, format)
```

作用：

更改日期格式。

---

## 示例

```sql
SELECT DATE_FORMAT('2017-06-15', '%Y-%m-%d')
```

结果：

```text
2017-06-15
```

---

<br>

# 交叉链接
```sql
select * from Students cross join Subjects
```

---

<br>

# 其他
```sql
NULL 安全相等运算符 <=>
取余数 %
length
ROUND(avg(),3)
IFNULL(grouped.attended_exams, 0)
sum(if(order_date = min_date, 1, 0)) --非常耗时
LEFT JOIN 如果右表没有匹配的行，则右表字段会返回 NULL,所以可以换inner join
保留关键字使用反引号转义，eg.`rank`
枚举类型的排序按题目的自定义来
```

