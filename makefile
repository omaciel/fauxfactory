help:
	@echo "Please use \`make <target>' where <target> is one of:"
	@echo "  docs        Compile documentation."
	@echo "  docs-clean  Remove documentation."
	@echo "  test        Run unit tests."

docs:
	@cd docs; $(MAKE) html

docs-clean:
	@cd docs; $(MAKE) clean

test:
	python -m unittest discover --start-directory tests --top-level-directory .

.PHONY: docs docs-clean test
