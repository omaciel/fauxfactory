help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo "  docs-clean    Remove documentation."
	@echo "  docs-doctest  Check code samples in the documentation."
	@echo "  docs-html     Compile documentation to HTML."
	@echo "  format         Run format8."
	@echo "  lint          Run format8 and pylint."
	@echo "  test          Run unit tests."
	@echo "  test-all      Run unit tests and doctests, measure coverage."

all: clean lint test-all check clean docs-clean docs-html

# Linting and formatting
check:
	uvx ruff check .

# Clean build artifacts
clean:
	rm -rf build/
	rm -rf dist/
	rm -rf *.egg-info
	find . -type d -name __pycache__ -exec rm -rf {} +
	find . -type f -name "*.pyc" -delete
	find . -type f -name "*.pyo" -delete
	find . -type f -name "*.pyd" -delete

docs-clean:
	cd docs && rm -rf _build/*

docs-doctest:
	cd docs && rye run sphinx-build -b doctest -d _build/doctrees   . _build/doctest

docs-html:
	cd docs && rye run sphinx-build -b html -d _build/doctrees   . _build/html

format:
	uvx ruff format .

lint: check format

install-dev:
	uv pip install -e ".[dev]"

build: clean
	uv build


publish:
	uv publish

test: install-dev
	uv run --with '.[test]' pytest -v

test-all: install-dev
	uv run --with pytest-cov --with '.[test]' pytest --cov-report term-missing --cov=fauxfactory

.PHONY: help build check clean docs-clean docs-doctest docs-html format lint build publish test test-all
