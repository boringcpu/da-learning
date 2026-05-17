# DATE_ADD

## 基本用法

```sql
DATE_ADD(date, INTERVAL value addunit)
```

作用：

给日期增加1天。

---

## 示例

```sql
SELECT DATE_ADD('2025-01-01', INTERVAL 1 DAY)
```

结果：

```text
2025-01-02
```