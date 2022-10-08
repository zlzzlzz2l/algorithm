SELECT WAREHOUSE_ID, WAREHOUSE_NAME, ADDRESS,
    CASE WHEN FREEZER_YN IS NULL THEN 'N'
    ELSE FREEZER_YN END AS "FREEZER_YN"
    FROM FOOD_WAREHOUSE WHERE ADDRESS LIKE '경기도%' ORDER BY WAREHOUSE_ID;