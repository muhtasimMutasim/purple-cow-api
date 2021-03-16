FROM python:3.7-slim-buster

RUN apt-get update && \
    apt-get install -y --no-install-recommends gcc && \
    apt-get install -y --no-install-recommends libffi-dev libssl-dev && \
    apt-get install -y --no-install-recommends python3-dev python3-cffi && \
    apt-get install -y build-essential make

COPY requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . .
CMD uvicorn main:app --host 0.0.0.0 --port 3000  --reload
