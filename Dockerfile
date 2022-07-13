FROM python:3.13-slim

RUN useradd -m openvoicepacks -b /opt
RUN apt-get update && apt-get install -y ffmpeg

COPY dist/openvoicepacks*.whl /tmp/
RUN pip install /tmp/openvoicepacks*.whl

USER openvoicepacks
WORKDIR /opt/openvoicepacks
