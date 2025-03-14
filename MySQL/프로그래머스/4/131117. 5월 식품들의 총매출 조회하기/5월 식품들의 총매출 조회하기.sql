SELECT P.PRODUCT_ID, P.PRODUCT_NAME, SUM(PRICE * AMOUNT) TOTAL_SALES
FROM FOOD_PRODUCT P
JOIN FOOD_ORDER O ON P.PRODUCT_ID = O.PRODUCT_ID
WHERE O.PRODUCE_DATE LIKE '2022-05%'
GROUP BY 1
ORDER BY 3 DESC, 1