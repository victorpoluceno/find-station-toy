VENV_PATH = venv
JSON_STATIONS = [[[0, 0], 10]]
JSON_POINT = [0, 0]

install:
	virtualenv -p python3 $(VENV_PATH)
	$(VENV_PATH)/bin/pip install -r requirements.txt

test: check
	PYTHONPATH=src/ $(VENV_PATH)/bin/py.test src/tests/*

check:
	$(VENV_PATH)/bin/mypy --strict src/.

run: check
	PYTHONPATH=src venv/bin/python src/main.py --json_stations '$(JSON_STATIONS)' --json_point '$(JSON_POINT)'