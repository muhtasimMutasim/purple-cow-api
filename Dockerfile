FROM python:3.7-slim-buster

RUN apt-get update && \
    apt-get install --no-install-recommends -y build-essential make && \
    apt-get install --no-install-recommends -y gcc 

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY . .
CMD uvicorn main:app --host 0.0.0.0 --port 5057  --reload
