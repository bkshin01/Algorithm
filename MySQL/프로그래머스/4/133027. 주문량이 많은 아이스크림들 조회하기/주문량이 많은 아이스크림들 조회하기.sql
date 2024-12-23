-- 코드를 입력하세요
WITH T AS (
    SELECT FH.FLAVOR, SUM(FH.TOTAL_ORDER + J.TOTAL_ORDER)
    FROM FIRST_HALF FH
    JOIN JULY J ON FH.FLAVOR = J.FLAVOR
    GROUP BY 1
    ORDER BY 2 DESC
    LIMIT 3)
SELECT FLAVOR
FROM T