load:
	python -m src.etl.loader

ratios:
	python -m src.etl.validator

test:
	pytest

report:
	python -m src.etl.validator

dashboard:
	@echo "Dashboard target will be implemented later."

api:
	@echo "API target will be implemented later."

clean:
	@echo "Cleaning generated files..."