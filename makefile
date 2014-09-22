define run-doctest =
cd docs && $(MAKE) doctest
endef

help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo "  docs-clean    Remove documentation."
	@echo "  docs-doctest  Check code samples in the documentation."
	@echo "  docs-html     Compile documentation to HTML."
	@echo "  test          Run unit tests and doctests."

docs-clean:
	cd docs && $(MAKE) clean

docs-doctest:
	$(run-doctest)

docs-html:
	cd docs && $(MAKE) html

test:
	python -m unittest discover --start-directory tests --top-level-directory .
	$(run-doctest)

.PHONY: help docs-clean docs-doctest docs-html test
