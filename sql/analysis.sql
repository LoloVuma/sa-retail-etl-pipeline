-- Query 1: Total sales by category
SELECT
    categories,
    SUM(sales_r_millions) AS total_sales_r_millions
FROM retail_sales
GROUP BY categories
ORDER BY total_sales_r_millions DESC;


-- Query 2: Total sales by month across all years
SELECT
    month_num,
    month_name,
    SUM(sales_r_millions) AS total_sales_r_millions
FROM retail_sales
GROUP BY month_num, month_name
ORDER BY month_num;

