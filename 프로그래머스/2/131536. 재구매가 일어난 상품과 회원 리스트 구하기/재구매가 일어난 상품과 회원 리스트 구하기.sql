-- 코드를 입력하세요

SELECT
    USER_ID,
    PRODUCT_ID
FROM
    (SELECT
        USER_ID,
        PRODUCT_ID,
        COUNT(*) AS COUNT
    FROM
        ONLINE_SALE
    GROUP BY
        USER_ID,
        PRODUCT_ID) AS O
WHERE
    O.COUNT >= 2
ORDER BY
    USER_ID ASC,
    PRODUCT_ID DESC