-- Check 1: Total number of rows
SELECT COUNT(*) AS total_rows
FROM retail_sales;


-- Check 2: Rows with missing values
SELECT COUNT(*) AS rows_with_missing_values
FROM retail_sales
WHERE categories IS NULL
   OR price_type IS NULL
   OR value_type IS NULL
   OR month_num IS NULL
   OR year IS NULL
   OR month_name IS NULL
   OR date IS NULL
   OR sales_r_millions IS NULL;


-- Check 3: Exact duplicate rows
SELECT COUNT(*) AS duplicate_rows
FROM (
    SELECT
        categories,
        price_type,
        value_type,
        month_num,
        year,
        month_name,
        date,
        sales_r_millions,
        COUNT(*) AS occurrences
    FROM retail_sales
    GROUP BY
        categories,
        price_type,
        value_type,
        month_num,
        year,
        month_name,
        date,
        sales_r_millions
    HAVING COUNT(*) > 1
);
