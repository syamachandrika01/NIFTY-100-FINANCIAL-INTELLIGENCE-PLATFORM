import pytest

from src.etl.normaliser import (
    normalize_year,
    normalize_ticker,
)


def test_year_integer():
    assert normalize_year(2022) == 2022


def test_year_string():
    assert normalize_year("2022") == 2022


def test_year_fy_string():
    assert normalize_year("FY2022") == 2022


def test_year_with_spaces():
    assert normalize_year(" 2022 ") == 2022


def test_year_float():
    assert normalize_year(2022.0) == 2022


def test_year_none():
    assert normalize_year(None) is None


def test_year_empty_string():
    assert normalize_year("") is None


def test_year_whitespace():
    assert normalize_year("   ") is None


def test_year_fy_lowercase():
    assert normalize_year("fy2022") == 2022


def test_year_fy_with_space():
    assert normalize_year("FY 2022") == 2022


def test_year_2020():
    assert normalize_year("2020") == 2020


def test_year_2021():
    assert normalize_year("2021") == 2021


def test_year_2023():
    assert normalize_year("2023") == 2023


def test_year_2024():
    assert normalize_year("2024") == 2024


def test_year_2025():
    assert normalize_year("2025") == 2025


def test_year_2019():
    assert normalize_year(2019) == 2019


def test_year_float_2023():
    assert normalize_year(2023.0) == 2023


def test_year_fy2024():
    assert normalize_year("FY2024") == 2024


def test_year_invalid_text():
    with pytest.raises(ValueError):
        normalize_year("ABC")




def test_ticker_uppercase():
    assert normalize_ticker("reliance") == "RELIANCE"


def test_ticker_already_uppercase():
    assert normalize_ticker("TCS") == "TCS"


def test_ticker_spaces():
    assert normalize_ticker(" TCS ") == "TCS"


def test_ticker_lowercase():
    assert normalize_ticker("infy") == "INFY"


def test_ticker_mixed_case():
    assert normalize_ticker("InFy") == "INFY"


def test_ticker_none():
    assert normalize_ticker(None) is None


def test_ticker_empty():
    assert normalize_ticker("") is None


def test_ticker_whitespace():
    assert normalize_ticker("   ") is None


def test_ticker_reliance():
    assert normalize_ticker("RELIANCE") == "RELIANCE"


def test_ticker_hdfc():
    assert normalize_ticker("hdfcbank") == "HDFCBANK"


def test_ticker_itc():
    assert normalize_ticker("itc") == "ITC"


def test_ticker_sbin():
    assert normalize_ticker("sbin") == "SBIN"


def test_ticker_wipro():
    assert normalize_ticker("Wipro") == "WIPRO"


def test_ticker_bajaj():
    assert normalize_ticker(" bajajfinance ") == "BAJAJFINANCE"


def test_ticker_numeric():
    assert normalize_ticker(123) == "123"

def test_year_dec_2012():
    assert normalize_year("Dec 2012") == 2012


def test_year_mar_2014():
    assert normalize_year("Mar 2014") == 2014


def test_year_mar_2015():
    assert normalize_year("Mar 2015") == 2015


def test_year_fy_with_space():
    assert normalize_year("FY 2024") == 2024


def test_year_float():
    assert normalize_year(2023.0) == 2023