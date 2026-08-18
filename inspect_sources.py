from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parent
RAW_DIR = BASE_DIR / "data" / "raw"


def inspect_excel_files():
    files = sorted(
        list(RAW_DIR.glob("*.xlsx")) +
        list(RAW_DIR.glob("*.xls"))
    )

    print(f"Found {len(files)} Excel files\n")

    for file in files:

        print("=" * 80)
        print(f"FILE: {file.name}")
        print("=" * 80)

        try:
            excel = pd.ExcelFile(file)

            print(f"Sheets: {excel.sheet_names}\n")

            for sheet in excel.sheet_names:

                df = pd.read_excel(
                    file,
                    sheet_name=sheet,
                    header=1
                )

                # Remove completely empty rows/columns
                df = df.dropna(
                    axis=0,
                    how="all"
                )

                df = df.dropna(
                    axis=1,
                    how="all"
                )

                print(f"Sheet: {sheet}")
                print(f"Rows: {len(df)}")
                print(f"Columns: {len(df.columns)}")
                print(f"Columns: {list(df.columns)}")

                print("\nFirst 3 rows:")
                print(df.head(3).to_string(index=False))

                print()

        except Exception as exc:
            print(f"ERROR: {exc}")


if __name__ == "__main__":
    inspect_excel_files()