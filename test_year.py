from src.etl.normaliser import normalize_year

print(normalize_year(2022))
print(normalize_year("2022"))
print(normalize_year("FY2022"))