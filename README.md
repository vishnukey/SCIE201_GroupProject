# Our Group Project

## Info
- data retrieved from https://data.calgary.ca/Government/311-Call-Centre/hk5h-uv5k
- based around the effectiveness of the 311 Call Centre in calgary

## Data Questions
1. How has call volume and effectiveness changed over the past 3 years?
2. What effect does the number of callers have on the expected delay times?
3. What is the average portion of calls that are being answered and abandoned?
4. What is the monthly average effectiveness?
        - effectiveness = offered / answered
5. What are the peak months in terms of volume?
6. How are call centres responding to changes in volume?

## Questions In Terms of SQL
1. 
```sql
SELECT 
        date, 
        offered,
        (answered*1.0)/offered*100 AS effectiveness
FROM 
        "<tableName>" 
ORDER BY 
        date;
```
2. 
```sql
SELECT 
        offered, 
        avg_ans_delay_seconds 
FROM 
        "<tableName>";
```
3. 
```sql
SELECT 
        offered, 
        answered, 
        abandonned 
FROM 
        "<tableName>";
```
4. 
```sql
SELECT 
        STRFTIME("%Y-%m", date) AS date, 
        AVG(answered)/AVG(offered)*100 AS "effectiveness" 
FROM 
        "<tableName>" 
GROUP BY 
        STRFTIME("%Y-%m", date);
```
5. 
```sql
SELECT 
        STRFTIME("%m", date), 
        AVG(offered) 
FROM 
        "<tableName>" 
GROUP BY 
        STRFTIME("%m", date);
```
6. 
```sql
SELECT 
        offered, 
        (answered*1.0)/offered*100 AS effectivness 
FROM 
        "<tableName>" 
ORDER BY 
        offered;
```

