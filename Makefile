help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo "  docs-clean    Remove documentation."
	@echo "  docs-doctest  Check code samples in the documentation."
	@echo "  docs-html     Compile documentation to HTML."
	@echo "  format         Run format8."
	@echo "  lint          Run format8 and pylint."
	@echo "  test          Run unit tests."
	@echo "  test-all      Run unit tests and doctests, measure coverage."

all: test-all lint docs-clean docs-html package-clean package

docs-clean:
	cd docs && rm -rf _build/*

docs-doctest:
	cd docs && rye run sphinx-build -b doctest -d _build/doctrees   . _build/doctest

docs-html:
	cd docs && rye run sphinx-build -b html -d _build/doctrees   . _build/html

format:
	rye run ruff format -v .

lint: format
	rye run ruff check -v .

package:
	rye build

package-clean:
	rye build --clean

publish:
	rye publish

test:
	rye run py.test -v

test-all:
	rye run py.test -v --cov-report term-missing --cov=fauxfactory

.PHONY: help docs-clean docs-doctest docs-html format lint package package-clean publish test test-all
