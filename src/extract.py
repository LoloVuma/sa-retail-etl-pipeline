
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
    print("Starting data extraction...")

    if not RAW_FILE.exists():
        print(f"Error: CSV file not found: {RAW_FILE}")
        return

    df = pd.read_csv(RAW_FILE)

    print("CSV loaded successfully!")
    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")


if __name__ == "__main__":
    main()
