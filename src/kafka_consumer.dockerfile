FROM python:3-slim

ENV PYTHONUNBUFFERED=True

WORKDIR /usr/src/app

COPY app/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "./kafka_consumer.py"]

COPY app/ .
