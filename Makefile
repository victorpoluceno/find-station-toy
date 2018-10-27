VENV_PATH = venv

install:
	virtualenv -p python3 $(VENV_PATH)
	$(VENV_PATH)/bin/pip install pytest
	$(VENV_PATH)/bin/pip install mypy

test: check
	PYTHONPATH=src/ $(VENV_PATH)/bin/py.test src/tests/*

check:
	$(VENV_PATH)/bin/mypy --strict src/.
