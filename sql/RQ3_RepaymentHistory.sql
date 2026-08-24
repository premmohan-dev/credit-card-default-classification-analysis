-- Research Question 3
-- How does repayment history relate to default status?
-- Purpose: Compare default rates by most recent repayment status.

SELECT
    PAY_0,
    COUNT(*) AS CustomerCount,
    AVG([default payment next month]) * 100 AS DefaultRate
FROM
    Data
GROUP BY
    PAY_0
ORDER BY
    PAY_0;
