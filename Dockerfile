FROM python:3

WORKDIR /usr/src/app
COPY requirements.txt ./
COPY src ./src

RUN	pip install virtualenv && virtualenv -p python3 venv && venv/bin/pip install -r requirements.txt

ENTRYPOINT ["./venv/bin/python", "./src/main.py"]