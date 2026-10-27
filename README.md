# South African Retail Sales ETL Pipeline

## Project Overview

This project builds an ETL pipeline using Python, Pandas, SQL, and Power BI to process and analyse South African retail trade sales data.

The pipeline extracts data from a CSV file, cleans and transforms it using Python, loads the processed data into a SQLite database, and uses SQL to analyse sales trends. The final stage is an interactive Power BI dashboard.

## Business Objectives

- Clean and validate retail sales data.
- Store structured data in a relational database.
- Analyse sales by retail category and month.
- Check data quality and verify the loading process.
- Present findings through a Power BI dashboard.

## Technologies

- **Python** — ETL scripting
- **Pandas** — data cleaning and transformation
- **SQLite** — data storage
- **SQL** — sales analysis and data-quality checks
- **Power BI** — interactive data visualisation
- **Git and GitHub** — version control and project documentation

## Data Source

[South African Retail Sales Analysis](https://github.com/naledi901/South-African-Retail-Sales-Analysis)

The dataset contains monthly South African retail trade sales records, with fields for retail category, price type, value type, month, year, date, and sales value.

## ETL Pipeline

1. **Extract:** Read the source CSV file and generate an extraction summary.
2. **Transform:** Standardise column names, convert dates, check data types, inspect missing values and duplicates, and save the cleaned dataset.
3. **Load:** Load the cleaned dataset into a SQLite database table named `retail_sales`.
4. **Analyse:** Use SQL queries to summarise sales by category and month.
5. **Validate:** Check record counts, missing values, duplicate records, and loading behaviour.
6. **Visualise:** Build a Power BI dashboard to present key performance indicators and sales trends.

## Data Quality and Validation

The current validation checks returned the following results:

| Check | Result |
|---|---:|
| Total records loaded | 5,824 |
| Columns in the cleaned dataset | 8 |
| Missing-value check | 0 rows with missing values |
| Duplicate-row check | 0 duplicate rows |
| Distinct retail categories | 7 |
| Earliest recorded date | January 2008 |
| Latest recorded date | April 2025 |

The dataset contains records for all 12 months from 2008 through 2024, and four months for 2025.

The loading process was rerun to verify that records were replaced rather than duplicated. The database still contained 5,824 rows after the rerun.

## SQL Analysis

The SQL scripts currently cover:

- Total sales by retail category.
- Monthly sales totals across the dataset.
- Overall summary metrics, including total records, category count, and year range.
- Data-quality checks for row counts, missing values, and duplicate records.

The current sum of the `sales_r_millions` column is 69,605,095. The dataset's units and scale should be verified before interpreting or displaying this value as a monetary amount.

## Project Structure

```text
sa-retail-etl-pipeline/
├── data/
│   ├── raw/
│   └── processed/
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── sql/
│   ├── analysis.sql
│   ├── data_quality.sql
│   └── dashboard_summary.sql
├── requirements.txt
├── .gitignore
└── README.md
```

Generated data files and the SQLite database are excluded from version control through `.gitignore`.

## Project Status

- [x] Project setup and source data documentation
- [x] Data extraction
- [x] Data transformation and cleaning
- [x] Load cleaned data into SQLite
- [x] SQL sales analysis
- [x] SQL data-quality checks
- [x] Dashboard summary query
- [ ] Power BI dashboard
- [ ] Final dashboard screenshots and documentation

## Future Improvements

- Complete the Power BI dashboard with key performance indicators, category comparisons, and monthly sales trends.
- Document the meaning and units of the source sales measure.
- Add dashboard screenshots and final findings to this README.
