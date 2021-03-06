# Our Group Project

## Info
- data retrieved from https://data.calgary.ca/Government/311-Call-Centre/hk5h-uv5k
- based around the effectiveness of the 311 Call Centre in calgary

## Questions With Accompying SQL Query
1. How has call volume and effectiveness changed over the past 3 years?
```sql
SELECT
        date,
        offered,
        (answered*1.0)/offered*100 AS effectiveness
FROM
        'calgary_combined'
WHERE
        STRFTIME('%Y',date) = '2015' AND
        (answered*1.0)/offered*100 < 100
ORDER BY
        date;
```
2. What effect does the number of callers have on the expected delay times?
```sql
SELECT
        offered,
        avg_ans_delay_seconds
FROM
        'calgary_combined';
```
3. What is the average portion of calls that are being answered and abandoned?
```sql
SELECT
        AVG(offered),
        AVG(answered)/AVG(offered)*100 AS answered,
        AVG(abandonned)/AVG(offered)*100 AS abandoned
FROM
        'calgary_combined';
```
4. What is the monthly average effectiveness? Where: effectiveness = offered / answered
```sql
SELECT
        STRFTIME('%Y-%m', date) AS date,
        AVG(answered)/AVG(offered)*100 AS effectiveness
FROM
        'calgary_combined'
GROUP BY
        STRFTIME('%Y-%m', date);
```
5. What are the peak months in terms of volume?
```sql
SELECT
        STRFTIME('%m', date) AS date,
        AVG(offered) AS received
FROM
        'calgary_combined'
GROUP BY
        STRFTIME('%m', date);
```
6. How are call centres responding to changes in volume?
```sql
SELECT
        offered,
        (answered*1.0)/offered*100 AS effectivness
FROM
        'calgary_combined'
ORDER BY
        offered
```
