# pull official base image
FROM python:3.11-slim

# set work directory
WORKDIR /usr/src/app/
RUN mkdir /usr/src/app/static
RUN mkdir /usr/src/app/media

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt

# copy project
COPY . .