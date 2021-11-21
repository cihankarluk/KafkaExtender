FROM python:3.8.9

# copy source code
COPY . /app
WORKDIR /app

RUN pip install .
