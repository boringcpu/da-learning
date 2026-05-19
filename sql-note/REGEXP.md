```sql
dna_sequence REGEXP '^ATG' AS has_start, # 以 ATG 开头 的序列
dna_sequence REGEXP 'TAA$|TAG$|TGA$' AS has_stop, # 以 TAA，TAG 或 TGA 结尾
dna_sequence REGEXP 'ATAT' AS has_atat, # 包含基序 ATAT
```