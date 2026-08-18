import re


def normalize_year(value):
    """
    Convert different year formats into an integer year.

    Examples:
        2024 -> 2024
        "2024" -> 2024
        2024.0 -> 2024
        "FY2024" -> 2024
        "FY 2024" -> 2024
        "Dec 2012" -> 2012
        "Mar 2014" -> 2014
        "Mar 2015" -> 2015
    """

    # None
    if value is None:
        return None

    # Integer
    if isinstance(value, int):
        return value

    # Float
    if isinstance(value, float):
        if value != value:  # NaN
            return None

        if value.is_integer():
            return int(value)

        raise ValueError(f"Invalid year value: {value}")

    # Convert to string
    value = str(value).strip()

    # Empty string
    if value == "":
        return None

    # FY2024 / FY 2024 / fy2024
    value = re.sub(r"^FY\s*", "", value, flags=re.IGNORECASE)

    # Plain numeric year
    if value.isdigit():
        return int(value)

    # Dec 2012
    # Mar 2014
    # March 2015
    match = re.search(r"(19|20)\d{2}", value)

    if match:
        return int(match.group())

    raise ValueError(f"Invalid year value: {value}")


def normalize_ticker(value):
    """
    Normalize company ticker symbols.

    Examples:
        "reliance" -> "RELIANCE"
        " RELIANCE " -> "RELIANCE"
        "hdfcbank" -> "HDFCBANK"
    """

    if value is None:
        return None

    value = str(value).strip()

    if value == "":
        return None

    return value.upper()