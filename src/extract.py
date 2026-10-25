
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

    summary_dir = PROJECT_DIR / "data" / "processed"
    summary_dir.mkdir(parents=True, exist_ok=True)

    summary_file = summary_dir / "extraction_summary.txt"

    summary = [
        "SOUTH AFRICAN RETAIL SALES - EXTRACTION SUMMARY",
        "=" * 50,
        f"Source file: {RAW_FILE.name}",
        f"Total rows: {df.shape[0]}",
        f"Total columns: {df.shape[1]}",
        "",
        "COLUMN NAMES AND DATA TYPES",
        "-" * 50,
    ]

    for column in df.columns:
        summary.append(f"{column}: {df[column].dtype}")

    missing_values = df.isnull().sum()

    summary.extend(["", "MISSING VALUES PER COLUMN", "-" * 50])

    for column, count in missing_values.items():
        summary.append(f"{column}: {count}")

    summary.extend([
        "",
        f"Total missing values: {int(missing_values.sum())}",
        "",
        "FIRST FIVE ROWS",
        "-" * 50,
        df.head().to_string(index=False),
    ])

    summary_file.write_text("\n".join(summary), encoding="utf-8")

    print(f"Rows: {df.shape[0]}")
    print(f"Columns: {df.shape[1]}")
    print(f"Summary saved to: {summary_file}")

if __name__ == "__main__":
    main()
