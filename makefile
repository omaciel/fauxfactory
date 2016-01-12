UNITTEST_CMD ?= unit2
UNITTEST_MOD ?= unittest
UNITTEST_ARGS ?= discover --start-directory tests --top-level-directory .

help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo "  docs-clean    Remove documentation."
	@echo "  docs-doctest  Check code samples in the documentation."
	@echo "  docs-html     Compile documentation to HTML."
	@echo "  flake         Run flake8."
	@echo "  lint          Run flake8 and pylint."
	@echo "  test          Run unit tests."
	@echo "  test-all      Run unit tests and doctests, measure coverage."

docs-clean:
	cd docs && $(MAKE) clean

docs-doctest:
	cd docs && $(MAKE) doctest

docs-html:
	cd docs && $(MAKE) html

flake:
	flake8 .

lint: flake
	pylint --reports=n --disable=I --ignore-imports=y fauxfactory docs/conf.py setup.py
# pylint should also lint the tests/ directory.

package:
	python setup.py sdist bdist_wheel

package-clean:
	rm -rf build dist fauxfactory.egg-info

publish:
	python setup.py register
	python setup.py sdist upload -s
	python setup.py bdist_wheel upload -s

test:
	$(UNITTEST_CMD) $(UNITTEST_ARGS)

test-all: flake docs-doctest
	coverage run -m $(UNITTEST_MOD) $(UNITTEST_ARGS)

.PHONY: help docs-clean docs-doctest docs-html flake lint package package-clean publish test test-all
