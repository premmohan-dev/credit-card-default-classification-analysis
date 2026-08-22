-- Data Preparation
-- Purpose: Count customers by default status.

SELECT
    [default payment next month],
    COUNT(*) AS CustomerCount
FROM
    Data
GROUP BY
    [default payment next month];
