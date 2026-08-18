from pathlib import Path
import pandas as pd

from src.etl.normaliser import normalize_year, normalize_ticker


BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = BASE_DIR / "data" / "raw"
PROCESSED_DIR = BASE_DIR / "data" / "processed"


def load_excel(file_path):
    """
    Load an Excel file into a pandas DataFrame.
    """

    if not file_path.exists():
        raise FileNotFoundError(
            f"Source file not found: {file_path}"
        )

    return pd.read_excel(file_path)


def normalize_dataframe(df):
    """
    Apply standard normalization to recognized columns.
    """

    df = df.copy()

    if "year" in df.columns:
        df["year"] = df["year"].apply(normalize_year)

    if "ticker" in df.columns:
        df["ticker"] = df["ticker"].apply(normalize_ticker)

    return df


def process_file(file_path):
    """
    Load and normalize one Excel file.
    """

    print(f"Loading: {file_path.name}")

    df = load_excel(file_path)
    df = normalize_dataframe(df)

    return df


def main():
    PROCESSED_DIR.mkdir(
        parents=True,
        exist_ok=True
    )

    files = list(RAW_DIR.glob("*.xlsx"))

    print(f"Found {len(files)} Excel files.")

    for file_path in files:
        df = process_file(file_path)

        output_path = (
            PROCESSED_DIR /
            f"{file_path.stem}.csv"
        )

        df.to_csv(
            output_path,
            index=False
        )

        print(
            f"Saved: {output_path.name} "
            f"({len(df)} rows)"
        )


if __name__ == "__main__":
    main()