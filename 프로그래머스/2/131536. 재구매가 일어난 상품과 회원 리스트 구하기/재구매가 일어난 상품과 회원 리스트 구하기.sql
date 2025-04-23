-- 코드를 입력하세요
SELECT DISTINCT user_id, product_id
FROM online_sale t
WHERE (t.user_id, t.product_id) IN (
    SELECT user_id, product_id
    FROM online_sale
    GROUP BY user_id, product_id
    HAVING COUNT(*) > 1
)
ORDER BY USER_ID ASC, PRODUCT_ID DESC