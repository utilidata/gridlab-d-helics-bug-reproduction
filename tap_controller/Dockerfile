FROM python:3.7-slim-buster

RUN python -m pip install --no-cache-dir helics==2.7.0.post2

WORKDIR /tap_controller
COPY tap_controller.py .
