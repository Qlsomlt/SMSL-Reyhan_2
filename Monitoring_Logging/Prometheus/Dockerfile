FROM python:3.10-slim

WORKDIR /app

RUN pip install --no-cache-dir prometheus-client

COPY exporter.py /app/exporter.py

CMD ["python", "exporter.py"]
