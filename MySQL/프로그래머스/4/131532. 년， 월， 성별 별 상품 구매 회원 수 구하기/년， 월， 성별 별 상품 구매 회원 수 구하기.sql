SELECT YEAR(SALES_DATE) YEAR,
       MONTH(SALES_DATE) MONTH,
       GENDER,
       COUNT(DISTINCT I.USER_ID) USERS
FROM USER_INFO I
JOIN ONLINE_SALE O ON I.USER_ID = O.USER_ID
WHERE I.GENDER IS NOT NULL
GROUP BY 1, 2, 3
ORDER BY 1, 2, 3