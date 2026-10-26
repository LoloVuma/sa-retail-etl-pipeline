from pathlib import Path
import pandas as pd

# Get the project folder
PROJECT_DIR = Path(__file__).resolve().parent.parent

# Locate the raw CSV file
RAW_FILE = (
    PROJECT_DIR
    / "data"
    / "raw"
    / "RETAIL TRADE SALES 2008 ONWARDS2 (2).csv"
)


def main():
    print("Starting data transformation...")

    # Check that the raw CSV file exists
    if not RAW_FILE.exists():
        raise FileNotFoundError(f"CSV file not found: {RAW_FILE}")

    # Load the raw dataset
    df = pd.read_csv(RAW_FILE)

    print(f"Original rows: {len(df)}")
    print(f"Original columns: {len(df.columns)}")

    
    # Standardise column names
    df.columns = (
        df.columns
        .str.strip()
        .str.replace(r"([a-z0-9])([A-Z])", r"\1_\2", regex=True)
        .str.lower()
        .str.replace(r"[^a-z0-9]+", "_", regex=True)
        .str.strip("_")
    )


    print("\nStandardised column names:")
    print(df.columns.tolist())

    # Convert the date column to datetime
    df["date"] = pd.to_datetime(df["date"], errors="raise")

    print("\nDate column data type:")
    print(df["date"].dtype)

    print("\nFirst five dates:")
    print(df["date"].head().to_list())


if __name__ == "__main__":
    main()
