FROM python:3.7-slim-buster

RUN apt-get update && \
    apt-get install -y gcc && \
    apt-get install -y --no-install-recommends libffi-dev libssl-dev python-dev python-cffi && \
    apt-get install -y build-essential make

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD uvicorn main:app --host 0.0.0.0 --port 3000  --reload
