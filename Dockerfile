FROM python:3.12-alpine

WORKDIR /source/

RUN apk --no-cache add curl

RUN apk --no-cache add bash

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | POETRY_HOME=/opt/poetry python && \
    cd /usr/local/bin && \
    ln -s /opt/poetry/bin/poetry && \
    poetry config virtualenvs.create false

# COPY requirements.txt /source/requirements.txt
COPY ./pyproject.toml ./poetry.lock* /source/

# RUN pip install --no-cache-dir -r requirements.txt

ARG INSTALL_DEV=false
RUN bash -c "if [ $INSTALL_DEV == 'true' ] ; then poetry install --no-root ; else poetry install --no-root --only main ; fi"

ENV PYTHONPATH=/app

COPY ./app /source/app
