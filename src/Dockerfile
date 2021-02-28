# Dockerfile
FROM python:3.9
RUN pip install pipenv
RUN mkdir /code
WORKDIR /web
COPY . /core/
RUN pipenv install --system --deploy --ignore-pipfile
ADD core /code/