-- Research Question 2
-- How do credit limits differ between customers who default and customers who do not?
-- Purpose: Compare average credit limits by default status.

SELECT
    [default payment next month],
    COUNT(*) AS CustomerCount,
    AVG(LIMIT_BAL) AS AverageCreditLimit
FROM
    Data
GROUP BY
    [default payment next month];
