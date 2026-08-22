-- Research Question 1
-- How do default rates vary across customer demographic groups?
-- Purpose: Calculate default rates by education level.

SELECT
    EDUCATION,
    COUNT(*) AS CustomerCount
FROM
    Data
GROUP BY
    EDUCATION
ORDER BY
    EDUCATION;
