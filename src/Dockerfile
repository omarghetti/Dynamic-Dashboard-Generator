FROM debian:stable-slim

ENV PYTHONUNBUFFERED=True
ENV LC_ALL=C.UTF-8
ENV LANG=C.UTF-8

RUN sed -i 's#deb.debian.org#ba.mirror.garr.it/mirrors#g' /etc/apt/sources.list
RUN apt-get update && apt-get install -y python3 python3-setuptools ca-certificates
RUN easy_install3 pip

WORKDIR /opt/dynamic-dashboards-generator/

COPY requirements.txt ./
RUN pip3 install --no-cache-dir -r requirements.txt

ARG SERVICE_PORT
EXPOSE ${SERVICE_PORT}

ENTRYPOINT flask run --host=0.0.0.0 --port=${SERVICE_PORT}

COPY app/ ./app/
