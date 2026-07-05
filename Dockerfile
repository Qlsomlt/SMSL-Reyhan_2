FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3-distutils \
    && rm -rf /var/lib/apt/lists/*

# Install pip
RUN wget https://bootstrap.pypa.io/pip/3.10/get-pip.py -O /tmp/get-pip.py && \
    python /tmp/get-pip.py && \
    rm /tmp/get-pip.py

RUN pip install --upgrade pip

# Install virtualenv
RUN pip install virtualenv

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "-m", "mlflow.models.container"]