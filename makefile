.PHONY: test project

pylint:
	pylint --reports=y ./scripts

pytest:
	pytest

# Total pytest coverage report
coverage:
	pytest --cov=./scripts --cov-report xml:cov.xml
	coverage report -m
