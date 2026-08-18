import re


def normalize_year(value):
    """
    Normalize different year formats into an integer year.

    Supported:
        2024       -> 2024
        2024.0     -> 2024
        "2024"     -> 2024
        "FY2024"   -> 2024
        "FY 2024"  -> 2024
        "Dec 2012" -> 2012
        "Mar 2014" -> 2014
        "Mar 2015" -> 2015

    Invalid formats raise ValueError.
    """

    if value is None:
        return None

    # Integer
    if isinstance(value, int) and not isinstance(value, bool):
        return value

    # Float
    if isinstance(value, float):
        if value != value:  # NaN
            return None

        if value.is_integer():
            return int(value)

        raise ValueError(f"Invalid year value: {value}")

    value = str(value).strip()

    if not value:
        return None

    # Plain year: "2024"
    if re.fullmatch(r"\d{4}", value):
        return int(value)

    # FY formats: "FY2024", "FY 2024", "fy2024"
    fy_match = re.fullmatch(r"FY\s*(\d{4})", value, re.IGNORECASE)

    if fy_match:
        return int(fy_match.group(1))

    # Month + year formats: "Dec 2012", "Mar 2014"
    month_year_match = re.fullmatch(
        r"(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)\s+(\d{4})",
        value,
        re.IGNORECASE
    )

    if month_year_match:
        return int(month_year_match.group(2))

    raise ValueError(f"Invalid year value: {value}")