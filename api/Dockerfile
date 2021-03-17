FROM python:3.7-alpine


RUN apk --update add bash nano git
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt
COPY . .
CMD uvicorn main:app --host 0.0.0.0 --port 3000  --reload
