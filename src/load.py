from pathlib import Path
import sqlite3
import pandas as pd

# Get the main project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Locate the cleaned CSV file
INPUT_FILE = (
    PROJECT_DIR
    / "data"
    / "processed"
    / "cleaned_retail_sales.csv"
)

# Choose where the SQLite database will be stored
DATABASE_FILE = PROJECT_DIR / "data" / "retail_sales.db"


def main():
    print("Starting database loading...")

    # Check that the cleaned CSV file exists
    if not INPUT_FILE.exists():
        raise FileNotFoundError(
            f"Cleaned CSV file not found: {INPUT_FILE}"
        )

    # Read the cleaned CSV into a DataFrame
    df = pd.read_csv(INPUT_FILE)

    print(f"Rows to load: {len(df)}")

    # Make sure the data folder exists
    DATABASE_FILE.parent.mkdir(parents=True, exist_ok=True)

    # Connect to the SQLite database
    with sqlite3.connect(DATABASE_FILE) as connection:

        # Load the data into a table named retail_sales
        df.to_sql(
            "retail_sales",
            connection,
            if_exists="replace",
            index=False
        )

        # Count the records stored in the database
        cursor = connection.execute(
            "SELECT COUNT(*) FROM retail_sales"
        )
        row_count = cursor.fetchone()[0]

    print(f"Rows loaded into database: {row_count}")
    print(f"Database saved to: {DATABASE_FILE}")

    # Confirm that every row was loaded
    if row_count != len(df):
        raise ValueError("The number of loaded rows does not match!")

    print("Database loading completed successfully.")


if __name__ == "__main__":
    main()
