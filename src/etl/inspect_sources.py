from pathlib import Path
import pandas as pd


BASE_DIR = Path(__file__).resolve().parents[2]
RAW_DIR = BASE_DIR / "data" / "raw"


def inspect_excel_files():
    files = list(RAW_DIR.glob("*.xlsx")) + list(RAW_DIR.glob("*.xls"))

    print(f"Found {len(files)} Excel files\n")

    for file in files:
        print("=" * 70)
        print(f"FILE: {file.name}")
        print("=" * 70)

        try:
            excel = pd.ExcelFile(file)

            print("Sheets:")
            for sheet in excel.sheet_names:
                print(f"  - {sheet}")

                df = pd.read_excel(file, sheet_name=sheet)

                print(f"    Rows: {len(df)}")
                print(f"    Columns: {len(df.columns)}")
                print(f"    Columns: {list(df.columns)}")
                print()

        except Exception as exc:
            print(f"ERROR: {exc}")


if __name__ == "__main__":
    inspect_excel_files()