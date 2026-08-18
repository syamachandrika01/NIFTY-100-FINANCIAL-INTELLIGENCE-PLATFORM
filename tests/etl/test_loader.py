from pathlib import Path

import pandas as pd
import pytest

from src.etl.loader import load_excel


def test_raw_directory_exists():
    path = Path("data/raw")
    assert path.exists()


def test_excel_files_exist():
    files = list(Path("data/raw").glob("*.xlsx"))
    assert len(files) > 0


def test_load_excel():
    files = list(Path("data/raw").glob("*.xlsx"))

    if not files:
        pytest.skip("No Excel files available")

    df = load_excel(files[0])

    assert isinstance(df, pd.DataFrame)


def test_loaded_dataframe_has_columns():
    files = list(Path("data/raw").glob("*.xlsx"))

    if not files:
        pytest.skip("No Excel files available")

    df = load_excel(files[0])

    assert len(df.columns) > 0