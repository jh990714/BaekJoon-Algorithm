-- 코드를 입력하세요
-- 2021년 가입한 회원들 중 상품을 구매한 회원수, 비율 (년, 월별)
SELECT
    YEAR(O.SALES_DATE) AS YEAR,
    MONTH(O.SALES_DATE) AS MONTH,
    COUNT(DISTINCT U.USER_ID) AS PURCHASED_USERS,
    ROUND(COUNT(DISTINCT U.USER_ID) / (SELECT COUNT(*) FROM USER_INFO WHERE JOINED LIKE '2021%'), 1) AS PUCHASED_RATIO
FROM 
    USER_INFO AS U
JOIN 
    ONLINE_SALE AS O ON U.USER_ID = O.USER_ID
WHERE 
    U.JOINED LIKE '2021%'
GROUP BY
    YEAR, MONTH
ORDER BY
    YEAR, MONTH