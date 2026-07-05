FROM python:3.10-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    python3.10 \
    python3.10-distutils \
    && ln -s -f $(which python3.10) /usr/bin/python \
    && rm -rf /var/lib/apt/lists/*

# Install pip
RUN wget https://bootstrap.pypa.io/get-pip.py -O /tmp/get-pip.py && \
    python /tmp/get-pip.py && \
    rm /tmp/get-pip.py

RUN pip install --upgrade pip

# Install virtualenv
RUN pip install virtualenv

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python", "-m", "mlflow.models.container"]
