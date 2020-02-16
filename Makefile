.PHONY: tests

tests: ## run tests quickly with the default Python
	PYTHONPATH="." python tests/test_bake_project.py
