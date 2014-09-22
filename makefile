unittest-args = -m unittest discover --start-directory tests --top-level-directory .

define doctest-cmd =
cd docs && $(MAKE) doctest
endef

help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo "  docs-clean    Remove documentation."
	@echo "  docs-doctest  Check code samples in the documentation."
	@echo "  docs-html     Compile documentation to HTML."
	@echo "  test          Run unit tests."
	@echo "  test-all      Run unit tests and doctests, measure coverage."

docs-clean:
	cd docs && $(MAKE) clean

docs-doctest:
	$(doctest-cmd)

docs-html:
	cd docs && $(MAKE) html

test:
	python $(unittest-args)

test-all:
	coverage run $(unittest-args)
	$(doctest-cmd)

.PHONY: help docs-clean docs-doctest docs-html test test-all
