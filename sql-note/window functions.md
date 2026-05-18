```text
row_number()——强制唯一，即123，RANK()——113，DENSE_RANK()——112
```

# dense_rank

```sql
# 185
with ranked as (
    select dense_rank() over (
        partition by departmentId order by salary desc) rs,
        name,salary,departmentId from Employee)
select d1.name Department,r1.name Employee,r1.Salary from (
    select * from ranked
    where rs<=3) r1
left join (select * from Department) d1
on d1.id=r1.departmentId 
```

---

<br>

# case when
```sql
# 1179
# 当多行数据满足一个条件时，case when只会提取第一个数据。
SELECT id, 
SUM(CASE WHEN month='Jan' THEN revenue END) AS Jan_Revenue,
SUM(CASE WHEN month='Feb' THEN revenue END) AS Feb_Revenue,
SUM(CASE WHEN month='Mar' THEN revenue END) AS Mar_Revenue,
SUM(CASE WHEN month='Apr' THEN revenue END) AS Apr_Revenue,
SUM(CASE WHEN month='May' THEN revenue END) AS May_Revenue,
SUM(CASE WHEN month='Jun' THEN revenue END) AS Jun_Revenue,
SUM(CASE WHEN month='Jul' THEN revenue END) AS Jul_Revenue,
SUM(CASE WHEN month='Aug' THEN revenue END) AS Aug_Revenue,
SUM(CASE WHEN month='Sep' THEN revenue END) AS Sep_Revenue,
SUM(CASE WHEN month='Oct' THEN revenue END) AS Oct_Revenue,
SUM(CASE WHEN month='Nov' THEN revenue END) AS Nov_Revenue,
SUM(CASE WHEN month='Dec' THEN revenue END) AS Dec_Revenue
FROM department
GROUP BY id
ORDER BY id
```

---

<br>

# row_number()
```sql
# 601
# 差值法
with s1 as (
    select id,visit_date,people, 
    id-row_number() over(order by id) g from Stadium
    where people>=100
)
# select * from (
select s3.id,s3.visit_date,s3.people from (
    select count(s1.id),s1.g from s1
    group by s1.g
    having count(s1.id)>2
) s2
left join (select s1.id,s1.visit_date,s1.people,s1.g from s1) s3
on s3.g=s2.g
```

---

<br>

# lead(expression, offset, default)/GROUP_CONCAT/NOT EXISTS
```sql
# 3617
# GROUP_CONCAT([DISTINCT] col2 [ORDER BY col2 ASC/DESC] [SEPARATOR 'str_val'])
# SQL 允许WHERE 子查询，EXISTS 子查询访问外层查询列
with s1 as (
  select student_id,subject,session_date,row_number() over (partition by student_id,subject order by session_date) r1 from study_sessions
),
#间隔2天
s3 as (
  select student_id,session_date,lead(session_date) over (partition by student_id order by session_date)-session_date ndays from study_sessions
),
# 重复顺序
s4 as(
   select student_id,r1,GROUP_CONCAT(subject ORDER BY session_date) AS subjects from s1
   group by student_id,r1
)
select distinct m3.*,s2.snum cycle_length,m2.total_study_hours from (
   select student_id,count(distinct subjects) num from s4
   group by student_id
) m1
left join (select student_id,sum(hours_studied) total_study_hours
from study_sessions
group by student_id) m2
on m2.student_id=m1.student_id
left join (select student_id,student_name,major from students) m3
on m3.student_id=m1.student_id
# 3学科，6学习记录
left join (
  select student_id,count(distinct subject) snum,count(subject) from s1
  group by student_id
  having count(distinct subject)>=3
  and count(subject)>=6
) s2
on s2.student_id=m1.student_id
where s2.student_id is not null
AND NOT EXISTS (
      SELECT 1 FROM s3
      WHERE s3.student_id = m1.student_id AND s3.ndays > 2
)
and m1.num=1
order by cycle_length desc,total_study_hours desc
```
