SELECT 
    A.AUTHOR_ID, 
    A.AUTHOR_NAME, 
    B.CATEGORY, 
    SUM(B.PRICE * S.SALES) TOTAL_SALES
FROM BOOK B
JOIN AUTHOR A ON B.AUTHOR_ID = A.AUTHOR_ID
JOIN BOOK_SALES S ON B.BOOK_ID = S.BOOK_ID
WHERE MONTH(S.SALES_DATE) = 1
GROUP BY 1, 3
ORDER BY 1, 3 DESC