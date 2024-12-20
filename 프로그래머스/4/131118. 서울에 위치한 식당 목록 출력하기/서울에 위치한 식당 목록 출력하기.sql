-- 코드를 입력하세요
SELECT
    I.REST_ID,
    I.REST_NAME,
    I.FOOD_TYPE,
    I.FAVORITES,
    I.ADDRESS,
    R.AVG_SCORE AS SCORE
FROM
    REST_INFO I,
    (
        SELECT
            REST_ID,
            ROUND(AVG(REVIEW_SCORE), 2) AS AVG_SCORE
        FROM
            REST_REVIEW
        GROUP BY
            REST_ID
    ) R
WHERE
    I.REST_ID = R.REST_ID AND
    I.ADDRESS LIKE "서울%"
ORDER BY
    SCORE DESC,
    I.FAVORITES DESC