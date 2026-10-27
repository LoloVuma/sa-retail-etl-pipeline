SELECT
    SUM(sales_r_millions) AS total_sales,
    COUNT(*) AS total_records,
    COUNT(DISTINCT categories) AS total_categories,
    MIN(year) AS first_year,
    MAX(year) AS last_year
FROM retail_sales;
